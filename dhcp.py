#https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol

from scapy.all import *
import pydivert


def sync(packet):
    #craft DHCP offer 
    #send DHCP offer
    

with pydivert.WinDivert("tcp.DstPort == 67") as syn:
    for packet in syn:
        syn.send(packet)
        sync(packet)

