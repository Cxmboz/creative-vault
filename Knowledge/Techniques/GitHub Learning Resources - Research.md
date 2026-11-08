---
type: knowledge
title: GitHub Learning Resources - Research
domain: [animation, modeling, texturing, scripting]
tags: [roblox-import, rigging, pbr, procedural]
tradition: n/a
part: n/a
author: claude
verified: false
status: draft
---
# GitHub learning resources: research report (first batch)

A bounded first pass at public GitHub repositories that can teach practical skills for
Blender animation, Blender-to-Roblox work and the [[Sword Arsenal]]. Not an exhaustive
search of GitHub.

## 1. Scope, date and limits

- **Inspected:** 2026-11-08. 25 candidates looked at, 11 evaluated in depth (section 3).
- **What "inspected" means here:** README and license file read for every candidate; for
  finalists, at least one substantive teaching page or source file was also read (listed in
  each profile). Nothing was cloned, installed or run.
- **Maintenance data** (last push, archived, fork, stars) came from
  [repos.ecosyste.ms](https://repos.ecosyste.ms), a third-party index of GitHub, because the
  GitHub API was not reachable from this workspace. Treat dates as approximate.
- **Your tools:** Blender 5.2.2, Roblox Studio with Eclipse Animator and RigEdit Lite, R6 rig.
  These come from [[Handoff - 2026-11-08]] and were **not** re-checked on your PC.
- **Not covered:** Blender's own manual and source live on projects.blender.org, not GitHub.
  They are cited as primary sources in the notes but were not scored.

**Main finding.** GitHub is strong for *tools* and *official docs-as-code* and weak for
animation teaching. The best teaching material found is Roblox's own documentation
repository. Animation principles, rigging and constraint teaching are better served by the
Blender manual than by any GitHub repository found in this pass.

## 2. Recommended starting sequence

1. **Roblox creator-docs: the Blender page and modeling specifications.** Read with
   [[Blender to Roblox Export Checklist]]. It confirms (or corrects) the scale and axis
   rules every weapon depends on.
2. **Interpolation.** Read [[Interpolation and Easing - Blender and Roblox]], then
   creator-docs `animation/curve-editor` and the Blender manual's F-Curve properties page.
   This is the fundamentals gap you named: why motion looks floaty or stiff.
3. **Weapon attachment.** [[Weapon Attachment - Prop Bones and Motor6D]] before adding the
   `Prop_Weapon` / `Prop_Scabbard` bones (handoff open item 5).
4. **Textures.** [[PBR Textures for Roblox SurfaceAppearance]] with the Physically Based
   dataset, before the C01 rebuild's materials are set.
5. **Later:** the Geometry Script book, when procedural fittings are next.

## 3. Comparison table

Scores use the 100-point framework (relevance 30, teaching 25, practical 20, credibility and
version fit 15, licensing clarity 10). They are reasoned judgments, not measurements.

| # | Repository | Category | Main subject | Difficulty, prerequisites | Best use for you | License | Compatibility | Score | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [Roblox/creator-docs](https://github.com/Roblox/creator-docs) | Learning resource | Official Roblox docs as Markdown: Blender setup, export, PBR, animation, engine API | Beginner to intermediate; none | The rulebook for Blender-to-Roblox, animation and textures | Prose CC-BY-4.0, code samples MIT (per README) | Current; pushed 2026-11-05 | 93 | Use now |
| 2 | [carson-katri/geometry-script](https://github.com/carson-katri/geometry-script) | Tool with educational docs | Write Geometry Nodes trees as Python | Intermediate; Python basics, Geometry Nodes basics | Procedural fittings and scabbard parts, readable by agents | GPL-3.0 | Docs say requires Blender 5.2+, builds per version; untested here | 81 | Useful later (use now for agent-built prototypes) |
| 3 | [AntonPalmqvist/physically-based-api](https://github.com/AntonPalmqvist/physically-based-api) | Asset collection (data) | Measured colour, metalness, roughness, IOR with references | Beginner; knowing linear vs sRGB colour | Base values for steel, iron, silver, brass, gold | CC0 1.0 (data) | Version-independent | 76 | Use now |
| 4 | [Roblox/roblox-blender-plugin](https://github.com/Roblox/roblox-blender-plugin) | Tool (reference implementation) | Upload meshes from Blender to Roblox via Open Cloud | Beginner; Roblox login | Faster re-uploads of weapon meshes as packages | MIT | States Blender 3.2+; 5.2 untested | 70 | Useful later |
| 5 | [Cautioned/Blender-Animations-Plugin](https://github.com/Cautioned/Blender-Animations-Plugin) | Tool | Blender ⇄ Roblox animation sync, Motor6D bone sync | Intermediate; rig mapping | Alternative to your Eclipse bridge for Blender-made combat animations | GPL-3.0 | Manifest min Blender 4.2; 5.2 untested | 69 | Useful later (evaluate) |
| 6 | [nutti/fake-bpy-module](https://github.com/nutti/fake-bpy-module) | Tool | Code completion for `bpy` in an editor | Beginner Python | Writing bpy scripts outside Blender without guessing names | MIT | A `fake-bpy-module-5.2` package exists on PyPI (2026-07-30) | 68 | Useful later |
| 7 | [ssloy/tinyrenderer](https://github.com/ssloy/tinyrenderer) | Learning resource | How rasterizers work, incl. tangent-space normal mapping | Advanced; C++, linear algebra | Understanding *why* normal maps and UVs behave as they do | Code: zlib-style permissive; course notes: no license stated | Version-independent | 66 | Useful later |
| 8 | [JacquesLucke/blender_vscode](https://github.com/JacquesLucke/blender_vscode) | Tool | Run and debug Blender scripts and add-ons from VS Code | Intermediate | Pairs with #6 once you script regularly | MIT | States Blender ≥ 2.8.34, extensions supported | 65 | Useful later |
| 9 | [Swordphin/raycastHitboxRbxl](https://github.com/Swordphin/raycastHitboxRbxl) | Tool (Luau module) | Raycast hit detection for melee weapons | Intermediate; Luau, Studio API | Hit detection once sword animations are in a game | MIT | Last push 2024-08; README points to DevForum for current docs | 65 | Useful later |
| 10 | [franMarz/TexTools-Blender](https://github.com/franMarz/TexTools-Blender) | Tool | UV layout and baking helpers | Intermediate; UV basics | Faster atlas packing and bakes | GPL-3.0 (LICENSE.txt) | States Blender 3.2+; last push 2024-12; 5.2 untested | 58 | Reference only for now |
| 11 | [aresdevo/animaide](https://github.com/aresdevo/animaide) | Tool (manual is educational) | Curve tools for animators: tween, blend, offset | Intermediate; Graph Editor | Read its manual for curve-editing ideas | GPL-3.0 (source header; no root LICENSE) | Likely broken on 5.x: source uses `action.fcurves`, removed in Blender 5.0 | 53 | Reference only |

Fewer than 12 finalists on purpose: the remaining candidates (section 5) did not meet the
standard for this project.

## 4. Profiles

### 1. Roblox/creator-docs: 93 (relevance 29, teaching 23, practical 19, credibility 14, license 8)
- **What it teaches:** the source of create.roblox.com/docs. Pages inspected:
  `content/en-us/art/blender.md` (units, import and export axes, FBX scale options),
  `art/modeling/specifications.md`, `art/modeling/export-requirements.md`,
  `art/modeling/texture-specifications.md`, `art/modeling/surface-appearance.md`,
  `animation/editor.md`, `animation/curve-editor.md`, `physics/assemblies.md`, and the
  `Motor6D` and `AnimationConstraint` class reference files.
- **Why here:** it is the authority on what Studio accepts. It confirmed the arsenal's unit
  standard and surfaced three things the handoff does not mention (20,000-triangle mesh cap,
  OpenGL-only normal maps, `AvatarJointUpgrade`; see the cards).
- **Start:** `art/blender.md` → `art/modeling/specifications.md` → `animation/curve-editor.md`.
- **Limits:** written for Studio, so Blender steps are brief; some links point at old Blender
  manual versions (one goes to 2.81). The repository is very large; read pages online.
- **Licensing:** prose CC-BY-4.0 and code samples MIT, as the README states. Images in the repo
  are not separately addressed; treat screenshots as link-only. Original summaries are fine.
- **Proposed exercise (untested):** the export round-trip in [[Blender to Roblox Export Checklist]].

### 2. carson-katri/geometry-script: 81 (22 / 20 / 17 / 14 / 8)
- **What it teaches:** a Python way of writing Geometry Nodes. Inspected: book `SUMMARY.md`,
  Installation, Tree Functions, Generators and Command-Line and Agent Tools pages.
- **Why here:** procedural parts are Tier 1 in the arsenal plan. Node trees as text are easier
  to review, version in Git and hand between agents than screenshots of nodes.
- **Prerequisites:** Python basics; what a Geometry Nodes modifier does.
- **Start:** the book's Introduction and Tree Functions pages.
- **Limits:** the installation page says each build matches one Blender version and the minimum
  is 5.2, which matches your reported 5.2.2, but nothing was installed or tested. The repo ships
  an AI-agent skill file; it was noted, not read as instructions.
- **Licensing:** GPL-3.0. Using it as a tool is fine; copying its source into our scripts
  would bring GPL obligations. (Assessment, not legal advice.)
- **Reading order:** Introduction → Installation → Tree Functions → Sockets → Using Nodes →
  Generators; the tutorials (Voxelize, City Builder) last.
- **Proposed exercise (untested, needs install approval):** describe a turned pommel as a tree:
  a profile curve revolved, with length and radius as inputs, then change the inputs to make
  three variants. Compare with how the jian's fittings were made in `build_sword.py`.

### 3. AntonPalmqvist/physically-based-api: 76 (20 / 15 / 18 / 13 / 10)
- **What it teaches:** measured material values. Inspected `deploy/v2/materials.json`: 122
  materials, each with colour (linear sRGB and ACEScg), metalness, roughness, complex IOR and
  a `references` list (Iron cites refractiveindex.info and an OpenPBR paper).
- **Why here:** removes guessing from base colours of blade and fitting metals.
- **Limits:** roughness values are clean-surface references (0 for the polished metals), not
  aged sword finishes. Colours are linear; see the PBR card for conversion.
- **Licensing:** data CC0 1.0; the shader-ball renders are CC BY 4.0 (stated in README).
- **Start:** the README, then search `materials.json` for a metal's name.
- **Proposed exercise:** in [[PBR Textures for Roblox SurfaceAppearance]].

### 4. Roblox/roblox-blender-plugin: 70 (20 / 15 / 14 / 11 / 10)
- **What it does:** uploads selected Blender objects to Roblox as packages, with auto-update.
  Inspected README installation and usage sections.
- **Caveats:** first run installs Python dependencies into Blender and needs a Roblox login.
  Both need your approval. Not required for animation work.
- **Proposed exercise (untested, needs approval):** upload a throwaway cube, change it in
  Blender, re-upload, and check that the Studio package auto-updates as the README describes.

### 5. Cautioned/Blender-Animations-Plugin: 69 (26 / 9 / 17 / 9 / 8)
- **What it does:** Blender add-on plus Studio plugin for live animation sync, bone-to-Motor6D
  sync and easing transfer. Inspected README, `roblox_animations/blender_manifest.toml`
  (min Blender 4.2.0, version 3.1.3) and the `docs/index.html` page (a landing page, not docs).
- **Lineage:** the README credits the original add-on by Den_S
  ([DevForum thread](https://devforum.roblox.com/t/blender-rig-exporteranimation-importer/34729)).
  `revate/Blender-Animations-Plugin` is a copy pointing back to this repo and was not counted.
- **Limits:** teaching value is low; the easing claim ("transfers losslessly where possible")
  is the author's, not tested. Blender 5.2 compatibility not checked.
- **Licensing:** GPL-3.0, plus the author's explicit request not to resell it on the Creator
  Store. Honor that.
- **Proposed exercise (backlog item 2, untested):** export the same 24-frame slash through
  Eclipse and through this plugin and compare curves in Studio's Curve Editor.

### 6. nutti/fake-bpy-module: 68 (15 / 14 / 15 / 14 / 10)
- Type stubs so an editor can autocomplete `bpy`. Inspected README install section and
  confirmed a 5.2 package on PyPI. Install only with approval.
- **Proposed exercise:** with the 5.2 stubs, type `bpy.types.Action.` and check that
  `fcurves` is *not* offered, as a quick way to see the 5.0 API change.

### 7. ssloy/tinyrenderer: 66 (13 / 22 / 10 / 14 / 7)
- A 14-lesson course on writing a software renderer. Inspected README lesson list and the
  [tangent-space normal mapping lesson](https://haqr.eu/tinyrenderer/tangent/), which explains
  why tangent-space maps survive mirrored and reused UVs and builds the tangent frame from UV
  edges. Advanced; useful for understanding, not for daily work. Notes have no stated license:
  link and summarize only.
- **Prerequisites:** the course's "More data!" (textures) and shading lessons, vectors and
  matrices. **Proposed exercise:** read only the tangent lesson's first half and explain in one
  paragraph why a mirrored UV island can share one normal-map region.

### 8. JacquesLucke/blender_vscode: 65 (14 / 14 / 14 / 13 / 10)
- VS Code extension that starts Blender, reloads add-ons and runs scripts. Inspected README.
  Worth it only once scripting becomes regular.

### 9. Swordphin/raycastHitboxRbxl: 65 (18 / 13 / 15 / 9 / 10)
- Raycast-based melee hit detection. README defers to its wiki and DevForum thread, so the
  GitHub copy may lag. Park until a combat prototype exists.

### 10. franMarz/TexTools-Blender: 58 (17 / 10 / 15 / 8 / 8)
- UV and bake helpers. README itself calls its documentation outdated; last push Dec 2024.
  Learn Blender's built-in UV and bake tools first.

### 11. aresdevo/animaide: 53 (20 / 15 / 6 / 4 / 8)
- An animator's curve toolkit with a clear illustrated [manual](https://aresdevo.github.io/animaide/).
  The README says development stopped and warns Blender's new animation system will likely
  break it. Static check: `utils/curve.py`, `utils/key.py`, `curve_tools/support.py` and
  `anim_offset/support.py` all use `action.fcurves`, which
  [Blender 5.0 removed](https://developer.blender.org/docs/release_notes/5.0/python_api/).
  Read the manual for ideas; do not install on 5.2.

## 5. Candidates not selected

| Repository | Reason |
| --- | --- |
| [Roblox/avatar](https://github.com/Roblox/avatar) | Beta test materials under a Roblox *Limited Use License*; README says Roblox does not commit to maintaining it. Link only |
| [PacktPublishing/Python-Scripting-in-Blender](https://github.com/PacktPublishing/Python-Scripting-in-Blender) | Book code without the book; targets Blender 3.3, before the 4.4/5.0 animation API changes |
| [CGArtPython/blender_plus_python](https://github.com/CGArtPython/blender_plus_python) | Active, MIT, but generative-art loops paired with videos; low relevance to weapons or character animation |
| [zeffii/BlenderPythonRecipes](https://github.com/zeffii/BlenderPythonRecipes) | Snippet wiki started in 2015; high version risk |
| [T-K-233/Blender-Python-Cookbook](https://github.com/T-K-233/Blender-Python-Cookbook) | CC0 but about 770 words in total; too thin |
| [TK-DZ/Roblox-IK-R15](https://github.com/TK-DZ/Roblox-IK-R15) | R15 not R6, no license, depends on the older Den_S add-on |
| revate/Blender-Animations-Plugin | Copy of Cautioned's repository |
| [blender/blender](https://github.com/blender/blender) | Read-only mirror of projects.blender.org; the Python API site is the better entry point |
| [blender/blender-addons](https://github.com/blender/blender-addons) | Archived mirror (June 2025); add-ons moved to the Extensions platform |
| [patriciogonzalezvivo/thebookofshaders](https://github.com/patriciogonzalezvivo/thebookofshaders) | All rights reserved; GLSL shader focus (priority C) |
| [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | Runs code in a live Blender; install is a piped web script. Parked pending a security decision |
| [KhronosGroup/glTF-Blender-IO](https://github.com/KhronosGroup/glTF-Blender-IO) | Already bundled with Blender; relevant only if we switch from FBX to glTF |
| [luau-lang/luau](https://github.com/luau-lang/luau) | Language implementation, not a tutorial. Its docs site is `luau-lang/site` (MIT) for later |
| [agmmnn/awesome-blender](https://github.com/agmmnn/awesome-blender) | Discovery index only (CC0). Useful for finding add-ons; no Roblox entries |

## 6. Licensing and compatibility caveats

Provenance per finalist (all inspected 2026-11-08; "summarize" means an original summary with a link):

| Repository | License found | Unclear areas | Link and summarize | Copy, modify, redistribute | Attribution |
| --- | --- | --- | --- | --- | --- |
| Roblox/creator-docs | `LICENSE` CC-BY-4.0 (prose); README names `LICENSE-CODE` MIT (code) | Images and screenshots not addressed | Yes | Prose and code yes, with attribution; images no | Credit Roblox, CC BY 4.0 / MIT notice |
| carson-katri/geometry-script | `LICENSE` GPL-3.0 | Book text assumed under the same license | Yes | Only under GPL-3.0 | GPL notice |
| AntonPalmqvist/physically-based-api | `LICENSE` CC0 1.0; data header repeats CC0 | Shader-ball renders are CC BY 4.0 | Yes | Data yes; renders with credit | None for data (courtesy credit in [[Credits]] optional) |
| Roblox/roblox-blender-plugin | `LICENSE.md` MIT | None found | Yes | Yes, keep MIT notice | MIT notice |
| Cautioned/Blender-Animations-Plugin | `LICENSE` GPL-3.0 | Author's extra request: no paid Creator Store re-uploads | Yes | Only under GPL-3.0 and honoring the request | GPL notice |
| nutti/fake-bpy-module | `LICENSE` MIT | None found | Yes | Yes | MIT notice |
| ssloy/tinyrenderer | `LICENSE.txt` zlib-style | Course notes on haqr.eu: no license stated | Yes | Code yes; notes no | Keep notice |
| JacquesLucke/blender_vscode | `LICENSE` MIT | None found | Yes | Yes | MIT notice |
| Swordphin/raycastHitboxRbxl | `LICENSE` MIT | Wiki and DevForum docs not covered | Yes | Code yes | MIT notice |
| franMarz/TexTools-Blender | `LICENSE.txt` GPL-3.0 header | Image links on renderhjs.net unlicensed | Yes | Only under GPL-3.0 | GPL notice |
| aresdevo/animaide | GPL-3.0 in `__init__.py` header; no root LICENSE | Manual site images | Yes | Only under GPL-3.0 | GPL notice |

- **Nothing was imported.** No code, text or images from any repository are in the vault.
  The cards are original summaries with links.
- **GPL repositories** (Geometry Script, Cautioned plugin, TexTools, AnimAide): use as tools,
  do not paste their code into our scripts.
- **Roblox docs:** prose CC-BY-4.0, code samples MIT; screenshots not separately licensed, so
  link to them rather than copying.
- **Blender 5.0 removed the legacy Action API** (`action.fcurves`, `action.groups`,
  `action.id_root`). Any script or tutorial that reads keyframes that way fails on your 5.2.2.
  This rules out most pre-2025 bpy animation material.
- **Roblox `AvatarJointUpgrade`:** R15 player characters in new experiences spawn with
  `AnimationConstraint` joints instead of `Motor6D`. The docs name R15 only; the effect on R6
  rigs and weapon grips is **unverified**. See [[Weapon Attachment - Prop Bones and Motor6D]].
- **Version numbers** for your tools are reported in the handoff, not checked on your PC.

## 7. Practice plan (proposed, untested)

Four short sessions, each tied to an open arsenal item:

| Session | Card | Task | Feeds |
| --- | --- | --- | --- |
| 1 | [[Blender to Roblox Export Checklist]] | Export the C01 jian with the checklist, import into an empty Baseplate, compare its size in Studio with Blender | C01 Roblox import gate |
| 2 | [[Interpolation and Easing - Blender and Roblox]] | One 24-frame slash on the R6 rig, three interpolation versions, compare in the Graph Editor | Combat animation fundamentals |
| 3 | [[Weapon Attachment - Prop Bones and Motor6D]] | Add `Prop_Weapon` to a *copy* of the R6 rig, parent the jian to it, key a 3-key swing | Handoff open item 5 |
| 4 | [[PBR Textures for Roblox SurfaceAppearance]] | Pull iron, silver and brass values; make a tiny test bake and check the normal map's green channel | C01 material gate |

## 8. Deeper notes from this batch

- [[Blender to Roblox Export Checklist]]
- [[Interpolation and Easing - Blender and Roblox]]
- [[Weapon Attachment - Prop Bones and Motor6D]]
- [[PBR Textures for Roblox SurfaceAppearance]]

## 9. Continuation backlog (ranked, not started)

1. **R6 and `AvatarJointUpgrade`.** Find out whether the upgrade changes R6 characters or
   Motor6D weapon grips (creator-docs + the linked DevForum announcements). It decides how the
   Studio rig is built.
2. **Animation export path.** Compare Cautioned's plugin with your Eclipse bridge on Blender 5.2:
   first read its source for removed 5.0 APIs (static check), then propose a test that needs your
   approval to install.
3. **bpy for Blender 5.x card.** Slotted Actions, channelbags and the 5.0 migration helpers, so
   future scripts and agents stop using removed calls. The release-note sources are already found.
4. **Geometry Script trial plan.** Read the remaining book chapters, then propose one scabbard
   fitting built both ways (bpy and Geometry Script) as a comparison.
5. **Animation fundamentals outside GitHub.** A short curriculum from the Blender manual
   (Dope Sheet, Graph Editor, NLA) and Roblox animation docs, since GitHub had nothing strong.

## Sources

- Repository READMEs, licenses and files linked in the table and profiles (inspected 2026-11-08)
- Maintenance metadata: [repos.ecosyste.ms](https://repos.ecosyste.ms) (third-party index)
- [Blender 5.0 Python API release notes](https://developer.blender.org/docs/release_notes/5.0/python_api/)
- [Roblox AnimationConstraint reference](https://create.roblox.com/docs/reference/engine/classes/AnimationConstraint)
