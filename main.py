from pyringcomm import *
import time

port = ringlink.DEFAULT_PORT

manager = ringman.Manager()
server = ringlink.Server(manager, port)

print("Starting server on port", port)
server.start()

while True:
    try:
        time.sleep(.1)
    except KeyboardInterrupt:
        print("[exiting server]")
        break
server.close()

