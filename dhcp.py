from scapy.all import *
import pydivert



with pydivert.WinDivert("tcp.DstPort == 67") as syn:
    for packet in syn:
        syn.send(packet)
        sync(packet)
