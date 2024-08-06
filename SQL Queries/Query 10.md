## Update BodyCam to TRUE for all traffic stops in Police District E, as there is certainty all officers in that district wear body cameras
```sql
UPDATE TrafficStop
SET BodyCam = ’TRUE’
FROM Location
WHERE (TrafficStop.Latitude =
Location.Latitude
AND TrafficStop.Longitude =
Location.Longitude)
AND PoliceDistrict = ’District E’;
