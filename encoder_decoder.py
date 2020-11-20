import numpy as np

# In this module I'm going to construct
# an encoding() function that encodes channels and corresponding indices
# Then The decoding() function which do inverse
enc = {}
def encode(x):
    # x1 : List of channels [tv, google, twitter, facebook, ...]
    for i in range (0, len(x)):
        enc[x[i]] = i
    return enc


def decode(I):
    # input rhe index and return the corresponding key
    for channel, index in enc.items():
        if (I == index):
            return channel

# If the Index not found the function returns None Type
# It could be used for exception as follows if (decode(r,t) == None):
#                                                print("Invalid Index")



#print(encode(["TV", "Google", "Twitter", "Facebook"]))
#print(decode(5))
                    ### Tested && Debugged ### 
