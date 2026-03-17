## SentinelNovaX API

**GET /query?disease={disease}&region={region}**

**Response:**
```json
{
  "project": "SentinelNovaX",
  "sources_used": ["disease.sh", "WHO", "CDC"],
  "risk_score": 0.78,
  "gnn_forecast": {...},
  "xai_alert": "🚨 HIGH RISK..."
}
