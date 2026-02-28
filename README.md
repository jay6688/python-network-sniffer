# Python Network Packet Sniffer 🌐

A lightweight, educational network packet sniffer built in Python using the `scapy` library. This tool intercepts and summarizes live network traffic at the packet level, demonstrating how data moves across a network and how different protocols (TCP, UDP, IPv4/IPv6) are structured.

## ⚠️ Educational Disclaimer
**This project is strictly for educational purposes.** It was built to understand network layers, packet structures, and how professional tools like Wireshark operate under the hood. Only run this tool on networks you own or have explicit permission to monitor.

## ✨ Features
* **Live Traffic Interception**: Captures raw network packets in real-time as they cross the network interface.
* **Protocol Summarization**: Extracts and displays high-level summaries of packets, identifying the hardware layer (Ethernet), routing layer (IP), and transport layer (TCP/UDP).
* **Configurable Capture Limits**: Built with a hard limit to safely capture a specific number of packets (e.g., 10) before automatically safely detaching the hook.

## ⚙️ Prerequisites
* Python 3.x
* `scapy` library (`pip install scapy`)
* **Npcap** or **WinPcap** system drivers installed (required for Windows to allow promiscuous mode packet capture).
* **Administrator/Root Privileges**: The script must be run as an Administrator to interact directly with the network card.

## 🧠 What I Learned
* **Network Layers (OSI Model)**: Seeing the practical application of Layer 2 (Ethernet), Layer 3 (IP), and Layer 4 (TCP/UDP) protocols.
* **Promiscuous Mode**: Understanding how network interfaces can be configured to read all traffic, not just traffic addressed to the host.
* **Library Integration**: Utilizing third-party industry-standard libraries (`scapy`) for complex, low-level system tasks.
