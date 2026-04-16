from typing import Dict, List, Optional


def _detect_type(entity: str) -> str:
    if "@" in entity:
        return "email"
    if any(entity.endswith(tld) for tld in (".com", ".net", ".org", ".io", ".co")):
        return "domain"
    if all(c.isdigit() or c == "." for c in entity):
        return "ip"
    return "username"


def _pivots_for_type(etype: str) -> List[str]:
    mapping = {
        "email": [
            "breach lookup",
            "gravatar hash",
            "username extraction",
            "linked domains",
            "social account discovery",
        ],
        "domain": [
            "whois lookup",
            "subdomain enumeration",
            "dns records",
            "historical hosting",
            "certificate transparency",
        ],
        "ip": [
            "geolocation",
            "asn lookup",
            "reverse dns",
            "open ports",
            "reputation check",
        ],
        "username": [
            "social handle search",
            "profile reuse detection",
            "avatar reuse",
            "related aliases",
        ],
    }
    return mapping.get(etype, [])


def pivot_entity(entity: str, etype: Optional[str] = None) -> Dict[str, object]:
    etype_final = (etype or _detect_type(entity)).lower()
    pivots = _pivots_for_type(etype_final)
    return {
        "entity": entity,
        "type": etype_final,
        "pivots": pivots,
    }
