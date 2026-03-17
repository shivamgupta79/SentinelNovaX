import requests
from typing import Dict, Any

def fetch_disease_sh(disease: str, region: str = "global") -> Dict[str, Any]:
    """Real-time disease statistics - Mandatory source"""
    try:
        # COVID as proxy - adapt for other diseases
        url = "https://disease.sh/v3/covid-19/world"
        resp = requests.get(url, timeout=10)
        data = resp.json()
        return {
            "source": "disease.sh",
            "disease": disease,
            "region": region,
            "cases": data.get("cases", 0),
            "deaths": data.get("deaths", 0),
            "recovered": data.get("recovered", 0),
            "timestamp": data.get("updated")
        }
    except Exception as e:
        return {"source": "disease.sh", "error": str(e), "fallback": True}
