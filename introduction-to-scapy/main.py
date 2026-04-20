# USING SCAPY TO CREATE,SEND AND RECEIVE PACKETS

from scapy.layers.inet import ICMP #To create an ICMP request packet
from scapy.layers.inet import IP #To create an IP layer packet
from scapy.sendrecv import sr1 #to send and receive packets

if __name__ == "__main__":

    src_IP = "192.168.155.47"
    dest_IP = "www.google.com"

    # create an IP layer packet
    IP_layer = IP(
        src = src_IP,
        dst = dest_IP
    )
    # IP_layer.show()

    # creat an icmp request packet
    ICMP_req = ICMP(id=100)
    # ICMP_req.show()

    # combine protocol layers using the / operator into a single packet
    packet = IP_layer/ICMP_req
    # packet.show()

    # send packet & receive a reply
    response = sr1(packet, iface = "eth0")
    if response:
        response.show()
    


