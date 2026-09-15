from isaacsim import SimulationApp

simulation_app = SimulationApp({
    "headless": True,
})

try:
    import runpy

    runpy.run_path(
        "/home/matt/Documents/isaac/armor_module/add_armor_lights.py",
        run_name="__main__",
    )
finally:
    simulation_app.close()