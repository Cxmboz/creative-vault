---
type: knowledge
title: Weapon Attachment - Prop Bones and Motor6D
domain: [animation, weapons]
tags: [rigging, roblox-import]
tradition: n/a
part: n/a
author: claude
verified: false
status: draft
---
# Weapon attachment: prop bones in Blender, Motor6D in Roblox

## In one sentence
Give the weapon its own bone in the rig and animate that bone, so the sword can follow the
hand, be adjusted on its own, and map one-to-one onto the animatable joint that holds it in
Roblox.

## Prerequisites
- Armatures, Pose mode, bone parenting.
- In Studio: what a Part, a Model and a joint are. Your existing katana setup
  (`KatanaHold` Motor6D, Right Arm → `Handle`) is the Roblox half of this.
- Out of scope here: IK/FK switching on the arm (set aside earlier at your request).

## Why it works this way
- **A prop bone is an extra joint.** Parenting the sword mesh straight to the hand bone welds it
  rigidly. A separate `Prop_Weapon` bone, child of the hand or arm bone, follows the hand by
  default (Blender bones inherit parent location, rotation and scale) but can also be keyed to
  twist the grip, slide the hand, or fly free during a throw.
- **Roblox works the same way.** A `Motor6D` joins two parts "in an animatable way"; its
  `Transform` is the per-frame offset an `Animator` writes. Your `KatanaHold` Motor6D is the
  Roblox twin of a Blender prop bone. Animation data for that joint is what moves the sword.
- **Changing what holds the sword** (scabbard on the left arm or hip, then the right hand after
  the draw) is a change of parent over time. Blender's *Child Of* constraint exists for this: its
  Influence can be keyed, "which makes it possible to switch to different parents over time".

## Key settings and numbers
| Item | Value or rule | From |
| --- | --- | --- |
| Bone inheritance | Child bones inherit parent location, rotation and scale; Inherit Rotation and Inherit Scale can be turned off per bone | Blender manual, bone Relations |
| Child Of: Set Inverse | Use when the child looks right with the constraint off but jumps when it is turned on | Blender manual, Child Of |
| Child Of: Influence | Animatable; two or more Child Of constraints can blend between parents | Same |
| Matching on a switch frame | "Copy Global Transform" is built into Blender since 5.0 (was an add-on) | Blender 5.0 release notes, Animation & Rigging |
| Motor6D | Part0 and Part1 joined; `Transform` set by an Animator or script | Roblox Motor6D reference |
| Avatar joints | With `StarterPlayer.AvatarJointUpgrade` on (default for new experiences), **R15** characters spawn with `AnimationConstraint` instead of Motor6D | Roblox Motor6D and AnimationConstraint reference |
| Roblox skinned rigs | at most 4 bone influences per vertex; bones exported at scale 1, rotation 0 | Roblox modeling specifications |

## Workflow (proposed, untested)
Blender, on a **copy** of `Blender R6.blend`. Two options; pick one per weapon setup.

**Option A: arm-parented (simplest; mirrors `KatanaHold`).**
1. In Edit mode on the armature, add bone `Prop_Weapon`. Place its head at the grip centre,
   matching the arsenal's sword origin (grip centre, blade along +Z). Parent it to the right arm
   bone, not connected.
2. Add `Prop_Scabbard` the same way under the left arm bone, its head at the scabbard mouth.
3. Parent the sword mesh to `Prop_Weapon` (bone parent) and the scabbard to `Prop_Scabbard`.
4. Animate the arm for the big motion and `Prop_Weapon` only for grip changes.

Limit: the sword can never leave the right arm, so a draw from a scabbard on the left side has
to be faked or handled in Roblox (a second joint enabled at the right moment, or a script changing
`Part0` at an animation event; both untested).

**Option B: constraint-parented (clean draws and hand switches in Blender).**
1. Parent `Prop_Weapon` to the rig's root bone instead of the arm, so no arm motion is inherited
   twice.
2. Add two Child Of constraints to it: one targeting `Prop_Scabbard`, one targeting the right arm
   bone.
3. On the frame before the hand closes, key Influence scabbard = 1, hand = 0. On the next frame,
   key scabbard = 0, hand = 1.
4. If the sword jumps on the switch, use Set Inverse on the constraint that takes over, or Copy
   Global Transform to keep its world position.

Trade-off: in Roblox, the matching joint would hang off the torso or root part rather than the
arm, and the exporter has to bake the sword's resulting motion. Whether Eclipse or a plugin does
that cleanly is unknown (research backlog item 2).

**Either option:** keep bone names identical to what the Roblox side expects. How your exporter
maps bone names to Motor6D or part names must be checked before names are final.

## Variations worth knowing
- **Armature constraint** instead of several Child Ofs: the Blender manual suggests it when the
  parents are all bones.
- **Weld instead of Motor6D** in Roblox: fine for a sword that never moves relative to the hand,
  but then the grip cannot be animated.

## Common mistakes
- Parenting the mesh directly to the hand bone, then fighting it to adjust the grip.
- Adding Child Of constraints to a bone that is still parented to the arm: the arm's motion
  is applied on top of the constraint's.
- Switching Child Of influence over several frames: the sword drifts between two parents.
- Scaling the prop bone: Roblox expects bones at scale 1.
- Assuming character joints are Motor6Ds in scripts. On upgraded R15 characters they are not;
  the docs warn that `FindFirstChildOfClass("Motor6D")` will find nothing.

## Open question (flagged)
The joint-upgrade docs name **R15** characters only. Whether it changes **R6** characters, or a
Motor6D you add yourself for a weapon, is not stated in the pages read. Your rig is R6, so this is
backlog item 1 in the research report.

## Proposed exercise (untested)
Do Option A steps 1 and 3 on a rig copy with the jian. Key a 3-key swing on the arm only, then add one key
that rotates `Prop_Weapon` 20° at the swing's end. Check that the sword follows the arm and that
the extra key adds a wrist flick without touching the arm.

## Connection to Sword Arsenal
This is handoff open item 5 ("Add the `Prop_Weapon` / `Prop_Scabbard` socket bones") and the
"rig swap test" prototype gate: every weapon with the same origin convention should drop onto the
same prop bone. It also underpins the planned Rimuru-inspired draw.

## Sources
- Blender 5.2 manual: [Child Of constraint](https://docs.blender.org/manual/en/latest/animation/constraints/relationship/child_of.html) ·
  [Bone relations](https://docs.blender.org/manual/en/latest/animation/armatures/bones/properties/relations.html)
- [Blender 5.0 release notes, Animation & Rigging](https://developer.blender.org/docs/release_notes/5.0/animation_rigging/) (Copy Global Transform built in)
- Roblox creator-docs: [Motor6D](https://create.roblox.com/docs/reference/engine/classes/Motor6D) ·
  [AnimationConstraint](https://create.roblox.com/docs/reference/engine/classes/AnimationConstraint) ·
  [modeling specifications](https://create.roblox.com/docs/art/modeling/specifications) ·
  [source repo](https://github.com/Roblox/creator-docs)
- [[Handoff - 2026-11-08]] · [[GitHub Learning Resources - Research]]
