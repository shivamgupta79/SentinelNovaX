from pydantic import BaseModel
from typing import Dict, List, Optional
from datetime import datetime

class DiseaseData(BaseModel):
    source: str
    cases: Optional[int] = None
    deaths: Optional[int] = None
    trend: Optional[str] = None
    alerts: Optional[List[str]] = None
    timestamp: datetime

class QueryResponse(BaseModel):
    project: str
    query: Dict[str, str]
    sources_used: List[str]
    fused_data: Dict[str, DiseaseData]
    gnn_forecast: Dict[str, float]
    xai_alert: str
    risk_score: float
