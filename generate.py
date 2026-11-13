import csv
import os
import random

SEED = 20261022
random.seed(SEED)

os.makedirs("output", exist_ok=True)

with open("output/shipments.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "shipment_id",
        "status"
    ])

    for i in range(1, 101):
        shipment_id = f"SHP-2026-{i:06d}"
        status = random.choice([
            "IN_TRANSIT",
            "DELIVERED"
        ])

        writer.writerow([
            shipment_id,
            status
        ])

print("✅ shipments.csv generated successfully")