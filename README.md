# Maya CFX Pre-Roll Generator

This repository contains a Python script for **Autodesk Maya** that automatically creates a **pre-roll** for **Character FX** scenes. It is useful for simulating dynamics such as hair, cloth, or muscles, allowing the movement to settle before the main animation begins.🎬

---

## ⚙️ Features

🦴 If your character doesn't have Controllers, it uses the joints.

![](https://cdnb.artstation.com/p/assets/images/images/089/285/679/original/oliver-silva-p-case1-ezgif-com-optimize.gif?1750555591)
🎮 If your character is rigged with Controllers, it uses those instead.

![](https://cdnb.artstation.com/p/assets/images/images/089/285/681/original/oliver-silva-p-case2-ezgif-com-optimize.gif?1750555595)
🎯 If there is more than one object with Controllers in the scene, you can filter which ones will be affected. Just select the group which cointains the Controllers you want to be affected.

![](https://cdna.artstation.com/p/assets/images/images/089/285/682/original/oliver-silva-p-case3-ezgif-com-optimize.gif?1750555598)

---

## 🛠️ How Does It Work?

- 👤 The character is placed in its rest pose.
- ⌛ The user defines the pre-roll time range.
- 🎞️ Pre-roll keyframes are created before the start of the animation.
- ✅ It gives you feedback of which Action is been taken.

>Use the variable `preRoll` and change its value to the specific time you need of pre-roll.
>![](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/189bf827-1699-4f3c-b45e-509d0f35a0db/dk03sxd-d94107c4-2d03-4388-8cbf-f6f2b816bfa8.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzE4OWJmODI3LTE2OTktNGYzYy1iNDVlLTUwOWQwZjM1YTBkYlwvZGswM3N4ZC1kOTQxMDdjNC0yZDAzLTQzODgtOGNiZi1mNmYyYjgxNmJmYTguZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.9UHBJA1qrm0SuzwlyqitTQukqhmpYEPXAqSBy3OmHD8)
>Use the variable `clothDamp` and change its value to set how much time you need for the physics to be stabilized.

---

## 🖥️ Requirements

- Ⓜ️ Autodesk Maya (2022+ recommended)
- 🐍 Python 3

---

## Installation

1. 📦 Download or clone this repository:

```bash
git clone https://github.com/imoliversp/pre-roll-for-simulation
```
---

For more information, check the [Maya commands](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/) in the [Autodesk](https://www.autodesk.com/) official website.

- [cmds.getAttr()](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/getAttr.html)
- [cmds.setAttr()](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/setAttr.html)
- [cmds.setKeyframe()](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/setKeyframe.html)
- [cmds.ls()](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/ls.html)
- [cmds.select()](https://help.autodesk.com/cloudhelp/2025/ENU/Maya-Tech-Docs/CommandsPython/select.html)

---

If you find this script useful, feel free to tag me on [LinkedIn](https://www.linkedin.com/in/imoliversp/) and share your experience. Your feedback is always appreciated!

Enquiries: _oliversp_art@outlook.com_

![](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/189bf827-1699-4f3c-b45e-509d0f35a0db/djzff4z-8caa0f09-eaa1-426e-b75b-a39b5d6ab12b.png/v1/fill/w_1280,h_157/imoliversp_bottompage02_by_imoliversp_djzff4z-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTU3IiwicGF0aCI6IlwvZlwvMTg5YmY4MjctMTY5OS00ZjNjLWI0NWUtNTA5ZDBmMzVhMGRiXC9kanpmZjR6LThjYWEwZjA5LWVhYTEtNDI2ZS1iNzViLWEzOWI1ZDZhYjEyYi5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.5FQNLosaNVJKaflhlwctRL7FDIabX5bFlFKV7df-4lc)
---

###### <p align="center">Made with ❤️</p>