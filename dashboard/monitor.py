import json
import os
import time

from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("PROXMOX_HOST")
user = os.getenv("PROXMOX_USER")
token = os.getenv("PROXMOX_TOKEN")

url = f"https://{host}:8006/api2/json/cluster/resources"

headers = {
	"Authorization": f"PVEAPIToken={user}={token}"
}

def get_proxmox_data():
	response = requests.get(
		url,
		headers=headers,
		verify=False
	)

	response.raise_for_status()

	return response.json()["data"]

history = []
vm_history = {}

while True:

	resources = get_proxmox_data()

	host_data = None
	vms = []
	storage = []

	for resource in resources:

		if resource["type"] == "node":
			host_data = {
				"cpu": resource["cpu"] * 100,
				"memory_used": resource["mem"],
				"memory_total": resource["maxmem"],
				"cores": resource["maxcpu"]
			}

		elif resource["type"] == "qemu":

			vmid = resource["vmid"]

			if vmid not in vm_history:
				vm_history[vmid] = []

			memory_percent = (
				resource["mem"] / resource["maxmem"]
			) * 100

			vm_history[vmid].append({
				"time": datetime.now().strftime("%H:%M:%S"),
				"cpu": resource["cpu"] * 100,
				"memory": memory_percent
			})

			vms.append({
				"name": resource["name"],
				"vmid": resource["vmid"],
				"status": resource["status"],
				"uptime": resource["uptime"],
				"cpu": resource["cpu"] * 100,
				"memory_used": resource["mem"],
				"memory_total": resource["maxmem"],
				"netin": resource["netin"],
				"netout": resource["netout"],
				"history": vm_history[vmid]
			})
		elif resource["type"] == "storage":
			storage.append({
				"name": resource["storage"],
				"used": resource["disk"],
				"total": resource["maxdisk"]
			})

	data = {
		"host": host_data,
		"storage": storage,
		"vms": vms,
		"history": history
	}

	history.append({
		"time": datetime.now().strftime("%H:%M:%S"),
		"cpu": host_data["cpu"],
		"memory": (
			host_data["memory_used"] /
			host_data["memory_total"]
		) * 100
	})

	if len(history) > 150:
		history.pop(0)

	temp_file = "/var/www/html/status.json.tmp"

	with open(temp_file, "w") as file:
		json.dump(data, file, indent=4)

	os.replace(temp_file, "/var/www/html/status.json")

	print("Dashboard data updates", flush=True)
	
	time.sleep(2)
