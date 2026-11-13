import pandas as pd
import os
import random

SEED = 20261022
random.seed(SEED)

os.makedirs("output", exist_ok=True)

carriers = []

for i in range(1, 11):
    carriers.append({
        "carrier_id": f"CAR-{i:03d}",
        "carrier_name": f"Carrier {i}",
        "reliability_score": round(
            random.uniform(0.80, 0.99), 2
        )
    })

carriers_df = pd.DataFrame(carriers)

carriers_df.to_csv(
    "output/carriers.csv",
    index=False
)
facilities = []

for i in range(1, 101):
    facilities.append({
        "facility_id": f"FAC-{i:03d}",
        "facility_name": f"Distribution Center {i}",
        "capacity": random.randint(
            1000,
            5000
        )
    })

facilities_df = pd.DataFrame(
    facilities
)

facilities_df.to_csv(
    "output/facilities.csv",
    index=False
)
shipments = []

for i in range(1, 101):

    shipments.append({
        "shipment_id":
        f"SHP-2026-{i:06d}",

        "carrier_id":
        random.choice(
            carriers_df["carrier_id"]
        ),

        "origin_facility":
        random.choice(
            facilities_df["facility_id"]
        ),

        "destination_facility":
        random.choice(
            facilities_df["facility_id"]
        ),

        "status":
        random.choice([
            "IN_TRANSIT",
            "DELIVERED"
        ])
    })

shipments_df = pd.DataFrame(shipments)

shipments_df.to_csv(
    "output/shipments.csv",
    index=False
)
routes = []

for i in range(1, 51):

    routes.append({
        "route_id": f"RTE-{i:03d}",
        "route_name": f"Route {i}",
        "expected_duration_hours": random.randint(12, 120)
    })

routes_df = pd.DataFrame(routes)

routes_df.to_csv(
    "output/routes.csv",
    index=False
)
shipment_legs = []

for i in range(1, 101):

    shipment_id = f"SHP-2026-{i:06d}"

    for leg in range(1, 4):

        shipment_legs.append({
            "leg_id":
            f"LEG-{shipment_id}-{leg:02d}",

            "shipment_id":
            shipment_id,

            "sequence_no":
            leg,

            "from_facility":
            random.choice(
                facilities_df["facility_id"].tolist()
            ),

            "to_facility":
            random.choice(
                facilities_df["facility_id"].tolist()
            )
        })

shipment_legs_df = pd.DataFrame(
    shipment_legs
)

shipment_legs_df.to_csv(
    "output/shipment_legs.csv",
    index=False
)



print("carriers.csv generated")
print("facilities.csv generated")
print("shipments.csv generated")
print("routes.csv generated")
print("shipment_legs.csv generated")