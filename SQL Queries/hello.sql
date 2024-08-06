SELECT Person_ID, Sex, Race, Age
FROM Person
WHERE Age > (SELECT AVG(Age) FROM Person;
-- hello
