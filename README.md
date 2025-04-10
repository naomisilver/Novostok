# Novostok - Handheld Emulation Console (Raspberry Pi 5)

**Novostok** is a DIY open-source emultation console designed around the **Raspberry Pi 5** with a focus on performance, affordability and replicability. This project was developed as part of a BSc (Hons) Applied Computing dissertation and includes full documentation of the design, assembly and testing process.

> Built to emulate consoles up to the PlayStation 2 with full button parity and minimal latency.

---

## Features
- Fully custom enclosure designed and modeled in Fusion
- 3D printable STL files for all physical parts
- USB HID input handling via Raspberyr Pi Pico and `usb_hid` (Adafruit CircuitPython)
- Dual joystick support using ADS1115 for analgoue input
- Low latency performance using RetroPie and Raspberry Pi OS Lite
- Modular design for easy upgrades and guture expansion

---

## Repository structure

```text
📁 archive/           # Old or unused STL models and scripts
📁 hardware/          # STL files, wiring diagrams, build photos
📁 firmware/          # Pico and Pi scripts for input and control
📁 software/          # RetroPie setup scripts, optional demo games
📁 docs/              # Dissertation PDF, images, and licensing
📁 assets/            # Branding, media, animations
📄 LICENSE            # MIT License for software and hardware
📄 README.md          # This file
📄 .gitignore
```

## Build guide and documentation

A full build guide, including wiring, assembly, dependencies, and usage instructions is available within the [GitHub Wiki](https://github.com/naomisilver/novostok/wiki).
It includes:
- Bill of Materials
- Assembly and soldering
- Software installation
- Input and display setup

---

## Licesning

This repository uses dual licensing to distinguish between code/design and written documentation:
-**Software, STL files and hardware diagrams** are licensed under the [MIT License](./LICENSE).
You're free to use, modify and redistribute with attribution.

-**Dissertation and supporting documentation** (including the build guide) are licensed uder the [Creative Commons Atrribution-NoDerivitives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/).
You may reference but not alter or redistribute this content without permission. See [`docs/LICENSE.docs`](./docs/LICENSE.docs).

---

## Showcase

<p align="center">
  <img src="docs/images/device_assembled.jpg" alt="Novostok device assembled" width="500" />
  <br>
  <i>TBD</i>
</p>






