---
type: knowledge
title: Blender to Roblox Export Checklist
domain: [modeling, weapons]
tags: [roblox-import]
tradition: n/a
part: n/a
author: claude
verified: false
status: draft
---
# Blender to Roblox export checklist

## In one sentence
A weapon arrives in Studio at the right size and facing the right way only when Blender's
units, the exporter's scale and axis options, and Studio's importer all agree, and the mesh
already meets Roblox's geometry rules.

## Prerequisites
- Exporting a file from Blender; selecting objects; Object vs Edit mode.
- What a stud is (Roblox's length unit).

## Why it works this way
- **Different "up".** Blender treats Z as up; Studio treats Y as up. The exporter and importer
  both have axis settings so the model is turned once, not twice.
- **Different units.** Blender defaults to metres; Studio uses studs. Setting Blender's Unit
  System to None makes 1 Blender unit read as a plain number, which the arsenal standard maps to
  1 stud. The FBX format then adds its own unit scale, which is why Roblox warns that default
  FBX exports import "at an unexpectedly large scale". One of its alternative fixes is an export
  scale of 0.01, which implies the error is about 100 times.
- **Studio is strict about meshes** because it renders and collides with them in real time:
  one material per mesh, no holes, a triangle cap.

## Key settings and numbers
| Setting or rule | Value | From |
| --- | --- | --- |
| Scene ‣ Units ‣ Unit System | None | Roblox Blender page, "Configure units" |
| Scene ‣ Units ‣ Rotation | Degrees | Same |
| FBX ‣ Transform ‣ Apply Scalings | FBX Unit Scale (recommended; other scale values left at 1.0) | Roblox Blender page, "Adjust scale (FBX)" |
| Export ‣ Forward / Up | Z Forward / Y Up | Roblox Blender page, "Export settings" |
| Export ‣ Include | Limit to Selected Objects | Same |
| FBX ‣ Path Mode | Copy, with Embed Textures on | Roblox export settings page |
| FBX ‣ Armature ‣ Add Leaf Bones | Off | Same |
| FBX ‣ Bake Animation | Off, unless the file carries animation | Same |
| Studio importer | World Forward = Front, World Up = Top, Scale Unit = Stud, Insert Using Scene Position on | Roblox Blender page, "Blender to Studio" |
| Triangles per mesh | at most 20,000 | Roblox modeling specifications |
| Geometry | watertight, quads where possible (no n-gons), never zero thickness | Same |
| Materials | one per mesh | Roblox texture specifications |
| Skinned meshes | bones at scale 1 and rotation 0, root at 0,0,0, at most 4 bone influences per vertex, no influence on the root | Roblox modeling specifications |
| Animation in an FBX | one animation track per file | Same |

## Workflow
1. Check the scene: Unit System None, Rotation Degrees.
2. Check the mesh: triangle count (Viewport Overlays ‣ Statistics), no n-gons, no open edges,
   one material slot, transforms applied.
3. Select only what goes into the file (for example `Sword` or `Scabbard`).
4. Export FBX with the settings in the table.
5. In Studio, import with the importer settings in the table.
6. Measure in Studio. A 4-stud sword should read about 4 studs. If it is far larger (around
   100 times, by the reasoning above), the FBX scale step was missed.

## Variations worth knowing
- **glTF instead of FBX.** The Roblox Blender page notes Studio also imports glTF, which does
  not need the FBX scaling settings. Not tested in our pipeline.
- **Two other scale fixes** exist (export Scale 0.01, or scene Unit Scale 0.01). The Roblox page
  warns the second can cause camera and other issues in Blender. The arsenal uses the
  recommended one.
- **Avatar items** (accessories, bodies) have their own, stricter specifications. Weapons
  used as game models follow the general ones above.

## Common mistakes
- Exporting the whole scene, including the rig, lights or reference planes.
- Leaving *Add Leaf Bones* on: extra `_end` bones appear in Studio.
- Fixing a size problem by scaling the model in Studio, which breaks the 1 unit = 1 stud match
  the animation rig relies on.
- Trusting older tutorials: the Roblox page itself says many guides use inconsistent scale
  settings.

## Proposed exercise (untested)
Export the C01 jian (`Sword_Model\Jian_Sword_Roblox.blend`) with this checklist into a test
folder, import into an empty Baseplate, and record three numbers: length in Blender, length in
Studio, triangle count. Then try a glTF export of the same object and note any difference.

## Connection to Sword Arsenal
The handoff standards (1 Blender unit = 1 stud, Unit System None, FBX Unit Scale, root parts
named `Handle` / `Scabbard`) agree with Roblox's docs. The arsenal budgets (4k triangles, 8k for
signature weapons) sit well under the 20,000 cap, and the one-material rule is why each weapon
uses a single texture atlas. This card is the checklist for the prototype gate "Roblox import".

## Sources
- Roblox creator-docs, Blender page: [rendered](https://create.roblox.com/docs/art/blender) ·
  [source](https://github.com/Roblox/creator-docs/blob/main/content/en-us/art/blender.md)
- [Export settings](https://create.roblox.com/docs/art/modeling/export-requirements)
- [General modeling specifications](https://create.roblox.com/docs/art/modeling/specifications)
- [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications)
- [[GitHub Learning Resources - Research]] · [[Handoff - 2026-11-08]]
