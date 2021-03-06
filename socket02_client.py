import socket
import pickle

class Client:
  def __init__(self, server_ip="127.0.0.1", server_port=8989):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.socket.setblocking(0)
    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.serv_addr=(server_ip, server_port)
    self.entities = {}

  def send(self, ):
    self.socket.sendto(pickle.dumps([1.0, -1.0, 0.57997]),self.serv_addr)

  def receive(self):
    try:
        data, addr = self.socket.recvfrom(1024)
        print('from',addr,'data',data)
    except socket.error as e:
        return

client = Client()
client.send()
client.receive()