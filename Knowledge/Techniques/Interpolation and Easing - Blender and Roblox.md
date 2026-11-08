---
type: knowledge
title: Interpolation and Easing - Blender and Roblox
domain: [animation]
tags: [easing]
tradition: n/a
part: n/a
author: claude
verified: false
status: draft
---
# Interpolation and easing in Blender and Roblox

## In one sentence
Keys set the poses; interpolation decides how the in-between frames are filled, and the shape
of that curve is what makes a sword swing feel heavy, snappy, floaty or robotic.

## Prerequisites
- Setting keyframes on the R6 rig in Pose mode; the Timeline and Dope Sheet.
- Knowing that a value (say, the arm's X rotation) can be drawn as a line over time.

## Why it works this way
In the Graph Editor each animated channel is an **F-Curve**: time runs left to right, the value
runs up and down. Reading one is the core skill:

- **Flat** = the value is not changing (a hold).
- **Steep** = the value changes fast (the strike).
- **Bending into flat** = slowing down (easing out of motion, a settle).
- **A bump past the next key** = overshoot. Sometimes wanted (follow-through), often a bug.

Speed, not pose, is what the eye reads as weight. Two animations with identical keys can feel
completely different because their curves differ.

## Key settings and numbers
**Blender** (Graph Editor; Blender 5.2 manual)

| Setting | Options | What it does |
| --- | --- | --- |
| Interpolation (T) | Constant, Linear, Bézier, plus Easing and Dynamic Effects presets | Constant holds then jumps (blocking); Linear keeps a steady speed; Bézier is smooth in value and speed (default) |
| Easing (Ctrl-E) | Automatic, Ease In, Ease Out, Ease In Out | For the Easing and Dynamic presets: In = starts slow, Out = ends slow |
| Handle type (V) | Automatic, Auto Clamped, Vector, Aligned, Free | Auto Clamped prevents overshoot between keys; Vector gives straight segments; Free allows a sharp change of direction |
| Handle Smoothing | None, Continuous Acceleration | The manual suggests Auto Clamped by default and Automatic only where overshoot is wanted |

**Roblox Studio** (Animation Editor and Curve Editor)

| Setting | Options | What it does |
| --- | --- | --- |
| Easing style | Linear, Constant, CubicV2, Elastic, Bounce | Per keyframe |
| Easing direction | In, Out, InOut | In = slow start, Out = slow end (same meaning as Blender) |
| Curve Editor tangents | handles per key; "Set Tangent to Zero" resets one | Same idea as Blender's handles |
| Rotation type | Euler angles or quaternions | Studio converts quaternions to Euler when you open the Curve Editor unless you choose quaternions first |

## Worked conceptual example (proposed, untested)
A one-handed horizontal slash at your usual 30 fps, keys on 3s:

| Frame | Pose |
| --- | --- |
| 0 | Ready |
| 9 | Wind-up (anticipation) |
| 12 | Contact |
| 15 | Follow-through, slightly past contact |
| 27 | Recover to ready |

- With every key on default Bézier + Auto Clamped, frames 9 → 12 ease out of the wind-up and
  into contact, so the fastest part of the swing lands between keys and the hit feels soft.
- Making the key at 9 leave fast (a steeper curve after 9, or Vector handles on the right side of
  key 9 and the left side of key 12, which straightens that segment) puts the speed into the strike. Leaving 15 → 27 eased gives a heavy settle.
- In the Graph Editor this shows as a long gentle rise, a near-vertical drop, then a slow
  flattening. That silhouette is the thing to recognise, not the exact numbers.

## Variations worth knowing
- **Blocking first:** set everything to Constant while posing, so you judge poses only; switch to
  Bézier once timing works. The manual calls Constant "normally only used during the initial
  blocking stage".
- **Dynamic effects** (Back, Bounce, Elastic) fake physics. Back with Ease Out overshoots then
  returns, close to a follow-through, but on a sword arm it usually reads as cartoonish.
- **Carrying curves to Roblox:** an exporter either converts Blender's curves to Roblox easing,
  or bakes a key on every frame. Baking preserves the look but makes the animation hard to edit
  in Studio. The Cautioned plugin README claims easing transfers "losslessly where possible";
  untested. How your Eclipse bridge handles it is not documented here yet.

## Common mistakes
- **Everything eased:** smooth in and out of every key makes combat floaty. Strikes need a fast
  section.
- **Automatic (unclamped) handles** overshooting, so the blade passes through the target or the
  wrist wobbles between two still poses.
- **Rotation flips:** large Euler rotations can spin the long way round. Roblox's Curve Editor has
  an Euler angles order setting; check rotation type before converting in Studio.
- **Judging motion only in the viewport.** The curve shows the problem before you can see it.

## Proposed exercise (untested)
On a copy of your R6 rig, key the slash above on the right arm only. Save three versions:
(1) all Constant, (2) all Bézier + Auto Clamped, (3) as (2) but Vector handles from 9 to 12.
Play each at full speed, then screenshot the arm's rotation curve for each. Write one line on
which hit feels strongest and what its curve looks like.

## Connection to Sword Arsenal
Every weapon class will need draws, slashes and resheathes. Weight is sold mostly by timing, so
heavier blades (E01 longsword) and lighter ones (C01 jian) can share poses but differ in curves.
This card is the fundamentals gap noted in your animation work: Graph Editor and interpolation
explain *why* a motion looks wrong.

## Sources
- Blender 5.2 manual: [F-Curve properties](https://docs.blender.org/manual/en/latest/editors/graph_editor/fcurves/properties.html)
  (interpolation, easing, handle types, handle smoothing) and
  [F-Curve editing](https://docs.blender.org/manual/en/latest/editors/graph_editor/fcurves/editing.html) (shortcuts T, Ctrl-E, V)
- Roblox creator-docs: [Animation Editor](https://create.roblox.com/docs/animation/editor) (easing style and direction) ·
  [Curve Editor](https://create.roblox.com/docs/animation/curve-editor) (tangents, rotation type) ·
  [source repo](https://github.com/Roblox/creator-docs)
- [Cautioned/Blender-Animations-Plugin README](https://github.com/Cautioned/Blender-Animations-Plugin) (easing-transfer claim)
- [AnimAide manual](https://aresdevo.github.io/animaide/) for curve-tool ideas (the add-on itself is likely incompatible with 5.x; see the research report)
- [[GitHub Learning Resources - Research]]
