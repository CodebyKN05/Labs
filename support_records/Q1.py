requests = [
    {"id": 101, "customer": "Asha", "category": "Billing",
     "status": "open", "phone": "9876543210"},
    {"id": 102, "customer": "Rohan", "category": "Account",
     "status": "closed", "phone": "9822011223"},
    {"id": 103, "customer": "Meera", "category": "Billing",
     "status": "open"},
    {"id": 104, "customer": "Kabir", "category": "General",
     "status": "open", "phone": "9890012345"},
    {"id": 105, "customer": "Sana", "category": "Account",
     "status": "open", "phone": ""},
    {"id": 106, "customer": "Asha", "category": "Billing",
     "status": "closed", "phone": "9876543210"},
]

for r in requests:
    print(r["id"], r["customer"] )
    