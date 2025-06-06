import csv
import os

try:
    import vs
except ImportError:
    raise SystemExit('This script must be executed inside Vectorworks with the vs module.')


def _call_vs_function(possible_names, *args):
    """Try to call the first available Vectorworks function from
    ``possible_names`` with ``args``.
    ``possible_names`` should be an iterable of function name strings.
    """
    for name in possible_names:
        func = getattr(vs, name, None)
        if callable(func):
            return func(*args)
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
            ['GetClassLW', 'GetClassLineWeight', 'GetClLW'], class_name
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
            ['GetClassFPat', 'GetClassFillPat', 'GetClFPat'], class_name
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
