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

cat_counts = {}
for r in requests:
    cat = r["category"]
    if cat in cat_counts:
        cat_counts[cat] = cat_counts[cat] + 1
    else:
        cat_counts[cat] = 1

for cat in cat_counts:
    open_in_cat = 0
    for r in requests:
        if r["category"] == cat and r["status"] == "open":
            open_in_cat = open_in_cat + 1
    print(cat + ":", cat_counts[cat], "total,", open_in_cat, "open")