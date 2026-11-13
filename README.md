# Logistics ETA Prediction and Delay Detection

## Problem Statement

Combine carrier events, route plans, weather data, and facility queues to estimate shipment ETA and identify potential delays.

## Objective

Build an end-to-end workflow that:

- Generates synthetic logistics data
- Simulates shipment movement
- Produces ETA predictions
- Detects delays
- Tracks disruptions
- Validates data quality

## Entities

- Shipment
- ShipmentLeg
- Carrier
- Route
- TrackingEvent
- Facility
- FacilityQueue
- WeatherEvent
- ETAEstimate
- DelayReason

## Output Files

- shipments.csv
- shipment_legs.csv
- carriers.csv
- routes.csv
- tracking_events.csv
- facilities.csv
- facility_queue.csv
- weather_events.csv
- eta_estimates.csv
- delay_reasons.csv
- ground_truth.csv

## Seed

20261022

## Run

```bash
python generate.py
```