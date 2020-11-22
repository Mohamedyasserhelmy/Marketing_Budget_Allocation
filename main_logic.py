import numpy as np
import crossover as c
import encoder_decoder as ed

channels_list = []          # List of channels names
channels_ROI = []           # List of channels of roi to be transformed into %
chrom_list = []             # population list
lu_list = []                # lower and upper list

budget = int(input("Enter the Marketing budget in thousands : \n"))
Nofchannels = int(input("Enter The number of marketing channels : \n"))

for _ in range (Nofchannels):
    c_name, c_value = input("Enter name and ROI of each channel : \n").split(" ")
    channels_list.append(c_name)
    channels_ROI.append(c_value)

for __ in range (Nofchannels):
    l, u = input("Enter the lower (k) and upper bounds (%) of investment in each channel:\n(enter x if there is no bound)\n").split(" ")
    if (l != "x"):
        lu_list.append((float((float(l)*1000)/(budget*1000) * 100),u))
    else :
        lu_list.append((l,u))

print(ed.encode(channels_list))
print(ed.decode(3))
