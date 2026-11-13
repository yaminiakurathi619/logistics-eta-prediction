# Entity Relationships

Carrier (1) ---> (N) Shipment

Shipment (1) ---> (N) ShipmentLeg

Shipment (1) ---> (N) TrackingEvent

Facility (1) ---> (N) FacilityQueue

Facility (1) ---> (N) WeatherEvent

Shipment (1) ---> (N) ETAEstimate

Shipment (1) ---> (N) DelayReason

## Primary Keys

- carrier_id
- facility_id
- shipment_id
- route_id
- leg_id
- event_id
- weather_id
- queue_id
- eta_id
- delay_id

## Foreign Keys

- shipment.carrier_id → carrier.carrier_id
- shipment_leg.shipment_id → shipment.shipment_id
- tracking_event.shipment_id → shipment.shipment_id
- weather_event.facility_id → facility.facility_id
- facility_queue.facility_id → facility.facility_id