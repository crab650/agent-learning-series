from dataclasses import dataclass
from typing import List


@dataclass
class ToolSpec:
    name: str
    description: str
    keywords: List[str]


TOOLS = [
    ToolSpec(
        name="get_mes_finished_goods_inventory",
        description="Query MES finished goods inventory by material code. Return available stock quantity, warehouse, and storage location for finished products.",
        keywords=["成品", "成品庫存", "finished goods", "庫存"]
    ),
    ToolSpec(
        name="get_raw_material_inventory",
        description="Query raw material inventory by material code. Return available raw material stock quantity, warehouse, and bin location.",
        keywords=["原料", "原料庫存", "raw material", "庫存"]
    ),
    ToolSpec(
        name="get_material_master",
        description="Query material master data by material code. Return specification, package type, product family, and status.",
        keywords=["規格", "物料主檔", "包裝", "產品別", "status"]
    ),
    ToolSpec(
        name="get_shipments",
        description="Query shipment schedule, delivery status, and outgoing quantities by material code.",
        keywords=["出貨", "shipment", "delivery", "交期"]
    ),
    ToolSpec(
        name="analyze_kpi",
        description="Analyze inventory, shipment, and operational KPIs to identify trends, risks, and anomalies.",
        keywords=["分析", "趨勢", "風險", "異常", "KPI"]
    )
]