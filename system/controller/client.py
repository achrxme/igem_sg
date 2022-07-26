import socket

def extract_dx_dy(rcv_str_dx_dy):

    idx_x = rcv_str_dx_dy.find('x')
    idx_y = rcv_str_dx_dy.find('y')
    idx_end = rcv_str_dx_dy.find('q')

    idx_data_x = idx_x+1
    idx_data_y = idx_y+1

    str_x = rcv_str_dx_dy[idx_data_x:idx_data_y-1]
    str_y = rcv_str_dx_dy[idx_data_y:idx_end]

    int_x = int(str_x)
    int_y = int(str_y)

    return int_x, int_y


def order_classify(order):
    HOST = '192.168.0.17'
    PORT = 9999
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    
    send_msg = order
    send_data = send_msg.encode()
    
    #send
    print("[client] : send msg")
    client_socket.send(send_data)
    
    #receive
    rcv_data = client_socket.recv(64)
    print("[client] : recv suc/fail")
    rcv_msg = rcv_data.decode()

    client_socket.close()

    if order == 'grip_test':
        msg = rcv_msg
        print(msg)
        return msg    #return str

    elif order == 'get_pos':
        rcv_dx, rcv_dy = extract_dx_dy(rcv_msg)
        return rcv_dx, rcv_dy  #return int, int

    else :
        print('unexpected order')
        return 'unexpected order'  # return 'unexpected order'
