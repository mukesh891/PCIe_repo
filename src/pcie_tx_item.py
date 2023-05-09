#class pcie_tx_item:
#    print("2. This is pcie_tx_item class")
#    def __init__(self):
#      self.fmt=0
#      self.bdf = 0b1011    
#class cfg_type(IntEnum):
#   type0 =0
#   type1 =1

from pcie_lib import *

from enum import IntEnum

#class pcie_pkg:
class pcie_tx_item:
    print("2. This is pcie_tx_item class")
    def __init__(self, name="", size_in_bytes=0, xwr=0):
        self.requester_id           = random.getrandbits(16)
        self.completer_id           = random.getrandbits(16)
        self.completer_id           = 0 
        ##################################################
        self.type                   = random.choice([4,5])
        self.first_dw_be            = 0b0011
        self.ep                     = 0 
        self.td                     = 0
        self.tc                     = random.getrandbits(3)
        self.tc                     = 0 
        self.attr0                  = random.getrandbits(2)
        self.attr1                  = random.getrandbits(1)
        self.attr0                  = 0 
        self.attr1                  = 0
        self.at                     = random.getrandbits(2)
        self.at                     = 0
        self.length                 = random.getrandbits(10)

        #self.bus                    = random.getrandbits(8)
        #elf.device                 = random.getrandbits(5)
        #elf.function               = random.getrandbits(3)
        self.tag                    = random.getrandbits(8)
        self.last_dw_be             = random.getrandbits(4)
        self.last_dw_be             = 0 
        
        self.payload                = random.getrandbits(32)
        self.reserve_bit1           = random.choice([0,1])
        self.reserve_bit2           = random.choice([0,1])
        self.reserve_bit3           = random.choice([0,1])
        self.reserve_bit4           = random.choice([0,15])
        self.reserve_bit5           = random.choice([0,3])
        self.th                     = 0 
        ######### initializing reserved bits to zero ########
        self.reserve_bit1           = 0
        self.reserve_bit2           = 0
        self.reserve_bit3           = 0
        self.reserve_bit4           = 0
        self.reserve_bit5           = 0
        #####################################################

        self.ext_register_number    = random.choice([0,15])
        self.ext_register_number    = 0
        self.register_number        = random.choice([0,63])
        #self.command_num = random.getrandbits(32)
        ############### code for byte conv #############
        self.name = name
        self.size_in_bytes = size_in_bytes
        self.xwr = xwr
        ################################################
    

    def print_var(self):
        pprint(vars(self))
        '''s = bin(self.first_dw_be)
        pprint(s)
        a = 20
        print(bytes(a))
        b=BitArray(uint = a , length = 10).bin
        pprint(b)
        for i in range(1,11): 
            pprint(b[i-1:i])
'''
    def bitwise_read():
        s = bin(self.first_dw_be)
        pprint(s)
        a = 20
        print(bytes(a))
        b=BitArray(uint = a , length = 10).bin
        pprint(b)
        for i in range(1,11): 
            pprint(b[i-1:i])
    
 
class tlp_fmt(IntEnum):
    cfgrd=0b000
    cfgwr=0b010

class tlp_type(IntEnum):
    cfgwr0=0b0001
    cfgrd0=0b0010
    cfgwr1=0b0011
    cfgrd1=0b0100


pkg = pcie_tx_item()
pkg.print_var()
