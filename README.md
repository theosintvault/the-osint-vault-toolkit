# The OSINT Vault Toolkit

An open-source companion toolkit inspired by the proprietary investigation tools inside The OSINT Vault.  
This repository provides lightweight, practical utilities that mirror real investigative workflows: reconnaissance, pivoting, metadata extraction, reporting, and structured note-taking.

The goal is simple: provide investigators with clean, dependable, minimal-dependency tools that can be dropped directly into casework.

---

## Core Philosophy

This toolkit follows the same principles that guide The OSINT Vault:

- Tools must be **purpose-built**, not bloated.
- Output should be **structured**, not noisy.
- Workflows should be **repeatable**, not improvised.
- Code must be **readable, auditable, and modifiable**.
- Everything should support real investigative use—not demos, not toys.

---

## Modules

### **dork_patterns/**
Open-source dork patterns and a CLI generator inspired by the proprietary  
**Google Dork Generator** on The OSINT Vault.  
Includes YAML-based pattern sets and a simple generator for reconnaissance pivots.

### **pivots/**
A lightweight pivoting engine modeled after the  
**Multi‑Search Launcher**.  
Uses YAML definitions to launch coordinated searches across multiple endpoints.

### **bookmarklets/**
Browser-native bookmarklets inspired by the  
**Bookmarklet Library**.  
Useful for metadata extraction, DOM inspection, link mapping, and in-page reconnaissance.

### **reporting/**
Utilities that support structured intelligence reporting, similar in spirit to the  
**Intelligence Report Composer**.  
Includes timeline builders, summary generators, and markdown templates.

### **notes/**
Tools for organizing raw investigative notes, reflecting the workflow behind the  
**OSINT Vault Note Organizer**.  
Includes note structuring, tagging, and index generation.

### **samples/**
Example data for testing:
- URLs  
- Logs  
- Metadata  
- Browser artifacts  

---

## Usage

Each module is standalone.  
No frameworks. No heavy dependencies.  
Run tools directly from the command line.

Example:

