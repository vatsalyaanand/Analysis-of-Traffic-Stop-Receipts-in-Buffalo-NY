## Update the Ethnicity of person with Person ID = 10, whose Ethnicity was previously set to ’UNKNOWN’
```sql
UPDATE Person
SET Ethnicity = ’Not Hispanic’
WHERE Person_ID = 10;
