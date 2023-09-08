import socket
import struct
import matplotlib.pyplot as plt
import numpy as np

def convert4U8ToF32(int_list):
    return struct.unpack('>f', bytes(int_list))[0]

HOST = '192.168.5.123'
PORT = 5566

def main():
    ## TCP client connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:
        indata = s.recv(2048)
        if len(indata) == 0: ## Connection closed
            s.close()
            print('server closed connection.')
            break
        elif len(indata) > 0:
            break
    ## Received data and convert 4U8 to float
    data_len = len(list(indata))//4
    data_float_list = []
    for i in range(data_len//2):
        data = convert4U8ToF32(indata[i*4: (i+1)*4])
        data_float_list.append(data)

    ## Plot
    frequency = np.linspace(0, data_len//2, data_len//2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power spectrum')
    plt.bar(frequency, data_float_list)
    plt.show()

if __name__ == '__main__':
    main()