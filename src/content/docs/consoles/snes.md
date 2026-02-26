---
title: SNES / Super Famicom
description: Mods, repairs, and upgrades for the SNES (all revisions) and Super Famicom.
---

> Options listed without ranking. Compatibility can vary by hardware revision — always verify before purchasing.

## Display Mods

### RGB / HDMI Output

- **SNES RGB Bypass** (borti4938) — Open-source RGB bypass mod for SNES. Addresses video noise present in stock output. See [GitHub](https://github.com/borti4938/SNES_RGB_Bypass). → [Full details](/projects/snes-rgb-bypass)
- **SNES 2-Chip RGB Filter Mod** — Documented on Aussie Arcade for the SHVC-CPU-001 2-chip boards. Addresses the video dot-crawl/noise inherent to 2-chip SNES revisions. See [Aussie Arcade thread](https://www.aussiearcade.com/topic/90003-snes-sfc-shvc-cpu-001-2-chip-rgb-filter-mod-video-fix/).
- **SNES Edge Enhancer DIY Kit** (Voultar) — DIY kit addressing sharpness and edge enhancement in SNES video output. Available from [voultar.com](https://voultar.com).
- **SuperPico Digital** (fliperama86) — Experimental SNES digital video output project. Community member zwenergy noted it is "more experimental yet" compared to other HDMI solutions. See [GitHub](https://github.com/fliperama86/superpico-digital).
- **SNES CPU Replacement via FPGA** — A Hackaday article about FPGA-based SNES CPU replacement was shared in the community. See [Hackaday](https://hackaday.com/2025/03/31/a-snes-cpu-replacement-via-fpga/).

### S-Video

- **Insurrection Industries Double-Shielded S-Video Cable** — Covers SNES, N64, and GameCube. Shared by RayneX in the community. Available from Stone Age Gamer.

## Storage / Flash Carts

- **FXPak Pro (sd2snes)** (Krikzz / ikari_01) — The long-running open-source FPGA-based flash cart for SNES and Super Famicom. Supports enhancement chips that most other carts cannot emulate — SA-1, Super FX, DSP, etc. Active firmware development continues. [Buy · Krikzz](https://krikzz.com/our-products/cartridges/fxpak-pro.html) · [GitHub](https://github.com/sd2snes/sd2snes) → [Full details](/projects/fxpak-pro)
- **Epilogue GB Operator (SNES edition)** — Epilogue marketed a limited-edition SNES cartridge reader. JesusBurnsNeon noted the marketing approach in community discussion: "preorders starting Tuesday for $60."
- **SA-1 Root** (VitorVilela7) — Project for accelerating SNES games using the SA-1 co-processor. Relevant for homebrew and repro builds. See [GitHub](https://github.com/VitorVilela7/SA1-Root).

## Common Repairs

### Known Failure Points

- **SNES revision differences** — 1-chip vs 2-chip board revisions have different video output characteristics. 1-chip boards produce sharper RGB with less noise. RetroRGB maintains a version comparison guide: [retrorgb.com/snesversioncompare.html](https://www.retrorgb.com/snesversioncompare.html).
- **Capacitors (SNES Jr.)** — The smaller SNES Jr. boards have electrolytic caps that can leak and damage board traces.
- **Cartridge connector** — Pin contact issues are common; cleaning with IPA and carefully bending pins restores contact.
- **Power LED / power switch** — Aging on older units; straightforward component swaps.

### Capacitor Replacement

- Primarily relevant for SNES Jr. (SNS-101) boards. Full-size SNES boards are generally more robust but not exempt on very old units.

## Shell / Cosmetic Mods

- **SNES-CON** (Rondo Products) — Reverse polarity center-pin adapter for SNES. Available from [rondoproducts.com](https://rondoproducts.com/products/reverse-polarity-center-pin-adapter).
- **SNES Jr. CPU Repro PCB** (qwertymodo) — An open-source SNES Jr. CPU board reproduction. Shared by starlightk7: "Qwertymodo has released his SNES Jr repro." See [GitHub](https://github.com/qwertymodo/kicad-snn-cpu-01).
---

## FPGA Hardware

- **OpenSFC** (starlightk7) — Open-source FPGA-based Super Famicom/SNES console. Aims to be a fully open hardware alternative to original SFC/SNES hardware, including support for standard mods like NESRGB-style installs. Pre-release as of early 2026; first units were approaching completion. [Buy when available · 1Up Restorations](https://1uprestorations.com) · [RetroUpgrades](https://retroupgrades.com) → [Full details](/projects/opensfc)

## Controllers

- **8Bitdo Sn30 2.4GHz Wireless Gamepad** — Wireless controller for original SNES/SFC. Discussed by RayneX in community. Available from Amazon.
- **IBlueControlMod** (Handheld Legend) — Internal Bluetooth wireless controller adapter for SNES. See [handheldlegend.com](https://handheldlegend.com/products/snes-internal-bluetooth-wireless-controller-adapter).
- **Brook Wingman SNES Converter** — Allows modern controllers to be used on SNES hardware. Available from Amazon.

## Community Notes

- The SNES revision question (1-chip vs 2-chip) is actively discussed; community member Gaw stated "best bet for snes is a new FPGA console" in context of hardware reliability.
- Community member starlightk7 is actively working on SNES-adjacent hardware projects including OpenSFC and the SNES Jr. CPU repro.
- JesusBurnsNeon expressed hope for a "SNES GEM" (RetroGEM/PixelFX HDMI for SNES), linking it to a theoretical future Saturn GEM.
- Community member zwenergy noted the difficulty of SNES digital video: "Like 15-bit color + you also need to listen to the data bus in order to sniff for brightness setting commands."
- NESMaker (now renamed) was noted as announcing SNES development tooling ([timeextension.com](https://www.timeextension.com/news/2024/08/homebrew-tool-nesmaker-changes-name-announces-snes-develo)).
- A FamiCoun Famicom-to-NES/SNES front expansion adapter (jeffqchen) was shared by Dubesinhower for adapter-related discussion.
- The Mesen2 multi-system emulator (SourMesen) was shared as a reference emulator for SNES accuracy.

## Resources

- [SNES RGB Bypass (GitHub)](https://github.com/borti4938/SNES_RGB_Bypass)
- [SNES Version Compare (RetroRGB)](https://www.retrorgb.com/snesversioncompare.html)
- [Voultar – SNES Edge Enhancer](https://voultar.com)
- [SA1-Root (GitHub)](https://github.com/VitorVilela7/SA1-Root)
- [SNES Jr. CPU Repro (GitHub)](https://github.com/qwertymodo/kicad-snn-cpu-01)
- [SuperPico Digital (GitHub)](https://github.com/fliperama86/superpico-digital)
- [Mesen2 Emulator (GitHub)](https://github.com/SourMesen/Mesen2)
- [IBlueControlMod (Handheld Legend)](https://handheldlegend.com/products/snes-internal-bluetooth-wireless-controller-adapter)

---

*This page was generated from community discussion in the DMC Discord. Last updated: 2026-02-25.*
