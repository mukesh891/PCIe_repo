from pcie_lib import *
from pcie_config_obj import *
logging.info("Entering Driver class of ROOT COMPLEX ")

from try_pcie_rc_cfg_base_seq import * 
#from pcie_rc_cfg_base_seq import * 
from pcie_rc_callback import *
class pcie_rc_driver:
    def __init__(self):
        self.k=0
        self.m=0
    def drive_tx(self):
        num_pkts=argv.num_pkts
        err_eij = argv.err_eij
        err_pkt_no = argv.err_pkt_no 
        logging.info("Entering Driver class of ROOT COMPLEX ")
        ## INFO :Erro injection using commandline arg "--err_eij=1" ##
        #for i in range(num_pkts):
        if(err_eij):
            if(self.m<err_pkt_no):
                logging.info("Entering err_eij if statement ")
                err_eij_hdl = pcie_err_eij()
                #logging.info("ERROR INJECTION SUCCESSFUL AT THE DRIVER END")
                print("len(arr)->",len(arr))
                print("m->",self.m)
                print("k->",self.k)
                if(arr[self.m]==self.k and self.m<len(arr)):
                    logging.info("Entering err_eij array to inject ")
                    ## randomly choose between bdf and fmt err
                    j = random.choice([0,1,2])
                    j = 2 
                    print(j)
                    if(j==0):
                        print("In driver class modified BDF BEFORE eij->",tx.requester_id)
                        print(vars(tx)) 
                        tx.requester_id = err_eij_hdl.requester_id_err_eij()
                        print("In driver class modified BDF AFTER eij->",tx.requester_id)
                        print(vars(tx)) 
                    if(j==1):
                        print("In driver class modified FMT BEFORE eij->",tx.fmt)
                        print(vars(tx)) 
                        tx.fmt = err_eij_hdl.pcie_fmt_err_eij()
                        print("In driver class modified FMT AFTER eij->",tx.fmt)
                        print(vars(tx))
                    if(j==2):
                        print("In driver class modified TYPE BEFORE eij->",tx.type)
                        print(vars(tx)) 
                        tx.type = err_eij_hdl.pcie_type_err_eij()
                        print("In driver class modified TYPE AFTER eij->",tx.type)
                        print(vars(tx))  
                self.m=self.m+1
        self.k=self.k+1

    def err_eij_file_handle(self):
        logging.info("Entering err_eij_file_handle() funstion ")
        fmt_str                 =format(tx.fmt, '03b')       
        requester_id_str        =format(tx.requester_id, '016b')       
        completer_id_str        =format(tx.completer_id, '016b')       
        type_str                =format(tx.type, '05b')      
        first_dw_be_str         =format(tx.first_dw_be, '04b')
        ep_str                  =format(tx.ep, '01b')        
        td_str                  =format(tx.td, '01b')        
        tc_str                  =format(tx.tc, '03b')        
        attr0_str               =format(tx.attr0, '02b')     
        attr1_str               =format(tx.attr1, '01b')     
        at_str                  =format(tx.at, '02b')        
        length_str              =format(tx.length, '010b')    
        #bus_str        =format(self.bustx8b')       
        #device_str     =format(self.devtx '05b')    
        #function_str   =format(self.funtxn, '03b')  
        tag_str                 =format(tx.tag, '08b')       
        last_dw_be_str          =format(tx.last_dw_be, '04b') 
        reserve_bit4_str        =format(tx.reserve_bit4, '04b')
        
        ext_register_number_str =format(tx.ext_register_number, '04b')
        register_number_str     =format(tx.register_number, '06b')
                     
        #addresses  =format(self.addresstx'04b')
        reserve_bit5_str        =format(tx.reserve_bit5, '02b')
        
        payload_str             = format(tx.payload, '032b')
        ###############################################
        
        ## Concatenating all the value into tlp_pkt in string format of binary value ##
        err_tlp_packet = (str(fmt_str)+str(type_str)+str(tx.reserve_bit1)+
        str(tc_str        )+str(tx.reserve_bit2)+
        str(attr1_str     )+
        str(tx.reserve_bit3)+
        str(tx.th)+
        str(td_str        )+
        str(ep_str        )+
        str(attr0_str     )+
        str(at_str        )+
        str(length_str    )+
        str(requester_id_str)+
        str(tag_str       )+
        str(last_dw_be_str)+
        str(first_dw_be_str)+
        str(completer_id_str)+
        str(reserve_bit4_str)+
        str(ext_register_number_str)+
        str(register_number_str)+
        str(reserve_bit5_str)+
        str(payload_str))
        ##################################################################################
        
        ## puting the tlp_packet into queue ##
        err_pkt_queue.put(err_tlp_packet)
        print(err_tlp_packet)

p = pcie_rc_driver()
tx=pcie_seq_rc_config_pkt()
for i in range(num_pkts):
    tx.cfg0_pkt() 
    p.drive_tx()
    p.err_eij_file_handle()
