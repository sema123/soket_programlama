import generalfunctions

HOST=generalfunctions.HOST
PORT=generalfunctions.PORT

def client_yakala(sock,addr):
    try:
        msg=generalfunctions.gelen_mesaj(sock)
        print("{} : {}".format(addr,msg))
        generalfunctions.mesaj_gonder(sock, msg)
    except ConnectionError as cerror:
        print("Hata",cerror.strerror)
    except BrokenPipeError as berror:
        print("Hata",berror.strerror)
    finally:
        sock.close()

if __name__ =="__main__":
    listen_sock = generalfunctions.socket_olustur_dinle(HOST,PORT)
    addr=listen_sock.getsockname()

    print("{}adres uzerinde dinleniyor".format(addr))

    while True:
        client_sock, addr = listen_sock.accept()
        print("{}adresinden baglanti geldi".format(addr))
        client_yakala(client_sock, addr)