import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  site: 'https://dubesinhower.github.io',
  base: '/dmc-wiki',
  integrations: [
    starlight({
      title: 'DMC Wiki',
      description: 'The Dubesinhower Modding Community Wiki — community-sourced knowledge on retro console mods, repairs, and upgrades.',
      social: [
        { icon: 'discord', label: 'Discord', href: 'https://t.co/csIvwMwymP' },
      ],
      editLink: {
        baseUrl: 'https://github.com/dubesinhower/dmc-wiki/edit/main/',
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
          label: 'Consoles',
          items: [
            { label: 'All Consoles', link: '/consoles/' },
          ],
        },
        {
          label: 'Nintendo',
          items: [
            { label: 'NES / Famicom', link: '/consoles/nes' },
            { label: 'SNES / Super Famicom', link: '/consoles/snes' },
            { label: 'Nintendo 64', link: '/consoles/n64' },
            { label: 'GameCube', link: '/consoles/gamecube' },
            { label: 'Game Boy Advance', link: '/consoles/gba' },
          ],
        },
        {
          label: 'Sega',
          items: [
            { label: 'Genesis / Mega Drive', link: '/consoles/genesis' },
            { label: 'Saturn', link: '/consoles/saturn' },
          ],
        },
        {
          label: 'Sony',
          items: [
            { label: 'PlayStation', link: '/consoles/ps1' },
          ],
        },
                {
          label: 'Topics',
          items: [
            { label: 'All Topics', link: '/topics/' },
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
