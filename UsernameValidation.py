def CodelandUsernameValidation(strParam):
    str = strParam
    #condition 1: The username is between 4 and 25 characters

    if len(str)<4 or len(str)>25:
        return "false"

    #condition 2: It must start with a letter.

    elif ((ord(str[0]) < 65) or (ord(str[0])> 90 and ord(str[0]) < 97) or (ord(str[0]) > 122)):
        return "false"

    #condition 4: It cannot end with an underscore character.


    if str[-1] == "_":
        return "false"

    #condition 3:  It can only contain letters, numbers, and the underscore character.

    a=0
    length=len(str)

    while a < length:
        if not (((ord(str[a])>64 and ord(str[a])<91) or (ord(str[a])>96 and ord(str[a])<123)) or (ord(str[a])>47 and ord(str[a])<58) or (str[a]=="_")):
            return("false")
            break
        a+=1

    return "true"
