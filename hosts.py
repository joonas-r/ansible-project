#!/usr/bin/env python3
import yaml
import json
import sys

with open("vars/baseline.yml") as f:
    v = yaml.safe_load(f)

base_hostname = v["hostname"]
ips = v.get("ips", [])

old_hosts = []
new_hosts = []

hostvars = {}

for i, ip in enumerate(ips, start=1):
    hostname = f"{base_hostname}-{i}"

    old_hosts.append(hostname)
    new_hosts.append(hostname)

    hostvars[hostname] = {
        "ansible_host": ip
    }

inventory = {
    "old": {
        "hosts": old_hosts,
        "vars": {
            "ansible_user": v["old_username"]
        }
    },
    "new": {
        "hosts": new_hosts,
        "vars": {
            "ansible_user": v["username"]
        }
    },
    "all": {
        "children": ["old", "new"],
        "vars": {
            "ansible_python_interpreter": "/usr/bin/python3"
        }
    },
    "_meta": {
        "hostvars": hostvars
    }
}

json.dump(inventory, sys.stdout)
