import bincopy
import re 

with open("hex_code.txt","r") as f:
    for line in f:
        int_val = int(line,16)
        bin_val = bin(int_val)
        s = str(bin_val)
        st = re.sub("^0b",'',s)
        print(s, "->", st[len(st)-3:len(st)])
#00111000010100000000000000011000000000000000000000000
#000000000011000000000000000000000000

