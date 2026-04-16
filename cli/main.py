def main():
    import sys
    from pivot_engine.pivot import run_pivot

    if len(sys.argv) < 2:
        print("Usage: osintvault <entity>")
        return

    entity = sys.argv[1]
    result = run_pivot(entity)

    print(result)
