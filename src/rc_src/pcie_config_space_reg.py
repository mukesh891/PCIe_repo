import pciutils 
bus = pciutils.PCIUtils().find_devices() 
dev = bus[0] 
# Set the register offset and value 
reg_offset = 0x10 
reg_value = 0x12345678 
# Write to the register 
dev.write_config_dword(reg_offset, reg_value)
print(dev.read_config_dword(reg_offset, reg_value))

