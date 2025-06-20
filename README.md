# Maya CFX Pre-Roll Generator

This repository contains a Python script for **Autodesk Maya** that automatically creates a **pre-roll** for **Character FX** scenes. It is useful for simulating dynamics such as hair, cloth, or muscles, allowing the movement to settle before the main animation begins.

---

## Features

- If your character doesn't have Controllers, it uses the joints.
- If your character is rigged with Controllers, it uses those instead.
- If there is more than one object with Controllers in the scene, you can filter which ones will be affected. Just select the group which cointains the character you want to be affected.

---

## How Does It Work?

- The character is placed in its rest pose.
- Pre-roll keyframes are created before the start of the animation.
- The user defines the pre-roll time range.
- It gives you feedback of which Action is been taken.

---

## Requirements

- Autodesk Maya (2022+ recommended)
- Python 3

---

## Installation

1. Download or clone this repository:

```bash
git clone https://github.com/imoliversp/pre-roll-for-simulation?tab=readme-ov-file
```
---
If you find this script useful, feel free to tag me and share your experience. Your feedback is always appreciated!

Enquiries: oliversp_art@outlook.com