---
title: HDMI Mods
description: Internal and adapter-based HDMI output mods for retro consoles — clean digital video without a scaler.
---

> HDMI mods give retro consoles a direct digital output, bypassing aging analog circuits. Whether it's a clean plug-and-play dongle or a full internal install, this is one of the most-discussed mod categories in the DMC community.

## Overview

HDMI mods convert a console's native digital or analog video signal into HDMI output. Internal mods tap into the console's video hardware directly, while adapter-based solutions (dongles) plug into existing expansion ports. The goal is lag-free, clean video that works with any modern display — though most community members still pair these with a quality upscaler for best results.

## Options / Products

### Internal Mods

- **PixelFX Retro GEM** — FPGA-based internal HDMI mod available for a wide range of consoles including PS1, PS2, GameCube, N64, Wii, and more. Produced by PixelFX (@pixelfxco). Includes an OSD and GameID integration. Community members widely discuss the GEM line as the current go-to for internal HDMI installs. The GEM also includes a universal upscaler kit variant.
- **UltraHDMI (N64)** — An older internal HDMI mod for the N64. Community members note that some people still pay a premium for it despite the Retro GEM now being available for N64.
- **XboxHDMI / Stellar XboxHD+** — Internal HDMI mod for original Xbox, developed by MakeMHz. Community members use profile integrations with the PixelFX Morph scaler.
- **GCVideo / Pluto IIx** — FPGA-based HDMI output for GameCube via the Digital AV port. A well-established solution; community members reference it for GameCube owners who don't want to do a full GEM install.
- **OpenTendo HDMI** — Open source project to add HDMI to the NES; discussed humorously in community as "OpenTenHDMI."
- **FX Direct** — Open source board from PixelFX (GitLab: `pixelfx-public/fx-direct`) related to GEM connectivity.
- **Panasonic Q Internal HDMI Mod** — GitHub project (`HDR/Panasonic-Q-Internal-HDMI-Mod`) for the GameCube/DVD hybrid console.

### Adapters & Dongles

- **RetroTINK Dongles** — Mike Chi (@retrotink2) released a line of console-specific HDMI adapter cables/dongles. Community members followed these closely as a simpler alternative to internal mods.
- **AVE HDMI (Wii Mini)** — An HDMI adapter that works with the Wii Mini (requires one extra wire). Discussed as a quick solution.
- **Reflex Prism** — Made by MiSTer Addons. A digital-to-analog and HDMI bridge for MiSTer; community members noted its use for running GameCube games via HDMI directly.
- **JAG2HD** — HDMI video adapter for Atari Jaguar by Humble Bazooka; available at Stone Age Gamer.

### Switches & Infrastructure

- **gscartsw** — Widely discussed analog SCART switch; many members use it alongside HDMI-modded consoles.
- **Infinity Switch** — An anticipated all-in-one switch (from Arthrimus) that would combine HDMI and analog inputs in one unit. Community members followed this closely and discussed it as a potential replacement for separate HDMI and SCART switch setups. HDMI port count was debated repeatedly in Discord.
- **Otaku Games SCART Switch Mod** — A community mod that allows a generic HDMI switch to support profile switching via voltage sensing. Code by svirant: `github.com/svirant/RT4k_HD15_serial_control`.

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
