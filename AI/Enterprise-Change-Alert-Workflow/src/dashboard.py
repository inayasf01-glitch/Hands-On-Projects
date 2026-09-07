from pathlib import Path
import json
import html
import re


ALERT_LOG = Path("alerts/alert_log.json")
OUTPUT = Path("alerts/dashboard.html")


def load_alerts():
    if not ALERT_LOG.exists():
        return []

    try:
        return json.loads(
            ALERT_LOG.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError:
        return []


def format_inline_markdown(text):
    """
    Convert the limited Markdown formatting commonly returned
    by the AI architecture review into safe HTML.
    """

    text = html.escape(text)

    # Convert **bold text** to <strong>bold text</strong>
    text = re.sub(
        r"\*\*(.+?)\*\*",
        r"<strong>\1</strong>",
        text
    )

    return text


def format_ai_review(ai_review):
    """
    Convert the AI's Markdown-style response into readable HTML.
    """

    lines = ai_review.splitlines()
    formatted_lines = []

    for line in lines:
        stripped = line.strip()

        # Empty line
        if not stripped:
            formatted_lines.append(
                "<div class='review-space'></div>"
            )
            continue

        # Horizontal rule
        if stripped == "---":
            formatted_lines.append("<hr>")
            continue

        # Markdown heading
        if stripped.startswith("### "):
            heading = format_inline_markdown(
                stripped[4:].strip()
            )

            formatted_lines.append(
                f"<h4>{heading}</h4>"
            )
            continue

        # Numbered list item
        numbered_match = re.match(
            r"^(\d+)\.\s+(.*)$",
            stripped
        )

        if numbered_match:
            number = numbered_match.group(1)
            content = format_inline_markdown(
                numbered_match.group(2)
            )

            formatted_lines.append(
                f"""
                <div class="review-number">
                    <span class="review-number-value">
                        {number}.
                    </span>
                    <span>
                        {content}
                    </span>
                </div>
                """
            )
            continue

        # Bullet list item
        if stripped.startswith("* "):
            content = format_inline_markdown(
                stripped[2:].strip()
            )

            formatted_lines.append(
                f"""
                <div class="review-bullet">
                    <span class="bullet-symbol">•</span>
                    <span>{content}</span>
                </div>
                """
            )
            continue

        # Normal paragraph
        content = format_inline_markdown(stripped)

        formatted_lines.append(
            f"<p>{content}</p>"
        )

    return "\n".join(formatted_lines)


def badge(value):
    value = str(value)

    return (
        f'<span class="badge">'
        f'{html.escape(value)}'
        f'</span>'
    )


def build_ai_review(alert):
    ai_review = alert.get(
        "ai_architecture_review",
        ""
    )

    if not ai_review:
        return """
        <div class="ai-review-empty">
            AI-assisted review is not available for this artifact.
        </div>
        """

    formatted_review = format_ai_review(
        ai_review
    )

    return f"""
    <div class="ai-review">

        <div class="ai-review-header">

            <strong>
                AI-Assisted Architecture Review
            </strong>

            <span class="advisory-label">
                Advisory — Human Review Required
            </span>

        </div>

        <div class="ai-review-content">
            {formatted_review}
        </div>

    </div>
    """


def build_dashboard(alerts):

    total_changes = len(alerts)

    new_files = sum(
        1
        for alert in alerts
        if alert.get("action") == "New file detected"
    )

    modified_files = sum(
        1
        for alert in alerts
        if alert.get("action") == "File modified"
    )

    validation_pass = sum(
        1
        for alert in alerts
        if alert.get("validation_status") == "PASS"
    )

    validation_fail = sum(
        1
        for alert in alerts
        if alert.get("validation_status") == "FAIL"
    )

    high_priority = sum(
        1
        for alert in alerts
        if alert.get("priority") == "High"
    )

    medium_priority = sum(
        1
        for alert in alerts
        if alert.get("priority") == "Medium"
    )

    low_priority = sum(
        1
        for alert in alerts
        if alert.get("priority") == "Low"
    )

    high_governance_risk = sum(
        1
        for alert in alerts
        if alert.get("governance_risk") == "High"
    )

    systems = len({
        alert.get("system", "Unknown")
        for alert in alerts
    })

    review_queue = sum(
        1
        for alert in alerts
        if alert.get("review_status") == "Required"
    )

    rows = ""
    ai_reviews = ""

    for alert in reversed(alerts):

        validation = alert.get(
            "validation_status",
            "Unknown"
        )

        priority = alert.get(
            "priority",
            "Unknown"
        )

        governance_risk = alert.get(
            "governance_risk",
            "Unknown"
        )

        failed_checks = [
            field
            for field, result in alert.get(
                "validation_results",
                {}
            ).items()
            if result == "FAIL"
        ]

        issues = (
            ", ".join(failed_checks)
            if failed_checks
            else "None"
        )

        rows += f"""
        <tr>

            <td>
                {html.escape(
                    alert.get("system", "Unknown")
                )}
            </td>

            <td>
                {html.escape(
                    alert.get("file", "Unknown")
                )}
            </td>

            <td>
                {html.escape(
                    alert.get("version", "Unknown")
                )}
            </td>

            <td>
                {html.escape(
                    alert.get(
                        "change_type",
                        "Unknown"
                    )
                )}
            </td>

            <td>
                {html.escape(
                    alert.get(
                        "business_impact",
                        "Unknown"
                    )
                )}
            </td>

            <td>
                {badge(validation)}
            </td>

            <td>
                {badge(priority)}
            </td>

            <td>
                {badge(governance_risk)}
            </td>

            <td>
                {html.escape(issues)}
            </td>

            <td>
                {html.escape(
                    alert.get(
                        "detected",
                        "Unknown"
                    )
                )}
            </td>

        </tr>
        """

        ai_reviews += f"""
        <div class="review-card">

            <div class="review-card-header">

                <div>

                    <h3>
                        {html.escape(
                            alert.get(
                                "system",
                                "Unknown"
                            )
                        )}
                    </h3>

                    <p>
                        {html.escape(
                            alert.get(
                                "file",
                                "Unknown"
                            )
                        )}

                        · Version

                        {html.escape(
                            alert.get(
                                "version",
                                "Unknown"
                            )
                        )}
                    </p>

                </div>

                <div class="review-badges">

                    {badge(priority)}

                    {badge(governance_risk)}

                    {badge(validation)}

                </div>

            </div>

            {build_ai_review(alert)}

            <div class="human-review">

                <strong>
                    Human Architecture Review:
                </strong>

                {html.escape(
                    alert.get(
                        "status",
                        "Pending Architecture Review"
                    )
                )}

            </div>

        </div>
        """

    if not rows:
        rows = """
        <tr>
            <td colspan="10">
                No architecture changes detected.
            </td>
        </tr>
        """

    if not ai_reviews:
        ai_reviews = """
        <div class="ai-review-empty">
            No architecture reviews available.
        </div>
        """

    return f"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>

<title>
    Enterprise Architecture Enablement Dashboard
</title>

<style>

    body {{
        font-family: Arial, sans-serif;
        margin: 0;
        background: #f4f6f8;
        color: #1f2937;
    }}

    header {{
        background: #111827;
        color: white;
        padding: 28px 40px;
    }}

    header h1 {{
        margin: 0 0 8px;
        font-size: 28px;
    }}

    header p {{
        margin: 0;
        color: #d1d5db;
    }}

    main {{
        padding: 30px 40px;
        max-width: 1500px;
        margin: auto;
    }}

    .section-title {{
        margin-top: 32px;
        margin-bottom: 15px;
        font-size: 20px;
    }}

    .cards {{
        display: grid;
        grid-template-columns:
            repeat(auto-fit, minmax(190px, 1fr));
        gap: 16px;
    }}

    .card {{
        background: white;
        padding: 22px;
        border-radius: 10px;
        box-shadow:
            0 2px 8px rgba(0,0,0,0.08);
    }}

    .card .label {{
        font-size: 13px;
        color: #6b7280;
        margin-bottom: 8px;
    }}

    .card .value {{
        font-size: 30px;
        font-weight: bold;
    }}

    .table-container {{
        background: white;
        border-radius: 10px;
        overflow-x: auto;
        box-shadow:
            0 2px 8px rgba(0,0,0,0.08);
    }}

    table {{
        width: 100%;
        border-collapse: collapse;
        min-width: 1250px;
    }}

    th,
    td {{
        padding: 14px;
        text-align: left;
        border-bottom:
            1px solid #e5e7eb;
        font-size: 13px;
    }}

    th {{
        background: #f9fafb;
        font-weight: bold;
    }}

    .badge {{
        display: inline-block;
        padding: 5px 9px;
        border-radius: 999px;
        background: #e5e7eb;
        font-size: 12px;
        font-weight: bold;
    }}

    .review-card {{
        background: white;
        border-radius: 10px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow:
            0 2px 8px rgba(0,0,0,0.08);
    }}

    .review-card-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 20px;
        margin-bottom: 20px;
    }}

    .review-card-header h3 {{
        margin: 0 0 6px;
        font-size: 18px;
    }}

    .review-card-header p {{
        margin: 0;
        color: #6b7280;
        font-size: 13px;
    }}

    .review-badges {{
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        justify-content: flex-end;
    }}

    .ai-review {{
        border-left: 4px solid #374151;
        background: #f9fafb;
        border-radius: 6px;
        overflow: hidden;
    }}

    .ai-review-header {{
        padding: 14px 18px;
        border-bottom:
            1px solid #e5e7eb;
        display: flex;
        justify-content: space-between;
        gap: 15px;
        align-items: center;
    }}

    .advisory-label {{
        font-size: 11px;
        font-weight: bold;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }}

    .ai-review-content {{
        padding: 18px;
        overflow-x: auto;
    }}

    .ai-review-content p {{
        margin: 0 0 10px 0;
        line-height: 1.6;
    }}

    .ai-review-content h4 {{
        margin: 22px 0 10px 0;
        font-size: 14px;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 0.3px;
        color: #374151;
    }}

    .ai-review-content h4:first-child {{
        margin-top: 0;
    }}

    .ai-review-content hr {{
        border: 0;
        border-top:
            1px solid #e5e7eb;
        margin: 18px 0;
    }}

    .review-bullet {{
        display: flex;
        gap: 8px;
        margin: 7px 0;
        line-height: 1.55;
    }}

    .bullet-symbol {{
        font-weight: bold;
        flex-shrink: 0;
    }}

    .review-number {{
        display: flex;
        gap: 8px;
        margin: 7px 0;
        line-height: 1.55;
    }}

    .review-number-value {{
        font-weight: bold;
        min-width: 22px;
        flex-shrink: 0;
    }}

    .review-space {{
        height: 8px;
    }}

    .ai-review-empty {{
        background: white;
        padding: 20px;
        border-radius: 8px;
        color: #6b7280;
    }}

    .human-review {{
        margin-top: 18px;
        padding: 14px 18px;
        background: #f3f4f6;
        border-radius: 6px;
        font-size: 13px;
    }}

    .architecture-note {{
        background: white;
        padding: 20px;
        border-left:
            4px solid #374151;
        border-radius: 6px;
        margin-top: 25px;
        line-height: 1.6;
    }}

    .footer {{
        margin-top: 35px;
        color: #6b7280;
        font-size: 12px;
    }}

    @media (max-width: 700px) {{

        header {{
            padding: 24px;
        }}

        main {{
            padding: 24px;
        }}

        .review-card-header {{
            flex-direction: column;
        }}

        .review-badges {{
            justify-content: flex-start;
        }}

        .ai-review-header {{
            flex-direction: column;
            align-items: flex-start;
        }}

    }}

</style>

</head>

<body>

<header>

    <h1>
        Enterprise Architecture Enablement Dashboard
    </h1>

    <p>
        Automated architecture artifact monitoring,
        validation, prioritization, and review tracking
    </p>

</header>

<main>

<h2 class="section-title">
    Portfolio Overview
</h2>

<div class="cards">

    <div class="card">
        <div class="label">
            Total Changes
        </div>
        <div class="value">
            {total_changes}
        </div>
    </div>

    <div class="card">
        <div class="label">
            Systems Affected
        </div>
        <div class="value">
            {systems}
        </div>
    </div>

    <div class="card">
        <div class="label">
            New Artifacts
        </div>
        <div class="value">
            {new_files}
        </div>
    </div>

    <div class="card">
        <div class="label">
            Modified Artifacts
        </div>
        <div class="value">
            {modified_files}
        </div>
    </div>

    <div class="card">
        <div class="label">
            Validation Passed
        </div>
        <div class="value">
            {validation_pass}
        </div>
    </div>

    <div class="card">
        <div class="label">
            Validation Failed
        </div>
        <div class="value">
            {validation_fail}
        </div>
    </div>

    <div class="card">
        <div class="label">
            High Priority
        </div>
        <div class="value">
            {high_priority}
        </div>
    </div>

    <div class="card">
        <div class="label">
            High Governance Risk
        </div>
        <div class="value">
            {high_governance_risk}
        </div>
    </div>

    <div class="card">
        <div class="label">
            Review Queue
        </div>
        <div class="value">
            {review_queue}
        </div>
    </div>

</div>

<h2 class="section-title">
    Architecture Review Queue
</h2>

<div class="table-container">

<table>

<thead>

<tr>

    <th>System</th>
    <th>Artifact</th>
    <th>Version</th>
    <th>Change Type</th>
    <th>Business Impact</th>
    <th>Validation</th>
    <th>Priority</th>
    <th>Governance Risk</th>
    <th>Validation Issues</th>
    <th>Detected</th>

</tr>

</thead>

<tbody>

{rows}

</tbody>

</table>

</div>

<h2 class="section-title">
    AI-Assisted Architecture Reviews
</h2>

<p>
    AI-generated analysis is advisory and supports,
    but does not replace, human architecture review
    and governance decisions.
</p>

{ai_reviews}

<div class="architecture-note">

    <strong>Workflow:</strong>

    Architecture Artifact
    -&gt;
    Change Detection
    -&gt;
    Metadata Extraction
    -&gt;
    Standards Validation
    -&gt;
    Change Classification
    -&gt;
    AI-Assisted Review
    -&gt;
    Human Architecture Review
    -&gt;
    Dashboard

</div>

<div class="footer">

    Prototype for enterprise architecture enablement
    and workflow automation.

    Current implementation uses local Python automation,
    Gemini AI analysis, persistent JSON audit records,
    and generated HTML.

</div>

</main>

</body>

</html>
"""


def main():
    alerts = load_alerts()

    dashboard = build_dashboard(
        alerts
    )

    OUTPUT.write_text(
        dashboard,
        encoding="utf-8"
    )

    print(
        f"Dashboard generated: {OUTPUT}"
    )


if __name__ == "__main__":
    main()