import zerorpc

class RPCPulsa(object):

    def recv_order(self, a, b):
        c = zerorpc.Client()
        c.connect("tcp://127.0.0.1:9999")
        status = c.check_saldo(b)
        if status == 1:
            return "Pulsa sebesar %s sukses diisi ke nomor %s." % (b,a)
        else:
            return "Saldo tidak mencukupi"
try :
    s = zerorpc.Server(RPCPulsa())
    s.bind("tcp://0.0.0.0:4242")
    s.run()
except KeyboardInterrupt:
    print("Keluar")
