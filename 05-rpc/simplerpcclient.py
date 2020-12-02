import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
# print(c.hello("RPC"))
hasil = c.add(20,10)
print(hasil)