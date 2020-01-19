import subprocess

def get_devices():
    result = str(subprocess.check_output(["arp", "-a"]))

    devices = set()
    for word in result.split():
        if ":" in word:
            devices.add(word)
            
    return devices

def main():
    """Main function"""
    print("Finding devices...")

    devices = get_devices()

    print(f"There are {len(devices)} devices on your current network.")

if __name__ == "__main__":
    main()
