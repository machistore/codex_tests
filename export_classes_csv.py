import csv
import os

try:
    import vs
except ImportError:
    raise SystemExit('This script must be executed inside Vectorworks with the vs module.')


def _call_vs_function(possible_names, *args):
    """Call the first available Vectorworks function from ``possible_names``.

    ``possible_names`` is an iterable of function name strings.  The first
    callable attribute found on ``vs`` will be invoked.  If none of the names
    exist, ``None`` is returned so that callers can handle missing APIs without
    raising ``AttributeError``.
    """

    for name in possible_names:
        func = getattr(vs, name, None)
        if callable(func):
            return func(*args)

    return None


def _color_to_tuple_string(color_index):
    """Convert a Vectorworks color index to an RGB tuple string if possible."""
    rgb = None
    if isinstance(color_index, (tuple, list)) and len(color_index) == 3:
        rgb = color_index
    else:
        rgb = _call_vs_function(
            [
                'ColorIndexToRGB',
                'IndexToRGB',
                'NumToRGB',
            ],
            color_index,
        )

    if isinstance(rgb, (tuple, list)) and len(rgb) == 3:
        return f"({rgb[0]}, {rgb[1]}, {rgb[2]})"

    return str(color_index)


def get_class_attributes(class_name):
    """Return a dictionary with common class attributes."""
    attrs = {
        'name': class_name,
        'use_graphic': _call_vs_function(
            ['GetClassUseGraphic', 'GetClUseGraphic'],
            class_name,
        ),
        'line_weight': _call_vs_function(
            [
                'GetClassPenWeight',
                'GetClassLW',
                'GetClassLineWeight',
                'GetClLW',
            ],
            class_name,
        ),
        'line_color_fore': _color_to_tuple_string(
            _call_vs_function(
                ['GetClassPenForeColor', 'GetClassPenFore', 'GetClPenFore'],
                class_name,
            )
        ),
        'line_color_back': _color_to_tuple_string(
            _call_vs_function(
                ['GetClassPenBackColor', 'GetClassPenBack', 'GetClPenBack'],
                class_name,
            )
        ),
        'line_style': _call_vs_function(
            ['GetClassLineStyle', 'GetClassLS', 'GetClLS'],
            class_name,
        ),
        'fill_style': _call_vs_function(
            ['GetClassFillPattern', 'GetClassFPat', 'GetClassFillPat', 'GetClFPat'],
            class_name,
        ),
        'fill_color_fore': _color_to_tuple_string(
            _call_vs_function(
                ['GetClassFillForeColor', 'GetClassFillFore', 'GetClFillFore'],
                class_name,
            )
        ),
        'fill_color_back': _color_to_tuple_string(
            _call_vs_function(
                ['GetClassFillBackColor', 'GetClassFillBack', 'GetClFillBack'],
                class_name,
            )
        ),
        'visibility': _call_vs_function(
            ['GetClassVisibility', 'GetCVis'],
            class_name,
        ),
        'fill_color': _call_vs_function(
            ['GetClassFillColor', 'GetClFillColor'],
            class_name,
        ),
        'sync_line_opacity': _call_vs_function(
            ['GetClassSyncLineOpacity', 'GetClSyncLineOpacity'],
            class_name,
        ),
        'fill_opacity': _call_vs_function(
            [
                'GetClassOpacity',
                'GetClOpacity',
                'GetClassFillOpacity',
                'GetClFillOpacity',
            ],
            class_name,
        ),
        'use_drop_shadow': _call_vs_function(
            ['GetClassUseDropShadow', 'GetClUseDropShadow'],
            class_name,
        ),
        'shadow_offset_x': _call_vs_function(
            ['GetClassDropShadowOffsetX', 'GetClDropShadowOffsetX'],
            class_name,
        ),
        'shadow_offset_y': _call_vs_function(
            ['GetClassDropShadowOffsetY', 'GetClDropShadowOffsetY'],
            class_name,
        ),
        'shadow_blur': _call_vs_function(
            ['GetClassDropShadowBlur', 'GetClDropShadowBlur'],
            class_name,
        ),
        'shadow_color': _call_vs_function(
            ['GetClassDropShadowColor', 'GetClDropShadowColor'],
            class_name,
        ),
        'shadow_opacity': _call_vs_function(
            ['GetClassDropShadowOpacity', 'GetClDropShadowOpacity'],
            class_name,
        ),
        'shadow_angle': _call_vs_function(
            ['GetClassDropShadowAngle', 'GetClDropShadowAngle'],
            class_name,
        ),
        'line_color': _call_vs_function(
            [
                'GetClassPenColor',
                'GetClPenColor',
                'GetClassLineColor',
                'GetClLineColor',
            ],
            class_name,
        ),
        'line_thickness': _call_vs_function(
            [
                'GetClassLineThickness',
                'GetClassPenThickness',
                'GetClLineThickness',
                'GetClPenThickness',
            ],
            class_name,
        ),
        'line_marker': _call_vs_function(
            ['GetClassLineMarker', 'GetClLineMarker'],
            class_name,
        ),
        'line_opacity': _call_vs_function(
            ['GetClassLineOpacity', 'GetClLineOpacity'],
            class_name,
        ),
        'use_text_attrs': _call_vs_function(
            ['GetClassUseTextAttrs', 'GetClUseTextAttrs', 'GetClassUseText'],
            class_name,
        ),
        'text_style': _call_vs_function(
            ['GetClassTextStyle', 'GetClTextStyle'],
            class_name,
        ),
        'use_text_style': _call_vs_function(
            ['GetClUseTextStyle', 'GetClassUseTextStyle'],
            class_name,
        ),
        'beginning_marker': _call_vs_function(
            ['GetClassBeginningMarker', 'GetClBeginningMarker'],
            class_name,
        ),
        'end_marker': _call_vs_function(
            ['GetClassEndMarker', 'GetClEndMarker'],
            class_name,
        ),
        'by_style': _call_vs_function(
            ['GetClassByStyle', 'GetClByStyle'],
            class_name,
        ),
        'opacity_n': _call_vs_function(
            ['GetClOpacityN', 'GetClassOpacityN'],
            class_name,
        ),
        'vector_fill': _call_vs_function(
            ['GetClVectorFill', 'GetClassVectorFill'],
            class_name,
        ),
        'drop_shadow_enabled': _call_vs_function(
            ['GetCLDropShadowEnabled'],
            class_name,
        ),
        'class_options': _call_vs_function(
            ['GetClassOptions'],
            class_name,
        ),
        'drop_shadow_data': _call_vs_function(
            ['GetCLDrpShadowData'],
            class_name,
        ),
        'line_style_n': _call_vs_function(
            ['GetClLSN'],
            class_name,
        ),
        'text_style_ref': _call_vs_function(
            ['GetClTextStyleRef'],
            class_name,
        ),
    }
    return attrs


def main():
    num_classes = vs.ClassNum()
    class_data = []
    for idx in range(1, num_classes + 1):
        class_name = vs.ClassList(idx)
        attrs = get_class_attributes(class_name)
        if 'drop_shadow_data' in attrs:
            attrs['drop_shadow_data'] = str(attrs['drop_shadow_data'])
        class_data.append(attrs)

    if not class_data:
        vs.AlrtDialog('No classes found.')
        return

    base_path = vs.GetFPathName()
    if base_path.lower().endswith('.vwx'):
        base_path = os.path.dirname(base_path)
    csv_path = os.path.join(base_path, 'class_settings.csv')

    fieldnames = list(class_data[0].keys())
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(class_data)

    vs.AlrtDialog('Class settings exported to: ' + csv_path)


if __name__ == '__main__':
    main()
