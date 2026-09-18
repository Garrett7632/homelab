# Version 1.0 Monitoring Dashboard

## Overview

The Version 1.0 monitoring dashboard is a custom web-based interface created to provide visibility into the homelab infrastructure.

The dashboard was developed directly on the Linux environment using SSH and the terminal.

## Technologies

- HTML
- CSS
- JavaScript
- Python
- Proxmox API

## Purpose

The dashboard provides a centralized view of infrastructure information that would otherwise require checking individual systems or the Proxmox management interface.

The goal was to create a simple interface for monitoring the status and resource usage of the homelab.

## Monitoring

The dashboard collects information from the Proxmox environment and displays infrastructure metrics including:

- CPU utilization
- Memory utilization
- CPU cores
- Virtual machine information
- Storage information
- System uptime
- Service status

## Backend Monitoring

A Python monitoring script communicates with the Proxmox API and collects information about the infrastructure.

The collected information is provided to the web dashboard for display.

## Frontend

The dashboard interface is built using standard web technologies:

- HTML for structure
- CSS for layout and styling
- JavaScript for dynamic content and visualization

The interface was designed as a web-based dashboard that can be accessed through a browser on the local network.

## Service Management

The monitoring system runs as a Linux systemd service.

Using systemd allows the monitoring process to run in the background and automatically start with the system.

## Development Process

Version 1.0 was developed directly on the Ubuntu Linux environment through SSH and the Linux terminal.

This provided hands-on experience with:

- Linux administration
- Python development
- API integration
- Web development
- Systemd service management
- Debugging
- Server-side monitoring

## Version 1.0 Challenges

During development, several issues were identified and resolved, including:

- Monitoring service failures
- Excessive system logging
- JSON file read/write conflicts
- Dashboard visualization errors
- Dynamic dashboard updates
- Storage display consistency

These issues provided practical experience troubleshooting a continuously running Linux application.

## Version 2.0

Version 2.0 is currently being developed as a dedicated application.

The goal is to build upon the functionality of Version 1.0 while providing a more scalable architecture and expanding the dashboard beyond the original web-based implementation.
