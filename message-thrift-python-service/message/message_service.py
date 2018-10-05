from message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class MessageServiceHandler:
    def sendMobileMessage(self, mobile, message):
        print "sendMobileMessage"
        return True

    def sendEmailMessage(self, email, message):
        print "sendEmailMessage"
        return True
if _name_ == '_main_':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket(None, "9090")
    tfactory - 