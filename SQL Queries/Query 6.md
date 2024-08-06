## Retrieve the details of each traffic stop, along with the person who was stopped, and location of the traffic stop, ordered by date issued in descending order
```sql
SELECT TrafficStop.TSR_ID,
TrafficStop.Reason,
TrafficStop.BodyCam,
TrafficStop.DateIssued,
Person.Race, Person.Age, Person.Sex,
Person.Ethnicity, Location.Address,
Location.ZipCode, Location.Neighborhood,
Location.PoliceDistrict
FROM TrafficStop
JOIN Person
ON TrafficStop.Person_ID = Person.Person_ID
JOIN Location
ON TrafficStop.Latitude = Location.Latitude
AND TrafficStop.Longitude = Location.Longitude
ORDER BY TrafficStop.DateIssued DESC;
