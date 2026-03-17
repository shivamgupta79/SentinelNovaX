from .disease_sh import fetch_disease_sh
from .who_odata import fetch_who_data
# Import other 5 sources...

def fetch_all_sources(disease: str, region: str = "global") -> dict:
    """Fetch from ALL 7 mandatory sources"""
    sources = {}
    
    # Parallel execution in production
    sources["disease_sh"] = fetch_disease_sh(disease, region)
    sources["who"] = fetch_who_data(disease, region)
    # ... add other 5
    
    return sources
