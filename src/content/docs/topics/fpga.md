---
title: FPGA
description: FPGA-based retro hardware — MiSTer, Analogue consoles, and open source core development.
---

> FPGA (Field-Programmable Gate Array) hardware recreates retro console logic at the silicon level rather than through software emulation. In this community, MiSTer is the dominant FPGA platform, with the Analogue Pocket as the other widely discussed device.

## Overview

FPGAs can be programmed to replicate the exact behavior of retro console hardware, including timing, audio, and video characteristics that software emulators approximate. MiSTer FPGA runs on the DE10-Nano development board (Intel Cyclone V FPGA) with optional expansion boards. Analogue builds consumer-grade FPGA consoles in purpose-built shells. The community has a dedicated `#mister` channel and an `#analogue-pocket` channel.

---

## MiSTer FPGA

- **MiSTer FPGA** — The open-source, community-developed FPGA platform built on the DE10-Nano board. Runs cores for hundreds of systems. Widely discussed as a cost-effective, accurate alternative to original hardware. A full stack kit runs roughly $175 as of mid-2025. [MiSTer forums](https://misterfpga.org) · [GitHub – core development](https://github.com/MiSTer-devel)

- **DE10-Nano** — The Intel Cyclone V FPGA development board that MiSTer runs on. Available with aluminum shells for a more finished look.

- **MiSTer Addons** — A popular MiSTer accessories vendor. Sells expansion boards, the Reflex Prism, and publishes a newsletter covering MiSTer developments. [MiSTer Addons](https://misteraddons.com)

- **Reflex Prism** — Digital-to-analog converter from MiSTer Addons. Outputs MiSTer video to analog displays and scalers, including CRTs. Used by community members who run MiSTer alongside traditional analog infrastructure. [Buy · MiSTer Addons](https://misteraddons.com/products/reflex-prism-hdmi-to-analog)

- **Zaparoo** — NFC-based game launcher for MiSTer. Tap an NFC card or tag to launch a game — adds a physical-library feel to the digital collection. App supports title IDs, tags, and a companion phone app. [Zaparoo site](https://zaparoo.org)

### Notable MiSTer Cores

- **N64 Core** — Notable for being considered impossible on MiSTer for years before it was achieved.
- **SNES Core** — Active community discussion; some members note it's based on an existing emulator core rather than a ground-up FPGA recreation.
- **Saturn Core** — In development; SH2 implementation is the main challenge.
- **MultisystemFPGA** — A community platform project for a multi-core FPGA console. Tracked by multiple community members. [@MultisystemFPGA on X](https://twitter.com/MultisystemFPGA)

---

## Analogue Consoles

Analogue builds FPGA-based consumer hardware with original-cartridge compatibility and their OpenFPGA platform for community-developed cores. [Analogue site](https://www.analogue.co)

- **Analogue Pocket** — Handheld FPGA device with Game Boy form factor. Plays original cartridges and OpenFPGA community cores. Added cartridge dumping in December 2025. Community members use EverDrives with it. [Product page](https://www.analogue.co/pocket)

- **Analogue 3D** — N64 FPGA console. Shipped in late 2025 after delays. Funtastic edition 8BitDo controllers started shipping January 2026. [Product page](https://www.analogue.co/3d)

- **Analogue Duo** — NEC PC-Engine / TurboGrafx-16 FPGA console. Still available as of early 2026. [Product page](https://www.analogue.co/duo)

- **OpenFPGA** — Analogue's platform for running community-developed cores on Pocket and compatible devices. Runs ROMs directly without cartridges.

---

## Other FPGA Platforms

- **Superstation** — A long-awaited community FPGA project. Some members who purchased it remain skeptical about delivery.

- **Chromatic** — FPGA handheld mentioned by community members. Available secondhand for around $80; limited community enthusiasm.

---

## System Compatibility

MiSTer has cores for most retro systems. Analogue devices are console-specific:

- **NES / Famicom** — MiSTer core
- **SNES / Super Famicom** — MiSTer core, Analogue Super Nt (legacy, discontinued)
- **Sega Genesis / Mega Drive** — MiSTer core, Analogue Mega Sg (legacy, discontinued)
- **Nintendo 64** — MiSTer core, Analogue 3D
- **Game Boy / GBC / GBA** — MiSTer core, Analogue Pocket
- **PC-Engine / TG-16** — MiSTer core, Analogue Duo
- **PlayStation** — MiSTer core
- **Saturn** — MiSTer core (in development)

---

## Community Notes

- Kytor: *"Why buy an Analogue system only to use a flash cart, when you could just use a MiSTer?"* — A recurring philosophical debate.
- Vuscav: *"These days it's like a $175 kit for the whole stack and it does the upscaling. Ares is better for the things it's compatible with, but higher cost of entry."*
- Gaw notes Analogue's production scarcity is partly a risk-management decision; starlightk7 disagrees, calling it deliberate artificial scarcity.
- Redherring32: *"So tired of people using ancient FPGAs for stuff."* — Commentary on projects still using outdated FPGA chips when newer Lattice/Gowin options exist.

---

*This page was generated from community discussion in the Dubesinhower Modding Community Discord. Last updated: 2026-02-25.*
