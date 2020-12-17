
def blink(num, speed, pin=2):
    """Blink helper"""
    import machine
    import time

    pin = machine.Pin(pin, machine.Pin.OUT)
    pin.on()
    def toggle(p):
        p.value(not p.value())

    s = 500
    if speed is 'fast':
        s = 150
    for x in range(2*num):
        toggle(pin)
        time.sleep_ms(s)


def debug(msg):
    """print or send to email or do nothing"""
    print(msg)

    # simple http client call
def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, PROXY_PORT)[0][-1]
    #print(addr)
    s = socket.socket()
    s.settimeout(12.0)
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    ret = ''
    while True:
        data = s.recv(100)
        if data:
            ret += str(data, 'utf8')
        else:
            break
    s.close()
    return ret
