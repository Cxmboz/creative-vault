# Instructions for AI agents (Claude, Codex, others)

This repository is a curated creative knowledge vault. Read this file fully before using it.

## Finding things

1. Read `index.json` first. It lists every note with its type, tags, domain, license,
   reuse status and verification status. Rebuild it with `python scripts/build_index.py`
   if it looks stale.
2. Then open only the notes you need. Do not read the whole vault.
3. Notes link to each other with `[[Note Name]]`; follow links for context.
4. Large files are NOT in this repository. An asset note's `local_path` points into the
   separate asset library (`../Creative Assets`), which may only exist on the owner's PC.

## Writing notes

- Always start from a template in `_templates/` and fill the header block per
  `_system/Note Schema.md`.
- Set `author` to yourself and `verified: false`. Only the owner, or a check against the
  cited source, sets `verified: true`.
- Never guess a license. Unknown means `license: unknown` and `reuse: reference-only`.
- Every reference or asset note must cite `source_url`.
- One topic per note. Keep cards short; link instead of repeating.
- Run `python scripts/build_index.py` after adding or editing notes and fix any warnings.

## Rules that always apply

- `_system/License Policy.md`: what may go into a model or a published game.
- `_system/Originality Rules.md` and `_system/Cliche List.md`: how references are used.
- Never commit large binaries (models, textures, HDRIs, .blend, video). See `.gitignore`.
- Never store or trace contemporary concept art from ArtStation, Pinterest or similar.
