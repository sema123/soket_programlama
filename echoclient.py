import socket
import generalfunctions

HOST="127.0.0.1"
PORT=generalfunctions.PORT

if __name__=="__main__":
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            print("{}:{} bagladi".format(HOST, PORT))
            print("mesajinizi giriniz (cikmak icin q):")
            msg = input()
            if msg == "q":
                break
            generalfunctions.mesaj_gonder(sock, msg)
            print("mesaj gonderildi:{}".format(msg))

            msg = generalfunctions.gelen_mesaj(sock)
            print("Alinan echo :" +msg)

        except ConnectionError as cerror:
            print("Hata",cerror.args)
            break
        finally:
            sock.close()
            print("Baglanti sonlandi")
