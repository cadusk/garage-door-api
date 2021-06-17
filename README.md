![Garage Door Logo](docs/logo.jpg)

# Garage Door API - RaspberryPi
> Python implementation of sensors and components management to
> remotely control garage door.

As part of my home automation solution, Garage Door API is responsible
for the garage door management.

Hardware used in this project are:
* Raspberry Pi Zero W
* DockerPi I2C relay PHAT
* Reed magnetic sensors
* Garage Door remote control

More details about the hardware and set up [here][1].

## Getting Started

This API requires Python3 and Flask.

```shell
git clone https://github.com/cadusk/garage-door-api-python.git
cd garage-door-api
pip install -r requirements.txt
FLASK_APP=run.py flask run
```

### Initial configuration

External components are controlled via I2C interfaces. Make sure your Raspberry
Pi has I2C interfaces enabled. If you need instructions on how to enable I2C
interfaces on a Raspberry PI, find how [here][2].

By default, it will run in `production` mode. Make sure your configuration
matches what is defined in `config.py`.

## Developing

It's a good practice to create a virtual environment to isolate dependencies
required from conflicting with other software/projects you might have
installed.

```shell
git clone https://github.com/cadusk/garage-door-api-python.git
cd garage-door-api
python3 -m venv .venv
pip install -U pip
pip install -r requirements.txt
FLASK_APP=run.py FLASK_ENV=development flask run
```

To learn more about creating python3 virtual environments, take a look at the
[official documentation][3].

### Testing

> TODO: no tests yet

## Deploying

### Preparing your Raspberry PI image
https://www.raspberrypi.org/documentation/installation/installing-images/mac.md

### Wifi and SSH - headless install
- https://www.raspberrypi.org/documentation/configuration/wireless/headless.md
- https://raspberrypi.stackexchange.com/questions/67649/raspberry-pi-zero-w-headless-using-wpa-supplicant-conf-not-working#82923

### Installing required software
git? curl? i2c-tools?

### Initial configuration
- run on boot?
- initialize configuration

[1]: docs/hardware.md "Hardware info"
[2]: docs/i2c.md "How to detect and test I2C devices"
[3]: https://docs.python.org/3/library/venv.html "How to create Python3 virtual environments"
