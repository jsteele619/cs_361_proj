import time
import zmq

def comm_translate():

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5560")

    yes = socket.send_json({'heelo': 34})
    time.sleep(1)
    message = socket.recv_json
    socket.close()


comm_translate()


