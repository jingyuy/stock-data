
def getIntOrNull(str):
    try:
        value = int(str)
        return value
    except ValueError:
        return None