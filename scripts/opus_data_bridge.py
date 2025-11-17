"""
MOBILE-FRIENDLY Opus Data Bridge
Run this on your phone to generate data for Oduobuk
"""

import json
import random
from datetime import datetime, timedelta

def generate_sample_tickets(num_tickets=5):
    """Generate sample support tickets for Opus testing"""
    customers = ["John Smith", "Sarah Johnson", "Mike Chen", "Emily Davis", "Alex Wong"]
    issues = [
        "Cannot login to account - password reset not working",
        "Mobile app crashing on iOS",
        "Double charged for subscription", 
        "Need refund for canceled service",
        "Feature request: dark mode"
    ]
    
    tickets = []
    for i in range(num_tickets):
        ticket = {
            "ticket_id": f"TKT{1000 + i}",
            "customer_name": random.choice(customers),
            "customer_email": f"user{i}@example.com",
            "issue_description": random.choice(issues),
            "category": random.choice(["technical", "billing", "general"]),
            "priority": random.choice(["low", "medium", "high"]),
            "created_at": datetime.now().isoformat(),
            "status": "new"
        }
        tickets.append(ticket)
    
    return tickets

def analyze_ticket_mock(ticket):
    """Mock AI analysis - works without API key"""
    return {
        "category": ticket['category'],
        "sentiment": "neutral",
        "urgency_score": 8 if ticket['priority'] == 'high' else 5,
        "suggested_team": "technical" if ticket['category'] == "technical" else "billing",
        "summary": "Requires investigation",
        "analysis_method": "mock_mobile"
    }

def create_opus_data():
    """Generate Opus-ready data"""
    print("📱 Generating sample data on mobile...")
    
    tickets = generate_sample_tickets(5)
    opus_data = []
    
    for ticket in tickets:
        analysis = analyze_ticket_mock(ticket)
        
        formatted_ticket = {
            "workflow_input": {
                "ticket_id": ticket['ticket_id'],
                "customer_info": {
                    "name": ticket['customer_name'],
                    "email": ticket['customer_email']
                },
                "issue_details": {
                    "description": ticket['issue_description'],
                    "category": ticket['category'],
                    "priority": ticket['priority']
                },
                "ai_analysis": analysis,
                "metadata": {
                    "created_at": ticket['created_at'],
                    "source": "mobile_data_bridge"
                }
            }
        }
        opus_data.append(formatted_ticket)
    
    # Save to file
    with open('data/opus_mobile_data.json', 'w') as f:
        json.dump(opus_data, f, indent=2)
    
    print(f"✅ Generated {len(opus_data)} tickets for Opus!")
    print("📁 File: data/opus_mobile_data.json")
    return opus_data

# Run immediately when file is executed
if __name__ == "__main__":
    data = create_opus_data()
    print("🎯 Data ready for Oduobuk's Opus workflow!")
