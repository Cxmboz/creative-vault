---
type: moc
title: Note Schema
status: active
---
# Note schema

Every note starts with a header block (YAML frontmatter). Agents filter on these fields,
and `scripts/build_index.py` compiles them into `index.json`.

| Field | Values | Required for |
| --- | --- | --- |
| `type` | knowledge, reference, asset, weapon, project, moc | all |
| `title` | text | all |
| `domain` | list: weapons, environments, props, characters, animation, scripting, texturing, modeling, ui | all but moc |
| `tags` | list, see [[Tag Glossary]] | all but moc |
| `tradition` | japanese, chinese, european, middle-eastern, south-asian, original, n/a | knowledge, reference, weapon |
| `part` | blade, guard, grip, pommel, scabbard, fitting, ornament, whole, n/a | knowledge, reference |
| `source_type` | museum, artist, pin, product, owner-attachment, doc | reference |
| `ref_class` | historical, artistic, mixed, process | reference |
| `style_track` | grounded, futuristic | reference (artistic) |
| `creator` | name as credited, or "unidentified" | reference, asset |
| `creator_terms` | the creator's stated terms, if any (e.g. "NO AI, do not re-upload") | when stated |
| `ai_generated` | true, false, unknown | artistic references |
| `source_name` | text | reference, asset |
| `source_url` | link | reference, asset |
| `license` | CC0, public-domain, CC-BY-4.0, CC-BY-SA, CC-BY-NC, CC-BY-ND, CC-BY-NC-SA, proprietary, unknown | reference, asset |
| `reuse` | free, credit-required, reference-only, do-not-use | reference, asset |
| `local_path` | path inside `../Creative Assets` | asset |
| `author` | owner, claude, codex | all |
| `verified` | true, false | all |
| `verified_on` | YYYY-MM-DD | when verified |
| `status` | draft, active, archived | all |

`reuse` follows from `license` (see [[License Policy]]). Notes written by an agent start
with `verified: false`.

## Element origin labels (in reference notes)

Every reference note has an **Elements** table. Each element is labeled:

- **Historical**: belongs to the real weapon or tradition (documented in museum objects).
- **Artistic**: an addition by an artist; not part of the historical weapon.
- **Process**: a working method, not a design element.
