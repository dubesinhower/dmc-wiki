---
title: Upscalers
description: Video upscalers and line doublers for displaying retro console output on modern displays — covering RetroTINK, PixelFX, OSSC, and more.
---

> Upscalers bridge the gap between retro console video output (240p, 480i, RGB, component) and modern displays (HDMI, 4K TVs, monitors). They're the centerpiece of most community members' setups, and RetroTINK and PixelFX are the two most widely discussed brands in the DMC.

## Overview

Upscalers take analog (or sometimes digital) video signals from retro consoles and convert them to a resolution and format compatible with modern displays — typically 1080p or 4K over HDMI. Quality upscalers apply minimal processing to preserve the feel of the original hardware. High-end devices offer scanlines, per-game profiles, HDR output, and serial control integration. RetroTINK (Mike Chi / @retrotink2) and PixelFX (@pixelfxco) dominate community discussion by a wide margin.

## Options / Products

### RetroTINK (by Mike Chi / @retrotink2)

- **RetroTINK 5X Pro** — Mid-range upscaler supporting up to 1080p. Accepts component, S-Video, composite, and SCART/RGB. The primary scaler for most community setups. Integrates with Swiss on GameCube for native GB Player resolution mode. [Buy · RetroTINK](https://www.retrotink.com/product-page/5x-pro)

- **RetroTINK 4K** — High-end flagship scaler (~$750). Supports 4K output, HDR, and rotation. The professional-tier option per community consensus. [Buy · RetroTINK](https://www.retrotink.com/product-page/retrotink-4k)

- **RetroTINK 4K CE** — A more affordable 4K variant, but missing rotation — a key feature for some members. [Buy · RetroTINK](https://www.retrotink.com)

- **RetroTINK Dongles** — Console-specific HDMI adapter cables. Plug-and-play alternative to internal HDMI mods. [RetroTINK site](https://www.retrotink.com)

*Note: In April 2025, RetroTINK paused US shipments temporarily due to tariff concerns.*

### PixelFX (by @pixelfxco)

- **PixelFX Morph 4K** — Upscaler and line processor widely followed as an alternative to the RetroTINK 4K. Regular firmware updates; community members track feature parity with the Tink 4K closely. Bonzo: *"PixelFX is slow but steady for making products at a fair price. The integration between their products is really cool."* [Buy · PixelFX](https://www.pixelfx.co/morph-4k)

- **Morph Analog Bridge** — Add-on for the Morph 4K, expanding analog input options. [PixelFX site](https://www.pixelfx.co)

- **PixelFX Infinity Switch** — Anticipated combined HDMI/analog switch from PixelFX. Community members followed this closely and hoped it would ship in 2025–2026. Not yet available as of early 2026. [PixelFX site](https://www.pixelfx.co)

- **PixelFX Retro GEM** — While primarily an internal HDMI mod, the GEM integrates closely with the Morph and other PixelFX products. See [HDMI Mods](/topics/hdmi).

### OSSC (Open Source Scan Converter)

- **OSSC** — Open-source FPGA-based line multiplier. Budget-accessible entry point; does not do full upscaling but multiplies the line count (2x–5x) for compatibility with displays that accept non-standard resolutions. [Buy · Video Game Perfection](https://www.videogameperfection.com/products/ossc/)

- **OSSC Pro** — Updated version with Legacy AV and RF input support. Going through a board revision as of February 2026; stock at VGP was expected to be limited until Q2 2026. [Buy · Video Game Perfection](https://www.videogameperfection.com/products/ossc-pro/)

### Legacy / Alternative Scalers

- **Framemeister (XRGB Mini)** — A Japanese upscaler (by Micomsoft). Older but still in use; community members reference it as a legacy option. GabeShack mentioned it alongside newer scalers.
- **Morph 4K (earlier models)** — Ongoing firmware development makes older Morph units increasingly capable.
- **GBSC** — Mentioned by subierekt as part of a scaler chain.

## Console Compatibility

Upscalers are generally signal-agnostic — they accept whatever the console outputs. Key pairings discussed in the community:

- **GameCube + Tink5x** — RayneX and others use Swiss + Tink5x for native GB Player resolution
- **Dreamcast + Tink5x** — Vuscav uses a Retro Access SCART cable directly to Tink5x for 480p output
- **All RGB/SCART consoles → gscartsw → Tink5x/Tink4K/Morph** — The most common analog chain setup
- **HDMI-modded consoles → Morph** — The GEM integrates with Morph profiles for per-game settings
- **MiSTer → Morph or Tink** — FPGA output to scaler for display on modern TVs

## Community Notes

- The community has a clear two-brand dynamic: **RetroTINK** (established, trusted, Mike Chi direct) vs. **PixelFX Morph** (growing rapidly, community integration via GEM ecosystem).
- RayneX: *"It's an $800 professional device [Tink4K] that does what it does extremely well but man, the names… mudding up the RetroTink name itself as time goes on."*
- Tubo: *"My Morph and Tink fw are both like a year behind."* — Firmware updates for both scalers are frequent; many members fall behind.
- GabeShack: *"No excuses on the Morph. It's on WiFi for Christ's sake."*
- The Morph vs. Tink4K feature comparison is an ongoing community conversation. Vuscav in March 2025: *"If someone that owns both had to give a feature parity percentage, how's the morph compare to the Tink 4K?"*
- starlightk7 noted that resolution switching being rough on the Morph at the time pushed Mike Chi to improve the Tink in that area — "competition is good on display."
- donutswdad built a companion tool for the RT4K using HD-15 serial control (GitHub: `svirant/RT4k_HD15_serial_control`), and the Otaku SCART switch mod allows SCART profile switching alongside the Tink.
- obieone: *"Lawd, better get your Tink4K before '26."* — Anticipating price increases or tariff impacts.
- A PixelFX Morph 4K vertical stand is available on Printables.

## Resources

- <https://www.retrotink.com> — RetroTINK official site
- <https://retrotink-llc.github.io/firmware/4k-experimental.html> — RetroTINK experimental firmware
- <https://www.pixelfx.co> — PixelFX official site
- <https://www.pixelfx.co/post/pixel-fx-newsletter> — PixelFX newsletter
- <https://junkerhq.net/xrgb/index.php?title=Morph_4K> — Morph 4K wiki (junkerhq.net)
- <https://github.com/svirant/RT4k_HD15_serial_control> — RT4K serial control (HD-15/Otaku switch)
- <https://www.printables.com/model/892683-pixelfx-morph-4k-vertical-stand> — Morph 4K vertical stand (Printables)
- <https://www.theverge.com/news/651007/retrotink-us-shipments-suspended-trump-tariffs> — RetroTINK tariff pause (Apr 2025)

---
*This page was generated from community discussion in the DMC Discord. Last updated: 2026-02-25.*
