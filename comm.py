import time
import zmq

def comm_translate(text, lang):

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5545")

    socket.send_json({'lang': lang, 'text': text})
    time.sleep(1)
    message = socket.recv_json
    socket.close()
    return message




