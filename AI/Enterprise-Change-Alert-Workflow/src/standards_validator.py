REQUIRED_FIELDS = [
    "System",
    "Version",
    "Change Type",
    "Description",
    "Owner",
    "Business Impact",
    "Environment",
    "Review Required"
]


def validate_metadata(metadata):
    results = {}

    for field in REQUIRED_FIELDS:
        value = metadata.get(field, "").strip()

        if value:
            results[field] = "PASS"
        else:
            results[field] = "FAIL"

    return results


def overall_status(results):
    if all(status == "PASS" for status in results.values()):
        return "PASS"

    return "FAIL"
