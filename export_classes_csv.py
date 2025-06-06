import csv
import os

try:
    import vs
except ImportError:
    raise SystemExit('This script must be executed inside Vectorworks with the vs module.')


def _call_vs_function(possible_names, *args):
    """Call the first available Vectorworks function from ``possible_names``.

    ``possible_names`` is an iterable of function name strings.  This helper now
    prints the name of the Vectorworks function that will be called so that, when
    running the script inside Vectorworks, it is easy to see which API is in use
    and spot deprecated calls.
    """

    for name in possible_names:
        func = getattr(vs, name, None)
        if callable(func):
            print(f"\u2192 \u547c\u3073\u51fa\u3057\u5148 vs \u95a2\u6570: {name}(), \u5f15\u6570: {args}")
            return func(*args)
        else:
            print(f"  \u2605 vs\u30e2\u30b8\u30e5\u30fc\u30eb\u306b '{name}' \u3068\u3044\u3046\u95a2\u6570\u304c\u898b\u3064\u304b\u308a\u307e\u305b\u3093\u3067\u3057\u305f。")

    raise AttributeError(
        f"None of the following Vectorworks functions are available: {possible_names}"
    )


def get_class_attributes(class_name):
    """Return a dictionary with common class attributes."""
    attrs = {
        'name': class_name,
        'use_graphic': _call_vs_function(
            ['GetClassUseGraphic', 'GetClUseGraphic'], class_name
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
        'line_color_fore': _call_vs_function(
            ['GetClassPenForeColor', 'GetClassPenFore', 'GetClPenFore'],
            class_name,
        ),
        'line_color_back': _call_vs_function(
            ['GetClassPenBackColor', 'GetClassPenBack', 'GetClPenBack'],
            class_name,
        ),
        'line_style': _call_vs_function(
            ['GetClassLineStyle', 'GetClassLS', 'GetClLS'], class_name
        ),
        'fill_style': _call_vs_function(
            [
                'GetClassFillPattern',
                'GetClassFPat',
                'GetClassFillPat',
                'GetClFPat',
            ],
            class_name,
        ),
        'fill_color_fore': _call_vs_function(
            ['GetClassFillForeColor', 'GetClassFillFore', 'GetClFillFore'],
            class_name,
        ),
        'fill_color_back': _call_vs_function(
            ['GetClassFillBackColor', 'GetClassFillBack', 'GetClFillBack'],
            class_name,
        ),
        'visibility': _call_vs_function(
            ['GetClassVisibility', 'GetCVis'], class_name
        ),
        'use_fill_attrs': _call_vs_function(
            [
                'GetClassUseFill',
                'GetClassUseFillAttrs',
                'GetClUseFill',
                'GetClUseFillAttrs',
            ],
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
                'GetClassLineWeight',
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
    }
    return attrs


def main():
    num_classes = vs.ClassNum()
    class_data = []
    for idx in range(1, num_classes + 1):
        class_name = vs.ClassList(idx)
        attrs = get_class_attributes(class_name)
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
