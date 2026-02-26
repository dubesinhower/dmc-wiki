---
title: PC-Engine / TurboGrafx-16
description: Mods, repairs, and upgrades for the PC-Engine, TurboGrafx-16, and related variants.
sidebar:
  order: 16
---

> Options listed without ranking. Compatibility can vary by hardware revision — always verify before purchasing.

The PC-Engine platform has more naming variants than almost any console: **PC Engine** (Japan, 1987), **TurboGrafx-16** (US, 1989), **CoreGrafx** (Japan, revised RF-less model), **CoreGrafx II**, and the all-in-one **PC Engine Duo / Duo-R / Duo-RX**, which include the CD-ROM² add-on built in. Hudson and NEC released the **SuperGrafx** — a beefed-up PC Engine with a second VDC — in Japan only, compatible with most PC Engine HuCards plus a handful of SuperGrafx-exclusive titles.

The key revision split for modding: the original **PC Engine** outputs composite and RF natively; the **TurboGrafx-16** outputs composite and RF by default. RGB output is possible on most variants via internal mods. The **PC Engine Duo/Duo-R** are popular modding targets because they combine the base hardware and CD add-on in one shell and are widely available.

The CD add-on ecosystem (TurboGrafx-CD / PC Engine CD-ROM²) is significant — many of the platform's best games are CD titles. Duo variants have this built in. The **Turbo EverDrive v2** handles HuCard-based games; CD images require a different approach (ODEs for the CD unit are uncommon — most players use a working drive or Duo).

## Storage / Flash Carts

The Turbo EverDrive v2 covers the full HuCard library across all hardware variants — PC Engine, CoreGrafx, TurboGrafx-16, and SuperGrafx. It does not load CD-ROM² titles (those require the CD-ROM² add-on or Duo hardware with a working drive).

<!-- DB:START section="Storage — Flash Carts" console=pc-engine -->
- **[Turbo EverDrive v2](https://krikzz.com/our-products/cartridges/)** by [Krikzz](https://x.com/krikzz)
  SD-based flash cart for PC-Engine and TurboGrafx-16. The standard flash cart for PC-Engine/TG-16. $60.
<!-- DB:END -->

## Display

### RGB Output

The PC Engine family is a common RGB mod target. Key context:

- **Original PC Engine (white):** RGB mod available targeting the HuC6270 VDC output. Several board revisions exist; RGB bypass kits and RGB amp boards are available from community sources. RetroRGB covers the PC Engine RGB mod in detail.
- **CoreGrafx / CoreGrafx II:** Already lacks RF output; RGB mod follows the same approach as the PC Engine. CoreGrafx is often preferred as a mod platform because RF circuitry removal simplifies the board.
- **TurboGrafx-16:** US variant. RGB mod approach is similar; see board-specific guides. Outputs composite and RF stock.
- **PC Engine Duo / Duo-R:** Popular mod targets. RGB amp boards designed specifically for the Duo are available from community builders. The Duo-R is the most common and affordable entry point.
- **SuperGrafx:** RGB mod is possible; the SuperGrafx has two VDCs and requires attention to which output is modded.

### HDMI

Dedicated internal HDMI options for the PC Engine/TG-16 are limited compared to platforms like PS1 or N64. The primary HDMI path is RGB output → SCART or component → external upscaler (RetroTINK 4K, PixelFX Morph 4K, etc.). Check the HDMI Mods and Upscalers topic pages for current upscaler options that accept analog input.

## Common Repairs

### Known Failure Points

- **HuCard connector** — The card edge connector oxidizes over time. Cleaning with IPA on a cotton swab, or a proper connector cleaning kit, typically restores contact. The TG-16 connector pins can also bend.
- **CD-ROM² drive laser (Duo models)** — The CD mechanism in Duo units is the most common failure point. Laser replacement is the standard repair; belts also wear out and are inexpensive to replace.
- **Capacitors (Duo)** — Duo and Duo-R boards have electrolytic capacitors that cause audio and video issues when they fail. Recapping is essentially mandatory on any Duo that hasn't been serviced. Multiple community guides exist for the Duo-R specifically.
- **AC adapter** — Original PC Engine and TG-16 AC adapters output DC at specific voltages. The PC Engine (Japan) uses a center-positive 9V adapter; do not substitute at random. Universal adapters with correct polarity and voltage are safe.
- **RF modulator** — On original PC Engine and TG-16 units, the RF section occasionally develops issues. Since most users move to composite or RGB output, the RF modulator is often bypassed or simply left disconnected.

### Capacitor Replacement

Recapping is strongly recommended for any PC Engine Duo or Duo-R. The original PC Engine and TG-16 are generally more robust but benefit from capacitor inspection on older units. Community-sourced BOM lists by model variant are available on the PC Engine Software Bible and related wikis.
