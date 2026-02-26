---
title: NES / Famicom
description: Mods, repairs, and upgrades for the NES (North American front-loader / top-loader) and Famicom.
---

> Options listed without ranking. Compatibility can vary by hardware revision — always verify before purchasing.

## Display Mods

### RGB Output

- **NESRGB** (Tim Worthington) — Internal RGB mod kit for the NES/Famicom. One of the longest-standing community-recommended RGB solutions. Installs internally and adds an RGB header to the board. Compatible with the original Famicom and NES front-loader; noted as compatible with OpenTendo replacement boards per community discussion. [Project site](https://etim.net.au/nesrgb/) · [Buy · Laser Bear Industries](https://www.laserbear.net)

- **Hi-Def NES** (Analogue) — Internal HDMI output mod for the NES front-loader. Discontinued by Analogue; units circulate secondhand. Added HDMI output with scanline and resolution options. Worth sourcing secondhand if HDMI is the goal and a donor console is available.

- **OpenTendo** — Open-source NES mainboard replacement project. A community-built reproduction of the NES front-loader main board with improvements. Designed to accept mods like NESRGB. [GitHub](https://github.com/Redherring32/OpenTendo)

### Composite / AV Restoration

- **POW Block AV/Power Board** (zaxour) — Replacement AV and power board for the NES front-loader. Addresses aging components on the original board. [Buy · zaxour Ko-fi](https://ko-fi.com/s/a42a9b282f)

- **NES Power Module Redesign** (ShawMerlin) — GitHub project redesigning the NES power module, including an RGB–Genesis 9-pin variant for RGB output. Drop-in improvement over the aging original power circuitry. [GitHub](https://github.com/ShawMerlin/NES-Power-Module-Redesign)

---

## Audio Mods

- **EPSM** (Perkka / Muramasa) — FM audio expansion board for NES and Famicom. Adds YM2149 and YM2203 sound chips via the NES expansion port, enabling FM synthesis audio playback on original hardware. Open-source project. [GitHub](https://github.com/perkka/epsm)

---

## Storage / Flash Carts

- **EverDrive N8 Pro** (Krikzz) — SD-based flash cart for NES and Famicom. Supports most mappers including expansion audio (VRC6, FDS, Namco 163, etc.). Community's go-to recommendation for a no-compromise NES flash cart. [Buy · Krikzz](https://krikzz.com/our-products/cartridges/en8.html)

- **FDS2NES** — PCB adapter that converts a Famicom Disk System RAM adapter (HVC-023) into a standard cart-slot solution, eliminating the need for the physical RAM adapter unit. Discussed via eBay listings in the community.

- **PowerPak** (RetroZone) — Earlier NES flash cart. Less discussed in recent community threads; EverDrive N8 Pro is the more commonly recommended option now.

---

## Common Repairs

### Known Failure Points

- **72-pin connector (front-loader)** — The ZIF connector degrades over time, causing blinking screens or grey screens on boot. Options: boiling the original connector, carefully bending the pins back, or replacing with a new third-party connector. Replacement connectors are widely available from Console5 and similar suppliers.

- **PPU / CPU clock crystal** — Can drift on aging boards, causing audio or sync problems. Crystal replacement is a low-cost repair.

- **Power LED** — Fails on some units; a standard LED swap.

- **Cartridge connector oxidation (Famicom)** — Common on Famicom edge connectors. Cleaning with IPA restores contact.

### Capacitor Replacement

- The Famicom board uses electrolytic capacitors that can leak or fail. Recapping is particularly relevant for audio quality, especially on units using the expansion audio connector for mappers like FDS, VRC6, and Namco 163.

---

## Shell / Cosmetic Mods

- **Famicom Cartridge Shells** (Muramasa Entertainment) — Translucent replacement cartridge shells for Famicom carts. Available directly from Muramasa's store. [Buy · Muramasa Entertainment](https://www.muramasaentertainment.com)

- **MouseBiteLabs NES Cartridge PCBs** — Open-source cartridge PCBs for NES discrete logic mappers. Useful for repro builds and cart repairs. [GitHub](https://github.com/MouseBiteLabs/NES-Cartridges/tree/main/Discrete%20Logic%20Mappers)

- **FamiCoun** (jeffqchen) — Open-source Famicom front-expansion to NES/SNES adapter. Allows Famicom expansion audio accessories to connect through to NES hardware. [GitHub](https://github.com/jeffqchen/FamiCoun-Famicom-Front-Expansion-NES-SNES-Adapter)

---

## Display — RGB Mods

<!-- DB:START section="Display — RGB Mods" console=nes -->
- **[NESRGB](https://etim.net.au/nesrgb/)** by [Tim Worthington](https://etim.net.au)
  Internal RGB mod kit for the NES and Famicom. Installs internally and adds an RGB header. Requires a donor PPU chip. Community standard for NES RGB for many years. The long-standing community-standard NES RGB solution. Widely documented and supported. Stable — no longer in active development. ~$40–60.
<!-- DB:END -->

## Audio Mods

<!-- DB:START section="Audio Mods" console=nes -->
- **[EPSM](https://github.com/perkka/epsm)** by [Muramasa](https://x.com/muramasa_ninja) / [Perkka](https://github.com/perkka)
  FM audio expansion board for NES/Famicom. Adds YM2149 and YM2203 sound chips to the NES expansion port, enabling FM synthesis audio. Community members including Muramasa are contributing connector and layout improvements. Brings FM synthesis audio to NES/Famicom hardware — the kind of expansion audio that Famicom Disk System and various Japanese mappers explored. Active open source development with community contributions.
<!-- DB:END -->

## Storage — Flash Carts

<!-- DB:START section="Storage — Flash Carts" console=nes -->
- **[EverDrive N8 Pro](https://krikzz.com/our-products/cartridges/)** by [Krikzz](https://x.com/krikzz)
  SD-based flash cart for NES and Famicom. Supports most mappers including expansion audio (VRC6, FDS, Namco 163, MMC5). The community standard NES flash cart. No-compromise NES flash cart — expansion audio support is the key differentiator over cheaper alternatives. $75.
<!-- DB:END -->

## PCB & Reproduction

<!-- DB:START section="PCB & Reproduction" console=nes -->
- **[MouseBiteLabs NES Cartridge PCBs](https://github.com/MouseBiteLabs/NES-Cartridges)** by [MouseBiteLabs](https://bsky.app/profile/mousebitelabs.bsky.social)
  Open source NES cartridge PCBs for discrete logic mappers. Free to fabricate from Gerbers. Essential for community repro builders and cart repair. Fully open source, well documented.
- **[OpenTendo](https://github.com/Redherring32/OpenTendo)** by [Redherring32](https://x.com/redherring32)
  Fully open source reproduction of the NES front-loader main board (NES-CPU-07). Designed to accept standard NES mods including NESRGB. Compatible with original NES shells and cartridge connectors. Enables NES hardware preservation without sourcing failing original boards. One of the few fully open source console main board reproductions. NESRGB compatibility confirmed by the community.
<!-- DB:END -->

## Accessories

<!-- DB:START section="Accessories" console=nes -->
- **[FamiCoun](https://github.com/jeffqchen/FamiCoun-Famicom-Front-Expansion-NES-SNES-Adapter)** by [jeffqchen](https://x.com/jeffqchen)
  Open source adapter connecting the Famicom's front expansion port to NES and SNES hardware. Allows Famicom expansion audio accessories to work through to NES hardware. Enables expansion audio on NES hardware without modifying the console itself.
<!-- DB:END -->

## Repairs & Power

<!-- DB:START section="Repairs & Power" console=nes -->
- **[POW Block AV/Power Board](https://ko-fi.com/s/a42a9b282f)** by [zaxour](https://x.com/zaxour)
  Replacement AV and power board for the NES front-loader. Addresses aging components on the original board. Solid drop-in upgrade for NES front-loaders with failing AV or power circuits. Open source.
<!-- DB:END -->
