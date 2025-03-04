# RPi Asset OTA Example with Particle and B504e
This is an example program illustrating how to use Particle's Asset OTA feature to "re-program" a Raspberry Pi. 

This application should be used alongside the [rpi-asset-ota-firmware](https://github.com/epietrowicz/rpi-asset-ota-firmware) project. The firmware is reponsible for receiving the latest script from a Particle OTA event and sending over a serial connection to the Raspberry Pi. This repository, rpi-asset-ota-app, shows how you can recieve the latest script via serial and execute it with a new subprocess.

This example uses a [Muon carrier board](https://store.particle.io/products/particle-muon-carrier-development-board?_pos=1&_sid=c8d3de25d&_ss=r) for the [B504e](https://store.particle.io/products/b-series-lte-cat-1-3g-noram-ethersim-x1?_pos=1&_sid=b0de3c689&_ss=r) and a [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/).

Below is a diagram showing this process works:

![rpi-asset-ota-diagram](https://github.com/user-attachments/assets/65ecf8e3-7ea1-493b-919f-85a5910c9769)


The Raspberry Pi and the Particle Muon should be connected as follows:

<img src="https://github.com/user-attachments/assets/8b46c27e-9e6d-487e-965b-40677b43f612" height=500 />

![desktop-view](https://github.com/user-attachments/assets/c351ec95-7e5c-46bd-82fd-92f03a9dd7de)
