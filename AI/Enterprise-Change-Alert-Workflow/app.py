import json
import subprocess
import sys
from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
ALERTS_DIR = BASE_DIR / "alerts"
MONITORED_DIR = BASE_DIR / "monitored_files"

ALERT_LOG = ALERTS_DIR / "alert_log.json"
DASHBOARD_FILE = ALERTS_DIR / "dashboard.html"
FILE_STATE = ALERTS_DIR / "file_state.json"

st.set_page_config(
    page_title="Enterprise Change Alert Workflow",
    page_icon="⚙️",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main {
        padding-top: 1.5rem;
    }

    .hero {
        padding: 1.5rem 1.8rem;
        border-radius: 14px;
        border: 1px solid rgba(128,128,128,0.25);
        margin-bottom: 1.5rem;
    }

    .stage {
        text-align: center;
        padding: 0.8rem 0.3rem;
        border-radius: 10px;
        border: 1px solid rgba(128,128,128,0.25);
        font-weight: 600;
    }

    .metric-card {
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(128,128,128,0.25);
        text-align: center;
    }

    .small-muted {
        color: #777;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_json(path):
    try:
        if path.exists():
            with open(path, "r", encoding="utf-8") as file:
                return json.load(file)
    except (json.JSONDecodeError, OSError):
        pass

    return {}


def get_monitored_files():
    if not MONITORED_DIR.exists():
        return []

    return sorted(
        [file for file in MONITORED_DIR.iterdir() if file.is_file()],
        key=lambda x: x.name.lower(),
    )


def get_alerts():
    data = load_json(ALERT_LOG)

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        for key in ("alerts", "alert_log", "records", "events"):
            if isinstance(data.get(key), list):
                return data[key]

    return []


def run_workflow():
    return subprocess.run(
        [sys.executable, "-m", "src.change_alert"],
        cwd=BASE_DIR,
        capture_output=True,
        text=True,
    )


def format_value(value):
    if value is None:
        return "—"

    if isinstance(value, (dict, list)):
        return json.dumps(value, indent=2)

    return str(value)


st.markdown(
    """
    <div class="hero">
        <h1>⚙️ Enterprise Change Alert Workflow</h1>
        <p>
            Automated architecture-change monitoring and alert generation
            using a Python event-driven workflow.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("Automated Workflow")

stages = [
    "Monitor",
    "Detect",
    "Metadata",
    "Classify",
    "Review",
    "Validate",
    "Alert",
]

columns = st.columns(len(stages))

for column, stage in zip(columns, stages):
    with column:
        st.markdown(
            f'<div class="stage">{stage}</div>',
            unsafe_allow_html=True,
        )

st.markdown("")

st.subheader("Run Architecture Change Scan")

st.write(
    "Scan the monitored architecture files and execute the complete "
    "change-detection workflow."
)

if st.button(
    "🔍 Scan for Architecture Changes",
    type="primary",
    use_container_width=True,
):
    with st.spinner("Running automated change-detection workflow..."):
        result = run_workflow()

    if result.returncode == 0:
        st.success(
            "✓ Automated change detection completed successfully."
        )

        if result.stdout.strip():
            with st.expander("Workflow execution details"):
                st.code(result.stdout)

    else:
        st.error("The workflow encountered an error.")

        if result.stderr.strip():
            st.code(result.stderr)


monitored_files = get_monitored_files()
alerts = get_alerts()

st.subheader("Workflow Status")

metric_columns = st.columns(3)

with metric_columns[0]:
    st.markdown(
        f"""
        <div class="metric-card">
            <h2>{len(monitored_files)}</h2>
            <div>Monitored Files</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with metric_columns[1]:
    st.markdown(
        f"""
        <div class="metric-card">
            <h2>{len(alerts)}</h2>
            <div>Generated Alerts</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with metric_columns[2]:
    status = "Ready" if MONITORED_DIR.exists() else "Unavailable"

    st.markdown(
        f"""
        <div class="metric-card">
            <h2>{status}</h2>
            <div>Workflow Status</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.subheader("Monitored Architecture Files")

if monitored_files:
    for file in monitored_files:
        try:
            size = file.stat().st_size
        except OSError:
            size = 0

        st.write(f"📄 **{file.name}** — {size:,} bytes")
else:
    st.info("No monitored architecture files were found.")


st.subheader("Generated Change Alerts")

if alerts:
    for index, alert in enumerate(alerts, start=1):
        with st.expander(f"Alert {index}"):
            if isinstance(alert, dict):
                for key, value in alert.items():
                    st.markdown(f"**{key}:**")
                    st.write(format_value(value))
            else:
                st.write(format_value(alert))
else:
    st.info(
        "No alert records are currently available. "
        "Run the scan to generate workflow results."
    )


st.subheader("Workflow Outputs")

output_columns = st.columns(3)

with output_columns[0]:
    if ALERT_LOG.exists():
        st.success("✓ Alert log available")

        with open(ALERT_LOG, "r", encoding="utf-8") as file:
            alert_content = file.read()

        st.download_button(
            "Download Alert Log",
            data=alert_content,
            file_name="alert_log.json",
            mime="application/json",
            use_container_width=True,
        )
    else:
        st.info("Alert log not generated yet.")

with output_columns[1]:
    if DASHBOARD_FILE.exists():
        st.success("✓ Dashboard available")

        with open(DASHBOARD_FILE, "r", encoding="utf-8") as file:
            dashboard_content = file.read()

        st.download_button(
            "Download Dashboard HTML",
            data=dashboard_content,
            file_name="dashboard.html",
            mime="text/html",
            use_container_width=True,
        )
    else:
        st.info("Dashboard has not been generated yet.")

with output_columns[2]:
    if FILE_STATE.exists():
        st.success("✓ File state available")

        with open(FILE_STATE, "r", encoding="utf-8") as file:
            state_content = file.read()

        st.download_button(
            "Download File State",
            data=state_content,
            file_name="file_state.json",
            mime="application/json",
            use_container_width=True,
        )
    else:
        st.info("File state has not been generated yet.")


st.divider()

st.subheader("About This Prototype")

st.write(
    """
    This student-built Python proof of concept demonstrates an automated
    workflow for monitoring architecture files, detecting changes,
    extracting metadata, classifying changes, performing architecture
    review and validation, and generating structured alerts.

    The project explores concepts relevant to enterprise technology,
    architecture governance, automation, AI-assisted analysis,
    documentation, and workflow optimization.
    """
)

st.markdown(
    '<p class="small-muted">'
    "Current implementation: Python prototype. "
    "Enterprise platform integrations such as SharePoint, Teams, "
    "Power Automate, or LeanIX are not implemented in this version."
    "</p>",
    unsafe_allow_html=True,
)