## Find persons involved in traffic stops who are older than the average age
```sql
SELECT Person_ID, Race, Age, Sex, Ethnicity
FROM Person
WHERE Age > (SELECT AVG(Age) FROM PERSON);
