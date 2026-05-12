from agent_learning_series.intent import IntentClassifier
from agent_learning_series.routing import route_tools
from agent_learning_series.memory.session_store import create_empty_session
from agent_learning_series.memory.agent import handle_user_message


def test_intent_classifier_inventory_query():
    result = IntentClassifier().classify("查詢 CB602 成品庫存")
    assert result.intent == "inventory_query"
    assert result.confidence >= 0.7


def test_routing_analysis_contains_kpi_tool():
    result = route_tools("幫我分析 CB602 庫存與出貨風險")
    tool_names = [t.name for t in result.selected_tools]
    assert "analyze_kpi" in tool_names
    assert "get_shipments" in tool_names


def test_memory_updates_material_and_summary():
    session = create_empty_session("test_user")
    session = handle_user_message(session, "請幫我查詢 CB602 今天庫存")
    wm = session["working_memory"]
    assert wm["current_material"] == "CB602"
    assert wm["last_time_reference"] == "today"
    assert "目前料號: CB602" in session["session_summary"]["summary"]
