## Insert new records into Person (perhaps from a certain day)
```sql
INSERT INTO Person
VALUES (4705, ’White’, 33, ’M’, ’Not Hispanic’),
(4706, ’Black’, 23, ’M’, ’Not Hispanic’),
(4707, DEFAULT, 51, ’F’, DEFAULT),
(4708, ’White’, 19, ’M’, ’Not Hispanic’);
