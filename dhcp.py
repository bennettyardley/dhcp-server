from scapy.all import *
import pydivert


def sync(packet):
    #craft DHCP offer 
    #send DHCP offer
    #wait for request
    #send ack
    #add taken ip to list

#wait for dhcp discovery 
with pydivert.WinDivert("tcp.DstPort == 67") as syn:
    for packet in syn:
        syn.send(packet)
        sync(packet)
        #test

