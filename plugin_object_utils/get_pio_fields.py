try:
    import vs
except ImportError:
    raise SystemExit('This script must be executed inside Vectorworks with the vs module.')


OBJ_VAR_OFFSET = 5  # plugin parameter object variables start at index 5


def get_object_var_value(handle, index):
    """Return the object variable value from ``handle`` at ``index``.

    The function tries the Vectorworks GetObjectVariable* calls in a sensible
    order and returns the first non ``None`` result.
    """
    value = vs.GetObjectVariableString(handle, index)
    if value:
        return value

    value = vs.GetObjectVariableReal(handle, index)
    if value != 0:
        return value

    value = vs.GetObjectVariableInt(handle, index)
    if value != 0:
        return value

    value = vs.GetObjectVariableLongInt(handle, index)
    if value != 0:
        return value

    value = vs.GetObjectVariableBoolean(handle, index)
    if value:
        return value

    handle_val = vs.GetObjectVariableHandle(handle, index)
    if handle_val:
        return handle_val

    return None


def get_pio_fields(handle):
    """Return a list of ``(name, value)`` for the parameters of a plug-in object.

    ``GetCustomObjectInfo`` historically returned four values, but newer
    Vectorworks versions include a leading boolean and may append additional
    values. The implementation therefore accepts either variant.
    """
    result = vs.GetCustomObjectInfo()
    vs.AlrtDialog(str(result))

    # Normalize the return signature to ``(success, name, obj, record, wall)``.
    if len(result) >= 5:
        success, obj_name, obj_handle, record_handle, wall_handle = result[:5]
    else:
        success = True
        obj_name, obj_handle, record_handle, wall_handle = result[:4]

    if not success or handle != obj_handle:
        return []

    num_params = vs.NumFields(record_handle)
    record_name = vs.GetName(record_handle)

    fields = []
    for i in range(1, num_params + 1):
        name = vs.GetFldName(record_handle, i)
        value = get_object_var_value(handle, OBJ_VAR_OFFSET + i)
        if value is None:
            # Fallback to record field as string
            value = vs.GetRField(handle, record_name, name)
        fields.append((name, value))
    return fields


def main():
    h = vs.FSActLayer()
    if not h:
        vs.AlrtDialog('Please select a plug-in object.')
        return

    all_lines = []
    while h:
        fields = get_pio_fields(h)
        if not fields:
            vs.AlrtDialog('Selected object is not a plug-in object.')
        else:
            lines = [f'{name}: {value}' for name, value in fields]
            all_lines.append('\n'.join(lines))
        h = vs.NextSObj(h)

    if all_lines:
        vs.AlrtDialog('\n\n'.join(all_lines))


if __name__ == '__main__':
    main()
