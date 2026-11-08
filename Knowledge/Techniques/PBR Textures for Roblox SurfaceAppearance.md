---
type: knowledge
title: PBR Textures for Roblox SurfaceAppearance
domain: [texturing, weapons]
tags: [pbr, baking, uv, colorway]
tradition: n/a
part: n/a
author: claude
verified: false
status: draft
---
# PBR textures for Roblox SurfaceAppearance

## In one sentence
Roblox shades a mesh from up to five texture maps on a `SurfaceAppearance`, and a weapon reads as
real steel, brass or lacquer only when each map holds the right kind of data in the format Roblox
expects.

## Prerequisites
- UV unwrapping basics (what a UV island and an atlas are).
- What a normal map does (fake surface detail by changing how light hits).
- Linear versus sRGB colour: the same colour can be written as two different sets of numbers.

## Why it works this way
PBR ("physically based rendering") splits a surface into separate properties: base colour, how
rough it is, whether it is metal, small bumps, and glow. Roblox uses the **metalness workflow**:
each pixel is either metal or non-metal, and metals take their reflection colour from the colour
map. That is why a steel blade is mostly "colour + metalness 1 + roughness", and why most painted
detail on metal belongs in roughness and normal maps rather than in colour.

## Key settings and numbers
| Item | Value | From |
| --- | --- | --- |
| Maps | Color (albedo), Normal, Roughness, Metalness, Emissive mask | Roblox PBR textures page |
| Color | RGB 24-bit; may carry alpha for the alpha modes below | Roblox texture specifications |
| Normal | RGB 24-bit, **OpenGL format, tangent space only**; flat = `[127, 127, 255]` | Same, and PBR page |
| Roughness, Metalness, Emissive | single-channel 8-bit greyscale | Roblox texture specifications |
| Metalness values | 0 or 100% in most cases | Roblox PBR page |
| UVs | one UV set, inside 0–1, overlaps allowed | Roblox texture specifications |
| Size guideline | 256×256 per 2×2×2-stud space; next size up if bigger | Same |
| Maximum size | the page states 4096×4096 in one section and 1024×1024 in its UV section | Same (internal conflict, flagged) |
| Alpha modes | Opaque, Overlay (default), Transparency, Tint mask | Roblox PBR page |
| Blender bake | Normal pass, Space = Tangent (manual: "the right choice in most cases"), Swizzle sets the axis per channel, Selected to Active bakes high-poly detail onto the low-poly | Blender manual, Baking |

**Measured metal values** (Physically Based dataset, CC0). The dataset gives linear sRGB; the
8-bit sRGB column is my conversion with the standard sRGB transfer function, values above 1
clamped. Unverified against a reference tool.

| Material | Linear sRGB (dataset) | 8-bit sRGB (converted) | Metalness |
| --- | --- | --- | --- |
| Iron | 0.530, 0.513, 0.494 | 192, 190, 187 | 1 |
| Stainless steel | 0.669, 0.639, 0.598 | 214, 209, 203 | 1 |
| Silver | 0.991, 0.985, 0.974 | 254, 253, 252 | 1 |
| Brass | 0.910, 0.778, 0.423 | 245, 228, 174 | 1 |
| Gold | 1.059, 0.773, 0.307 | 255, 228, 150 | 1 |
| Copper | 0.932, 0.623, 0.522 | 247, 207, 191 | 1 |

The dataset's roughness for these metals is 0 (clean polished reference). Real blade finishes need
roughness chosen deliberately; that is a design decision, not a measurement.

## Workflow
1. **UVs:** one atlas per mesh (Roblox allows one material per mesh), all islands inside 0–1.
2. **Bake detail** (ornament relief, the tested pipeline): Cycles, Bake Type Normal, Space
   Tangent, Selected to Active from the relief mesh onto the game mesh.
3. **Check the green channel.** OpenGL normal maps have green pointing "up" (+Y). Set Swizzle G
   to +Y before baking and confirm a raised ridge looks raised in Studio. If it looks dented,
   green is inverted. (OpenGL vs DirectX green direction is general graphics practice, not from
   the Roblox page.)
4. **Colour:** start metals from the table; paint variation into roughness first.
5. **Metalness:** pure black and white masks: blade and fittings 1, wrap, wood and lacquer 0.
6. In Studio, add a `SurfaceAppearance` to the MeshPart and assign the maps.

## Variations worth knowing
- **Tint mask** alpha mode tints the colour map by `SurfaceAppearance.Color` where alpha is
  opaque. This may suit the arsenal's **colorway** idea (one mesh, several colour schemes):
  alpha marks the cord or lacquer, the tint sets the colour. Untested.
- **Emissive mask** exists, but "glow or emissive effects by default" is on the [[Cliche List]];
  it needs a stated reason in the spec.

## Common mistakes
- Baking DirectX-style normals: detail lights from the wrong side.
- Using linear colour numbers directly as 8-bit PNG values: metals come out too dark.
- Lighting baked into the colour map (a "diffuse" map); the Roblox page separates albedo from
  older diffuse maps for this reason.
- Grey metalness (0.5) on steel: reads as plastic. Keep metalness binary unless there is a reason.
- Texture seams across a visible edge; the Roblox page warns normal maps accentuate seams.

## Proposed exercise (untested)
Make a 2×0.5×0.2-stud test bar. Bake a single raised line onto it at 256×256. Set colour to the
iron row above, metalness 1, roughness 0.35. Import into Studio. Record: does the line look raised,
and does iron read as metal under default lighting? Then flip Swizzle G and bake again to see the
mistake once, on purpose.

## Connection to Sword Arsenal
Covers the "materials" prototype gate and the "ornament through texture" direction in
[[Grounded Design Ideas]]. For a weapon about 4 studs long, the guideline suggests 512 maps; the
C01 jian uses a 1024 atlas, so keep 1024 only where close-up framing justifies it. Iron, silver
and brass values feed the jian rebuild's fittings.

## Sources
- Roblox creator-docs: [PBR textures](https://create.roblox.com/docs/art/modeling/surface-appearance) ·
  [Texture specifications](https://create.roblox.com/docs/art/modeling/texture-specifications) ·
  [source repo](https://github.com/Roblox/creator-docs)
- Blender 5.2 manual: [Baking](https://docs.blender.org/manual/en/latest/render/cycles/baking.html)
- [Physically Based API](https://github.com/AntonPalmqvist/physically-based-api), `deploy/v2/materials.json` (CC0; inspected 2026-11-08; Iron cites refractiveindex.info)
- [tinyrenderer: tangent-space normal mapping](https://haqr.eu/tinyrenderer/tangent/) for why tangent space is used
- [[Grounded Design Ideas]] · [[GitHub Learning Resources - Research]]
