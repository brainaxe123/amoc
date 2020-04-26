import pefile
string = input("Enter path of executable or dll file:  ")
pe = pefile.PE(string)
pe.print_info()
DllCharacteristics = pe.OPTIONAL_HEADER.DllCharacteristics
Machine = pe.FILE_HEADER.Machine
Characteristics = pe.FILE_HEADER.Characteristics
MajorSubsystemVersion = pe.OPTIONAL_HEADER.MajorSubsystemVersion
ImageBase = pe.OPTIONAL_HEADER.ImageBase
Subsystem = pe.OPTIONAL_HEADER.Subsystem
SizeOfOptionalHeader = pe.FILE_HEADER.SizeOfOptionalHeader
SizeOfStackReserve = pe.OPTIONAL_HEADER.SizeOfStackReserve
MajorLinkerversion = pe.OPTIONAL_HEADER.MajorLinkerVersion


#print(Characteristics)
array = [DllCharacteristics , Machine , 0,  Characteristics , MajorSubsystemVersion ,0, ImageBase , Subsystem , SizeOfOptionalHeader ,0,0,0,0,0, SizeOfStackReserve , MajorLinkerversion]
#print(array)