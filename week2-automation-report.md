WEEK 2 AUTOMATION REPORT
DATE: July 2026
TOPIC: Python Automation with Netmiko on GNS3
OBJECTIVE: SSH into a Cisco router and retrieve show commands using Python


1. ENVIRONMENT SETUP

| Item | Details |
|------|---------|
| Operating System | Ubuntu 24.04 |
| Network Simulator | GNS3 2.2.60 |
| Router Image | c3745-adventerprisek9-mz.124-25d.image |
| Router Platform | Cisco 3745 |
| Python Version | 3.12 |
| Netmiko Version | 4.7.0 |
| Router IP | 192.168.122.235 |
| Router Username | admin |
| Router Password | admin |


2. ROUTER CONFIGURATION

Commands used to enable SSH on the router:

enable
configure terminal
hostname R1
interface fastEthernet 0/0
ip address dhcp
no shutdown
exit
ip domain-name lab.local
crypto key generate rsa
1024
username admin password admin
enable secret admin
line vty 0 4
login local
transport input ssh
exit
end
write memory


3. SSH VERIFICATION

Command:
show ip ssh

Output:
SSH Enabled - version 1.99
Authentication timeout: 120 secs; Authentication retries: 3


4. PYTHON SCRIPT

File: connect_router.py

from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.122.235",
    "username": "admin",
    "password": "admin",
    "secret": "admin",
    "global_delay_factor": 2,
}

print("Connecting to GNS3 router...")
connection = ConnectHandler(**router)
connection.enable()
output = connection.send_command("show ip interface brief")
print(output)
connection.disconnect()
print("Disconnected.")


5. SCRIPT OUTPUT

Connecting to GNS3 router...

Interface          IP-Address      OK? Method Status        Protocol
FastEthernet0/0    192.168.122.235 YES DHCP   up            up
FastEthernet0/1    unassigned      YES NVRAM  down          down

Disconnected.


6. TROUBLESHOOTING LOG

| # | Error | Cause | Fix |
|---|-------|-------|-----|
| 1 | TCP connection timeout | Router IP conflict with Huawei router | Changed router IP to 192.168.122.235 |
| 2 | SSH connection refused | SSH not enabled on router | Configured crypto key and SSH settings |
| 3 | Unable to negotiate key exchange | SSH version mismatch | Used global_delay_factor in Netmiko |
| 4 | Ping from PC to router failed | Cloud not bridging correctly | Changed Cloud to NAT and set router to DHCP |


7. KEY LEARNINGS

1. GNS3 Cloud requires NAT or proper bridging to communicate with the host PC.
2. Cisco router interfaces are administratively down by default. Must use no shutdown.
3. SSH must be manually configured on Cisco IOS including crypto key generation.
4. Old Cisco IOS uses older SSH encryption. Netmiko handles this with global_delay_factor.
5. DHCP on the router allows it to get an IP from the host network automatically.
6. Netmiko allows Python to SSH into network devices and run commands programmatically.


8. NEXT STEPS

- Automate VLAN creation
- Backup router config automatically
- Configure multiple routers with a single script
- Monitor interface status with a loop
- Send configuration changes via Python


9. CONCLUSION

This lab successfully demonstrated automation of a Cisco router using Python and Netmiko. The router was configured with SSH, connected to the host PC via GNS3, and managed remotely using a Python script.

This is the foundation for network automation engineering.

---

END OF REPORT
