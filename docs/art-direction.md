# Art Direction

## Concept

The visual system is called **Purple Shadow Systems**. It combines original dark fantasy atmosphere with professional software engineering: black backgrounds, purple aura, luminous violet particles, abstract smoke, subtle technology panels, data routes, and high-contrast system architecture. The goal is to communicate evolution, engineering depth, and technical precision while remaining appropriate for recruiters.

## Palette

| Role | Hex |
| :--- | :--- |
| Primary background | `#030108` |
| Secondary background | `#0B0614` |
| Deep purple | `#2E1065` |
| Dark purple | `#4C1D95` |
| Primary purple | `#7C3AED` |
| Violet | `#8B5CF6` |
| Luminous purple | `#A855F7` |
| Lilac | `#C084FC` |
| Primary text | `#F5F3FF` |
| Secondary text | `#C4B5FD` |
| Quiet text | `#A1A1AA` |

Black and near-black carry the profile. Purple and lilac are reserved for focal aura, interface lines, repository highlights, section hierarchy, and badge accents. Red is not part of the identity.

## Typography

The main profile banner uses a system-safe serif stack for the `WilkerMonky` wordmark: `Georgia, Times New Roman, serif`. Supporting labels use Liberation Sans or Arial. No remote fonts are loaded, and the production PNGs are rendered locally from SVG source files.

## Proportions and style

- Hero: 8:3, optimized at 1600 x 600.
- Section and closing banners: 16:5, optimized at 1600 x 500.
- Portrait: 3:2, optimized at 1200 x 800.
- Maintain large type, a clear focal area, restrained detail, and single-column presentation.
- Use original abstract aura, smoke-like gradients, particles, data routes, architecture panels, and system UI lines.
- Keep the tone professional: no characters, faces, creatures, silhouettes, emblems, logos, copied lettering, official artwork, or recognizable compositions from reference material.

## Intellectual-property boundaries

The local reference image was used only to understand atmosphere, purple energy, contrast, and depth. The committed assets are original SVG compositions and must not copy protected characters, symbols, titles, official panels, proprietary typography, or recognizable marks from any reference work.

## Generation method and source files

The current production images are original SVG compositions rendered locally to PNG with ImageMagick on 4 August 2026. Source SVG files are retained in `assets/source/`; production PNG files remain in `assets/` for GitHub README compatibility.

## Current source files

| Production file | Source file | Size |
| :--- | :--- | :--- |
| `assets/wilker-fullstack-banner.png` | `assets/source/wilker-fullstack-banner.svg` | 1600 x 600 |
| `assets/wilker-developer-portrait.png` | `assets/source/wilker-developer-portrait.svg` | 1200 x 800 |
| `assets/engineering-focus-banner.png` | `assets/source/engineering-focus-banner.svg` | 1600 x 500 |
| `assets/featured-projects-banner.png` | `assets/source/featured-projects-banner.svg` | 1600 x 500 |
| `assets/research-publications-banner.png` | `assets/source/research-publications-banner.svg` | 1600 x 500 |
| `assets/wilker-closing-card.png` | `assets/source/wilker-closing-card.svg` | 1600 x 500 |

## Regenerate PNGs

Run these commands from the repository root:

```bash
magick assets/source/wilker-fullstack-banner.svg assets/wilker-fullstack-banner.png
magick assets/source/wilker-developer-portrait.svg assets/wilker-developer-portrait.png
magick assets/source/engineering-focus-banner.svg assets/engineering-focus-banner.png
magick assets/source/featured-projects-banner.svg assets/featured-projects-banner.png
magick assets/source/research-publications-banner.svg assets/research-publications-banner.png
magick assets/source/wilker-closing-card.svg assets/wilker-closing-card.png
```

## GitHub Stats Provider Notes

The previous `github-readme-stats.vercel.app` image URLs returned `503 text/plain` with a paused deployment message during validation. Alternative dynamic SVG providers tested during this update also failed to provide two reliable image cards. The README therefore uses stable GitHub profile links instead of embedding broken external images.

## Validate the profile

```bash
python3 .github/scripts/validate_profile.py
git diff --check
grep -RniE '<old-red-hex-values>' README.md README.pt-BR.md assets docs || true
```

## Future artwork guidance

1. Start from the palette above and one clear engineering idea.
2. Prefer original system interfaces, data routes, particles, architecture panels, and abstract aura fields.
3. Review for accidental resemblance to protected characters, symbols, logos, titles, panels, lettering, or proprietary fonts.
4. Check contrast and meaning at approximately 360 px viewport width.
5. Strip metadata, optimize file size, write useful alternative text, and document the source or prompt here.
6. Never introduce remote resources, scripts, or external fonts into SVG files.
