##  Find those individuals who are older than the average age in the Person table
```sql
SELECT Person.Person_ID, Person.Sex,
Person.Race, Person.Age
FROM Person
JOIN (SELECT AVG(Age) as AverageAge FROM Person)
AS AvgSub
ON Person.Age > AvgSub.AverageAge;
```
In an effort to improve performance and lower the cost, a new and more efficient way to query the same information is carried out without using ’JOIN’ or a subquery and is written as follows:
```sql
SELECT Person_ID, Sex, Race, Age
FROM Person
WHERE Age > (SELECT AVG(Age) FROM Person);
```
