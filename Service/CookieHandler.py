def handleCookie(cookies):
    str=''
    index = 0
    mapsize = len(cookies)
    for k, v in cookies.items():
        index = index + 1
        str += k + "=" + v
        if (index != mapsize):
            str += "; "
    return str