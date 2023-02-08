import time
import zmq
from menu import check_number
from message import messaging 

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://*:5560")

print("Connected to server")


while True:

    info = socket.recv_json()
    print(info)
    time.sleep(3)
    socket.send_json({'response': 200})
    messaging(body = info['heelo'])



    