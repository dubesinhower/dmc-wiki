---
title: RGB & SCART
description: RGB video output mods, SCART cabling, and analog signal infrastructure for retro consoles.
---

> RGB is the gold standard analog video format for retro console output — sharper and more accurate than composite or S-Video, and the foundation for a quality CRT or upscaler setup. SCART is the connector standard that carries RGB in Europe and among enthusiasts worldwide.

## Overview

Many retro consoles output RGB natively or can be modded to do so. RGB mods replace or supplement inferior video outputs (composite, RF) with a full RGB signal, typically delivered over a SCART cable to an upscaler or CRT. In this community, RGB is usually the first step before adding an HDMI mod or upscaler to the chain. retrorgb.com (run by Bob) is the canonical reference site for this topic.

## Options / Products

### RGB Mods by Console

- **NESRGB** — Widely discussed RGB mod for the NES. Replaces the PPU to output clean RGB. The v4.0 launch in 2022 was notably rocky; community members tracked revisions carefully. Produced by Tim Worthington. Requires a working PPU donor chip.
- **NESRGB alternative (Lava RGB)** — A newer alternative RGB board for NES with an available install guide. Community members noted a new version with updated install documentation.
- **2600RGB** — RGB mod for the Atari 2600. A new version was released in 2025 (via etim.net.au) with sync fixes; starlightk7 upgraded specifically for that.
- **N64 RGB (Arthrimus add-on)** — Arthrimus made an N64 RGB add-on for use with the N64 GEM. Community members noted this as an option for those running the GEM.
- **Genesis Model 1 Subcarrier Bypass** — A new method was documented on retrorgb.com (credited to community members including RGBeter) for improving Genesis Model 1 RGB output by bypassing the subcarrier.
- **RGBeter's RGBDRV** — A community-designed RGB driver board. Noted as great but with availability issues. RGBeter (RGBeter32X) is an active community member and hardware developer.
- **PC-Engine RGB (composite-color accurate)** — In development as of Jan 2026. GallandRegis working on an RGB mod that can also display composite-accurate colors.

### Cables & Connectors

- **Retro Access** — SCART and component cable maker. Widely used in the community; RayneX regularly shares their Bluesky posts. Known for high-quality cables including 32x patch cables and Genesis Model 1 cables with audio breakout.
- **Retro Gaming Cables** — Another cable vendor; community members compare them to Retro Access.
- **VGA to SCART adapter** — RayneX built an open-source VGA-to-SCART adapter PCB (BOM from Mouser, PCBs from OSH Park, SCART connectors from Amazon). Intended to route VGA-carrying scalers into SCART infrastructure.
- **SCART to VGA (open source)** — obieone/dan working on an open source SCART-to-VGA adapter for community use.

### Switches & Infrastructure

- **gscartsw** — An automatic SCART switch widely used in this community. GabeShack, subierekt, and others use one as the hub for all their SCART-connected consoles.
- **gcomp** — Component video switch, mentioned alongside gscartsw by Tubo.
- **Otaku Games SCART Switch Mod** — Allows a generic HDMI switch to sense voltage and switch profiles automatically. Serial control code by svirant (GitHub).

### Upscalers (see also: Upscalers page)

- **OSSC (Open Source Scan Converter)** — Open source, FPGA-based line multiplier. Available at Video Game Perfection (VGP). The OSSC Pro was noted as going through a parts change, with stock expected to be limited until Q2 2026.
- **OSSC Pro** — Updated version with additional features including Legacy AV and RF input support.
- **Framemeister (XRGB Mini)** — Older Japanese upscaler. Still in use; considered a legacy option by some community members.

## Console Compatibility

RGB output availability by console (native or with mod):

| Console | RGB Status |
|---|---|
| SNES / Super Famicom | Native RGB via SCART |
| Genesis / Mega Drive | Native RGB (Model 1 & 2) |
| PlayStation 1 | Native RGB via SCART |
| Saturn | Native RGB via SCART |
| Dreamcast | Native VGA/RGB |
| NES | Requires NESRGB mod |
| Neo Geo AES | Native RGB |
| Atari 2600 | Requires 2600RGB mod |
| PC-Engine | Native RGB (TurboGrafx with mod) |
| N64 | Requires RGB mod |

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
