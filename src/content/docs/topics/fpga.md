---
title: FPGA
description: FPGA-based retro hardware — MiSTer, Analogue consoles, and open source core development.
---

> FPGA (Field-Programmable Gate Array) hardware recreates retro console logic at the silicon level rather than through software emulation. In this community, MiSTer is the dominant FPGA platform — it has its own dedicated channel — with the Analogue Pocket as the other widely discussed device.

## Overview

FPGAs can be programmed to replicate the exact behavior of retro console hardware, including timing, audio, and video characteristics that software emulators approximate. This makes FPGA solutions attractive for accuracy-focused enthusiasts. MiSTer FPGA runs on the DE10-Nano development board (Intel Cyclone V FPGA) with optional expansion boards, while Analogue builds consumer-grade FPGA consoles in purpose-built shells. The community has a dedicated `#mister` channel and an `#analogue-pocket` channel.

## Options / Products

### MiSTer FPGA

- **MiSTer FPGA** — The open source, community-developed FPGA platform built on the DE10-Nano board. Runs cores for hundreds of systems. Community members reference MiSTer frequently as a cost-effective, accurate alternative to original hardware. A full stack kit is available for roughly $175 (as of mid-2025 per Vuscav).
- **DE10-Nano** — The Intel Cyclone V FPGA development board that MiSTer runs on. Available with aluminum shells; Vuscav notes these look more polished than bare project boxes.
- **MiSTerPi** — A Raspberry Pi-based MiSTer form factor variant. RayneX has one installed inside a cab with a custom power switch. Available from community builders.
- **MiSTer Addons** — A popular MiSTer accessories vendor (misteraddons.com). Sells add-on boards, the Reflex Prism (digital-to-analog bridge), and runs a newsletter.
- **Reflex Prism** — A digital-to-analog converter from MiSTer Addons for outputting MiSTer video to analog displays/scalers. RayneX uses it for connecting MiSTer to CRTs and analog infrastructure.
- **Zaparoo** — An NFC-based game launcher for MiSTer. Tap an NFC card/tag to a reader to launch a game. The Zaparoo App (v1.9.1+) supports title IDs, tags, and a companion phone app. Community members find it adds a physical-library feel.
- **Sinden Lightgun (MiSTer)** — The Sinden lightgun has MiSTer-specific support; SAG sells a holster/recoil version compatible with it.

### MiSTer Cores

- **SNES Core** — Widely discussed. Some community members note it's based on an existing emulator core. Redherring32 questions whether FPGA improves on modern accurate emulators for SNES.
- **N64 Core** — Notable for being considered impossible on MiSTer for years. Tubo: *"Remember when people thought N64 was impossible on MiSTer?"*
- **MegaDrive Core** — donutswdad references the Tesmart 16x1 switch compatibility with the MiSTer MegaDrive core specifically.
- **Saturn Core** — Gaw speculated the Saturn core development (SH2 implementation) may have contributed to the GameCube memory card development.
- **MultisystemFPGA** — A community account (@MultisystemFPGA / multisystemfpga.bsky.social) that covers FPGA multi-system development. RayneX and Dubesinhower share posts from this account regularly.
- **SNES CPU via FPGA** — hackaday.com covered a community project replacing the SNES CPU with an FPGA (March 2025).

### Analogue Consoles

Analogue builds FPGA-based consumer hardware with original-cartridge compatibility and their OpenFPGA platform for community-developed cores.

- **Analogue Pocket** — Handheld FPGA device with Game Boy form factor. Supports original cartridges and OpenFPGA community cores. Can also dump Game Boy cartridges (December 2025 feature). Community members use EverDrives with it. Tubo noted Analogue "never gives a shit" about EverDrive compatibility.
- **Analogue Duo** — NEC PC-Engine / TG-16 FPGA console. Community member subierekt notes it hasn't sold out even though the PC-Engine is a "holy grail" console.
- **Analogue 3D** — N64 FPGA console. Announced and shipped in late 2025. Funtastic edition 8BitDo controllers started shipping in January 2026. Community members were skeptical about delays but it shipped.
- **Analogue Editions 3D Prototype** — Analogue listed a 3D prototype edition (analogue.co/editions/3d-prototype).
- **OpenFPGA** — Analogue's platform for running community-developed cores on Pocket (and some other devices). Runs ROMs directly without cartridges.

### Other FPGA Platforms

- **Epilogue** — Released a limited edition SNES cartridge reader for $60 (preorder December 2025). Marketed similarly to Analogue's approach.
- **Superstation** — A long-awaited community FPGA project. Some members who purchased it remain skeptical about delivery; Tubo purchased one.
- **Chromatic** — Another FPGA handheld, mentioned by Vuscav. Available secondhand for around $80 but community enthusiasm was limited.

## Console Compatibility

MiSTer has cores for most retro systems. Analogue devices are console-specific:

| System | FPGA Solution |
|---|---|
| NES | MiSTer core |
| SNES | MiSTer core, Analogue Super Nt (legacy) |
| Genesis | MiSTer core, Analogue Mega Sg (legacy) |
| N64 | MiSTer core, Analogue 3D |
| Game Boy / GBC / GBA | MiSTer core, Analogue Pocket |
| PC-Engine / TG-16 | MiSTer core, Analogue Duo |
| Saturn | MiSTer core (in development) |
| PlayStation | MiSTer core |

## Community Notes

- Kytor: *"Why buy an Analogue system only to use a flash cart, when you could just use a MiSTer?"* — A recurring philosophical debate in the community.
- Vuscav: *"This is one reason MiSTer does pretty well — these days it's like a $175 kit for the whole stack and it does the upscaling. Ares is better for the things it's compatible with, but higher cost of entry."*
- Gaw notes Analogue is not a huge company and their production scarcity is partly a risk-management decision rather than purely a FOMO marketing tactic — though starlightk7 disagrees, calling it deliberate artificial scarcity.
- Redherring32: *"So tired of people using ancient FPGAs for stuff."* — Commentary on projects still using outdated Intel/Altera FPGAs when newer Lattice/Gowin options exist.
- The MiSTer community actively debates which FPGA chips (Lattice, Gowin, etc.) make better choices for new projects going forward. Alterac asked about this in January 2026.
- MultisystemFPGA is an ongoing community platform project for a multi-core FPGA console; community members find some of its design choices amusing.

## Resources

- <https://misterfpga.org> — MiSTer FPGA community forums
- <https://misteraddons.com> — MiSTer Addons (hardware and accessories)
- <https://github.com/MiSTer-devel> — MiSTer core development (GitHub)
- <https://www.analogue.co> — Analogue official site
- <https://www.timeextension.com/news/2025/12/you-can-now-use-the-analogue-pocket-to-dump-your-game-boy-cartridges> — Analogue Pocket cartridge dumping
- <https://hackaday.com/2025/03/31/a-snes-cpu-replacement-via-fpga/> — SNES CPU via FPGA (Hackaday)

---
*This page was generated from community discussion in the DMC Discord. Last updated: 2026-02-25.*
