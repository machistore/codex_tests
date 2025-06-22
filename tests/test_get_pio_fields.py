import sys
import types
from pathlib import Path
import runpy


def make_vs_stub(num_returns=5, success=True, selected_handles=None):
    vs = types.SimpleNamespace()
    vs.alerts = []
    base = (success, 'obj', None, 'rec_handle', 'wall_handle')

    if num_returns == 4:
        # Historical API without the leading boolean
        return_vals = base[1:]
    else:
        extras = tuple(f'extra{i}' for i in range(num_returns - 5)) if num_returns > 5 else ()
        return_vals = base + extras

    if selected_handles is None:
        selected_handles = ['obj_handle']

    vs.current_handle = selected_handles[0] if selected_handles else None

    def get_custom_object_info():
        vals = list(return_vals)
        if len(vals) >= 5:
            vals[2] = vs.current_handle
        else:
            vals[1] = vs.current_handle
        return tuple(vals)

    vs.GetCustomObjectInfo = get_custom_object_info

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

    def fs_act_layer():
        vs.current_handle = selected_handles[0] if selected_handles else None
        return vs.current_handle

    vs.FSActLayer = fs_act_layer

    next_map = {selected_handles[i]: selected_handles[i + 1] for i in range(len(selected_handles) - 1)}

    def next_s_obj(h):
        vs.current_handle = next_map.get(h)
        return vs.current_handle

    vs.NextSObj = next_s_obj
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


def test_main_no_selection(tmp_path):
    vs_stub = make_vs_stub(selected_handles=[])
    mod = load_module(vs_stub)
    mod['main']()
    assert vs_stub.alerts[-1] == 'Please select a plug-in object.'


def test_main_multiple_objects(tmp_path):
    vs_stub = make_vs_stub(selected_handles=['obj_handle', 'obj2'])
    mod = load_module(vs_stub)
    mod['main']()
    expected = (
        'field1: rec_field1\nfield2: rec_field2\n\n'
        'field1: rec_field1\nfield2: rec_field2'
    )
    assert vs_stub.alerts[-1] == expected


def test_main_invalid_object(tmp_path):
    vs_stub = make_vs_stub(success=False)
    mod = load_module(vs_stub)
    mod['main']()
    assert vs_stub.alerts[-1] == 'Selected object is not a plug-in object.'
