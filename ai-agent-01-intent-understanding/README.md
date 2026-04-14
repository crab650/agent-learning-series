專案目的

This project demonstrates the first layer of an AI agent pipeline: 
	understanding user intent before tool routing or task planning.

支援 intents
inventory_query
shipment_query
kpi_analysis
material_lookup
greeting
help
unknown

架構

User Query
   ↓
Normalization
   ↓
Rule-based Intent Classification
   ↓
Structured Intent Output



範例

Input:

查詢 CB602 成品庫存

Output:

{
  "query": "查詢 CB602 成品庫存",
  "intent": "inventory_query",
  "confidence": 0.9,
  "matched_by": "rule",
  "reason": "matched keywords: ['庫存', '成品']"
}


未來擴充
regex-based entity extraction
LLM fallback classification
confidence threshold
multilingual support