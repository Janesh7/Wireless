from scapy.all import *

ap_list = []  # empty list to store ssid

def Packet_info(pkt):  # paket parsing function
    if pkt.haslayer(Dot11):  # filtering only 802.11 traffic
        if ((pkt.type == 0) & (
                pkt.subtype == 8)):  # filtering the packets with frame type =0 which rep management frames and =8 represents beacon frames
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2)
                print("SSID: ", (pkt.addr2, pkt.info))


sniff(iface="mon0",
      prn=Packet_info)  # sniff the traffic with interface value to be mon0 which is a monitor mode for wireless packets and invoking Packet_info
# This script requires a wifi card that is capable of sniffing the air using monitor mode
