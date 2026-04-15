#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_dork.py <command>")
        return

    command = sys.argv[1]

    if command == "list":
        print("Listing available dork patterns...")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()

notepad dork_patterns/generate_dork.py
