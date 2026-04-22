# OSINT Vault Toolkit

[![PyPI version](https://badge.fury.io/py/osintvault.svg)](https://badge.fury.io/py/osintvault)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
- [dork_patterns](dork_patterns/README.md) – structured search generation  
- [pivot_engine](pivot_engine/README.md) – automated pivot workflows  

A modular toolkit for real-world OSINT workflows.  
Built for speed, clarity, and repeatable investigative processes.

---

## Install

pip install osintvault

[View on PyPI](https://pypi.org/project/osintvault/)

## Quickstart

1. **Clone the repository:**
   ```bash
   git clone https://github.com/theosintvault/the-osint-vault-toolkit.git
   cd the-osint-vault-toolkit
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run a basic command:**
   ```bash
   python osintvault.py test@example.com
   ```

---

## Usage

osintvault test@example.com  
osintvault 8.8.8.8  
osintvault username123  

---

## What It Does

- Email → breach checks, username pivots, gravatar lookup  
- Domain → WHOIS, subdomains, DNS records  
- IP → reputation + reverse DNS  
- Username → cross-platform search  

---

## Modules

dork_patterns/ → structured search generation  
pivot_engine/ → automated pivot workflows  
bookmarklets/ → browser-based analysis tools  
reporting/ → timeline + case structure  
notes/ → investigation tracking  
samples/ → test datasets  

---

## Design

- Single-purpose tools  
- Minimal dependencies  
- Structured output  
- Fast execution  
- Built for actual investigations  

---

## Example

osintvault target@example.com

Output:

- Check breaches → HaveIBeenPwned  
- Username search → WhatsMyName  
- Gravatar check → Gravatar  

---

## Contributing

Keep it simple:
- clear purpose  
- no bloat  
- readable code  
- real use case  

---

## Status

Active. Evolving with use.
