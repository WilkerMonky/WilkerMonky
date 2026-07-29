# Project Import Checklist

Use this checklist before connecting any project to the profile. A public portfolio never justifies exposing employer-owned code, credentials, personal data, research participants, or material without publication permission.

## Before import

- [ ] Confirm that the project may legally be published.
- [ ] Exclude code owned by an employer, including Banco do Brasil and BB Administradora de Consórcios.
- [ ] Search the working tree and Git history for tokens, API keys, passwords, private keys, connection strings, and internal URLs.
- [ ] Remove `.env` files and provide a sanitized `.env.example` containing placeholders only.
- [ ] Rotate every secret that has ever entered Git history; deleting it from the latest commit is not sufficient.
- [ ] Review personal data, logs, fixtures, database dumps, screenshots, and document metadata.
- [ ] Anonymize research participants and publish data only when consent and institutional rules allow it.
- [ ] Confirm repository ownership, contributor permissions, third-party licenses, and intellectual-property constraints.
- [ ] Choose and add an appropriate license only when authorized to license the complete repository.
- [ ] Create a recoverable backup before rewriting history.

Suggested read-only checks (adapt patterns to each technology):

```bash
git status
git log --all --oneline --decorate
git grep -n -I -E '(password|passwd|secret|token|api[_-]?key|private[_-]?key)'
git log --all -p -- .env '*.pem' '*.key'
```

These searches are indicators, not a complete security audit. Use a dedicated secret scanner and review its documentation before publishing.

## During import

- [ ] Preserve Git history and contributor attribution when possible.
- [ ] Configure the intended default branch, normally `main`.
- [ ] Add a technology-appropriate `.gitignore`.
- [ ] Add the approved license and contributor notices.
- [ ] Set a concise repository description, topics, and homepage.
- [ ] Write a README with problem, scope, architecture, prerequisites, configuration, execution, tests, security notes, and contribution boundaries.
- [ ] Add only sanitized screenshots and diagrams.
- [ ] Document environment variables without real values.
- [ ] Configure GitHub Actions with least privilege and actions pinned to immutable commit SHAs.
- [ ] Protect the default branch if collaboration or automated releases require it.

### Full mirror

Use a mirror only when the GitHub destination is new or intentionally prepared to receive every Git reference:

```bash
git clone --mirror URL_DO_GITLAB
cd NOME_DO_REPOSITORIO.git
git push --mirror URL_DO_GITHUB
```

> **Warning:** `git push --mirror` synchronizes all references and can overwrite or delete references at the destination. Never point it at an existing repository unless every destination reference has been reviewed and a recoverable backup exists.

### Standard branch import

This approach pushes the selected branch without mirroring every reference:

```bash
git clone URL_DO_GITLAB
cd NOME_DO_REPOSITORIO
git remote add github URL_DO_GITHUB
git push -u github main
```

If the source default branch has another name, inspect it first with `git branch --show-current`; do not assume or rename it without reviewing CI and documentation.

## After import

- [ ] Clone the GitHub repository into a clean directory and test installation from the published instructions.
- [ ] Run tests, linters, build, migrations, and Docker setup.
- [ ] Validate links, screenshots, diagrams, API examples, and environment-variable names.
- [ ] Replace the corresponding `Coming Soon` text in both profile READMEs with real repository and documentation links.
- [ ] Pin the repository on the GitHub profile.
- [ ] Configure repository description, topics, homepage, branch protection, and security settings.
- [ ] Create an initial release when the project is stable enough to version.
- [ ] Add a short, accessible video or GIF only if it improves understanding.
- [ ] Open issues for known limitations and future work.

## Project-specific review

### IGRIS

- Verify the allocation problem, genetic algorithm, compared strategies, and service boundaries directly from source.
- Correct any README content mixed with GradeMaker.
- Document Sunny, Morpheus, Rocket, the main application, React, PostgreSQL, and their communication paths.
- Add architecture and algorithm diagrams, execution instructions, screenshots, and only measured results.

### Academic Tutoring Management System

- Identify entities, business rules, users, roles, authentication, registration, and tutor-assignment flows from source.
- Produce architecture and entity diagrams after verification.

### GradeMaker

- Remove personal emails and real credentials from examples and history.
- Verify Docker commands, configuration, security model, domain boundaries, and API documentation.

### PGP Academy

- Confirm publication permission and contributor attribution.
- Describe Weslley's specific contribution without implying sole authorship.

### Soft Skills research

- Confirm publication rights for the paper and consent for every released dataset.
- Anonymize participants, remove document metadata, add `CITATION.cff`, and select an appropriate license.
