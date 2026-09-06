from pathlib import Path
from datetime import datetime
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors


# Load environment variables from .env
load_dotenv()


# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
STANDARDS_FILE = BASE_DIR / "standards" / "enterprise_tech_standards.md"
INPUTS_DIR = BASE_DIR / "inputs"
OUTPUTS_DIR = BASE_DIR / "outputs"


# Gemini models to try, in priority order
MODELS = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
]


# Number of attempts for temporary server failures
MAX_RETRIES = 3


def read_file(file_path: Path) -> str:
    """Read a UTF-8 text file and return its contents."""
    return file_path.read_text(encoding="utf-8")


def generate_with_retry(client, prompt: str):
    """
    Generate an AI response with automatic retries and model fallback.

    The primary model is tried first. Temporary server failures are
    retried with exponential backoff. If the primary model remains
    unavailable, the next model is attempted.
    """

    for model in MODELS:

        print(f"Using model: {model}")

        for attempt in range(1, MAX_RETRIES + 1):

            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                if not response.text:
                    raise RuntimeError(
                        f"{model} returned an empty response."
                    )

                print(f"Success: {model}")
                return response.text, model

            except errors.ServerError as exc:

                print(
                    f"Temporary server error with {model} "
                    f"(attempt {attempt}/{MAX_RETRIES})."
                )

                if attempt < MAX_RETRIES:
                    wait_seconds = 2 ** (attempt - 1)

                    print(
                        f"Waiting {wait_seconds} second(s) before retry..."
                    )

                    time.sleep(wait_seconds)

                else:
                    print(
                        f"{model} remained unavailable after "
                        f"{MAX_RETRIES} attempts."
                    )

            except errors.ClientError as exc:

                status_code = getattr(exc, "status_code", None)

                if status_code == 429:

                    print(
                        f"Rate limit encountered with {model} "
                        f"(attempt {attempt}/{MAX_RETRIES})."
                    )

                    if attempt < MAX_RETRIES:
                        wait_seconds = 2 ** (attempt - 1)

                        print(
                            f"Waiting {wait_seconds} second(s) before retry..."
                        )

                        time.sleep(wait_seconds)

                    else:
                        print(
                            f"{model} remained rate-limited after "
                            f"{MAX_RETRIES} attempts."
                        )

                else:
                    raise

    raise RuntimeError(
        "All configured Gemini models were unavailable. "
        "Please try again later."
    )


def analyze_proposal(proposal_text: str, standards_text: str):
    """Analyze an architecture proposal against enterprise standards."""

    client = genai.Client()

    prompt = f"""
You are ArchiGuard AI, an Enterprise Architecture compliance assistant.

Your task is to evaluate an IT architecture proposal against the
enterprise technology standards provided below.

IMPORTANT RULES:
- Evaluate the proposal only against the standards provided.
- Do not invent additional standards.
- Do not assume that a requirement is satisfied unless the proposal
  provides reasonable evidence.
- If the proposal does not provide enough information to determine
  compliance, use NEEDS REVIEW.
- Be precise and professional.
- Quote or reference specific evidence from the proposal when possible.

Return a Markdown report using exactly these sections:

# ArchiGuard AI Compliance Report

## Overall Status

Use exactly one of:
- PASSED
- FAILED
- NEEDS REVIEW

## Executive Summary

Provide a short summary of the architecture's compliance posture.

## Standards Evaluation

For each standard, provide:

### Standard [number] — [name]

- **Status:** PASSED, FAILED, or NEEDS REVIEW
- **Evidence:** Evidence from the proposal
- **Assessment:** Explain why the evidence satisfies, violates, or
  does not adequately address the standard.

## Violations

List every standard that received FAILED status.

If there are no violations, write:
"No failed standards identified."

## Remediation

For each failed or needs-review standard, provide a practical
recommendation.

If no remediation is required, write:
"No remediation actions identified."

## Review Limitations

Explain what could not be determined from the proposal.

Enterprise Technology Standards
--------------------------------

{standards_text}

--------------------------------

Architecture Proposal
--------------------------------

{proposal_text}

--------------------------------
"""

    return generate_with_retry(client, prompt)


def save_report(report: str, proposal_path: Path, model_used: str) -> Path:
    """Save a compliance report to the outputs directory."""

    OUTPUTS_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    report_name = (
        f"{proposal_path.stem}_compliance_{timestamp}.md"
    )

    report_path = OUTPUTS_DIR / report_name

    metadata = (
        f"<!--\n"
        f"Generated by ArchiGuard AI\n"
        f"Model: {model_used}\n"
        f"Generated: {datetime.now().isoformat(timespec='seconds')}\n"
        f"-->\n\n"
    )

    report_path.write_text(
        metadata + report,
        encoding="utf-8",
    )

    return report_path


def main():
    """Run ArchiGuard AI against all architecture proposals."""

    print("=" * 60)
    print("ARCHIGUARD AI")
    print("Automated Enterprise Architecture Compliance Engine")
    print("=" * 60)

    # Verify required files and directories
    if not STANDARDS_FILE.exists():
        raise FileNotFoundError(
            f"Standards file not found: {STANDARDS_FILE}"
        )

    if not INPUTS_DIR.exists():
        raise FileNotFoundError(
            f"Inputs directory not found: {INPUTS_DIR}"
        )

    # Read enterprise standards
    standards = read_file(STANDARDS_FILE)

    # Find architecture proposals
    proposals = sorted(INPUTS_DIR.glob("*.txt"))

    if not proposals:
        print("No architecture proposals were found.")
        return

    print(f"\nFound {len(proposals)} architecture proposal(s).")

    successful_reports = 0
    failed_reports = 0

    # Analyze each proposal
    for proposal_path in proposals:

        print("\n" + "-" * 60)
        print(f"Analyzing: {proposal_path.name}")
        print("-" * 60)

        try:
            proposal = read_file(proposal_path)

            report, model_used = analyze_proposal(
                proposal_text=proposal,
                standards_text=standards,
            )

            report_path = save_report(
                report=report,
                proposal_path=proposal_path,
                model_used=model_used,
            )

            print(f"Report created: {report_path}")
            successful_reports += 1

        except Exception as exc:

            print(
                f"ERROR: Could not analyze "
                f"{proposal_path.name}"
            )

            print(f"Reason: {exc}")

            failed_reports += 1

    print("\n" + "=" * 60)
    print("ARCHIGUARD AI ANALYSIS COMPLETE")
    print("=" * 60)

    print(f"Successful reports: {successful_reports}")
    print(f"Failed reports: {failed_reports}")


if __name__ == "__main__":
    main()