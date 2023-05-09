from pcie_rc_cfg_base_seq import * 

from pprint import pprint
class pcie_callbacks:
    print("This is pcie callback class")

class pcie_bdf_err_eij(pcie_callbacks):
    print("This is BDF error injection class")
    def bdf_eij_err(self):
        print("This is bdf eij err callback ")
        #pkt.cfg0_pkt()
        tl_pkt=pcie_seq_rc_config_pkt()
        tl_pkt.bdf=0xBADBDF
        print(tl_pkt.bdf)
        return tl_pkt.bdf

		
