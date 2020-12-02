import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

try : 
    nomor = input("Masukkan nomor HP: ")
    pulsa = input("Masukkan jumlah pulsa yang akan dibeli: ")
    result = c.recv_order(nomor,pulsa)
    print(result)
except KeyboardInterrupt:
    print("Keluar")