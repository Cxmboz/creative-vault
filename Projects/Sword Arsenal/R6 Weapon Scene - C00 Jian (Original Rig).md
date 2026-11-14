---
type: project
title: R6 Weapon Scene - C00 Jian (Original Rig)
domain: [animation, weapons]
tags: [rigging, roblox-import]
author: claude
verified: false
status: active
---
# R6 Weapon Scene - C00 Jian (Original Rig)

Goal: a ready-to-animate Blender scene with the C00 jian and its scabbard on a fresh copy of the
original R6 rig. The owner animates; nothing creative was added.

## Links
- Part of [[Sword Arsenal]].
- Method background: [[Weapon Attachment - Prop Bones and Motor6D]] · [[Blender to Roblox Export Checklist]]
- Deliverables (on the owner's PC, not in Git): `Downloads\Animation\Sword_Model\C00_R6_OriginalRig_Scene_2026-11-14\`
  - `C00_Jian_R6.blend` is the animator scene.
  - `README.md` has the controls and the switching procedure.
  - `Test_Report.md` has the checks.
  - `MANUAL_STEPS.md` has the Studio check and the untested items.
  - `SOURCE_HASHES.txt` has the hashes.

## What was built (observed in this session)
- Source: `Downloads\Animation\Blender R6.blend`, SHA-256 `bc6742db...760b0`, copied, never written to. The task note gives `Downloads\Blender R6.blend`; no file exists at that path.
- Controls: `Sword_Control` (child of `RightArm_Positioner`) and `Scabbard_Control` with a **Follow Space** property (0 Sword, 1 Left Arm, 2 Rig). The switch is one Armature constraint on a hidden helper bone, driven by simple-expression drivers (no Python needed).
- Export layer: `Handle` and `Scabbard` bones on `InternalArmature` copy the controls' world transforms. Sword and scabbard stay separate meshes. Tassel and cord are children of their meshes.
- Switching without a pop: key F-1, Copy Global Transform at F, change Follow Space, Paste, set the F-1 keys to Constant.
- The rig runs at 60 fps. The 2026-11-08 substitute scene said 24 fps. The frame rate was not changed.

## Validation (Blender 5.2.2 headless)
- 33 of 33 technical checks passed: carry, offset, switching at three frames, no pop, no double transform, no scaling, no dependency cycle, reopen, packed textures.
- Not tested: Roblox export and Studio playback, IK mode (a probe was inconclusive), the real Copy/Paste buttons, the file with the rig's scripts allowed.

## Decisions
| Date | Decision |
| --- | --- |
| 2026-11-14 | Built on the original rig copy rather than the substitute; the same build script as 2026-11-08 was reused after inspecting the original |
| 2026-11-14 | Bone names `Handle` / `Scabbard` kept for the export layer; `Prop_Weapon` / `Prop_Scabbard` (design doc) left as an owner decision |
