import socket, threading

import test_get_world_pos
import get_pos

#practice github
#practice pushshshshshshshshshs

def binder(client_socket, addr):

  print('Connected by', addr)
  try:
    while True:
      #receive
      data = client_socket.recv(64)
      msg = data.decode()
     
      if msg == 'get_pos' :

        dx, dy = get_pos.get_pos()
        str_dx = str(dx)
        str_dy = str(dy)
        str_dx_dy = 'x' + str_dx + 'y' + str_dy + 'q'

        #send
        data = str_dx_dy.encode()
        client_socket.send(data)
        break
      
      elif msg == 'get_world_pos' :
          x_result, y_result = test_get_world_pos.get_world_pos()

          x1 = str(x_result[0])
          x2 = str(x_result[1])
          x3 = str(x_result[2])
          x4 = str(x_result[3])
          x5 = str(x_result[4])
          x6 = str(x_result[5])
          x7 = str(x_result[6])

          y1 = str(y_result[0])
          y2 = str(y_result[1])
          y3 = str(y_result[2])
          y4 = str(y_result[3])
          y5 = str(y_result[4])
          y6 = str(y_result[5])
          y7 = str(y_result[6])

          str_x1_y1 = 'x' + x1 + 'y' + y1 +'q'
          str_x2_y2 = 'x' + x2 + 'y' + y2 +'q'
          str_x3_y3 = 'x' + x3 + 'y' + y3 +'q'
          str_x4_y4 = 'x' + x4 + 'y' + y4 +'q'
          str_x5_y5 = 'x' + x5 + 'y' + y5 +'q'
          str_x6_y6 = 'x' + x6 + 'y' + y6 +'q'
          str_x7_y7 = 'x' + x7 + 'y' + y7 + 'q'

          data1 = str_x1_y1.encode()
          data2 = str_x2_y2.encode()
          data3 = str_x3_y3.encode()
          data4 = str_x4_y4.encode()
          data5 = str_x5_y5.encode()
          data6 = str_x6_y6.encode()
          data7 = str_x7_y7.encode()

          client_socket.send(data1)
          client_socket.send(data2)
          client_socket.send(data3)
          client_socket.send(data4)
          client_socket.send(data5)
          client_socket.send(data6)
          client_socket.send(data7)

      else :
        print('[server] undefined order : ', msg)
        break  
        
  except:
    print("except : " , addr)
  finally:
   client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 9999))
server_socket.listen()
 
try:
  print("[SERVER START]")

  while True:
    client_socket, addr = server_socket.accept()
    th = threading.Thread(target=binder, args = (client_socket,addr))
    th.start()
except:
  print("[ERROR] server is not connected")
finally:
  server_socket.close()
 