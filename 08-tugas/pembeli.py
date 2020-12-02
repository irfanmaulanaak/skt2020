import zerorpc
import threading
import paho.mqtt.client as mqtt


nomor = input("Masukkan nomor HP: ")

client = mqtt.Client(client_id="sub"+nomor, clean_session=False)

client.connect("127.0.0.1", port=1883)

client.subscribe("/"+nomor, qos=1)

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

def on_message(client,obj,msg):
    print(msg.payload)

def on_connect(client, userData, flags, rc):
    print("Connected. Status "+str(rc))

client.on_connect = on_connect
client.on_message = on_message

def handle_thread(client):
    try : 
        client.loop_forever()
    except KeyboardInterrupt:
        print("Keluar")

clientThread = threading.Thread(target=handle_thread, args=(client,))
clientThread.start()

while True:
    pulsa = input("Masukkan jumlah pulsa yang akan dibeli: ")
    c.recv_order(nomor,pulsa)
