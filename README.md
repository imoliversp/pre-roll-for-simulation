![preCFX_thumbnail](https://github.com/imoliversp/contentMedia/blob/main/pre-roll-for-simulation/preCFX_thumbnail.png?raw=true)

# Maya CFX Pre-Roll Generator

This repository contains a Python script for **Autodesk Maya** that automatically creates a **pre-roll** for **Character FX** scenes. It is useful for simulating dynamics such as hair, cloth, or muscles, allowing the movement to settle before the main animation begins.🎬

---

## ⚙️ Features

🦴 If your character doesn't have Controllers, it uses the joints.

![preroll w jnt](https://github.com/imoliversp/contentMedia/blob/main/pre-roll-for-simulation/preroll_jnts.gif?raw=true)

🎮 If your character is rigged with Controllers, it uses those instead.

![preroll w ctrl 01](https://github.com/imoliversp/contentMedia/blob/main/pre-roll-for-simulation/preroll_ctrl.gif?raw=true)

🎯 If there is more than one object with Controllers in the scene, you can filter which ones will be affected. Just select the group which cointains the Controllers you want to be affected.

![preroll w ctrl 02](https://github.com/imoliversp/contentMedia/blob/main/pre-roll-for-simulation/preroll_filter_ctrl.gif?raw=true)

---

## 🛠️ How Does It Work?

- 👤 The character is placed in its rest pose.
- ⌛ The user defines the pre-roll time range.
- 🎞️ Pre-roll keyframes are created before the start of the animation.
- ✅ It gives you feedback of which Action is been taken.

Use the variable `preRoll` and change its value to the specific time you need of pre-roll.

![variables](https://github.com/imoliversp/contentMedia/blob/main/pre-roll-for-simulation/variables.gif?raw=true)

Use the variable `clothDamp` and change its value to set how much time you need for the physics to be settled.

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
2. Locate your Maya user _scripts_ folder:  
- Windows:
```C:\Users\<YourUsername>\Documents\maya\<version>\scripts ```  
- macOS:
```/Users/<YourUsername>/Library/Preferences/Autodesk/maya/<version>/scripts```  
- Linux:
```/home/<YourUsername>/maya/<version>/scripts```
3. Copy `preroll_CFX.py` into that folder.
4. Restart Maya.
5. Import it in the Script Editor.  

Optional steps:

6. Place the `preroll_CFX.png` in the _icons_ folder:
- Windows:
```C:\Users\<YourUsername>\Documents\maya\<version>\prefs\icons ```  
- macOS:
```/Users/<YourUsername>/Library/Preferences/Autodesk/maya/<version>/prefs/icons```  
- Linux:
```/home/<YourUsername>/maya/<version>/prefs/icons```
7. Add the script to the Shelf.
8. Edit Icon --> Icon Name --> Select the icon from the _icons_ folder.

>**Note**  
> You can delete the _mediaContent_ folder, as it's only for repository previews.
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

![imoliversp](https://github.com/imoliversp/contentMedia/blob/main/thumbnails/BottomPage2.png?raw=true)