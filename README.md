# Novostok - Handheld Emulation Console (Raspberry Pi 5)

**Novostok** is a DIY open-source emultation console designed around the **Raspberry Pi 5** with a focus on performance, affordability and replicability. This project was developed as part of a BSc (Hons) Applied Computing dissertation and includes full documentation of the design, assembly and testing process.

> Built to emulate consoles up to the PlayStation 2 with full button parity and minimal latency.

> Informal discussion time, the intention behind this project and the choice to do it was not to make the most amazing emulation console available. So many others have that covered like the [Null2](https://www.null2.co.uk/) and the [RetroLite](https://github.com/StonedEdge/Retro-Lite-CM4) just to name a few. The point was to challenge myself and explore concepts not covered within my discipline at university, to learn something that I might not get the opportunity to otherwise. I could've simply designed and ordered small runs of PCBs and carrier boards to complete this project but aside from the cost likely being far too high for a broke university student, that reduces some of the self imposed complexity or needing to manully juggle complex wire runs and soldering. This approach teaches the very fundementals of 3D modelling/printing, soldering, microelectronics and the intricacies of HCI in DIY devices like this, and personally, this project has satisfied me. The burns, headaches and flux fumes were well worth it as these skills can and will come in handy later in life, even if not in my career. There WILL be a version 2 that incorporates the above, with power management, speakers and such and hopefully the initial goal of getting it working for proper Nintendo DS emulation, when that happens it can be found [here]()

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
📁 docs/              # Dissertation PDF, images, and licensing
📁 assets/            # Branding, media, animations
📄 LICENSE            # MIT License for software and hardware
📄 README.md          # This file
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
- **Software, STL files and hardware diagrams** are licensed under the [MIT License](./LICENSE).
You're free to use, modify and redistribute with attribution.

- **Dissertation and supporting documentation** (including the build guide) are licensed uder the [Creative Commons Atrribution-NoDerivitives 4.0 International (CC BY-ND 4.0)](https://creativecommons.org/licenses/by-nd/4.0/).
You may reference but not alter or redistribute this content without permission. See [`docs/LICENSE.docs`](./docs/LICENSE.docs).

---

## Showcase

<p align="center">
  <img src="assets/images/The Novostok 2.jpg" alt="Novostok device assembled" width="750" />
</p>






