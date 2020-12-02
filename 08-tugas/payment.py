import zerorpc

class RPCPayment(object):
    saldo = 200000
    def check_saldo(self, a):
        print(int(a))
        print(self.saldo)
        check = int(a) < self.saldo
        print(check)
        if check:
            self.saldo -= int(a)
            return check

try :
    s = zerorpc.Server(RPCPayment())
    s.bind("tcp://0.0.0.0:9999")
    s.run()
except KeyboardInterrupt:
    print("Keluar")
