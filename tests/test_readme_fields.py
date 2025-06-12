import re
from pathlib import Path
import pytest
from export_classes_csv import get_class_attributes

def load_fields(path):
    text = Path(path).read_text(encoding='utf-8')
    m = re.search(r"<!--FIELDS-->(.*?)<!--/FIELDS-->", text, re.S)
    assert m, f"FIELDS markers missing in {path}; run scripts/generate_fields_md.py"
    return set(re.findall(r'- `([^`]+)`', m.group(1)))

@pytest.mark.parametrize(
    "filename,lang",
    [
        ("README.md", "README"),
        ("README.ja.md", "Japanese README"),
    ],
)
def test_readme_fields_up_to_date(filename, lang):
    code_keys = set(get_class_attributes("Dummy").keys())
    md_keys = load_fields(filename)
    assert (
        code_keys == md_keys
    ), f"{lang} fields are out of sync with code. Run scripts/generate_fields_md.py"
