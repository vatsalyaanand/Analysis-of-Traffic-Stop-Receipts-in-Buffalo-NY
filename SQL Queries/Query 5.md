## Find the number of traffic stops grouped by neighborhood in descending order
```sql
SELECT Location.Neighborhood,
COUNT(*) AS StopCount
FROM TrafficStop
JOIN Location
ON TrafficStop.Latitude =
Location.Latitude
AND TrafficStop.Longitude =
Location.Longitude
GROUP BY Location.Neighborhood
ORDER BY StopCount DESC;
