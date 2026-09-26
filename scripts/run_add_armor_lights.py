from pathlib import Path
from isaacsim import SimulationApp

simulation_app = SimulationApp({
    "headless": True,
})

try:
    import runpy
    current_dir = Path(__file__).resolve().parent
    runpy.run_path(
        str(current_dir / "add_armor_lights.py"),
        run_name="__main__",
    )
finally:
    simulation_app.close()
