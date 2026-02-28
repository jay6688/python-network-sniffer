from scapy.all import sniff

# 1. The callback function (What to do when we catch a packet)
def process_packet(packet):
    # This will print a high-level summary of the packet (e.g., "TCP 192.168.1.5 -> 8.8.8.8")
    print(packet.summary())

# 2. Start the sniffer
print("[*] Starting Network Sniffer...")
print("[*] Waiting to capture 10 packets...")

# sniff() tells the network card to start listening. 
# prn = the function to send the packet to.
# count = stop after capturing 10 packets.
sniff(prn=process_packet, count=10)

print("\n[*] Capture complete!")