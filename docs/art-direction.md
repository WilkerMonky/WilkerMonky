# Art Direction

## Concept

The visual system is called **Blue Shadow Systems**. It combines dark fantasy atmosphere with professional software engineering: deep black environments, electric-blue energy, controlled aura, particles, technical interface panels, data routes, and high-contrast system architecture. The intent is to suggest evolution, precision, and power without becoming a fan page or referencing protected anime material.

## Palette

| Role | Hex |
| :--- | :--- |
| Primary background | `#020617` |
| Secondary background | `#0B1120` |
| Deep blue | `#1D4ED8` |
| Primary blue | `#2563EB` |
| Electric blue | `#38BDF8` |
| Blue violet | `#6366F1` |
| Light text | `#E0F2FE` |
| Secondary text | `#94A3B8` |

Black and dark navy carry the profile. Electric blue is reserved for focal energy, interface lines, repository highlights, and hierarchy. The system intentionally avoids red accents.

## Typography

Final raster titles use locally installed Liberation Sans Bold and Liberation Sans Regular. Text is added deterministically through local SVG and ImageMagick rendering so spelling, size, and contrast remain stable. Future SVGs must use system-safe fonts or convert lettering to paths; they must not load remote fonts.

## Proportions and style

- Hero: 8:3, optimized at 1600 x 600.
- Section and closing banners: 16:5, optimized at 1600 x 500.
- Portrait: 3:2, optimized at 1200 x 800.
- Maintain large type, a clear focal area, restrained detail, and single-column presentation.
- Use original dark technology illustration, aura fields, abstract particles, and system UI panels.
- Keep the tone professional for recruiters: no characters, fandom references, spell names, emblems, panels, logos, or copyrighted compositions.

## Intellectual-property boundaries

Do not use characters, logos, skill names, official panels, images, covers, illustrations, symbols, proprietary fonts, or recognizable compositions from Solo Leveling or any other protected work. The only allowed inspiration is the broad combination of dark fantasy, electric blue, black, shadows, aura, and technology interfaces.

## Generation method and source files

The current production images are original SVG compositions rendered locally to PNG with ImageMagick on 4 August 2026. Source SVG files are retained in `assets/source/`; production PNG files keep their stable names in `assets/` so README references remain unchanged.

## Current source files

| Production file | Source file |
| :--- | :--- |
| `assets/wilker-fullstack-banner.png` | `assets/source/wilker-fullstack-banner.svg` |
| `assets/wilker-developer-portrait.png` | `assets/source/wilker-developer-portrait.svg` |
| `assets/featured-projects-banner.png` | `assets/source/featured-projects-banner.svg` |
| `assets/research-publications-banner.png` | `assets/source/research-publications-banner.svg` |
| `assets/wilker-closing-card.png` | `assets/source/wilker-closing-card.svg` |

## Future artwork guidance

1. Start from the palette above and one clear engineering idea.
2. Prefer original system interfaces, data routes, particles, architecture panels, and abstract aura fields.
3. Review for accidental resemblance to protected characters, symbols, logos, titles, panels, or proprietary fonts.
4. Check contrast and meaning at approximately 360 px viewport width.
5. Strip metadata, optimize file size, write useful alternative text, and document the source or prompt here.
6. Never introduce remote resources, scripts, or external fonts into SVG files.
