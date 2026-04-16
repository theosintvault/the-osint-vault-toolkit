# OSINT Vault Toolkit

A modular toolkit for real-world OSINT workflows.  
Built for speed, clarity, and repeatable investigative processes.

---

## Install

pip install osintvault

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
