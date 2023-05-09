from pcie_config_obj import *
import random
queue = {}
RC_BASE_ADDR = 0x10000
EP_BASE_ADDR = 0x100000
## 256kb of configuration space ##
CFG_SPACE = 256 * 2**10
# Define the queue as a dictionary with offset addresses as keys and values as lists of random data
for i in range (0,2**10):  # range for 1kb addr offset
    offset = (0x00+i) * 4
    data = [random.getrandbits(32)]
    queue[offset] = data
# Update the value at 0x08 offset
queue[0x08] = [0xfffffff]
# Print the queue
#for offset, data in queue.items():
#    print(f"Offset: {hex(offset)} Data: {[hex(data[0])]}")

## for RC_BASE_ADDR cfg
if(RC_BASE_ADDR):
    for i in range (0,CFG_SPACE):
        offset = (0x00 + RC_BASE_ADDR ) + 4*i
        data = [random.getrandbits(32)]
        queue[offset] = data
 
if(EP_BASE_ADDR):
   for i in range (0,CFG_SPACE):
       offset = (0x00 + RC_BASE_ADDR ) + 4*i
       data = [random.getrandbits(32)]
       queue[offset] = data
    
for offset, data in queue.items():
    print(f"Offset: {hex(offset)} Data: {[hex(data[0])]}")
