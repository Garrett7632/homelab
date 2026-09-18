# Troubleshooting and Lessons Learned

## Overview

Building Version 1.0 of the homelab involved troubleshooting issues across Linux, virtualization, networking, system services, APIs, and web development.

This document records some of the problems encountered during development and the approaches used to resolve them.

## Dashboard

### JSON Read/Write Conflict

The monitoring dashboard initially experienced errors when reading `status.json`.

The browser could attempt to read the file while the Python monitoring process was still writing to it. This resulted in incomplete JSON being read by the dashboard.

The solution was to use an atomic file replacement process:

1. Write the updated data to a temporary file.
2. Complete the write operation.
3. Replace the existing `status.json` with the completed temporary file.

This prevented the dashboard from reading partially written data.

### Dashboard Visualization Errors

The dashboard initially experienced errors when dynamically updating charts.

Charts were being recreated during dashboard updates, which resulted in invalid or unavailable canvas elements.

The dashboard was modified to properly manage chart instances and their associated elements during updates.

### Storage Display

Storage information initially appeared in inconsistent orders between updates.

The monitoring data was modified to sort storage entries consistently before displaying them.

## Linux Services

### Excessive System Logging

A rapidly restarting monitoring service generated a large amount of system logging.

This eventually consumed a significant amount of available disk space on the Ubuntu VM.

The issue was identified by examining system resource usage and system logs.

The service was stopped, the excessive logs were cleaned up, and the underlying service issue was addressed.

This demonstrated the importance of monitoring both application behavior and system resources.

## Minecraft Server

### Missing Mod Dependencies

The Fabric Minecraft server initially failed to start because required mod dependencies were missing.

The server logs were used to identify the missing dependencies, which were then installed before restarting the server.

### World Session Lock

A Minecraft server startup attempt encountered a world `session.lock` conflict because another server instance was already running.

The existing server process was identified and stopped before starting the server again.

### systemd Configuration

The Minecraft server was configured to run as a systemd service.

This replaced the need to manually start the server after system reboots and allows the service to automatically restart after unexpected failures.

## GPU Passthrough

The Intel integrated graphics hardware on the OptiPlex was configured for PCI passthrough to an Ubuntu virtual machine.

This required configuring IOMMU support and assigning the PCI device to the virtual machine.

After configuration, the Ubuntu VM was able to use the physical display connected to the OptiPlex.

## Lessons Learned

The Version 1.0 development process provided practical experience with:

- Reading and interpreting Linux logs
- Diagnosing service failures
- Managing systemd services
- Working with APIs
- Handling concurrent file access
- Debugging JavaScript applications
- Managing virtual machines
- Configuring PCI passthrough
- Troubleshooting server software
- Managing Linux resources
- Using SSH for remote administration

The troubleshooting process also reinforced the importance of making small changes, checking logs, and verifying the system after each configuration change.
