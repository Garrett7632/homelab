# Proxmox VE

## Overview

Proxmox VE is the virtualization platform used as the foundation of the homelab.

The Dell OptiPlex 3070 Micro functions as the physical Proxmox host, providing compute, memory, storage, and networking resources to the virtual machines running in the environment.

## Host Hardware

- System: Dell OptiPlex 3070 Micro
- CPU: Intel Core i5-9500T
- RAM: 16 GB DDR4
- Storage: 256 GB M.2 SSD
- Integrated Graphics: Intel UHD Graphics

## Virtual Machines

The Proxmox host currently runs Ubuntu-based virtual machines for homelab services.

These virtual machines provide isolated environments for applications and services while allowing resources to be managed centrally through Proxmox.

## GPU Passthrough

The Intel integrated GPU is configured for PCI passthrough to an Ubuntu virtual machine.

This allows the VM to directly access the physical integrated graphics hardware and output video to a monitor connected to the OptiPlex.

The passthrough configuration uses Proxmox's PCI device passthrough functionality and Intel IOMMU support.

## Resource Management

Proxmox is used to allocate and manage resources for the virtual machines, including:

- CPU
- Memory
- Storage
- Network interfaces
- PCI devices

Resource allocation can be adjusted as the requirements of individual services change.

## Management

The Proxmox environment is administered through its web interface and through SSH.

Linux-based virtual machines are also administered through SSH and the terminal.

## Role in the Homelab

Proxmox provides the virtualization layer for the homelab and allows multiple services to run independently on a single physical machine.

This architecture provides a foundation for expanding the environment with additional virtual machines, services, and physical hardware.
