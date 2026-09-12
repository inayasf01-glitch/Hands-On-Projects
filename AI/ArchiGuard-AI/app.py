from pathlib import Path
import re
import streamlit as st

from src.compliance_engine import analyze_proposal


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ArchiGuard AI",
    page_icon="🛡️",
    layout="wide",
)


# ============================================================
# STYLING
# ============================================================

st.markdown(
    """
    <style>
    .main {
        padding-top: 2rem;
    }

    .hero {
        padding: 1.5rem 0 1rem 0;
    }

    .hero h1 {
        font-size: 2.4rem;
        margin-bottom: 0.2rem;
    }

    .hero p {
        font-size: 1.05rem;
        color: #666;
    }

    .status-card {
        padding: 1rem 1.25rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid #ddd;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "inputs"
OUTPUT_DIR = BASE_DIR / "outputs"
STANDARDS_FILE = BASE_DIR / "standards" / "enterprise_tech_standards.md"


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">
        <h1>🛡️ ArchiGuard AI</h1>
        <p>
            Automated Enterprise Architecture Compliance Auditor
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "Evaluate architecture proposals against defined enterprise technology standards using AI-assisted analysis."
)


# ============================================================
# LOAD DATA
# ============================================================

proposal_files = sorted(INPUT_DIR.glob("*.txt"))

if not proposal_files:
    st.error("No architecture proposals were found in the inputs folder.")
    st.stop()

if not STANDARDS_FILE.exists():
    st.error("Enterprise technology standards file was not found.")
    st.stop()

standards = STANDARDS_FILE.read_text(encoding="utf-8")


# ============================================================
# PROPOSAL SELECTION
# ============================================================

st.markdown('<div class="section-title">1. Select Architecture Proposal</div>', unsafe_allow_html=True)

selected_proposal = st.selectbox(
    "Test proposal",
    proposal_files,
    format_func=lambda p: p.name,
)

proposal_text = selected_proposal.read_text(encoding="utf-8")


# ============================================================
# PROPOSAL DISPLAY
# ============================================================

with st.expander("View Architecture Proposal", expanded=True):
    edited_proposal = st.text_area(
        "Proposal content",
        value=proposal_text,
        height=250,
        label_visibility="collapsed",
    )


# ============================================================
# ANALYSIS
# ============================================================

st.markdown('<div class="section-title">2. Run AI Compliance Analysis</div>', unsafe_allow_html=True)

if st.button(
    "🔍 Analyze Architecture Proposal",
    type="primary",
    use_container_width=True,
):
    with st.spinner("Analyzing architecture proposal with Gemini AI..."):
        try:
            result = analyze_proposal(edited_proposal, standards)

            # The backend returns a tuple containing the report.
            if isinstance(result, tuple):
                report = next(
                    (
                        item
                        for item in result
                        if isinstance(item, str)
                        and "## Overall Status" in item
                    ),
                    None,
                )

                if report is None:
                    report = next(
                        (
                            item
                            for item in result
                            if isinstance(item, str)
                        ),
                        None,
                    )
            else:
                report = result

            if not isinstance(report, str):
                raise TypeError(
                    "The compliance engine did not return a text report."
                )

            st.session_state["report"] = report
            st.session_state["proposal_name"] = selected_proposal.name

        except Exception as e:
            st.error(f"Analysis failed: {e}")


# ============================================================
# DISPLAY REPORT
# ============================================================

if "report" in st.session_state:

    report = st.session_state["report"]

    st.markdown("---")
    st.markdown('<div class="section-title">3. Compliance Assessment</div>', unsafe_allow_html=True)

    # --------------------------------------------------------
    # Overall Status
    # --------------------------------------------------------

    status_match = re.search(
        r"## Overall Status\s+(PASSED|FAILED|NEEDS REVIEW)",
        report,
        re.IGNORECASE,
    )

    if status_match:
        status = status_match.group(1).upper()

        if status == "PASSED":
            st.success("✅ OVERALL STATUS: PASSED")
        elif status == "FAILED":
            st.error("❌ OVERALL STATUS: FAILED")
        else:
            st.warning("⚠️ OVERALL STATUS: NEEDS REVIEW")
    else:
        st.info("Overall status was not detected in the returned report.")

    # --------------------------------------------------------
    # Executive Summary
    # --------------------------------------------------------

    summary_match = re.search(
        r"## Executive Summary\s+(.*?)(?=\n## |\Z)",
        report,
        re.DOTALL | re.IGNORECASE,
    )

    if summary_match:
        st.markdown("### Executive Summary")
        st.write(summary_match.group(1).strip())

    # --------------------------------------------------------
    # Standards Evaluation
    # --------------------------------------------------------

    evaluation_match = re.search(
        r"## Standards Evaluation\s+(.*?)(?=\n## Violations|\Z)",
        report,
        re.DOTALL | re.IGNORECASE,
    )

    if evaluation_match:
        st.markdown("### Standards Evaluation")

        evaluation_text = evaluation_match.group(1).strip()

        # Split individual standards when headings are present.
        sections = re.split(
            r"(?=###\s+)",
            evaluation_text,
        )

        for section in sections:
            section = section.strip()

            if not section:
                continue

            if section.startswith("###"):
                heading_end = section.find("\n")

                if heading_end != -1:
                    heading = section[:heading_end].replace("###", "").strip()
                    body = section[heading_end + 1:].strip()

                    with st.expander(heading, expanded=False):
                        st.markdown(body)
                else:
                    st.markdown(section)

            else:
                st.markdown(section)

    # --------------------------------------------------------
    # Violations
    # --------------------------------------------------------

    violations_match = re.search(
        r"## Violations\s+(.*?)(?=\n## Remediation|\Z)",
        report,
        re.DOTALL | re.IGNORECASE,
    )

    if violations_match:
        st.markdown("### Violations")
        st.markdown(violations_match.group(1).strip())

    # --------------------------------------------------------
    # Remediation
    # --------------------------------------------------------

    remediation_match = re.search(
        r"## Remediation\s+(.*?)(?=\n## Review Limitations|\Z)",
        report,
        re.DOTALL | re.IGNORECASE,
    )

    if remediation_match:
        st.markdown("### Recommended Remediation")
        st.markdown(remediation_match.group(1).strip())

    # --------------------------------------------------------
    # Review Limitations
    # --------------------------------------------------------

    limitations_match = re.search(
        r"## Review Limitations\s+(.*?)(?:\Z)",
        report,
        re.DOTALL | re.IGNORECASE,
    )

    if limitations_match:
        with st.expander("Review Limitations"):
            st.markdown(limitations_match.group(1).strip())

    # --------------------------------------------------------
    # Raw Report
    # --------------------------------------------------------

    with st.expander("View Complete Generated Compliance Report"):
        st.markdown(report)

    # --------------------------------------------------------
    # Download
    # --------------------------------------------------------

    st.download_button(
        label="⬇️ Download Compliance Report",
        data=report,
        file_name="archiguard_compliance_report.md",
        mime="text/markdown",
        use_container_width=True,
    )
