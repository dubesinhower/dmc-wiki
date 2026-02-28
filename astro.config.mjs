// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'My Docs',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/withastro/starlight' }],
			sidebar: [
				{
					label: 'Nintendo',
					items: [
						{ label: 'NES', slug: 'consoles/nes' },
						{ label: 'SNES', slug: 'consoles/snes' },
						{ label: 'N64', slug: 'consoles/n64' },
						{ label: 'GameCube', slug: 'consoles/gamecube' },
						{ label: 'Game Boy', slug: 'consoles/gameboy' },
						{ label: 'Game Boy Advance', slug: 'consoles/gba' },
					],
				},
				{
					label: 'Sega',
					items: [
						{ label: 'Genesis / Mega Drive', slug: 'consoles/genesis' },
						{ label: 'Saturn', slug: 'consoles/saturn' },
						{ label: 'Dreamcast', slug: 'consoles/dreamcast' },
						{ label: 'Game Gear', slug: 'consoles/game-gear' },
					],
				},
				{
					label: 'Sony',
					items: [
						{ label: 'PlayStation (PS1)', slug: 'consoles/ps1' },
						{ label: 'PlayStation 2', slug: 'consoles/ps2' },
					],
				},
				{
					label: 'Other',
					items: [
						{ label: 'Neo Geo', slug: 'consoles/neo-geo' },
						{ label: 'Xbox (Original)', slug: 'consoles/xbox' },
						{ label: 'TurboGrafx-16 / PC Engine', slug: 'consoles/tg16-pce' },
						{ label: 'Pioneer LaserActive', slug: 'consoles/laser-active' },
						{ label: 'Atari Consoles', slug: 'consoles/atari' },
						{ label: 'Obscure & Other', slug: 'consoles/obscure' },
					],
				},
			],
		}),
	],
});
