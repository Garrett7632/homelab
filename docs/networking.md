# Network Architecture

## Overview

The homelab is connected to the local home network and uses private IPv4 addressing for communication between the Proxmox host, virtual machines, and other devices.

The Proxmox host and its virtual machines communicate over the local network, allowing services such as the monitoring dashboard and Minecraft server to be accessed from other devices on the network.

## Network Components

The current environment includes:

- Home network/router
- Proxmox host
- Ubuntu virtual machines
- Networked client devices
- Virtual machine network interfaces

## Proxmox Networking

Proxmox provides virtual networking for the virtual machines running on the host.

Virtual machines are connected to the network through Proxmox's virtual networking configuration, allowing them to communicate with other systems on the local network.

## Service Access

The homelab services are accessible over the local network.

Examples include:

- Proxmox management interface
- Ubuntu SSH access
- Monitoring dashboard
- Minecraft server

Administrative services are intended to remain accessible within the local network rather than being directly exposed to the public internet.

## Security Considerations

The homelab provides an environment for learning and experimenting with network and cybersecurity concepts.

Current considerations include:

- Keeping administrative services on the local network
- Using SSH for remote Linux administration
- Restricting RCON access to the local system
- Avoiding exposure of credentials and API tokens
- Separating public documentation from private infrastructure information

## Future Networking Plans

As the homelab expands, networking will be developed further.

Potential future improvements include:

- Managed networking equipment
- VLAN segmentation
- Dedicated firewall/router
- Network monitoring
- Separate IoT network
- Isolated cybersecurity laboratory network
- Additional physical servers
