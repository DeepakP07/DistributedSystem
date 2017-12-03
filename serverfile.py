import sys, socket
import threading
import Queue
import SocketServer
import os
import re
from cache import Cache
from locker import Locker
from fileserver import FileServer




  pool_size = 9
  student_id = "17310212"
  current_dir = DFS_ROOT_DIR
  cache = Cache()
  locker = Locker()
  servers = {}
  a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  a2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #Connect to first file server and pass its directory
  address = ("0.0.0.0", 8000)
  a.connect(address)
  a.send(FILE_SERVER1_DIR)
  data = a.recv(512)
  print data
