import random
import os,queue
import argparse
cwd = os.getcwd()
class pcie_config_obj:
    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--num_pkts', type= int , help = 'Total num of packets to be generated at generator side and must be positive value', default = 10)
        parser.add_argument('--err_eij', type= int , help = 'A bit value to represent error injection is done or not and must be 0,1', default = 0)
        parser.add_argument('--err_pkt_no', type= int , help = 'Total no. of error pkt to be injected', default = 0)
 
        return parser.parse_args()
c=pcie_config_obj
argv = pcie_config_obj.parse_args()
#num_pkts = argv.num_pkts
#class ex:
#    def __init__(self):
        
#obj=ex()
#print(num_pkts)
pkt_queue = queue.Queue()
err_pkt_queue = queue.Queue()
compl_pkt_queue = queue.Queue()
pkt_with_flag_queue = queue.Queue()
rc_reg = queue.Queue()

  
err_eij = argv.err_eij
num_pkts = argv.num_pkts
err_pkt_no = argv.err_pkt_no
arr_t =[0]*err_pkt_no
if(err_eij): 
    for i in range(err_pkt_no):
        arr_t[i] = random.randrange(num_pkts)
    arr = list(set(arr_t))
    arr.sort()
    print(arr)
    print(num_pkts)
	
