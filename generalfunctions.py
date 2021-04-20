import socket

HOST = "127.0.0.1"
PORT = 4040

def socket_olustur_dinle(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind((host,port))
    sock.listen(100)
    return sock

def gelen_mesaji_ayir(msg):
    parcalar= msg.split(b'\0')
    msgs=parcalar[:-1]
    kalan=parcalar[-1]
    return(msgs,kalan)

def gelen_mesajlar(sock, veri=bytes()):
    msgs = []

    while not msgs:
        gelen=sock.recv(4096)
        if not gelen:
             raise ConnectionError()

        veri=veri+gelen
        (msgs,kalan)=gelen_mesaji_ayir(veri)

    msgs=[msg.decode("utf-8") for msg in msg]
    return (msgs,kalan)



def gelen_mesaj(sock):

    veri = bytearray()
    msg = ""

    while not msg:
        gelen = sock.recv(4096)

        if not gelen:
            raise ConnectionError()
        veri = veri + gelen
        if b'\0' in gelen:
            msg = veri.rstrip(b'\0')

    msg = msg.decode("utf-8")
    return msg

def gonderilecek_mesaj(msg):
     msg += "\0"
     return msg.encode("utf-8")

def mesaj_gonder(sock,msg):
    veri = gonderilecek_mesaj(msg)
    sock.sendall(veri)

