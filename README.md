# Codex_Tests

This repository contains example scripts for testing Codex.

[日本語のREADMEはこちら](README.ja.md)

## Included Scripts

- export_classes_csv.py
  - Exports Vectorworks class settings to a CSV file named `class_settings.csv`.
  - The script collects many attributes including line and fill colors, opacities, text style usage, marker data, and vector fill patterns.
  - Recent updates added fields such as `use_text_style`, `beginning_marker`, `end_marker`, `by_style`, `opacity_n`, `vector_fill`, `drop_shadow_enabled`, `class_options`, `drop_shadow_data`, `line_style_n`, `text_style_ref`.
  - drop_shadow_data: `(1, 2, 3, 4, 5, 6, 7, 8)` is exported as a string in the CSV.
    - `None` becomes an empty string `""`.
  - drop_shadow_enabled uses the `GetCLDropShadowEnabled` API.

## Running the Python Scripts

To export class settings open Vectorworks, choose **Tools → Plug-ins → Run Python Script…** and select `export_classes_csv.py`. The script saves `class_settings.csv` to your desktop.

Regenerate the exported field list in this README with:

```bash
python scripts/generate_fields_md.py
```

### Exported Class Attributes

The script writes the following fields for each class:

<!--FIELDS-->
- `beginning_marker`
- `by_style`
- `class_options`
- `drop_shadow_data`
- `drop_shadow_enabled`
- `end_marker`
- `fill_color`
- `fill_color_back`
- `fill_color_fore`
- `fill_opacity`
- `fill_style`
- `line_color`
- `line_color_back`
- `line_color_fore`
- `line_marker`
- `line_opacity`
- `line_style`
- `line_style_n`
- `line_thickness`
- `line_weight`
- `name`
- `opacity_n`
- `shadow_angle`
- `shadow_blur`
- `shadow_color`
- `shadow_offset_x`
- `shadow_offset_y`
- `shadow_opacity`
- `sync_line_opacity`
- `text_style`
- `text_style_ref`
- `use_drop_shadow`
- `use_graphic`
- `use_text_attrs`
- `use_text_style`
- `vector_fill`
- `visibility`
<!--/FIELDS-->
## Tests

The `tests` directory contains a pytest suite. The file
`tests/test_export_classes_csv.py` checks that `export_classes_csv.py` creates the expected CSV and demonstrates how the Vectorworks API can be stubbed for testing.
