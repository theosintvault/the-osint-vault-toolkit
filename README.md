# The OSINT Vault Toolkit

A practical, open-source toolkit built to support real-world OSINT workflows.  
This repository contains focused utilities for reconnaissance, pivoting, metadata analysis, reporting, and structured note management.

Each component is designed to be simple, reliable, and usable in actual investigations — not just demonstrations.

---

## Overview

The OSINT Vault Toolkit provides modular tools that can be used independently or combined into larger investigative workflows.  
Everything is built with clarity, repeatability, and real-world use in mind.

---

## Modules

### dork_patterns/
Predefined search patterns and a CLI generator for building structured search queries.  
Useful for reconnaissance, surface discovery, and repeatable search logic.

---

### pivots/
YAML-based pivot definitions and a launcher for multi-source lookups.  
Designed to streamline repetitive searches across multiple platforms.

---

### bookmarklets/
Browser-based tools for:
- Metadata extraction  
- Link mapping  
- DOM inspection  
- On-page analysis  

No installation required — runs directly in the browser.

---

### reporting/
Utilities for structured intelligence reporting, including:
- Timeline generation  
- Markdown-based case templates  

Built for clean, consistent documentation.

---

### notes/
Lightweight tools for organizing investigative notes, tagging data, and maintaining structured case records.

---

### samples/
Test data for development and validation:
- URLs  
- Logs  
- Metadata  
- Browser artifacts  

---

## Design Principles

This toolkit is built around a few core rules:

- Single-purpose tools over complex systems  
- Predictable, structured output  
- Minimal dependencies  
- Readable, auditable code  
- Built for actual investigative use  

---

## Usage

Each module can be run independently from the command line.

Examples:

```bash
python3 dork_patterns/generate_dork.py list
python3 dork_patterns/generate_dork.py google login_pages
