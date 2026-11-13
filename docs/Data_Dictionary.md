# Data Dictionary

## Carrier

| Field | Type | Description |
|---------|---------|---------|
| carrier_id | String | Unique carrier identifier |
| carrier_name | String | Carrier name |
| reliability_score | Float | Carrier reliability score |

## Facility

| Field | Type | Description |
|---------|---------|---------|
| facility_id | String | Unique facility identifier |
| facility_name | String | Facility name |
| capacity | Integer | Facility processing capacity |

## Shipment

| Field | Type | Description |
|---------|---------|---------|
| shipment_id | String | Unique shipment ID |
| carrier_id | String | Carrier reference |
| origin_facility | String | Source facility |
| destination_facility | String | Destination facility |
| status | String | Current shipment status |

## Route

| Field | Type | Description |
|---------|---------|---------|
| route_id | String | Route identifier |
| route_name | String | Route name |
| expected_duration_hours | Integer | Planned duration |

## ShipmentLeg

| Field | Type | Description |
|---------|---------|---------|
| leg_id | String | Leg identifier |
| shipment_id | String | Shipment reference |
| sequence_no | Integer | Route sequence |
| from_facility | String | Origin facility |
| to_facility | String | Destination facility |

## TrackingEvent

| Field | Type | Description |
|---------|---------|---------|
| event_id | String | Event identifier |
| shipment_id | String | Shipment reference |
| event_type | String | Tracking event type |

## WeatherEvent

| Field | Type | Description |
|---------|---------|---------|
| weather_id | String | Weather event identifier |
| facility_id | String | Facility reference |
| severity | String | LOW/MEDIUM/HIGH |
| delay_minutes | Integer | Delay caused |

## FacilityQueue

| Field | Type | Description |
|---------|---------|---------|
| queue_id | String | Queue identifier |
| facility_id | String | Facility reference |
| queue_length | Integer | Queue size |
| avg_wait_minutes | Integer | Average wait time |

## ServiceLevel

| Field | Type | Description |
|---------|---------|---------|
| service_level_id | String | Service identifier |
| service_name | String | EXPRESS/STANDARD/ECONOMY |
| target_hours | Integer | SLA target |

## ETAEstimate

| Field | Type | Description |
|---------|---------|---------|
| eta_id | String | ETA identifier |
| shipment_id | String | Shipment reference |
| predicted_hours_remaining | Integer | Predicted ETA |
| prediction_status | String | ON_TIME/AT_RISK/DELAYED |

## DelayReason

| Field | Type | Description |
|---------|---------|---------|
| delay_id | String | Delay identifier |
| shipment_id | String | Shipment reference |
| reason | String | Delay cause |