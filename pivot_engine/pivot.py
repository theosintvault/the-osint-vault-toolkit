def run_pivot(entity):
    pivots = []

    if "@" in entity:
        pivots = [
            {"step": "Check breaches", "tool": "HaveIBeenPwned"},
            {"step": "Username search", "tool": "WhatsMyName"},
            {"step": "Gravatar check", "tool": "Gravatar"},
        ]

    elif entity.replace(".", "").isdigit():
        pivots = [
            {"step": "IP lookup", "tool": "AbuseIPDB"},
            {"step": "Reverse DNS", "tool": "DNSlytics"},
        ]

    elif "." in entity:
        pivots = [
            {"step": "WHOIS lookup", "tool": "Whois"},
            {"step": "Subdomain scan", "tool": "Amass"},
            {"step": "DNS records", "tool": "DNSdumpster"},
        ]

    else:
        pivots = [
            {"step": "Username search", "tool": "WhatsMyName"},
            {"step": "Social search", "tool": "Sherlock"},
        ]

    return {
        "entity": entity,
        "pivots": pivots
    }
