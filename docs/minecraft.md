# Minecraft Server

## Overview

The homelab hosts a dedicated modded Minecraft server running on Linux within the Proxmox environment.

The server is managed as a systemd service and is administered remotely through SSH and RCON.

## Server Software

- Minecraft: 1.21.1
- Server loader: Fabric
- Fabric Loader: 0.19.3
- Java: 21
- Fabric API: 0.116.15+1.21.1

## Server Resources

The Minecraft server is currently allocated:

- Initial memory: 2 GB
- Maximum memory: 4 GB

The server configuration can be adjusted as the homelab's resource requirements change.

## Mods

The server uses a collection of Fabric mods that expand gameplay and world generation.

Major mods include:

- Terralith
- Towns & Towers
- YUNG's Better Dungeons
- Farmer's Delight Refabricated
- Traveler's Backpack
- Waystones
- Lithium

Additional dependencies are installed as required by the individual mods.

## Service Management

The Minecraft server runs as a Linux systemd service.

This allows the server to:

- Start automatically with the system
- Run in the background
- Restart automatically after an unexpected failure
- Be managed using standard Linux service commands

The service uses the Fabric server launcher and Java to start the Minecraft server.

## Remote Administration

RCON is enabled for remote server administration.

The RCON configuration is restricted to the local system rather than being exposed directly to the public internet.

This allows administrative commands to be issued without requiring direct access to the Minecraft server console.

## Troubleshooting

Several issues were encountered during the setup and configuration of the server, including:

- Missing mod dependencies
- Minecraft server startup failures
- Conflicting server instances
- World `session.lock` conflicts
- Systemd service configuration
- RCON configuration

These issues were resolved through Linux command-line troubleshooting, log analysis, configuration changes, and service management.

## Current Status

The Minecraft server is currently running as part of the Version 1.0 homelab environment.

The server's resource allocation and configuration may be adjusted as the homelab develops.
