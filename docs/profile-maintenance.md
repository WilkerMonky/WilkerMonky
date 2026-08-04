# Profile Maintenance

The English README is the primary version. Update `README.md` and `README.pt-BR.md` in the same change, preserving facts, project status, links, and section order rather than translating word for word.

## Add or publish a project

1. Complete the [project import checklist](./project-import-checklist.md).
2. Copy an existing project block in both README files.
3. Replace the name, verified description, highlights, and stack.
4. Replace `Coming Soon` with real links only after testing them:

   ```md
   [Repository](https://github.com/WilkerMonky/REPOSITORY) • [Documentation](https://github.com/WilkerMonky/REPOSITORY#readme) • [Demo](https://verified-demo.example)
   ```

5. Omit `Documentation` or `Demo` when no real destination exists; do not use `#`, example URLs, or empty links.
6. Pin the strongest repositories from GitHub profile settings. Favor representative, maintained work over quantity.

## Update the résumé

Replace `assets/Weslley-Wilker-CV.pdf` with the approved public version while keeping the filename stable. Before publishing, verify that it contains no unwanted phone number, address, document identifier, hidden annotation, or metadata. The README intentionally does not display phone numbers.

## Replace artwork

Keep the current filenames and approximate proportions to avoid README changes:

| File | Target size | Role |
| :--- | :--- | :--- |
| `wilker-fullstack-banner.png` | 1600 x 600 | Profile hero |
| `wilker-developer-portrait.png` | 1200 x 800 | About illustration |
| `featured-projects-banner.png` | 1600 x 500 | Projects divider |
| `research-publications-banner.png` | 1600 x 500 | Research divider |
| `wilker-closing-card.png` | 1600 x 500 | Closing statement |

Export PNGs in sRGB, strip unnecessary metadata, keep each preferably near or below 1 MB, and test text at mobile width. Update alternative text if the visual meaning changes. See [art direction](./art-direction.md) before generating replacements.

## Update technologies and badges

- Add a technology only when supported by the résumé or a public repository.
- Keep badge count restrained; plain text is preferable for secondary tools and engineering practices.
- Use the blue and black palette in [art direction](./art-direction.md) and avoid adding animated or visitor-count widgets.
- Verify every badge and external statistic endpoint in both light and dark GitHub themes.

## Validate the profile

Run the same local checks used by CI:

```bash
python3 .github/scripts/validate_profile.py
git diff --check
```

Then inspect both README files in a Markdown preview and on GitHub after publication. Check narrow viewport wrapping, image alternative text, local files, external links, and the exact `username=WilkerMonky` parameter on statistic cards.

## Routine review

- Review the profile after every résumé or role change and at least quarterly.
- Remove stale demos and obsolete technologies.
- Confirm that planned projects are still labeled as planned.
- Keep professional experience free of confidential implementation details.
- Keep English and Portuguese claims aligned.
