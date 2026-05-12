from __future__ import annotations

from typing import Any


MOCK_FG = {
    "CB602": {"material_code": "CB602", "quantity": 120, "uom": "PCS"},
    "AX100": {"material_code": "AX100", "quantity": 35, "uom": "PCS"},
}

MOCK_RM = {
    "CB602": {"material_code": "CB602", "quantity": 80, "uom": "KG"},
    "AX100": {"material_code": "AX100", "quantity": 41, "uom": "KG"},
}


def get_mes_finished_goods_inventory(material_code: str) -> dict[str, Any]:
    data = MOCK_FG.get(material_code)
    if not data:
        raise ValueError(f"No finished goods data for material_code={material_code}")
    return data


def get_raw_material_inventory(material_code: str) -> dict[str, Any]:
    data = MOCK_RM.get(material_code)
    if not data:
        raise ValueError(f"No raw material data for material_code={material_code}")
    return data


def compare_inventory(step_outputs: dict[int, dict[str, Any]]) -> dict[str, Any]:
    fg = step_outputs[1]
    rm = step_outputs[2]
    gap = fg["quantity"] - rm["quantity"]
    status = "ok" if gap >= 0 else "shortage"
    return {
        "finished_goods_qty": fg["quantity"],
        "raw_material_qty": rm["quantity"],
        "gap": gap,
        "status": status,
    }
