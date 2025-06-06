import csv
import os

try:
    import vs
except ImportError:
    raise SystemExit('This script must be executed inside Vectorworks with the vs module.')


def get_class_attributes(class_name):
    """Return a dictionary with common class attributes."""
    attrs = {
        'name': class_name,
        'use_graphic': vs.GetClUseGraphic(class_name),
        'line_weight': vs.GetClPenWeight(class_name),
        'line_color_fore': vs.GetClPenFore(class_name),
        'line_color_back': vs.GetClPenBack(class_name),
        'line_style': vs.GetClPenStyle(class_name),
        'fill_style': vs.GetClFillStyle(class_name),
        'fill_color_fore': vs.GetClFillFore(class_name),
        'fill_color_back': vs.GetClFillBack(class_name),
        'visibility': vs.GetClassVisibility(class_name),
    }
    return attrs


def main():
    num_classes = vs.NumClasses()
    class_data = []
    for idx in range(1, num_classes + 1):
        class_name = vs.ClassList(idx)
        attrs = get_class_attributes(class_name)
        class_data.append(attrs)

    if not class_data:
        vs.AlrtDialog('No classes found.')
        return

    csv_path = os.path.join(vs.GetFPathName(), 'class_settings.csv')

    fieldnames = list(class_data[0].keys())
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(class_data)

    vs.AlrtDialog('Class settings exported to: ' + csv_path)


if __name__ == '__main__':
    main()
