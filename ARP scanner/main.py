# USING SCAPY FOR INFORMATION GATHERING
# ARP Scanner

from scapy.all import Ether, IP, ARP, srp

if __name__ == "__main__":
    # src_MAC = "08:00:27:61:05:9a "
    broadcast = "FF:FF:FF:FF:FF:FF:FF:FF" # send packet to all the devices in the network
    ether_layer = Ether(dst=broadcast) #set source & destination mac address
 
    IP_range = "192.168.173.0/24" #range of ip addresses/host devices to scan
    ARP_layer = ARP(pdst = IP_range) #set arp request & target ip address

    packet = ether_layer/ARP_layer #create packet with both layers
    # packet.show()

    response = srp(packet, iface = "eth0", timeout=2) #send and receive packet

    ans, unans = response

    for snd, rcv in ans:
        ip_addr = rcv[ARP].psrc
        MAC_addr = rcv[Ether].src

        print (f'IP = {ip_addr}, MAC = {MAC_addr}')
        # print (f'IP = {rcv[ARP].pdst}, MAC = {rcv[Ether].dst}')