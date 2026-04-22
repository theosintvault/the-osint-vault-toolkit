from pivot_engine.pivot import run_pivot


def section(title):
    print("\n" + "=" * 50)
    print(title.upper())
    print("=" * 50)


def mark(value):
    if value is True:
        return "[✓]"
    elif value is False:
        return "[x]"
    else:
        return "[ ]"


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: osintvault <target>")
        return

    entity = sys.argv[1]
    data = run_pivot(entity)

    section(f"ENTITY: {entity}")

    for pivot in data["pivots"]:
        step = pivot["step"]
        result = pivot["result"]

        print(f"\n{step.upper()}")

        # ---- EMAIL REP ----
        if step == "email reputation":
            if isinstance(result, dict):
                if "error" in result:
                    print(f"  [!] {result['error']}")
                else:
                    print(f"  reputation: {result.get('reputation')}")
                    print(f"  suspicious: {mark(result.get('suspicious'))}")

        # ---- GRAVATAR ----
        elif step == "gravatar check":
            print(f"  gravatar: {mark(result.get('gravatar'))}")

        # ---- USERNAMES ----
        elif step == "username generation":
            print("  usernames:")
            for u in result:
                print(f"   • {u}")

        # ---- USERNAME CHECK ----
        elif step == "username check":
            print("  platform hits:")
            for username, sites in result.items():
                positives = [s for s, v in sites.items() if v]

                if positives:
                    print(f"   [✓] {username} → {', '.join(positives)}")
                else:
                    print(f"   [x] {username}")

        # ---- SEARCH ----
        elif step == "search results":
            print("  results:")
            if isinstance(result, list):
                for item in result:
                    title = item.get("title")
                    link = item.get("link")
                    print(f"   • {title}")
                    print(f"     {link}")

            else:
                print(f"   {result}")
