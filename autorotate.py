import time
import requests
from stem import Signal
from stem.control import Controller
import configparser

def get_current_ip(status="renew"):
    try:
        url = "https://api.ipify.org"
        proxyDict = dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050')

        if status == "init":
            proxyDict = {}

        response = requests.get(url, proxies=proxyDict)
        return response.text
    except Exception as e:
        return str(e)

# Source: https://askubuntu.com/a/849773
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="")
        controller.signal(Signal.NEWNYM)  # Signal Tor to get a new IP

def rotate(interval: int) -> None:
    current_ip = get_current_ip("init")
    print(f"Current IP: {current_ip}")
    while True:
        try:
            renew_tor_ip()
            time.sleep(10)
            new_ip = get_current_ip()
            print(f"New IP: {new_ip}")
            print("IP address changed\n")
            time.sleep(interval)
        except KeyboardInterrupt:
            print("Terminated")
            quit()

def load_config():
    config = configparser.RawConfigParser()
    config.read('config.ini')
    tor_auth = config.get('CONFIG', 'password')
    default_interval = config.getint('CONFIG', 'interval')
    return tor_auth, default_interval

if __name__ == "__main__":
    tor_auth, default_interval = load_config()

    try:
        interval_input = input(f"Time interval to change IP in seconds [{default_interval}]: ")
        interval = int(interval_input) if interval_input else default_interval
    except ValueError:
        print(f"Invalid input. Using default interval: {default_interval}")
        interval = default_interval
    
    rotate(interval)