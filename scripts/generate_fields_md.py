import re
import sys
import types
from pathlib import Path

# Ensure the repository root is on sys.path so we can import export_classes_csv
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Provide a minimal stub for the Vectorworks `vs` module so that
# `export_classes_csv` can be imported outside of Vectorworks.
sys.modules.setdefault('vs', types.SimpleNamespace())
from export_classes_csv import get_class_attributes


def main():
    keys = sorted(get_class_attributes('Dummy').keys())
    lines = [f"- `{k}`" for k in keys]

    template = Path('README.md.template').read_text(encoding='utf-8')
    new_md = re.sub(
        r"<!--FIELDS-->[\s\S]*?<!--/FIELDS-->",
        "<!--FIELDS-->\n" + "\n".join(lines) + "\n<!--/FIELDS-->",
        template,
    )
    Path('README.md').write_text(new_md, encoding='utf-8')


if __name__ == '__main__':
    main()
