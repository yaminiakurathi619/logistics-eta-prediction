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

tracking_events = []

event_types = [
    "PICKED_UP",
    "ARRIVED_FACILITY",
    "DEPARTED_FACILITY",
    "IN_TRANSIT",
    "DELIVERED"
]

event_counter = 1

for i in range(1, 101):

    shipment_id = f"SHP-2026-{i:06d}"

    for _ in range(3):

        tracking_events.append({
            "event_id":
                f"EVT-{i:06d}-{event_counter:06d}",

            "shipment_id":
                shipment_id,

            "event_type":
                random.choice(event_types)
        })

        event_counter += 1

tracking_events_df = pd.DataFrame(
    tracking_events
)

tracking_events_df.to_csv(
    "output/tracking_events.csv",
    index=False
)
weather_events = []

for i in range(1, 101):

    weather_events.append({
        "weather_id": f"WTH-{i:06d}",
        "facility_id": random.choice(
            facilities_df["facility_id"].tolist()
        ),
        "severity": random.choice([
            "LOW",
            "MEDIUM",
            "HIGH"
        ]),
        "delay_minutes": random.randint(30, 480)
    })

weather_df = pd.DataFrame(weather_events)

weather_df.to_csv(
    "output/weather_events.csv",
    index=False
)

facility_queue = []

for i in range(1, 101):

    facility_queue.append({
        "queue_id": f"QUE-{i:06d}",
        "facility_id": random.choice(
            facilities_df["facility_id"].tolist()
        ),
        "queue_length": random.randint(1, 100),
        "avg_wait_minutes": random.randint(5, 180)
    })

facility_queue_df = pd.DataFrame(
    facility_queue
)

facility_queue_df.to_csv(
    "output/facility_queue.csv",
    index=False
)
delay_reasons = []

for i in range(1, 101):

    delay_reasons.append({
        "delay_id": f"DLY-2026-{i:06d}",
        "shipment_id": f"SHP-2026-{i:06d}",
        "reason": random.choice([
            "WEATHER",
            "FACILITY_CONGESTION",
            "ROUTE_CHANGE",
            "CARRIER_DELAY"
        ])
    })

delay_df = pd.DataFrame(
    delay_reasons
)

delay_df.to_csv(
    "output/delay_reasons.csv",
    index=False
)
ground_truth = [

    {
        "shipment_id":
        "SHP-2026-000010",

        "issue_type":
        "TIME_ORDER_VIOLATION"
    },

    {
        "shipment_id":
        "SHP-2026-000020",

        "issue_type":
        "DATA_LEAKAGE"
    },

    {
        "shipment_id":
        "SHP-2026-000030",

        "issue_type":
        "INVALID_STATE_TRANSITION"
    },

    {
        "shipment_id":
        "SHP-2026-000040",

        "issue_type":
        "IMPOSSIBLE_ROUTE_ORDER"
    }
]

ground_truth_df = pd.DataFrame(
    ground_truth
)

ground_truth_df.to_csv(
    "output/ground_truth.csv",
    index=False
)

print("carriers.csv generated")
print("facilities.csv generated")
print("shipments.csv generated")
print("routes.csv generated")
print("shipment_legs.csv generated")
print("tracking_events.csv generated")
print("weather_events.csv generated")
print("facility_queue.csv generated")
print("delay_reasons.csv generated")
print("ground_truth.csv generated")
