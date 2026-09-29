# RoboMaster Armor Module USD Models

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![USD Format](https://img.shields.io/badge/Format-USD%20%2F%20USDA%2FUSDC-blue)](https://openusd.org/)
[![Platform: Isaac Sim](https://img.shields.io/badge/Platform-Isaac%20Sim-orange)](https://developer.nvidia.com/isaac-sim)

This repository provides high-fidelity **Universal Scene Description (USD)** assets, CAD files, sticker/texture references, and generation scripts for **RoboMaster** armor modules (both small and large armor plates, outpost, and base models) based on official RoboMaster 2026 `.STEP` files and mechanical design diagrams.

Designed specifically for robotic simulation frameworks such as **NVIDIA Isaac Sim**, this package allows developers to easily integrate realistic RoboMaster competition environments and vision targets.

---

## Repository Structure

```text
armor_module/
├── CAD/
│   ├── AM02.STEP          # Small armor module CAD STEP file
│   ├── AM02.obj           # Small armor module OBJ mesh
│   ├── AM12.STEP          # Large armor module CAD STEP file
│   └── AM12.obj           # Large armor module OBJ mesh
├── USD/
│   ├── AM02.usd           # Small armor module base USD
│   ├── AM12.usd           # Large armor module base USD
│   ├── R1.usd / B1.usd    # Red/Blue armor USD (e.g., number 1, etc.)
│   ├── R1_lit.usd ...     # Red/Blue armor USD with pre-configured self-illumination / lighting
│   └── *_lit.usd          # Outpost and base USD assets with lighting/markers
├── image/
│   ├── 1.png - 4.png      # Armor number decals (1, 2, 3, 4)
│   ├── Base_large.png     # Large base armor graphic
│   ├── Base_small.png     # Small base armor graphic
│   ├── Outpost.png        # Outpost target graphic
│   └── Sentry.png         # Sentry armor / decal graphic
└── scripts/
    ├── add_armor_lights.py      # Python script utilizing OpenUSD & pxr to compute bounds & add illumination lights
    └── run_add_armor_lights.py  # Isaac Sim launcher script for batch light/shader generation
```

---

## Features & Assets

- **CAD Models (`CAD/`)**: Original STEP and exported OBJ meshes (`AM02` for small armor modules, `AM12` for large armor modules) derived from RoboMaster 2026 mechanical data.
- **USD Assets (`USD/`)**: Ready-to-use USD stages for Red (`R`) and Blue (`B`) teams across multiple robot types:
  - **Armor Plates**: `R1`, `B1`, etc., with corresponding lit variants (`R1_lit`, `B1_lit`, etc.) featuring embedded sphere lights and material highlights.
  - **Bases & Outposts**: `RBase_large_lit`, `BBase_small_lit`, `ROutpost_lit`, `BOutpost_lit`, etc., for simulation target scoring and perception tests.
- **Visual Textures (`image/`)**: Official competition number markers (`1.png` through `4.png`) and target decals (`Outpost.png`, `Base_small.png`, `Base_large.png`, `Sentry.png`) used for visual pattern recognition and armor classification training.
- **Automation Scripts (`scripts/`)**: Python utility using OpenUSD (`pxr`) and NVIDIA Isaac Sim (`SimulationApp`) to automatically compute bounding boxes of imported geometries and place directional/sphere illumination lights (`SphereLight`) precisely onto the armor faceplates.

---

## Usage & Integration

### 1. Loading in NVIDIA Isaac Sim / Omniverse
You can directly reference or open any `.usd` file from the `USD/` directory in Isaac Sim:
```python
from omniverse.isaac.core.utils.stage import add_reference_to_stage

# Example: Load Red 1 Lit Armor Module
asset_path = "/path/to/armor_module/USD/R1_lit.usd"
add_reference_to_stage(asset_path, "/World/R1_Armor")
```

### 2. Regenerating / Adding Illumination Lights
To batch-process USD assets and inject armor status lights using the helper script inside Isaac Sim:
```bash
python scripts/run_add_armor_lights.py
```

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
