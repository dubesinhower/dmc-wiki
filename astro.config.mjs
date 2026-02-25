import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  integrations: [
    starlight({
      title: 'Bleeding Retro Wiki',
      description: 'Community-sourced knowledge on retro console mods, repairs, and upgrades.',
      social: [
        { icon: 'discord', label: 'Discord', href: 'https://discord.gg/bleedingretro' },
      ],
      editLink: {
        baseUrl: 'https://github.com/bleedingretro/wiki/edit/main/',
      },
      sidebar: [
        {
          label: 'Getting Started',
          items: [
            { label: 'About This Wiki', link: '/' },
            { label: 'How to Use', link: '/guides/how-to-use' },
          ],
        },
        {
          label: 'Nintendo',
          items: [
            { label: 'NES / Famicom', link: '/consoles/nes' },
            { label: 'SNES / Super Famicom', link: '/consoles/snes' },
            { label: 'Nintendo 64', link: '/consoles/n64' },
            { label: 'GameCube', link: '/consoles/gamecube' },
            { label: 'Wii', link: '/consoles/wii' },
            { label: 'Game Boy', link: '/consoles/gameboy' },
            { label: 'Game Boy Advance', link: '/consoles/gba' },
            { label: '3DS', link: '/consoles/3ds' },
          ],
        },
        {
          label: 'Sega',
          items: [
            { label: 'Genesis / Mega Drive', link: '/consoles/genesis' },
            { label: 'Saturn', link: '/consoles/saturn' },
            { label: 'Dreamcast', link: '/consoles/dreamcast' },
            { label: 'Game Gear', link: '/consoles/game-gear' },
            { label: 'Sega CD / Mega CD', link: '/consoles/sega-cd' },
          ],
        },
        {
          label: 'Sony',
          items: [
            { label: 'PlayStation', link: '/consoles/ps1' },
            { label: 'PlayStation 2', link: '/consoles/ps2' },
            { label: 'PSP', link: '/consoles/psp' },
          ],
        },
        {
          label: 'SNK',
          items: [
            { label: 'Neo Geo MVS / AES', link: '/consoles/neo-geo' },
          ],
        },
        {
          label: 'Other',
          items: [
            { label: 'TurboGrafx-16 / PC Engine', link: '/consoles/tg16' },
            { label: 'Atari', link: '/consoles/atari' },
            { label: 'Xbox', link: '/consoles/xbox' },
            { label: 'Xbox 360', link: '/consoles/xbox-360' },
          ],
        },
        {
          label: 'Topics',
          items: [
            { label: 'HDMI Mods', link: '/topics/hdmi' },
            { label: 'RGB & SCART', link: '/topics/rgb' },
            { label: 'Flash Carts', link: '/topics/flash-carts' },
            { label: 'Optical Drive Emulators', link: '/topics/ode' },
            { label: 'Upscalers', link: '/topics/upscalers' },
            { label: 'FPGA', link: '/topics/fpga' },
            { label: '3D Printing', link: '/topics/3d-printing' },
          ],
        },
      ],
    }),
  ],
});
