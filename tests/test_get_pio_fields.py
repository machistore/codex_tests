import sys
import types
from pathlib import Path
import runpy


def make_vs_stub(num_returns=5):
    vs = types.SimpleNamespace()
    vs.alerts = []
    if num_returns == 4:
        vs.GetCustomObjectInfo = lambda: ('obj', 'obj_handle', 'rec_handle', 'wall_handle')
    else:
        values = ('obj', 'obj_handle', 'rec_handle', 'wall_handle', 'extra')
        vs.GetCustomObjectInfo = lambda: values[:num_returns]

    vs.NumFields = lambda record: 2
    vs.GetName = lambda record: 'rec'
    vs.GetFldName = lambda record, idx: f'field{idx}'
    vs.GetRField = lambda h, rec, fld: f'{rec}_{fld}'
    vs.GetObjectVariableString = lambda h, i: ''
    vs.GetObjectVariableReal = lambda h, i: 0
    vs.GetObjectVariableInt = lambda h, i: 0
    vs.GetObjectVariableLongInt = lambda h, i: 0
    vs.GetObjectVariableBoolean = lambda h, i: False
    vs.GetObjectVariableHandle = lambda h, i: None
    vs.FSActLayer = lambda: 'obj_handle'
    vs.AlrtDialog = lambda msg: vs.alerts.append(msg)
    return vs


def load_module(vs_stub):
    sys.modules['vs'] = vs_stub
    repo_root = Path(__file__).resolve().parents[1]
    path = repo_root / 'plugin_object_utils' / 'get_pio_fields.py'
    return runpy.run_path(str(path))


def test_get_pio_fields_with_extra_values(tmp_path):
    vs_stub = make_vs_stub(5)
    mod = load_module(vs_stub)
    fields = mod['get_pio_fields']('obj_handle')
    assert fields == [('field1', 'rec_field1'), ('field2', 'rec_field2')]


def test_get_pio_fields_four_values(tmp_path):
    vs_stub = make_vs_stub(4)
    mod = load_module(vs_stub)
    fields = mod['get_pio_fields']('obj_handle')
    assert fields == [('field1', 'rec_field1'), ('field2', 'rec_field2')]


def test_get_pio_fields_wrong_handle(tmp_path):
    vs_stub = make_vs_stub(5)
    mod = load_module(vs_stub)
    fields = mod['get_pio_fields']('other')
    assert fields == []
