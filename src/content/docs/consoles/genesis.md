---
title: Sega Genesis / Mega Drive
description: Mods, repairs, and upgrades for the Sega Genesis (all models) and Mega Drive.
---

> Options listed without ranking. Compatibility can vary by hardware revision — always verify before purchasing.

## Display Mods

### RGB / HDMI Output

- **Triple Bypass Mod** — Widely discussed RGB upgrade that bypasses the onboard video encoder. Replaces composite/RF output path with clean RGB directly from the VDP. Available pre-assembled from Stone Age Gamer and as a DIY kit. See [Stone Age Gamer listing](https://stoneagegamer.com/sega-genesis-mega-drive-triple-bypass-modification-version-2.html).
- **Genesis Model 1 Subcarrier Bypass** — New method for the Model 1 board, covered by RetroRGB. Discussed by GabeShack in the community. See [RetroRGB article](https://retrorgb.com/genesis-model-1-subcarrier-bypass-new-method-tested.html).
- **RGBeter32X open-source composite/S-Video board** — Community member RGBeter ([@RGBeter32X](https://twitter.com/RGBeter32X)) noted in Discord: "New composite and S-Video (better than any stock Genesis because we spent too long tuning the luma filtering), technically a subcarrier bypass." Described as open-source.
- **HDMI full solution** — Community members noted that achieving a full internal HDMI solution for Genesis requires multiple boards and has become expensive.

## Storage / Flash Carts

- **MegaSD** (TerraOnion) — Alternative flash cart supporting both Genesis and Mega CD titles on a single cart. [Product site](https://terraonion.com/en/producto/megasd/)

## Optical Drive Emulators (ODE)

- The Sega CD (add-on) has ODE options, but base Genesis/Mega Drive itself is cartridge-based and does not require an ODE.

## Common Repairs

### Known Failure Points

- **TMSS chip issues** — Early boards without TMSS can present compatibility problems. A TMSS disable mod exists as an open-source project at [consolesunleashed/sega-mega-drive-tmss-disable](https://github.com/consolesunleashed/sega-mega-drive-tmss-disable).
- **32X AV cable connector** — Specific AV link cables are required when combining the 32X with a Model 2 or Model 3; the wrong cable can cause signal issues. Console5 carries the 32X AV link cable.
- **Audio capacitors** — Model 1 boards in particular have electrolytics that affect audio output. Recapping improves audio fidelity.
- **Cartridge slot contact oxidation** — Cleaning with IPA restores reliability on older units.

### Capacitor Replacement

- Recapping is relevant for all Genesis revisions, but audio quality benefits most noticeably on Model 1 units. VA0 and VA1 boards are discussed separately due to different BOM.

## Shell / Cosmetic Mods

- **Retro Game Restore shells** — Replacement shells for the Mega Drive 2 available from Retro Game Restore. A project kickstarter was shared by Dubesinhower in the community. See [retrogamerestore.com](https://retrogamerestore.com/store/md2shl/).
- **pxlmod v1.3 Controller Port Adapter Kit** — Adapter kit for modifying Genesis controller ports. Available from Console5.
- **3D-printed components** — Community members discussed 3D printing replacements for 32X and Genesis shell components.

## Display — RGB Mods

<!-- DB:START section="Display — RGB Mods" console=genesis -->
- **[4BP Quadruple Bypass](https://ko-fi.com/s/51d6725bbe)** by [zaxour](https://x.com/zaxour)
  Extended RGB bypass mod for Sega Genesis/Mega Drive supporting additional signal paths beyond the standard Triple Bypass. DIY kit. The most comprehensive Genesis RGB bypass available, from a well-known open source developer.
<!-- DB:END -->

## Storage — Flash Carts

<!-- DB:START section="Storage — Flash Carts" console=genesis -->
- **[Mega EverDrive Pro](https://krikzz.com/our-products/cartridges/)** by [Krikzz](https://x.com/krikzz)
  Genesis flash cart with Sega CD game emulation built in. Note: not compatible with ODE-based Sega CD implementations (MODE, GDEMU). Krikzz confirmed fixing this would require a ground-up rewrite. The only flash cart that combines Genesis + Sega CD in one cart — but the ODE incompatibility is a known hard limitation. $100.
- **[Mega EverDrive X3 / X5 / X7](https://krikzz.com/our-products/cartridges/)** by [Krikzz](https://x.com/krikzz)
  SD-based flash carts for Sega Genesis/Mega Drive. X3/X5 cover the full Genesis and 32X library (~$40–60). X7 adds more storage and speed. None support Sega CD. X5 is the budget entry point covering the entire Genesis + 32X library. Best value in the EverDrive lineup. $40–$80.
<!-- DB:END -->
