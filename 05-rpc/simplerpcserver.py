import zerorpc

class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name
    def add (self,num1,num2):
        return (num1 + num2)
    def substract(self,num1,num2):
        return (num1 - num2)
try :
    s = zerorpc.Server(HelloRPC())
    s.bind("tcp://0.0.0.0:4242")
    s.run()
except KeyboardInterrupt:
    print("Keluar")