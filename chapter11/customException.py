class ConnectionException(Exception):
    pass

try:
    raise ConnectionException('Cannot connect ... is it time to panic?')
except ConnectionException as e:
    print('Got:', str(e))