def isnumber(value: str | int | float):
    """
    check if value can be converted to an integer.
    """
    if type(value) == int or type(value) == float:
        return True
    if type(value) != str:
        return False
    if value == '':
        return False
    if len(value.split('.')) == 2:
        return isnumber(value.split('.')[0]) and isnumber(value.split('.')[1])
    rt = list(value)
    if rt[0] == "-" and not value == "-":
        for i in range(1, len(rt)):
            if not rt[i] == "0" and not rt[i] == "1" and not rt[i] == "2" and not rt[i] == "3" and not rt[i] == "4" and not \
                    rt[
                        i] == "5" and not \
                    rt[i] == "6" and not rt[i] == "7" and not rt[i] == "8" and not rt[i] == "9":
                return False
    else:
        for i in range(0, len(rt)):
            if not rt[i] == "0" and not rt[i] == "1" and not rt[i] == "2" and not rt[i] == "3" and not rt[i] == "4" and not \
                    rt[
                        i] == "5" and not \
                    rt[i] == "6" and not rt[i] == "7" and not rt[i] == "8" and not rt[i] == "9":
                return False
    return True