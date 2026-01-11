import subprocess

hosts = ["8.8.8.8", "1.1.1.1", "192.168.1.100"]

for host in hosts:
    result = subprocess.run(
        ["ping", "-c", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print(f"{host} is UP")
    else:
        print(f"{host} is DOWN")
