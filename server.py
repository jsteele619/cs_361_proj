import time
import zmq
from menu import check_number
from message import messaging 

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://*:5560")

print("Listening at port 5560")

while True:
    info = socket.recv_json()
    print(info['phone'])
    val = check_number(info["phone"])
    if val is False:
        socket.send_json({'response': 400, 'message': "phone number wasn't correct"})
        continue
    try:
        messaging(info['content'])
        
        socket.send_json({'response': 200, 'message': "successful, check your phone"})
    except Exception as e:
        socket.send_json({'response': 400, 'message': e})





    