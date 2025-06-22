# Maya CFX Pre-Roll Generator

This repository contains a Python script for **Autodesk Maya** that automatically creates a **pre-roll** for **Character FX** scenes. It is useful for simulating dynamics such as hair, cloth, or muscles, allowing the movement to settle before the main animation begins.🎬

---

## ⚙️ Features

🦴 If your character doesn't have Controllers, it uses the joints.

![preroll w jnt](https://github.com/imoliversp/pre-roll-for-simulation/blob/main/mediaContent/preroll_jnts.gif?raw=true)

🎮 If your character is rigged with Controllers, it uses those instead.

![preroll w ctrl 01](https://github.com/imoliversp/pre-roll-for-simulation/blob/main/mediaContent/preroll_ctrl.gif?raw=true)

🎯 If there is more than one object with Controllers in the scene, you can filter which ones will be affected. Just select the group which cointains the Controllers you want to be affected.

![preroll w ctrl 02](https://github.com/imoliversp/pre-roll-for-simulation/blob/main/mediaContent/preroll_filter_ctrl.gif?raw=true)

---

## 🛠️ How Does It Work?

- 👤 The character is placed in its rest pose.
- ⌛ The user defines the pre-roll time range.
- 🎞️ Pre-roll keyframes are created before the start of the animation.
- ✅ It gives you feedback of which Action is been taken.

Use the variable `preRoll` and change its value to the specific time you need of pre-roll.

![variables](https://github.com/imoliversp/pre-roll-for-simulation/blob/main/mediaContent/variables.gif?raw=true)

Use the variable `clothDamp` and change its value to set how much time you need for the physics to be stabilized.

>**Note**  
> If your transformation attributes (translate, rotate, scale) are locked. Their locked state will remain unchanged.

---

## 🖥️ Requirements

- Ⓜ️ Autodesk Maya (2022+ recommended)
- 🐍 Python 3

---

## 📦 Installation

1. Download or clone this repository:

```bash
git clone https://github.com/imoliversp/pre-roll-for-simulation
```
2. Locate your Maya user scripts folder  
- Windows:
```C:\Users\<YourUsername>\Documents\maya\<version>\scripts ```  
- macOS:
```/Users/<YourUsername>/Library/Preferences/Autodesk/maya/<version>/scripts```  
- Linux:
```/home/<YourUsername>/maya/<version>/scripts```
3. Copy `preroll_CFX/py` into that folder.
4. Restart Maya.
5. Import it in the Script Editor

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

![imoliversp](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/189bf827-1699-4f3c-b45e-509d0f35a0db/djzff4z-8caa0f09-eaa1-426e-b75b-a39b5d6ab12b.png/v1/fill/w_1280,h_157/imoliversp_bottompage02_by_imoliversp_djzff4z-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTU3IiwicGF0aCI6IlwvZlwvMTg5YmY4MjctMTY5OS00ZjNjLWI0NWUtNTA5ZDBmMzVhMGRiXC9kanpmZjR6LThjYWEwZjA5LWVhYTEtNDI2ZS1iNzViLWEzOWI1ZDZhYjEyYi5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.5FQNLosaNVJKaflhlwctRL7FDIabX5bFlFKV7df-4lc)