# pivot_engine

Automates investigative pivot workflows in OSINT. Streams data from one investigative step to the next for efficiency and speed.

## Purpose

The module is built to:
- Chain together multiple OSINT lookups on a piece of data
- Automate “pivoting” across search engines, social sites, public records, and other sources

## Directory Structure

- `pivot.py` - Main logic for orchestrating pivot actions
- `api/` - (Describe the purpose of this submodule if present)

## Example Usage

```python
from pivot_engine.pivot import PivotEngine

engine = PivotEngine()
engine.pivot('target@example.com')
```

## TODO

- Document available pivot types
- List supported data sources
- Add more code snippets and expected output

## Author

Maintained by @theosintvault
