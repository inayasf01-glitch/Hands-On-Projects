from pathlib import Path
from datetime import datetime
import json

from src.metadata_parser import parse_metadata
from src.standards_validator import validate_metadata, overall_status
from src.change_classifier import classify_change
from src.ai_architecture_review import analyze_architecture


MONITORED_DIR = Path("monitored_files")
ALERTS_DIR = Path("alerts")
STATE_FILE = ALERTS_DIR / "file_state.json"
ALERT_LOG = ALERTS_DIR / "alert_log.json"


MONITORED_DIR.mkdir(exist_ok=True)
ALERTS_DIR.mkdir(exist_ok=True)


def load_json(path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return default

    return default


def save_json(path, data):
    path.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8"
    )


def scan_files():
    previous_state = load_json(STATE_FILE, {})
    alert_log = load_json(ALERT_LOG, [])

    current_state = {}

    for file_path in MONITORED_DIR.iterdir():
        if not file_path.is_file():
            continue

        modified_time = file_path.stat().st_mtime
        modified_timestamp = datetime.fromtimestamp(
            modified_time
        ).isoformat()

        current_state[file_path.name] = modified_timestamp

        if file_path.name not in previous_state:
            action = "New file detected"

        elif previous_state[file_path.name] != modified_timestamp:
            action = "File modified"

        else:
            continue

        metadata = parse_metadata(file_path)

        validation_results = validate_metadata(metadata)
        validation_status = overall_status(validation_results)

        classification = classify_change(
            metadata,
            validation_status
        )

        print("\nARCHITECTURAL CHANGE DETECTED")
        print("-----------------------------")
        print(f"File: {file_path.name}")
        print(f"System: {metadata.get('System', 'Unknown')}")
        print(f"Version: {metadata.get('Version', 'Unknown')}")
        print(f"Change Type: {metadata.get('Change Type', 'Unknown')}")
        print(f"Owner: {metadata.get('Owner', 'Unknown')}")
        print(
            f"Business Impact: "
            f"{metadata.get('Business Impact', 'Unknown')}"
        )
        print(
            f"Environment: "
            f"{metadata.get('Environment', 'Unknown')}"
        )
        print(f"Validation: {validation_status}")
        print(f"Priority: {classification['priority']}")
        print(
            f"Governance Risk: "
            f"{classification['governance_risk']}"
        )
        print(f"Review: {classification['review_status']}")

        print("\nRunning AI-assisted architecture review...")

        try:
            ai_review = analyze_architecture(file_path)

        except Exception as error:
            ai_review = (
                "AI review unavailable. "
                f"Error: {error}"
            )

        alert = {
            "file": file_path.name,
            "action": action,
            "detected": datetime.now().isoformat(timespec="seconds"),

            "system": metadata.get("System", "Unknown"),
            "version": metadata.get("Version", "Unknown"),
            "change_type": metadata.get("Change Type", "Unknown"),
            "description": metadata.get("Description", "Unknown"),
            "owner": metadata.get("Owner", "Unknown"),
            "business_impact": metadata.get(
                "Business Impact",
                "Unknown"
            ),
            "environment": metadata.get(
                "Environment",
                "Unknown"
            ),
            "review_required": metadata.get(
                "Review Required",
                "Unknown"
            ),

            "validation_status": validation_status,
            "validation_results": validation_results,

            "priority": classification["priority"],
            "priority_reason": classification["priority_reason"],

            "governance_risk": classification[
                "governance_risk"
            ],
            "governance_reason": classification[
                "governance_reason"
            ],

            "review_status": classification[
                "review_status"
            ],

            "ai_architecture_review": ai_review,

            "status": "Pending Architecture Review"
        }

        alert_log.append(alert)

        print("\nAI-ASSISTED ARCHITECTURE REVIEW")
        print("--------------------------------")
        print(ai_review)

        print("\nStatus: Pending Architecture Review")

    save_json(STATE_FILE, current_state)
    save_json(ALERT_LOG, alert_log)

    print("\nScan complete.")


if __name__ == "__main__":
    scan_files()