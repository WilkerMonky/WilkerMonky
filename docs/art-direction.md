# Art Direction

## Concept

The visual system is called **Connected City Engineering**. It combines a nighttime city, software architecture panels, data nodes, and abstract network lines to express full-stack integration, vigilance, responsibility, and reliable engineering. The atmosphere takes broad inspiration from urban graphic novels while remaining an original professional identity with no licensed characters or marks.

## Palette

| Role | Hex |
| :--- | :--- |
| Primary background | `#05070D` |
| Secondary background | `#0B1120` |
| Deep blue | `#111827` |
| Primary red | `#DC2626` |
| Light red | `#EF4444` |
| White | `#F8FAFC` |
| Gray | `#94A3B8` |

Dark navy carries the composition, white maintains contrast, and red is reserved for connections, focus points, and hierarchy.

## Typography

Final raster titles use locally installed Liberation Sans Bold and Liberation Sans Regular. Text is added after illustration generation so spelling, size, and contrast remain deterministic. Future SVGs must use system-safe fonts or convert lettering to paths; they must not load remote fonts.

## Proportions and style

- Hero: 8:3, optimized at 1600 × 600.
- Section and closing banners: 16:5, optimized at 1600 × 500.
- Portrait: 3:2, optimized at 1200 × 800.
- Maintain large type, a clear focal area, restrained detail, and single-column presentation.
- Use modern graphic-novel linework with editorial technology illustration, not a childish comic treatment.

## Intellectual-property boundaries

Do not use Marvel imagery, the Spider-Man name, Peter Parker, Miles Morales, existing costumes, masks, poses, web shooters, spider emblems, or logos. Do not trace or remix online artwork. Abstract connection lines, city architecture, code, data, and system diagrams must be independently generated. A future original masked character should be used only after a deliberate similarity review; the current system avoids masked characters entirely.

## Generation method and source files

The five illustration bases were created with OpenAI's built-in image generation tool on 29 July 2026. Text overlays, resizing, sRGB conversion, metadata stripping, and PNG optimization were completed locally with ImageMagick. Generated source images are retained by the tool outside the repository; final production files are in `assets/`. This document and Git history are the reproducible creative record.

## Prompts used

All prompts shared these constraints: original imagery; palette `#05070D`, `#0B1120`, `#111827`, `#DC2626`, `#EF4444`, `#F8FAFC`, `#94A3B8`; no text in the generated base; no brands, watermarks, copyrighted characters, costumes, masks, emblems, spiders, or recognizable superhero poses.

### Hero

> Create a professional wide GitHub banner with a futuristic night skyline, abstract technical network lines, and subtle frontend, backend, API, and relational database panels. Use a mature graphic-novel editorial style and reserve uncluttered space for a later title.

### Developer portrait

> Create an original, unmasked adult developer in an urban technology workspace using multiple monitors that visualize software architecture, APIs, and connected systems. Use professional contemporary clothing and precise architectural linework.

### Featured projects

> Visualize a horizontal system flowing from frontend panels through backend services and API gateways to databases, tests, containers, and infrastructure. Reserve dark space for a later section title.

### Research and publications

> Visualize rigorous technology research through documents, anonymized interview silhouettes, datasets, charts, notes, and knowledge nodes. Keep the scene analytical, humane, privacy-aware, and uncluttered.

### Closing card

> Create a restrained future city connected by precise abstract lines converging on a stable systems node. Leave central space for a statement and communicate reliability, responsibility, and quiet confidence.

## Future artwork guidance

1. Start from the same palette and one clear engineering idea.
2. Generate illustration without text; add verified text locally.
3. Review for accidental resemblance to protected characters or symbols.
4. Check contrast and meaning at approximately 360 px viewport width.
5. Strip metadata, optimize file size, write useful alternative text, and document the prompt here.
6. Never introduce remote resources, scripts, or external fonts into SVG files.
