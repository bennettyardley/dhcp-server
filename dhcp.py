from scapy.all import *
import pydivert

#https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol

def sync(packet):
    packet.
    sendp(Ether(src

with pydivert.WinDivert("tcp.DstPort == 67") as syn:
    for packet in syn:
        syn.send(packet)
        sync(packet)
