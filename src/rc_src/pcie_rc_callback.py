from pcie_rc_cfg_base_seq import * 
from try_pcie_rc_cfg_base_seq import * 

from pprint import pprint
class pcie_callbacks:
    print("This is pcie callback class")

class pcie_err_eij(pcie_callbacks):
    print("This is BDF error injection class")
    def requester_id_err_eij(self):
        print("This is bdf eij err callback ")
        #pkt.cfg0_pkt()
        tl_pkt=pcie_seq_rc_config_pkt()
        tl_pkt.requester_id=0xBADBDF
        print(tl_pkt.requester_id)
        return tl_pkt.requester_id

    def pcie_fmt_err_eij(self):
        print("This is  eij err callback ")
        #pkt.cfg0_pkt()
        tl_pkt=pcie_seq_rc_config_pkt()
        tl_pkt.fmt = random.choice([1,3,4,5,6,7])
        print(tl_pkt.fmt)
        return tl_pkt.fmt   
    
    def pcie_type_err_eij(self):
        print("This is  eij err callback ")
        #pkt.cfg0_pkt()
        tl_pkt=pcie_seq_rc_config_pkt()
        tl_pkt.type = random.choice([0,1,2,3,5,6,7])
        print(tl_pkt.type)
        return tl_pkt.type   


