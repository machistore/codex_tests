import re
import pytest
from export_classes_csv import get_class_attributes

def load_fields(path):
    text = open(path, encoding='utf-8').read()
    return set(re.findall(r'- `([^`]+)`', text))

def test_readme_fields_up_to_date():
    code_keys = set(get_class_attributes('Dummy').keys())
    md_keys = load_fields('README.md')
    assert code_keys == md_keys, "README fields are out of sync with code"
