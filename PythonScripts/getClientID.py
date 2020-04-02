import bge
import socket
import time
import random

controller = bge.logic.getCurrentController()
obj = controller.owner
scene = bge.logic.getCurrentScene()
obj['ID'] = random.randint(100000,999999)
print(obj['ID'])