from pathlib import Path
import shutil

from pxr import Usd, UsdGeom, UsdLux, Gf


def add_lights(source_path: str, output_path: str, color: tuple[float, float, float]) -> None:
    source = Path(source_path)
    output = Path(output_path)

    if output.exists():
        raise FileExistsError(
            f"{output} 已存在。为防止覆盖手动灯光位置，请先备份或删除该派生文件。"
        )
    shutil.copy2(source, output)

    stage = Usd.Stage.Open(str(output))
    root = stage.GetDefaultPrim()

    if not root:
        roots = list(stage.GetPseudoRoot().GetChildren())
        if len(roots) != 1:
            raise RuntimeError(f"无法确定 USD 根节点: {roots}")
        root = roots[0]

    root_path = root.GetPath()

    bounds = UsdGeom.BBoxCache(
        Usd.TimeCode.Default(),
        [UsdGeom.Tokens.default_, UsdGeom.Tokens.render],
    ).ComputeLocalBound(root).ComputeAlignedRange()

    minimum = bounds.GetMin()
    maximum = bounds.GetMax()

    center_x = (minimum[0] + maximum[0]) / 2.0
    center_y = (minimum[1] + maximum[1]) / 2.0
    center_z = (minimum[2] + maximum[2]) / 2.0

    size_y = maximum[1] - minimum[1]
    size_z = maximum[2] - minimum[2]

    # 当前数字板局部 X 方向是板面法线方向。
    # 将灯放在正面，并分别靠近左右两侧。
    front_x = maximum[0] + 0.008

    for index, side in enumerate((-1.0, 1.0)):
        light_path = f"{root_path}/ArmorColorLight_{index}"
        light = UsdLux.SphereLight.Define(stage, light_path)

        light.CreateColorAttr(Gf.Vec3f(*color))
        light.CreateIntensityAttr(8000.0)
        light.CreateRadiusAttr(0.025)

        light_xform = UsdGeom.Xformable(light.GetPrim())
        light_xform.AddTranslateOp().Set(
            Gf.Vec3d(
                front_x,
                center_y + side * size_y * 0.38,
                center_z + size_z * 0.05,
            )
        )

    stage.SetDefaultPrim(root)
    stage.GetRootLayer().Save()
    print(f"saved: {output}")
    print(f"root: {root_path}")
    print(f"bounds: {minimum} -> {maximum}")


add_lights(
    "/home/matt/Documents/isaac/armor_module/R3.usd",
    "/home/matt/Documents/isaac/armor_module/R3_lit.usd",
    (1.0, 0.01, 0.01),
)

add_lights(
    "/home/matt/Documents/isaac/armor_module/B3.usd",
    "/home/matt/Documents/isaac/armor_module/B3_lit.usd",
    (0.01, 0.08, 1.0),
)
