import zerorpc

class RPCPayment(object):
    saldo = 200000
    def check_saldo(self, a):
        if self.saldo > int(a):
            return 1
        else:
            return 0

try :
    s = zerorpc.Server(RPCPayment())
    s.bind("tcp://0.0.0.0:9999")
    s.run()
except KeyboardInterrupt:
    print("Keluar")
