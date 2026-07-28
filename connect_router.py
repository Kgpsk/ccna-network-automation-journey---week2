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
