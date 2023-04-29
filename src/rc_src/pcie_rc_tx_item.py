import sys
import random
sys.path.append("/home/mukesh/PCIe/PCIe_repo/src/")
from pprint import pprint
from pcie_tx_item import pcie_tx_item

import fcntl
import os 

class pcie_rc_tx_item(pcie_tx_item):
    print("2. This is pcie_rc_tx_item class")
    def __init__(self):
      super().__init__()

class pcie_rc_cfg0_pkt(pcie_tx_item):
    print("2. This is pcie_rc_tx_item class")
    def __init__(self):
        super().__init__()
    def cfg0_pkt(self):
        self.transaction_type = random.getrandbits(8)
        self.bdf = random.getrandbits(16)
        self.cfg_type = random.getrandbits(1)
        self.first_dw_be = 0b0011
        self.ep = random.getrandbits(1)
        self.block = random.getrandbits(1)
        self.td= random.getrandbits(1)
        self.transaction_type = random.getrandbits(8)	
        self.bdf = 10
        self.conf_type = 0
        self.ep = 1
        self.td = 0

    def print_f(self):
        pprint(vars(self))

    def file_handle(self):
        #with open("/home/mukesh/PCIe/PCIe_repo/src/rc_src/Hex_file.txt","w") as f:
        f = open("/home/mukesh/PCIe/PCIe_repo/src/rc_src/Hex_file.txt","w")
        #fcntl.flock(f, fcntl.LOCK_SH)
        #for f in fil:
        for i in range(0,10):
            self.cfg0_pkt()
            transaction_type_arr = [self.transaction_type]
            bdf_arr       =[self.bdf]
            first_dw_be_arr   =[self.first_dw_be]
            transaction_type_head = ''.join('{:02X}'.format(a) for a in transaction_type_arr)
            bdf_head = ''.join('{:04X}'.format(a) for a in bdf_arr)
            ## Converting rest of the header config to hex format: START ##
            ## as all the below fields are of 1 bit so no bit manupulation is required ##
            #conf_type     =[self.conf_type]
            #ep_arr        =[self.ep]
            #block         =[self.block]
            #td_arr        =[self.td]
            fdb_str = format(self.first_dw_be, '04b')
            s0=str(self.conf_type)
            s1=fdb_str
            s2=str(self.ep)
            s3=str(self.block)
            s4=str(self.td)
            s5=s0+s1+s2+s3+s4
            print(s5)
            rest_head = hex(int(s5, 2))[2:].upper()
            print(rest_head )
            ## Converting rest of the header config to hex format: END ##
            f.write(transaction_type_head )
            f.write(bdf_head)
            f.write(rest_head)

            f.write("\n")
            ## for Dict Formatting ##
            #f.write(str(vars(self)))
            #f.write("\n")
        f.close()
c = pcie_rc_cfg0_pkt()
c.file_handle()

#self.packet = [self.bdf, self.conf_type, self.block, self.ep, self.td]
                #pkt_dict["bdf"] = self.bdf 
                #pkt_dict["conf_type"] = self.conf_type 
                #pkt_dict["block"] = self.block 
                #pkt_dict["ep"] = self.ep 
                #pkt_dict["td"] = self.td

