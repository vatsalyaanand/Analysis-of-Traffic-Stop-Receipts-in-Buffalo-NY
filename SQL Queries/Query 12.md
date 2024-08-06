## Delete all traffic stops that occurred between 10/1/2022 and 11/4/2022 in which the reason for the issuance was ’SPEEDING’
```sql
DELETE FROM TrafficStop
WHERE Reason = ’SPEEDING’
AND DateIssued >= ’2022-10-01 00:00:00’
AND DateIssued <= ’2022-11-04 23:59:59’;
