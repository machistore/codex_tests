import sys
import types
import csv
from pathlib import Path
import importlib

def make_vs_stub(tmp_path, classes):
    vs = types.SimpleNamespace()
    vs.classes = classes
    vs.alerts = []

    vs.ClassNum = lambda: len(classes)
    vs.ClassList = lambda idx: classes[idx-1]
    vs.GetClUseGraphic = lambda name: True
    vs.GetClPenWeight = lambda name: 15
    vs.GetClPenFore = lambda name: 1
    vs.GetClPenBack = lambda name: 2
    vs.GetClPenStyle = lambda name: 3
    vs.GetClFillStyle = lambda name: 4
    vs.GetClFillFore = lambda name: 5
    vs.GetClFillBack = lambda name: 6
    vs.GetClassVisibility = lambda name: 0
    vs.GetFPathName = lambda: str(tmp_path)
    vs.AlrtDialog = lambda msg: vs.alerts.append(msg)
    return vs


def load_module(vs_stub):
    sys.modules['vs'] = vs_stub
    repo_root = Path(__file__).resolve().parents[1]
    if str(repo_root) not in sys.path:
        sys.path.insert(0, str(repo_root))
    if 'export_classes_csv' in sys.modules:
        del sys.modules['export_classes_csv']
    return importlib.import_module('export_classes_csv')


def test_get_class_attributes(tmp_path):
    vs_stub = make_vs_stub(tmp_path, ['Test'])
    module = load_module(vs_stub)
    attrs = module.get_class_attributes('Test')
    assert attrs['name'] == 'Test'
    assert attrs['line_weight'] == 15
    assert attrs['visibility'] == 0


def test_main_exports_csv(tmp_path):
    classes = ['A', 'B']
    vs_stub = make_vs_stub(tmp_path, classes)
    module = load_module(vs_stub)

    module.main()

    csv_file = tmp_path / 'class_settings.csv'
    assert csv_file.exists()

    with csv_file.open() as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == len(classes)
    assert rows[0]['name'] == 'A'
    assert vs_stub.alerts
    assert 'Class settings exported to:' in vs_stub.alerts[-1]

