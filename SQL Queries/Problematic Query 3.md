## Find the count of traffic stop receipts issued on Fridays and Saturdays for each hour of the day and order by frequency in descending order
```sql
SELECT HourOfDay,
COUNT(HourOfDay) AS Frequency
FROM TrafficStop
WHERE BodyCam = true
AND (DayOfWeek = ’FRIDAY’
OR DayOfWeek = ’Saturday’)
GROUP BY HourOfDay
ORDER BY Frequency DESC;
```
In an effort to improve performance and lower the cost, an indexing technique is implemented on the DayOfWeek column in the TrafficStop relation as follows:
```sql
CREATE INDEX BC_INDEX ON TrafficStop(DayOfWeek);
```
