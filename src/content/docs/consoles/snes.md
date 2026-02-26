---
title: SNES / Super Famicom
description: Mods, repairs, and upgrades for the SNES (all revisions) and Super Famicom.
---

> Options listed without ranking. Compatibility can vary by hardware revision — always verify before purchasing.

## Display Mods

### RGB / HDMI Output

- **SNES RGB Bypass** (borti4938) — Open-source RGB bypass mod for SNES. Addresses video noise present in stock output. See [GitHub](https://github.com/borti4938/SNES_RGB_Bypass).
- **SNES 2-Chip RGB Filter Mod** — Documented on Aussie Arcade for the SHVC-CPU-001 2-chip boards. Addresses the video dot-crawl/noise inherent to 2-chip SNES revisions. See [Aussie Arcade thread](https://www.aussiearcade.com/topic/90003-snes-sfc-shvc-cpu-001-2-chip-rgb-filter-mod-video-fix/).
- **SNES Edge Enhancer DIY Kit** (Voultar) — DIY kit addressing sharpness and edge enhancement in SNES video output. Available from [voultar.com](https://voultar.com).
- **SuperPico Digital** (fliperama86) — Experimental SNES digital video output project. Community member zwenergy noted it is "more experimental yet" compared to other HDMI solutions. See [GitHub](https://github.com/fliperama86/superpico-digital).
- **SNES CPU Replacement via FPGA** — A Hackaday article about FPGA-based SNES CPU replacement was shared in the community. See [Hackaday](https://hackaday.com/2025/03/31/a-snes-cpu-replacement-via-fpga/).

### S-Video

- **Insurrection Industries Double-Shielded S-Video Cable** — Covers SNES, N64, and GameCube. Shared by RayneX in the community. Available from Stone Age Gamer.

## Storage / Flash Carts

- **FXPak Pro (sd2snes)** (Krikzz / ikari_01) — The long-running open-source FPGA-based flash cart for SNES and Super Famicom. Supports enhancement chips that most other carts cannot emulate — SA-1, Super FX, DSP, etc. Active firmware development continues. [Buy · Krikzz](https://krikzz.com/our-products/cartridges/fxpak-pro.html) · [GitHub](https://github.com/sd2snes/sd2snes)
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

## Controllers

- **8Bitdo Sn30 2.4GHz Wireless Gamepad** — Wireless controller for original SNES/SFC. Discussed by RayneX in community. Available from Amazon.
- **IBlueControlMod** (Handheld Legend) — Internal Bluetooth wireless controller adapter for SNES. See [handheldlegend.com](https://handheldlegend.com/products/snes-internal-bluetooth-wireless-controller-adapter).
- **Brook Wingman SNES Converter** — Allows modern controllers to be used on SNES hardware. Available from Amazon.

## Display — RGB Mods

<!-- DB:START section="Display — RGB Mods" console=snes -->
- **SNES Edge Enhancer** by [Voultar](https://x.com/Voultar)
  A DIY SNES video enhancement kit that sharpens the SNES video output by boosting edge definition. Sold as a kit; install is streamed by Voultar. Note: community investigation ongoing (as of Feb 2026) into whether it can stress the PPU2 analog DAC under certain conditions. A popular and widely discussed SNES video mod from one of the most prominent SNES modders in the community. The ongoing PPU2 concern is active community discussion.
- **[SNES RGB Bypass](https://github.com/borti4938/SNES_RGB_Bypass)** by [borti4938](https://github.com/borti4938)
  Open source internal RGB bypass mod for SNES/Super Famicom. Addresses the video noise present in stock output by bypassing the onboard video encoder. The go-to open source SNES RGB mod. Widely installed, well documented, and free to build.
<!-- DB:END -->

## Storage — Flash Carts

<!-- DB:START section="Storage — Flash Carts" console=snes -->
- **[FXPak Pro (sd2snes)](https://github.com/sd2snes/sd2snes)** by [Krikzz](https://x.com/krikzz) / [ikari_01](https://github.com/ikari-pl)
  FPGA-based flash cart for SNES and Super Famicom. Supports enhancement chips that other carts cannot emulate — SA-1, Super FX, DSP series, MSU-1, and more. Open source firmware, active development. Manufactured by Krikzz; designed by ikari_01. The only SNES flash cart that handles enhancement chips. Essential for playing SA-1 games (Super Mario RPG, Kirby Super Star) and Super FX games (Star Fox, Doom) from SD card. ~$185. [Buy](https://krikzz.com/our-products/cartridges/fxpak-pro.html)
<!-- DB:END -->

## Accessories

<!-- DB:START section="Accessories" console=snes -->
- **[FamiCoun](https://github.com/jeffqchen/FamiCoun-Famicom-Front-Expansion-NES-SNES-Adapter)** by [jeffqchen](https://x.com/jeffqchen)
  Open source adapter connecting the Famicom's front expansion port to NES and SNES hardware. Allows Famicom expansion audio accessories to work through to NES hardware. Enables expansion audio on NES hardware without modifying the console itself.
<!-- DB:END -->

## PCB & Reproduction

<!-- DB:START section="PCB & Reproduction" console=snes -->
- **[OpenSFC](https://1uprestorations.com)** by [starlightk7](https://x.com/starlightk7)
  An open source replacement mainboard for the Super Famicom/SNES console. Aims to be a fully open hardware alternative to original SFC/SNES hardware. One of the very few attempts at a fully open source SNES replacement mainboard (similar to OpenTendo for NES). Community interest is high given SNES hardware reliability concerns (aging PPU chips). Controllers launched first as early access via Ko-Fi in early 2026.
<!-- DB:END -->
