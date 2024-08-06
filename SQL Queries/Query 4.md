## Find the locations (addresses and neighborhoods) where traffic stops without body cameras were issued on weekends
```sql
SELECT Location.Address, Location.Neighborhood
FROM TrafficStop
JOIN Location ON
TrafficStop.Latitude
= Location.Latitude
AND TrafficStop.Longitude
= Location.Longitude
WHERE TrafficStop.BodyCam = FALSE
AND (TrafficStop.DayOfWeek = ’SATURDAY’
OR TrafficStop.DayOfWeek = ’SUNDAY’)
GROUP BY Location.Neighborhood, Location.Address;
