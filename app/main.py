from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List
import uvicorn
from src.data_ingestion import fetch_all_sources
from src.agents.fusion_agent import FusionAgent
from src.agents.prediction_gnn import GNNPredictor
from src.agents.alert_xai import XAIAlertGenerator

app = FastAPI(
    title="SentinelNovaX - Disease Surveillance AI",
    description="MedFusion Hackfest 2026 - Round 1 Backend",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    disease: str
    region: str = "global"

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "project": "SentinelNovaX",
        "integrated_sources": 7,
        "timestamp": "2026-03-17T11:00:00Z"
    }

@app.get("/query")
async def query_disease(disease: str, region: str = "global"):
    try:
        # Fetch from 5+ mandatory sources
        raw_data = fetch_all_sources(disease, region)
        
        # AI Pipeline (Our differentiator)
        fusion = FusionAgent()
        fused_data = fusion.align_and_normalize(raw_data)
        
        gnn = GNNPredictor()
        forecast = gnn.predict_outbreak(fused_data)
        
        xai = XAIAlertGenerator()
        alert = xai.generate_explanation(forecast, fused_data)
        
        return {
            "project": "SentinelNovaX",
            "query": {"disease": disease, "region": region},
            "sources_used": list(raw_data.keys()),
            "fused_data": fused_data,
            "gnn_forecast": forecast,
            "xai_alert": alert,
            "risk_score": forecast.get("risk_score", 0.0)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
