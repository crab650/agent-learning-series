from dataclasses import dataclass
from typing import List


@dataclass
class SelectedTool:
    name: str
    reason: str


@dataclass
class RouteResult:
    intent: str
    selected_tools: List[SelectedTool]


def detect_intent(query: str) -> str:
    q = query.lower()
    if any(word in q for word in ["分析", "風險", "趨勢", "異常", "kpi"]):
        return "analysis"
    if "成品" in q and "庫存" in q:
        return "finished_goods_inventory"
    if "原料" in q and "庫存" in q:
        return "raw_material_inventory"
    if any(word in q for word in ["規格", "物料主檔", "包裝", "status"]):
        return "material_lookup"
    if any(word in q for word in ["出貨", "shipment", "交期"]):
        return "shipment_lookup"
    return "general_query"


def route_tools(query: str) -> RouteResult:
    intent = detect_intent(query)
    selected = []

    if intent == "finished_goods_inventory":
        selected.append(SelectedTool(name="get_mes_finished_goods_inventory", reason="使用者明確查詢成品庫存"))
    elif intent == "raw_material_inventory":
        selected.append(SelectedTool(name="get_raw_material_inventory", reason="使用者明確查詢原料庫存"))
    elif intent == "material_lookup":
        selected.append(SelectedTool(name="get_material_master", reason="使用者明確查詢物料規格或主檔資訊"))
    elif intent == "shipment_lookup":
        selected.append(SelectedTool(name="get_shipments", reason="使用者明確查詢出貨或交期資訊"))
    elif intent == "analysis":
        q = query.lower()
        if "庫存" in q and "成品" in q:
            selected.append(SelectedTool(name="get_mes_finished_goods_inventory", reason="分析前需要成品庫存資料"))
        if "庫存" in q and "原料" in q:
            selected.append(SelectedTool(name="get_raw_material_inventory", reason="分析前需要原料庫存資料"))
        if any(word in q for word in ["出貨", "shipment", "交期"]):
            selected.append(SelectedTool(name="get_shipments", reason="分析前需要出貨資料"))
        selected.append(SelectedTool(name="analyze_kpi", reason="使用者要求分析、風險或趨勢判斷"))

    return RouteResult(intent=intent, selected_tools=selected)
