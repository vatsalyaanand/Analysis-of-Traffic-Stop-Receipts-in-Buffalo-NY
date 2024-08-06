Find the average age and the number of traffic stops grouped by race
```sql

SELECT Person.Race,
ROUND(AVG(Person.Age), 2) AS AvgAge,
COUNT(*) AS StopCount
FROM Person
JOIN TrafficStop ON
Person.Person_ID = TrafficStop.Person_ID
GROUP BY Person.Race
ORDER BY StopCount DESC;
