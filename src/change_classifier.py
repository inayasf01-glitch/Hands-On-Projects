def classify_change(metadata, validation_status):
    business_impact = metadata.get("Business Impact", "").strip().lower()
    review_required = metadata.get("Review Required", "").strip().lower()

    if business_impact == "high":
        priority = "High"
        priority_reason = "High business impact requires architecture review."
    elif business_impact == "medium":
        priority = "Medium"
        priority_reason = "Medium business impact warrants architecture review."
    elif business_impact == "low":
        priority = "Low"
        priority_reason = "Low business impact change."
    else:
        priority = "Low"
        priority_reason = "Business impact is unknown; review metadata before approval."

    if validation_status == "FAIL":
        governance_risk = "High"
        governance_reason = "Required architecture metadata is missing."
    else:
        governance_risk = "Low"
        governance_reason = "Required architecture metadata is complete."

    if review_required == "yes" or validation_status == "FAIL":
        review_status = "Required"
    else:
        review_status = "Not Required"

    return {
        "priority": priority,
        "priority_reason": priority_reason,
        "governance_risk": governance_risk,
        "governance_reason": governance_reason,
        "review_status": review_status
    }
