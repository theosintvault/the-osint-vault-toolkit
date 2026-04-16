from .pivot import PivotEngine

def main():
    engine = PivotEngine()
    result = engine.pivot("email", "test@example.com")
    print(result)

if __name__ == "__main__":
    main()
