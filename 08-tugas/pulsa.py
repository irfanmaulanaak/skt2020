import zerorpc
import threading
import paho.mqtt.client as mqtt

class RPCPulsa(object):

    def get_status(self,amount):
        return self.c.check_saldo(amount)

    def recv_order(self, a, b):
        self.c = zerorpc.Client()
        self.c.connect("tcp://127.0.0.1:9999")
        self.client = mqtt.Client(client_id="pub1", clean_session=False)
        self.client.connect("127.0.0.1", port=1883)
        status = self.get_status(b)
        if status:
            self.client.publish("/"+a, payload="Transaksi Berhasil", qos=1)
        else:
            self.client.publish("/"+a, payload="Transaksi Gagal", qos=1)
try :
    def conn():
        s = zerorpc.Server(RPCPulsa())
        s.bind("tcp://0.0.0.0:4242")
        s.run()
    clientThread = threading.Thread(target=conn, args=())
    clientThread.start()
except KeyboardInterrupt:
    print("Keluar")
