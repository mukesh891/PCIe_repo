import random
#from pkt_dict import *
from pcie_com_file import *


print("ep_base_pkt block")



class ep_base_pkt():
	
	
	def checker_fn_base(self, pkt_num):
		
		header = format(0, '0128b')   #default set
		header = pkt_queue.queue[pkt_num]

		print('********************************************** base packet number {} ***********************************************'.format(pkt_num))
		print('base header is {}'.format(header))

		return header
		