from pcie_lib import *
from pcie_config_obj import *
logging.info("Entering Driver class of ROOT COMPLEX ")

from pcie_rc_cfg_base_seq import * 

from pcie_rc_callback import *

class pcie_rc_driver:
    def drive_tx(self):
        err_eij = argv.err_eij
        logging.info("Entering Driver class of ROOT COMPLEX ")
        print("in driver class modified bdf BEFORE eij->",tx.requester_id)
        print(vars(tx)) 
        ## INFO :Erro injection using commandline arg "--err_eij=1" ##
        if(err_eij):
            logging.info("ERROR INJECTION SUCCESSFUL AT THE DRIVER END")
            bdf_cb = pcie_bdf_err_eij()
            tx.requester_id = bdf_cb.bdf_eij_err()
            print("in driver class modified bdf AFTER eij->",tx.requester_id)
        print(vars(tx)) 
tx=pcie_seq_rc_config_pkt()
p = pcie_rc_driver()
p.drive_tx()

