import rpyc
from constRPYC import * #-

class Client:
  conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT) # Connect to the directory server
  (addr, port) = conn_directory.root.exposed_lookup('DBList')
  print (addr, port)

  conn = rpyc.connect(addr, port)
  conn.root.exposed_append(2)       # Call an exposed operation,
  conn.root.exposed_append(4)       # and append two elements
  print (conn.root.exposed_value())   # Print the result
