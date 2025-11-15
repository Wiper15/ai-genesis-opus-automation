# Sample data generator for Opus workflow testing
import json

def create_sample_data():
    """Generate sample support tickets for testing"""
    sample_tickets = [
        {
            "ticket_id": "TKT001",
            "customer_name": "John Doe",
            "customer_email": "john@example.com",
            "issue": "Cannot login to account",
            "priority": "high",
            "category": "technical",
            "description": "Getting error message when trying to login with correct credentials."
        },
        {
            "ticket_id": "TKT002",
            "customer_name": "Jane Smith",
            "customer_email": "jane@example.com",
            "issue": "Billing charge question",
            "priority": "medium", 
            "category": "billing",
            "description": "Unexpected charge on last month's invoice, need clarification."
        },
        {
            "ticket_id": "TKT003",
            "customer_name": "Bob Wilson",
            "customer_email": "bob@example.com",
            "issue": "Feature request",
            "priority": "low",
            "category": "enhancement",
            "description": "Would like to see dark mode option in mobile app."
        }
    ]
    
    # Save sample data
    with open('data/sample_inputs/support_tickets.json', 'w') as f:
        json.dump(sample_tickets, f, indent=2)
    
    print("✅ Sample support tickets created in data/sample_inputs/")
    print("📊 Sample data includes: 3 support tickets with different priorities/categories")

if __name__ == "__main__":
    create_sample_data()
