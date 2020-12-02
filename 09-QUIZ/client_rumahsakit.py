import zerorpc

c = zerorpc.Client()

server_ip = input("IP RPC Server Rumah Sakit : ")
server_port = input("Port RPC Server Rumah Sakit : ")


c.connect("tcp://"+server_ip+":"+server_port)

try:
    nik = input("NIK : ")
    nama = input("Nama : ")
    alamat = input("Alamat : ")
    penyakit = input("Penyakit : ")
    result = c.recv_data(nik,nama,alamat,penyakit)
    print(result)
except KeyboardInterrupt:
    print("Keluar")

