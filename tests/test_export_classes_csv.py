import sys
import types
import csv
import os
from pathlib import Path
import importlib

def make_vs_stub(tmp_path, classes, return_file_path=False):
    vs = types.SimpleNamespace()
    vs.classes = classes
    vs.alerts = []

    vs.ClassNum = lambda: len(classes)
    vs.ClassList = lambda idx: classes[idx-1]
    vs.GetClassUseGraphic = lambda name: True
    vs.GetClUseGraphic = lambda name: True

    vs.GetClassPenWeight = lambda name: 15
    vs.GetClassLW = lambda name: 15
    vs.GetClassLineWeight = lambda name: 15
    vs.GetClLW = lambda name: 15

    vs.GetClassPenForeColor = lambda name: 1
    vs.GetClassPenFore = lambda name: 1
    vs.GetClPenFore = lambda name: 1
    vs.GetClassPenBackColor = lambda name: 2
    vs.GetClassPenBack = lambda name: 2
    vs.GetClPenBack = lambda name: 2

    # Conversion from color index to RGB tuple
    vs.ColorIndexToRGB = lambda idx: (idx, idx, idx)
    vs.IndexToRGB = lambda idx: (idx, idx, idx)

    vs.GetClassLineStyle = lambda name: 3
    vs.GetClassLS = lambda name: 3
    vs.GetClLS = lambda name: 3

    vs.GetClassFillPattern = lambda name: 4
    vs.GetClassFPat = lambda name: 4
    vs.GetClassFillPat = lambda name: 4
    vs.GetClFPat = lambda name: 4

    vs.GetClassFillForeColor = lambda name: 5
    vs.GetClassFillFore = lambda name: 5
    vs.GetClFillFore = lambda name: 5
    vs.GetClassFillBackColor = lambda name: 6
    vs.GetClassFillBack = lambda name: 6
    vs.GetClFillBack = lambda name: 6

    vs.GetClassVisibility = lambda name: 0
    vs.GetCVis = lambda name: 0

    vs.GetClassUseFill = lambda name: True
    vs.GetClassUseFillAttrs = lambda name: True
    vs.GetClUseFill = lambda name: True
    vs.GetClUseFillAttrs = lambda name: True

    vs.GetClassFillColor = lambda name: 7
    vs.GetClFillColor = lambda name: 7

    vs.GetClassSyncLineOpacity = lambda name: True
    vs.GetClSyncLineOpacity = lambda name: True

    vs.GetClassOpacity = lambda name: 80
    vs.GetClOpacity = lambda name: 80
    vs.GetClassFillOpacity = lambda name: 80
    vs.GetClFillOpacity = lambda name: 80

    vs.GetClassUseDropShadow = lambda name: True
    vs.GetClUseDropShadow = lambda name: True

    vs.GetClassDropShadowOffsetX = lambda name: 2.54
    vs.GetClDropShadowOffsetX = lambda name: 2.54
    vs.GetClassDropShadowOffsetY = lambda name: 2.54
    vs.GetClDropShadowOffsetY = lambda name: 2.54
    vs.GetClassDropShadowBlur = lambda name: 1.27
    vs.GetClDropShadowBlur = lambda name: 1.27
    vs.GetClassDropShadowColor = lambda name: 8
    vs.GetClDropShadowColor = lambda name: 8
    vs.GetClassDropShadowOpacity = lambda name: 50
    vs.GetClDropShadowOpacity = lambda name: 50
    vs.GetClassDropShadowAngle = lambda name: 45
    vs.GetClDropShadowAngle = lambda name: 45

    vs.GetClassPenColor = lambda name: 1
    vs.GetClPenColor = lambda name: 1
    vs.GetClassLineColor = lambda name: 1
    vs.GetClLineColor = lambda name: 1

    vs.GetClassLineThickness = lambda name: 0.1
    vs.GetClassPenThickness = lambda name: 0.1
    vs.GetClLineThickness = lambda name: 0.1
    vs.GetClPenThickness = lambda name: 0.1

    vs.GetClassLineMarker = lambda name: 'arrow'
    vs.GetClLineMarker = lambda name: 'arrow'

    vs.GetClassLineOpacity = lambda name: 90
    vs.GetClLineOpacity = lambda name: 90

    vs.GetClassUseTextAttrs = lambda name: True
    vs.GetClUseTextAttrs = lambda name: True
    vs.GetClassUseText = lambda name: True

    vs.GetClassTextStyle = lambda name: 'ゴシック'
    vs.GetClTextStyle = lambda name: 'ゴシック'
    vs.GetClUseTextStyle = lambda name: True
    vs.GetClassBeginningMarker = lambda name: (1, 2, 3)
    vs.GetClassEndMarker = lambda name: (4, 5, 6)
    vs.GetClassByStyle = lambda name: False
    vs.GetClOpacityN = lambda name: 75
    vs.GetClVectorFill = lambda name: 'pattern'
    vs.GetCLDropShadowEnabled = lambda name: True
    vs.GetClassOptions = lambda name: 3
    vs.GetCLDrpShadowData = lambda name: (1, 2, 3, 4, 5, 6, 7, 8)
    vs.GetClLSN = lambda name: 12
    vs.GetClTextStyleRef = lambda name: 'ref'
    if return_file_path:
        vs.GetFPathName = lambda: str(tmp_path / 'doc.vwx')
    else:
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
    assert 'use_fill_attrs' not in attrs
    assert attrs['line_color_fore'] == '(1, 1, 1)'
    assert attrs['fill_color_fore'] == '(5, 5, 5)'
    assert attrs['line_thickness'] == 0.1
    assert attrs['shadow_offset_x'] == 2.54
    assert attrs['use_text_style'] is True
    assert attrs['beginning_marker'] == (1, 2, 3)
    assert attrs['end_marker'] == (4, 5, 6)
    assert attrs['by_style'] is False
    assert attrs['opacity_n'] == 75
    assert attrs['vector_fill'] == 'pattern'
    assert attrs['drop_shadow_enabled'] is True
    assert attrs['class_options'] == 3
    assert attrs['drop_shadow_data'] == (1, 2, 3, 4, 5, 6, 7, 8)
    assert attrs['line_style_n'] == 12
    assert attrs['text_style_ref'] == 'ref'


def test_main_exports_csv(tmp_path):
    classes = ['A', 'B']
    vs_stub = make_vs_stub(tmp_path, classes)
    module = load_module(vs_stub)

    desktop = tmp_path / 'Desktop'
    desktop.mkdir()
    old_home = os.environ.get('HOME')
    os.environ['HOME'] = str(tmp_path)
    try:
        module.main()
    finally:
        if old_home is not None:
            os.environ['HOME'] = old_home
        else:
            del os.environ['HOME']

    csv_file = desktop / 'class_settings.csv'
    assert csv_file.exists()

    with csv_file.open() as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == len(classes)
    assert rows[0]['name'] == 'A'
    assert 'line_thickness' in rows[0]
    assert 'shadow_offset_x' in rows[0]
    assert 'use_text_style' in rows[0]
    assert 'drop_shadow_enabled' in rows[0]
    assert rows[0]['line_weight'] == '15'
    assert rows[0]['line_color_fore'] == '(1, 1, 1)'
    assert rows[0]['vector_fill'] == 'pattern'
    assert rows[0]['drop_shadow_data'] == '(1, 2, 3, 4, 5, 6, 7, 8)'
    assert rows[0]['visibility'] == '0'
    assert vs_stub.alerts
    assert 'Class settings exported to:' in vs_stub.alerts[-1]


def test_main_exports_csv_with_vwx_path(tmp_path):
    classes = ['A']
    vs_stub = make_vs_stub(tmp_path, classes, return_file_path=True)
    module = load_module(vs_stub)

    desktop = tmp_path / 'Desktop'
    desktop.mkdir()
    old_home = os.environ.get('HOME')
    os.environ['HOME'] = str(tmp_path)
    try:
        module.main()
    finally:
        if old_home is not None:
            os.environ['HOME'] = old_home
        else:
            del os.environ['HOME']

    csv_file = desktop / 'class_settings.csv'
    assert csv_file.exists()


def test_drop_shadow_data_none(tmp_path):
    vs_stub = make_vs_stub(tmp_path, ['A'])
    vs_stub.GetCLDrpShadowData = lambda name: None
    module = load_module(vs_stub)

    desktop = tmp_path / 'Desktop'
    desktop.mkdir()
    old_home = os.environ.get('HOME')
    os.environ['HOME'] = str(tmp_path)
    try:
        module.main()
    finally:
        if old_home is not None:
            os.environ['HOME'] = old_home
        else:
            del os.environ['HOME']

    csv_file = desktop / 'class_settings.csv'
    with csv_file.open() as f:
        rows = list(csv.DictReader(f))

    assert rows[0]['drop_shadow_data'] == ''


def test_drop_shadow_data_formatted(tmp_path):
    vs_stub = make_vs_stub(tmp_path, ['A'])
    module = load_module(vs_stub)

    desktop = tmp_path / 'Desktop'
    desktop.mkdir()
    old_home = os.environ.get('HOME')
    os.environ['HOME'] = str(tmp_path)
    try:
        module.main()
    finally:
        if old_home is not None:
            os.environ['HOME'] = old_home
        else:
            del os.environ['HOME']

    csv_file = desktop / 'class_settings.csv'
    with csv_file.open() as f:
        rows = list(csv.DictReader(f))

    assert rows[0]['drop_shadow_data'] == '(1, 2, 3, 4, 5, 6, 7, 8)'

