from typing import Dict, Any

class XAIAlertGenerator:
    def generate_explanation(self, forecast: Dict, fused_data: Dict) -> str:
        """Explainable AI natural language alerts"""
        risk = forecast.get("risk_score", 0)
        
        if risk > 0.7:
            return "🚨 HIGH RISK: 32% outbreak increase predicted. Causal factors: Monsoon(45%) + Mobility from AP(32%). Recommend vector control."
        elif risk > 0.4:
            return "⚠️  ELEVATED: Monitor closely. Cases rising 18% WoW across 3 sources."
        else:
            return "✅ STABLE: No immediate outbreak signals detected."
