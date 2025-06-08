# codex_tests

This repository contains example scripts for testing Codex.

[日本語のREADMEはこちら](README.ja.md)

## Included Scripts

- `export_classes_csv.py` - Exports Vectorworks class settings to a CSV file named `class_settings.csv`. The script collects many attributes including line and fill colors, opacities, text style usage, marker data, and vector fill patterns. Recent updates added fields such as `use_text_style`, `beginning_marker`, `end_marker`, `by_style`, `opacity_n`, and `vector_fill`.
## Tests

The `tests` directory contains a pytest suite. The file
`tests/test_export_classes_csv.py` checks that `export_classes_csv.py` creates the expected CSV and demonstrates how the Vectorworks API can be stubbed for testing.
