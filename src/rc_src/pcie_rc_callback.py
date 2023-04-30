from pcie_rc_tx_item import pcie_rc_cfg0_pkt
from pcie_rc_tx_item import pcie_rc_cfg0_pkt  

from pprint import pprint
class pcie_callbacks:
    print("This is pcie callback class")
#    def bdf_eij_err(self):
#        print("This is bdf eij err callback ")
#        #pkt.cfg0_pkt()
#        pkt.bdf=50
#        print(pkt.bdf)
#pkt=pcie_rc_cfg0_pkt()
#pkt.print_f()
#cb = pcie_callback()
#cb.bdf_eij_err()
#pkt.print_f()


class pcie_bdf_err_eij(pcie_callbacks):
    print("This is BDF error injection class")
    def bdf_eij_err(self):
        print("This is bdf eij err callback ")
        #pkt.cfg0_pkt()
        tl_pkt.bdf=50
        print(tl_pkt.bdf)
tl_pkt=pcie_rc_cfg0_pkt()
tl_pkt.print_f()
bdf_cb = pcie_bdf_err_eij()
bdf_cb.bdf_eij_err()
tl_pkt.print_f()

		
