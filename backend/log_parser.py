def detect_severity(log_line: str) -> str:
    log_line = log_line.lower()

    if "critical" in log_line:
        return "CRITICAL"
    elif "error" in log_line:
        return "HIGH"
    elif "warning" in log_line:
        return "MEDIUM"
    else:
        return "LOW"


def extract_issues(log_text: str):
    lines = log_text.splitlines()

    errors = []
    warnings = []

    for line in lines:
        if "error" in line.lower():
            errors.append({
                "message": line.strip(),
                "severity": detect_severity(line)
            })

        elif "warning" in line.lower():
            warnings.append({
                "message": line.strip(),
                "severity": detect_severity(line)
            })

    return {
        "errors": errors,
        "warnings": warnings
    }