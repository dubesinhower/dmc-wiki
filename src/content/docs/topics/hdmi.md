---
title: HDMI Mods
description: Internal and adapter-based HDMI output mods for retro consoles — clean digital video without a scaler.
---

> HDMI mods give retro consoles a direct digital output, bypassing aging analog circuits. Whether it's a clean plug-and-play dongle or a full internal install, this is one of the most-discussed mod categories in the DMC community.

## Overview

HDMI mods convert a console's native digital or analog video signal into HDMI output. Internal mods tap into the console's video hardware directly, while adapter-based solutions (dongles) plug into existing expansion ports. The goal is lag-free, clean video that works with any modern display — though most community members still pair these with a quality upscaler for best results.

## Options / Products

### Internal Mods

- **PixelFX Retro GEM** — FPGA-based internal HDMI mod available for PS1, PS2, GameCube, N64, Wii, and more. Includes an OSD and GameID integration. The current community go-to for internal HDMI installs. [Buy · Stone Age Gamer](https://stoneagegamer.com/retro-gem-universal-hdmi-upscaler-kit-for-ps1-ps2-n64-pixelfx.html) · [PixelFX site](https://pixelfx.co)

- **UltraHDMI (N64)** — An older internal HDMI mod for the N64. Community members note that some people still pay a premium for it despite the Retro GEM now covering N64. Worth sourcing secondhand if you find one at a fair price.

- **XboxHDMI / Stellar XboxHD+** — Internal HDMI mod for original Xbox, developed by MakeMHz. Integrates with PixelFX Morph scaler profiles. [MakeMHz site](https://makemhz.com/products/xboxhd)

- **GCVideo / Pluto IIx** — FPGA-based HDMI output for GameCube via the Digital AV port. Well-established solution for GameCube owners who don't want a full GEM install. Requires a GameCube with the Digital AV Out port (not present on DOL-101). [Buy · Castlemania Games](https://www.castlemaniagames.com/products/pluto-iix-hdmi-mod-for-gamecube)

- **FX Direct** — Open-source board from PixelFX related to GEM connectivity. [GitLab](https://gitlab.com/pixelfx-public/fx-direct)

- **Panasonic Q Internal HDMI Mod** — GitHub project adding internal HDMI to the Panasonic Q (GameCube/DVD hybrid). [GitHub](https://github.com/HDR/Panasonic-Q-Internal-HDMI-Mod)

### Adapters & Dongles

- **RetroTINK Dongles** — Console-specific HDMI adapter cables by Mike Chi (@retrotink2). A simpler alternative to internal mods — no soldering required. Covers multiple systems. [RetroTINK site](https://www.retrotink.com)

- **AVE HDMI (Wii Mini)** — HDMI adapter for the Wii Mini. Requires one additional wire during installation. A quick, low-cost solution for HDMI output on the Wii Mini. Available from various resellers; search "Wii Mini HDMI adapter."

- **Reflex Prism** — Digital-to-analog and HDMI bridge for MiSTer, made by MiSTer Addons. Used for routing MiSTer output to analog displays and scalers. [Buy · MiSTer Addons](https://misteraddons.com/products/reflex-prism-hdmi-to-analog)

- **JAG2HD** — HDMI video adapter for the Atari Jaguar, by Humble Bazooka. [Buy · Stone Age Gamer](https://stoneagegamer.com/jag2hd-video-adapter-for-atari-jaguar-humble-bazooka.html)

### Switches & Infrastructure

- **gscartsw** — Widely discussed analog SCART switch. Many members use it alongside HDMI-modded consoles to manage mixed analog/digital setups. [gscartsw site](https://www.gretrostuff.com)

- **Infinity Switch** — Anticipated all-in-one switch from Arthrimus that would combine HDMI and analog inputs. Community members followed this closely; HDMI port count changed in every discussion thread.

- **Otaku Games SCART Switch Mod** — Community mod allowing a generic HDMI switch to support profile switching via voltage sensing. Code by svirant. [GitHub](https://github.com/svirant/RT4k_HD15_serial_control/tree/main/Otaku%20Games%20Scart%20Switch)

## Console Compatibility

- **GameCube** — GCVideo dongle, GEM internal, Prism adapter
- **N64** — Retro GEM, UltraHDMI (legacy)
- **PS1 / PS2** — Retro GEM (PS2 no-cut phat mount available via 3D print)
- **Wii** — Retro GEM (in development), AVE HDMI dongle
- **Original Xbox** — XboxHDMI / Stellar XboxHD+
- **Neo Geo** — MV1C-based Taitoc HDMI upgrade via OMVS
- **Atari Jaguar** — JAG2HD adapter
- **Panasonic Q** — Internal HDMI mod (GitHub: HDR)
- **PC-FX** — ODE-integrated HDMI (in development as of early 2026)
- **SNES** — atract working on an SNES HDMI mod (noted by Dubesinhower, May 2025)
- **3DS** — No widely available flash cart or HDMI solution as of early 2026; community awaits

## Community Notes

- RayneX: *"People still pay a premium for UltraHDMI even with GEM available. Old internet info will still influence."*
- Community consensus is to pair HDMI-modded consoles with a quality scaler (RetroTINK or Morph) for best results on modern displays.
- The Infinity Switch generated sustained discussion — HDMI port count changed every time someone asked, so members stopped asking.
- Breakaway HDMI cables (like mini-HDMI to HDMI) are recommended to protect GEM ports from port stress.
- PixelFX newsletters are a primary source for GEM updates; Dubesinhower summarizes them for the community.
- Blueshell3D made a custom back panel with HDMI cutout for the GameCube GEM install (available on Printables).
- The Wii GEM and full-size PS1 port were two of the most anticipated upcoming releases as of early 2026.

## Resources

- <https://www.pixelfx.co/hdmi-retro-gem> — PixelFX Retro GEM product page
- <https://www.pixelfx.co/post/pixel-fx-newsletter> — PixelFX newsletters
- <https://gitlab.com/pixelfx-public/fx-direct> — FX Direct open source repo
- <https://github.com/HDR/Panasonic-Q-Internal-HDMI-Mod> — Panasonic Q HDMI mod
- <https://misteraddons.com/products/reflex-prism-hdmi-to-analog> — Reflex Prism at MiSTer Addons
- <https://stoneagegamer.com/jag2hd-video-adapter-for-atari-jaguar-humble-bazooka.html> — JAG2HD
- <https://github.com/svirant/RT4k_HD15_serial_control/tree/main/Otaku%20Games%20Scart%20Switch> — Otaku SCART switch mod code
- <https://retrotink-llc.github.io/firmware/4k-experimental.html> — RetroTINK experimental firmware

---
*This page was generated from community discussion in the DMC Discord. Last updated: 2026-02-25.*
