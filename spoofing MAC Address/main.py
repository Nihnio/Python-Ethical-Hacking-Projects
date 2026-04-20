import subprocess

# print eth0/interface information

# subprocess.run(
#     ["ifconfig","eth0"],
#     shell=True,
# )

if __name__ == "__main__":
    interface = "eth0"
    new_mac = "22:11:22:33:44:57"

print("shutting down the interface")
subprocess.run(
    ["ifconfig", "eth0", "down"],
)

print(f'changing the NIC hardware address of {interface} to {new_mac}')
subprocess.run(
    ["ifconfig", interface, "hw","ether", new_mac]
)

print ("MAC address changed to", new_mac)
subprocess.run(
    ["ifconfig", interface, "up"]
)
print(f'network interface turned on')

