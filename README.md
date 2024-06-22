# Tor IP rotator
Tor IP Rotator is a Python tool designed to rotate your IP address for the Tor network at specified intervals. This tool ensures that your IP changes every X seconds, enhancing your privacy and anonymity while using the Tor network. It's ideal for scenarios where frequent IP changes are necessary, such as web scraping, data collection, or enhancing online privacy.

## Features
Configurable Interval: Easily set the interval time to change IP addresses via configuration file or user input.
User-Friendly: Clear prompts and messages for easy usage.

## Requirements
- Python 3.5 < x
- Tor
- Requests
- Requets Socks
- Stem
- configparser

## Installation
Clone the repository:
```sh
git clone git@github.com:ariyaadinatha/tor-ip-rotator.git
```

Install the necessary dependencies:
```sh
pip install -r requirements.txt
```

## Usage
1. Ensure Tor is running on your machine.
2. Rename `config.ex.ini` to `config.ini`
3. Configure the interval in the `config.ini` file or provide it as an input when prompted.
4. Run the script:
```sh
python3 autorotate.py
```

## Configuration
Edit the config.ini file to set the default interval for IP rotation:
```ini
[CONFIG]
password = TOR_PASSWORD # TOR password  
interval = 60 # Default time interval
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.
