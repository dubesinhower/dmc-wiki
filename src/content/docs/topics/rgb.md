---
title: RGB & SCART
description: RGB video output mods, SCART cabling, and analog signal infrastructure for retro consoles.
---

> RGB is the gold standard analog video format for retro console output — sharper and more accurate than composite or S-Video, and the foundation for a quality CRT or upscaler setup. SCART is the connector standard that carries RGB in Europe and among enthusiasts worldwide.

## Overview

Many retro consoles output RGB natively or can be modded to do so. RGB mods replace or supplement inferior video outputs (composite, RF) with a full RGB signal, typically delivered over a SCART cable to an upscaler or CRT. In this community, RGB is usually the first step before adding an HDMI mod or upscaler to the chain. retrorgb.com (run by Bob) is the canonical reference site for this topic.

## Options / Products

### RGB Mods by Console

- **NESRGB** — Internal RGB mod for the NES and Famicom. Produced by Tim Worthington. Replaces the PPU to output clean RGB; requires a donor PPU chip. The community go-to for NES RGB for years. [Project site](https://etim.net.au/nesrgb/) · [Buy · Laser Bear](https://www.laserbear.net)

- **2600RGB** — RGB mod for the Atari 2600. A new version was released in 2025 with sync fixes; starlightk7 upgraded specifically for the sync improvements. Also by Tim Worthington. [Project site](https://etim.net.au)

- **N64 RGB add-on** (Arthrimus) — An N64 RGB board designed to complement the N64 GEM install. An option for those running the GEM who also want RGB output.

- **Genesis Model 1 Subcarrier Bypass** — A method documented on RetroRGB for improving Genesis Model 1 RGB output by bypassing the subcarrier. Open-source; credited to community members including RGBeter. [RetroRGB article](https://retrorgb.com/genesis-model-1-subcarrier-bypass-new-method-tested.html)

- **RGBDRV** (RGBeter / RGBeter32X) — Community-designed open-source RGB driver board. Noted as high quality but with availability issues. [@RGBeter32X on X](https://twitter.com/RGBeter32X)

- **PC-Engine RGB mod (composite-color accurate)** — In development as of January 2026. GallandRegis working on an RGB mod that can display composite-accurate colors alongside standard RGB output.

### Cables & Connectors

- **Retro Access** — SCART and component cable maker. Widely used in the community; known for high-quality cables including Genesis Model 1 cables with audio breakout and 32X patch cables. [Retro Access](https://retro-access.com)

- **Retro Gaming Cables** — Another well-regarded cable vendor. Community members compare them to Retro Access; both are considered quality options. [Retro Gaming Cables](https://www.retrogamingcables.co.uk)

- **VGA to SCART adapter** (RayneX) — Open-source VGA-to-SCART adapter PCB. Routes VGA-carrying scalers into SCART infrastructure. BOM from Mouser, PCBs from OSH Park.

### Switches & Infrastructure

- **gscartsw** — Automatic SCART switch. Widely used as the hub for all SCART-connected consoles in a setup. Sync-on-luma and sync-on-composite supported. [gscartsw site](https://www.gretrostuff.com)

- **gcomp** — Component video switch, mentioned alongside gscartsw for component-output consoles.

- **Otaku Games SCART Switch Mod** — Allows a generic HDMI switch to auto-switch profiles via voltage sensing. Code by svirant. [GitHub](https://github.com/svirant/RT4k_HD15_serial_control/tree/main/Otaku%20Games%20Scart%20Switch)

### Upscalers (see also: [Upscalers](/topics/upscalers))

- **OSSC (Open Source Scan Converter)** — Open-source FPGA-based line multiplier. Budget-accessible entry point for RGB setups. Available from Video Game Perfection. [Buy · VGP](https://www.videogameperfection.com/products/ossc/)

- **OSSC Pro** — Updated version with Legacy AV and RF input support. Gaw noted in Feb 2026 that it was going through a board revision; stock was expected to be limited until Q2 2026. [Buy · VGP](https://www.videogameperfection.com/products/ossc-pro/)

- **Framemeister (XRGB Mini)** — Japanese upscaler by Micomsoft. Still in use; considered a legacy option by many community members compared to OSSC and RetroTINK.

## Console Compatibility

RGB output by console (native or with mod):

- **SNES / Super Famicom** — Native RGB via SCART multi-out
- **Genesis / Mega Drive** — Native RGB (Model 1 & 2); Model 3 requires mod
- **PlayStation 1** — Native RGB via SCART multi-out
- **Sega Saturn** — Native RGB via SCART multi-out
- **Dreamcast** — Native VGA / RGB via VGA box or SCART
- **Neo Geo AES** — Native RGB
- **NES / Famicom** — Requires NESRGB mod
- **Atari 2600** — Requires 2600RGB mod
- **PC-Engine / TG-16** — Native RGB (requires RGB cable); TurboGrafx composite-only without mod
- **Nintendo 64** — Requires RGB mod (revision-dependent)

## Community Notes

- retrorgb.com is the go-to reference for virtually any RGB mod. Community members share new articles from the site regularly (LaserActive PSU replacement, Genesis subcarrier bypass, OSSC Pro updates, etc.).
- RGBeter (community member) is active in open source RGB hardware development, including the RGBDRV and related projects.
- The community is split on SCART vs. VGA as the primary analog connection. Gaw argues VGA is more future-proof since modern scalers support HD-15 and serial. Others prefer SCART for its convenience with existing infrastructure.
- subierekt: *"SCART cables are cheaper than HDRetrovision cables."*
- Tubo: *"gscarts still sell well. People still pay a premium for UltraHDMI even with GEM available. Old internet info will still influence."*
- Mike Chi (RetroTINK) has been noted as not being a fan of SCART — an observation that generated community discussion.
- GabeShack has been looking to redo Atari RGB-to-SCART cabling, specifically wanting a cable with a 1/8" tail that routes cleanly into the SCART connector.
- The NESRGB community and OpenTendo (Redherring32) have had friction; Redherring32 noted that NESRGB compatibility is not an OpenTendo issue and asked people to stop using his GitHub issues page for it.

## Resources

- <https://retrorgb.com> — retrorgb.com — the canonical RGB reference site
- <https://retrorgb.com/genesis-model-1-subcarrier-bypass-new-method-tested.html> — Genesis Model 1 bypass doc
- <https://retrorgb.com/ossc-pro-legacy-av-with-rf-input.html> — OSSC Pro with RF input
- <https://etim.net.au/shop/shop.php?crn=210&rn=552&action=show_detail> — 2600RGB new version
- <https://retro-access.com> — Retro Access cable shop
- <https://github.com/svirant/RT4k_HD15_serial_control/tree/main/Otaku%20Games%20Scart%20Switch> — Otaku SCART switch mod

---
*This page was generated from community discussion in the DMC Discord. Last updated: 2026-02-25.*
