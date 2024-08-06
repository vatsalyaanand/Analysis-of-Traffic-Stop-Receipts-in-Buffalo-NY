## Find the top 10 reasons for traffic stop receipts being issued in police district A

```sql
SELECT Reason, COUNT(*) AS StopCount
FROM TrafficStop
JOIN Location ON TrafficStop.Latitude
= Location.Latitude
AND TrafficStop.Longitude =
Location.Longitude
WHERE Location.PoliceDistrict =
’District A’
GROUP BY Reason
ORDER BY StopCount DESC
LIMIT 10;
```
In an effort to improve performance and lower the cost, an indexing technique is implemented on the PoliceDistrict column in the Location relation as follows:
```sql
CREATE INDEX PD_INDEX ON Location(PoliceDistrict);
