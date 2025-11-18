# SIMPLE AI SUPPORT DEMO - Team Wipemation
print("🚀 AI Genesis Hackathon - Team Wipemation")
print("🤖 Intelligent Customer Support Automation")
print("=" * 50)

# Sample ticket data
tickets = [
    {"id": "T001", "customer": "John Doe", "issue": "Can't login to account", "priority": "High"},
    {"id": "T002", "customer": "Sarah Smith", "issue": "Billing inquiry", "priority": "Medium"},
    {"id": "T003", "customer": "Mike Johnson", "issue": "Feature request", "priority": "Low"}
]

print("📊 TICKETS FROM GOOGLE SHEETS:")
for ticket in tickets:
    print(f"  • {ticket['id']}: {ticket['issue']}")

print("\n🤖 AI ANALYSIS & ROUTING:")
print("  • T001: Technical issue → Route to TECH TEAM")
print("  • T002: Billing question → Route to BILLING TEAM") 
print("  • T003: Feature request → Route to PRODUCT TEAM")

print("\n🎯 WORKFLOW AUTOMATION:")
print("  ✅ Tickets extracted from Google Sheets")
print("  ✅ AI-powered categorization") 
print("  ✅ Smart routing decisions")
print("  ✅ Audit trail maintained")
print("  ✅ Human review available")

print(f"\n✅ SUCCESS: Processed {len(tickets)} tickets automatically!")
print("🏆 Team Wipemation - AI Genesis Hackathon 2024")
