from scapy.all import ls, IP

if __name__ == "__main__":
    src_ip = "192.168.155.47"
    dst_ip = "www.amazon.com"

    IP_layer = IP(
        src = src_ip,
        dst = dst_ip
    )
    print(ls(IP_layer)) #the ls function
    print(f'Destination is = {IP_layer.proto}') #accesing individual fields in a layer
    print(IP_layer.summary()) #Get a summmary of the layer