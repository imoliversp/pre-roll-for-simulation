# 🎬 Maya CFX Pre-Roll Generator

Este repositorio contiene un script en Python para **Autodesk Maya** que crea de forma automática un **pre-roll** en escenas de **Character FX**. Es útil para simular dinámicas como cabello, ropa o músculos, dando tiempo a que se estabilicen antes de la animación principal.

---

## 🚀 Características

- 🔁 Crea fotogramas previos con keyframes "seguros" antes del inicio de la animación.
- 🧵 Ideal para simulaciones de **nCloth**, **nHair**, **XGen**, **Maya Fields**, etc.
- ⏱ Establece automáticamente el rango de tiempo del pre-roll.
- 🔒 Opcionalmente bloquea atributos para evitar cambios accidentales.
- 🧰 Compatible con Maya 2020 en adelante (puede funcionar en versiones anteriores).

---

## 🛠 Requisitos

- Autodesk Maya (2020+ recomendado)
- Python 2.7 o Python 3 (según versión de Maya)
- Acceso a Maya `cmds` y `OpenMaya` (incluidos por defecto)

---

## 📦 Instalación

1. Descarga o clona este repositorio:

```bash
git clone https://github.com/imoliversp/pre-roll-for-simulation?tab=readme-ov-file
