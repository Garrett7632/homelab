# Homelab Infrastructure

## Overview

The homelab is built around a Dell OptiPlex 3070 Micro running Proxmox VE as the virtualization host.

The current Version 1.0 environment uses an Ubuntu Linux virtual machine to host and manage several services, including a custom infrastructure monitoring dashboard and a modded Minecraft server.

## Physical Hardware

### Dell OptiPlex 3070 Micro

- CPU: Intel Core i5-9500T
- RAM: 16 GB DDR4
- Storage: 256 GB M.2 SSD
- Graphics: Intel UHD Graphics
- Operating System: Proxmox VE

The OptiPlex serves as the primary compute host for the homelab.

## Virtualization

### Proxmox VE

Proxmox VE is used as the virtualization platform for the homelab.

The Proxmox host provides the underlying compute, memory, storage, and networking resources for the virtual machines within the environment.

## Current Services

### Infrastructure Monitoring Dashboard

A custom web-based dashboard was developed to monitor the homelab infrastructure.

The dashboard uses:

- Python
- HTML
- CSS
- JavaScript
- Proxmox API

The monitoring system collects infrastructure information and presents it through a web interface.

### Minecraft Server

The homelab hosts a modded Minecraft server running on Linux.

Current technologies include:

- Minecraft 1.21.1
- Fabric
- Fabric API
- Multiple gameplay and world-generation mods
- RCON
- systemd

## Hardware Passthrough

The Intel integrated graphics hardware on the OptiPlex is passed through to an Ubuntu VM using Proxmox.

This allows the physical display connected to the OptiPlex to be used by the VM.

## Networking

The homelab uses a local network to provide connectivity between the Proxmox host, VMs, and other devices.

Network configuration and service-specific details will be documented separately as the infrastructure continues to develop.

## Current Architecture

```text
Dell OptiPlex 3070 Micro
│
└── Proxmox VE
    │
    └── Ubuntu Linux VM
        │
        ├── Infrastructure Monitoring Dashboard
        │   ├── Python
        │   ├── Proxmox API
        │   └── HTML / CSS / JavaScript
        │
        └── Modded Minecraft Server
            ├── Fabric
            ├── Fabric API
            ├── Mods
            ├── RCON
            └── systemd
```
