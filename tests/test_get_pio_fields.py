import sys
import types
from pathlib import Path
import runpy


def make_vs_stub(num_returns=5, success=True):
    vs = types.SimpleNamespace()
    vs.alerts = []
    base = (success, 'obj', 'obj_handle', 'rec_handle', 'wall_handle')

    if num_returns == 4:
        # Historical API without the leading boolean
        return_vals = base[1:]
    else:
        extras = tuple(f'extra{i}' for i in range(num_returns - 5)) if num_returns > 5 else ()
        return_vals = base + extras

    vs.GetCustomObjectInfo = lambda: return_vals

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


def test_get_pio_fields_with_bool_and_extra(tmp_path):
    # bool flag + 4 expected values + one extra value
    vs_stub = make_vs_stub(6)
    mod = load_module(vs_stub)
    fields = mod['get_pio_fields']('obj_handle')
    assert fields == [('field1', 'rec_field1'), ('field2', 'rec_field2')]


def test_get_pio_fields_no_bool(tmp_path):
    vs_stub = make_vs_stub(4)
    mod = load_module(vs_stub)
    fields = mod['get_pio_fields']('obj_handle')
    assert fields == [('field1', 'rec_field1'), ('field2', 'rec_field2')]


def test_get_pio_fields_failure_flag(tmp_path):
    vs_stub = make_vs_stub(5, success=False)
    mod = load_module(vs_stub)
    fields = mod['get_pio_fields']('obj_handle')
    assert fields == []


def test_get_pio_fields_wrong_handle(tmp_path):
    vs_stub = make_vs_stub(5)
    mod = load_module(vs_stub)
    fields = mod['get_pio_fields']('other')
    assert fields == []
