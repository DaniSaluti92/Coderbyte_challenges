def FindIntersection(strArr):
    list_string_1 = strArr[0].split(',')
    list_1 = list(map(int, list_string_1))
    list_string_2 = strArr[-1].split(',')
    list_2 = list(map(int, list_string_2))
    intersection = []
    for i in list_1:
        for j in list_2:
            if i == j:
                intersection.append(i)

    for n in intersection:
        int(n)

    if intersection == []:
        return "false"
    else:
        return ','.join(map(str,intersection))
