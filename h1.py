#!/usr/bin/env python3
import yaml
import json
import sys

with open("vars/baseline.yml") as f:
    v = yaml.safe_load(f)

hostname = v["hostname"]

linux_ips = v.get("ips", [])
windows_ips = v.get("windows_ips", [])

old_hosts = []
new_hosts = []
windows_hosts = []
hostvars = {}

# LINUX HOSTS 
for i, ip in enumerate(linux_ips, start=1):
    host = f"{hostname}-{i}"

    old_hosts.append(host)
    new_hosts.append(host)

    hostvars[host] = {
        "ansible_host": ip,
        "ansible_user": v["old_username"],
        "ansible_port": v.get("ssh_port", 22),

        "ansible_connection": "ssh",
        "ansible_ssh_private_key_file": v.get(
            "ssh_key_file",
            "~/.ssh/id_ed25519"
        )
    }

# WINDOWS HOSTS
for i, ip in enumerate(windows_ips, start=1):
    host = f"{hostname}-win-{i}"

    windows_hosts.append(host)

    hostvars[host] = {
        "ansible_host": ip,
        "ansible_user": v["win_user"],
        "ansible_shell_type": "powershell",
        "ansible_password": v["win_user_pass"],

        "ansible_connection": "ssh",
        "ansible_port": v.get("wssh_port", 22),
        "ansible_remote_tmp": "tempdir"

    }

# INVENTORY STRUCTURE
inventory = {
    "old": {
        "hosts": old_hosts
    },
    "new": {
        "hosts": new_hosts
    },
    "windows": {
        "hosts": windows_hosts
    },
    "all": {
        "children": ["old", "new", "windows"]
#        "vars": {
#            "ansible_python_interpreter": "/usr/bin/python3"


    },
    "_meta": {
        "hostvars": hostvars
    }
}

json.dump(inventory, sys.stdout, indent=2)
