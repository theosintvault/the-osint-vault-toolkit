# The OSINT Vault Toolkit

An open-source companion toolkit inspired by the investigative workflows behind The OSINT Vault.  
This repository contains practical utilities used for reconnaissance, pivoting, metadata inspection, reporting, and structured note-taking.  
Each tool is designed to be direct, reliable, and suitable for real investigative work.

## Modules

### dork_patterns/
Pattern sets and a command-line generator for building structured search dorks.  
Useful for reconnaissance, surface discovery, and repeatable search logic.

### pivots/
YAML-driven pivot definitions and a launcher for multi-engine lookups.  
Built to streamline repetitive search workflows across multiple platforms.

### bookmarklets/
Browser-native bookmarklets for in-page analysis, metadata extraction, link mapping, and DOM inspection.

### reporting/
Utilities that support structured intelligence reporting, including timeline generation and markdown-based case templates.

### notes/
Tools for organizing investigative notes, tagging information, and building simple indexes for case material.

### samples/
Example data for testing:
- URLs
- Logs
- Metadata
- Browser artifacts

## Philosophy

This toolkit follows a few straightforward principles:

- Tools should be single-purpose and easy to understand.
- Output must be structured and predictable.
- Dependencies should be minimal unless absolutely required.
- Code must be readable, auditable, and easy to modify.
- Everything should support real investigative workflows.

## Usage

Each tool is standalone and can be run directly from the command line.

Examples:

python3 dork_patterns/generate_dork.py list  
python3 dork_patterns/generate_dork.py google login_pages

## Contributing

Contributions are welcome if they follow the same principles:

- Single-purpose
- Minimal dependencies
- Clear investigative relevance
- Clean, readable code
