# implementasi server di sini
import zerorpc
import threading
import paho.mqtt.client as mqtt
import json

class ServerRS(object):

    data_all_pasien = []
    def recv_data(self,_nik,_nama,_alamat,_penyakit):
        data_pasien = {
            "nik": _nik,
            "nama": _nama,
            "alamat": _alamat,
            "penyakit": _penyakit
        }
        data_all_pasien.append(data_pasien)
        return data_pasien
    def send_data_rs(self,_namars):
        self.client=mqtt.Client(client_id=_namars, clean_session=False)
        self.client.connect("127.0.0.1", port=1883)
        self.client.publish("patient",payload=json.dumps(data_all_pasien),qos=1)
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
    def on_message(self,client,obj,msg):
        print(msg.payload)
    

    def __init__(self):
        try:
            nama_rs = input("Nama Rumah Sakit : ")
            send_data_rs(nama_rs)
            self.client=mqtt.Client(client_id=nama_rs, clean_session=False)
            self.client.connect("127.0.0.1", port=1883)
            self.client.subscribe("patient",qos=1)
            self.client.on_connect=self.on_connect
            self.client.on_message=self.on_message
            server_port = input("Port RPC Server Rumah Sakit : ")
            def conn():
                s = zerorpc.Server(ServerRS())
                s.bind("tcp://0.0.0.0:"+server_port)
                s.run()        
            clientThread = threading.Thread(target=conn, args=())
            clientThread.start()    def __init__(self):
        except KeyboardInterrupt:
            print("Keluar")

        

