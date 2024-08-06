## Identify the 5 locations (addresses) with the highest number of traffic stops
```sql
SELECT Location.Address, Location.ZipCode,
Location.Neighborhood,
Location.PoliceDistrict,
COUNT(*) as StopCount
FROM TrafficStop
JOIN Location ON
TrafficStop.Latitude =
Location.Latitude
AND TrafficStop.Longitude =
Location.Longitude
GROUP BY Location.Address,
Location.ZipCode,
Location.Neighborhood,
Location.PoliceDistrict
ORDER BY StopCount DESC
LIMIT 5;
