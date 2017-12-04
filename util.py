# util module
def parse_url(SERVER):
    temp = SERVER.split(':')
    if len(temp) != 1:
        port = int(temp[1])
    else:
        port = 6667
    return temp[0], port