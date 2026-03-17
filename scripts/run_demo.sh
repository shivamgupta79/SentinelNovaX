#!/bin/bash
echo "🚀 Launching SentinelNovaX..."
docker-compose up -d
sleep 15
echo "🌱 Seeding demo data..."
python scripts/seed_demo_data.py
echo ""
echo "✅ SentinelNovaX LIVE!"
echo "🔗 API Docs: http://localhost:8000/docs"
echo "🧪 Test Query:"
curl -s "http://localhost:8000/query?disease=dengue&region=hyderabad" | jq '.risk_score, .xai_alert'
