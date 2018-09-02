from  bge import logic, types, events
import socket
import pickle

class Server :
  def __init__(self, host="127.0.0.1", port=8989):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.socket.setblocking(0)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.socket.bind((host,port))
    self.addr_user={}
    print('server created')

  def receive(self):
    try:
        data, addr = self.socket.recvfrom(1024)
        print(data, pickle.loads(data), addr)

    except Exception as e:
        return

def update(ctrl) :
  if not 'server' in ctrl.owner.getPropertyNames() :
    ctrl.owner['server'] = Server()
  ctrl.owner['server'].receive()

