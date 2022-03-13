from scapy.all import *

i = 1  # number of deauth frames


def deauth_frame(pkt):
    if pkt.haslayer(Dot11):  # check for dot11 layer
        if ((pkt.type == 0) & (pkt.subtype == 12)):  # packet subtype = 12 indicates the deauth frame
            global i
            print("Deauth frame detected: ", i)
            i = i + 1


sniff(iface="mon0", prn=deauth_frame)
