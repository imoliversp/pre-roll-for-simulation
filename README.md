![preCFX_thumbnail](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/189bf827-1699-4f3c-b45e-509d0f35a0db/dk05hzn-1ea19cf0-d6fc-4549-9d31-1e2e9210b339.png/v1/fill/w_1280,h_334/precfx_thumbnail_by_imoliversp_dk05hzn-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MzM0IiwicGF0aCI6IlwvZlwvMTg5YmY4MjctMTY5OS00ZjNjLWI0NWUtNTA5ZDBmMzVhMGRiXC9kazA1aHpuLTFlYTE5Y2YwLWQ2ZmMtNDU0OS05ZDMxLTFlMmU5MjEwYjMzOS5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.AOBOttAE1s4VmkRqu1r5j2z_pdFjUvSPkAxDP2PUhq8)

# Maya CFX Pre-Roll Generator

This repository contains a Python script for **Autodesk Maya** that automatically creates a **pre-roll** for **Character FX** scenes. It is useful for simulating dynamics such as hair, cloth, or muscles, allowing the movement to settle before the main animation begins.🎬

---

## ⚙️ Features

🦴 If your character doesn't have Controllers, it uses the joints.

![preroll w jnt](https://www.deviantart.com/stash/0pqwrwh9xi9)

🎮 If your character is rigged with Controllers, it uses those instead.

![preroll w ctrl 01](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/189bf827-1699-4f3c-b45e-509d0f35a0db/dk05jmj-ab9dab99-a0b9-47b5-8b4a-0bd48e091eb5.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzE4OWJmODI3LTE2OTktNGYzYy1iNDVlLTUwOWQwZjM1YTBkYlwvZGswNWptai1hYjlkYWI5OS1hMGI5LTQ3YjUtOGI0YS0wYmQ0OGUwOTFlYjUuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.7p_RsZJd67Os5CgO4quKZ2hVzapyIweufelSEcEPzzE)

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
8. Edit Icon --> Icon Name --> Select the icon from the folder.
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

![imoliversp](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/189bf827-1699-4f3c-b45e-509d0f35a0db/dk05jdb-a5dcae78-fe61-449a-b2e4-85110febccb4.png/v1/fill/w_1280,h_157/imoliversp_bottompage_by_imoliversp_dk05jdb-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTU3IiwicGF0aCI6IlwvZlwvMTg5YmY4MjctMTY5OS00ZjNjLWI0NWUtNTA5ZDBmMzVhMGRiXC9kazA1amRiLWE1ZGNhZTc4LWZlNjEtNDQ5YS1iMmU0LTg1MTEwZmViY2NiNC5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.WTb_Rzw80ZbYve9sV5sjIPr4r_G3hc46b9OLkyYazG0)