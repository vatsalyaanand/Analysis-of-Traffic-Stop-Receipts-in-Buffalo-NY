# Analysis of Traffic Stop Receipts in Buffalo, NY

## I. Project Overview
This project and supplemental report serve to investigate, analyze, and communicate findings about records of traffic stop receipts issued in the City of Buffalo and its thirty-five neighborhoods from October 1, 2022, to October 17, 2023.

## II. Problem Statement

### A. Problem Discussion and Questions
It is paramount for the City of Buffalo to keep receipts of the traffic stops they issue to individuals on a daily basis so there is a clear record of law violations for citizens in an effort to sustain public safety. At the same time, it is often the case and trend that high-frequency issues of traffic stop receipts in certain regions can correspond to lower standards of living, socioeconomic status, and greater levels of poverty for those in and around that region. Analyzing a database that contains a number of features related to a traffic stop, including, but not limited to, demographic information of individuals such as age, race, and ethnicity, and location information, such as the neighborhood, council district, and police district that a traffic stop receipt is issued, can give vital information as to how city officials may allocate resources and implement programs to not only improve public safety but ensure a more sustainable future for the neighborhoods of Buffalo.

There are a multitude of reasons that require the analysis of such a database as traffic stop receipts in the City of Buffalo in an effort to solve problems across several domains. The City of Buffalo is one of the most impoverished metropolitan areas in the United States, and oftentimes government officials only truly analyze what are deemed the most contributing factors to poverty, such as crime rates, household income, and educational experience, while not focusing on factors that may not be as obvious, such as traffic stop issues. The analysis of this database brings in an additional perspective to the much broader issue of poverty that the city faces. This database’s analysis intends to uncover information that can be used to address some less obvious issues that contribute to poverty in the city, and aid in curbing such trends for the better and moving towards a safer and healthier Buffalo.

Some of the questions we wish to answer are as follows:

1. **What neighborhoods in the City of Buffalo over the analyzed time period have had the highest rate of traffic stop violations?** 
   - How can this be used to implement programs that focus on public safety sustainability in those specific areas?
2. **Is there a higher frequency of traffic violations at specific times?** 
   - Should there be more focus on better monitoring during those specific times in an attempt to curb those higher traffic issue rates?
3. **How do personal demographics play a role in traffic stop receipts issued?** 
   - Is there a disparity in how traffic stop receipts are issued based on certain demographics?
4. **Is there a difference in traffic stop details based on whether a police officer has a body camera on their person or not?**
5. **What kinds of violations are most prevalent?** 
   - Is there a specific street-level location that sees many traffic stop receipts issued that needs the attention of city officials?

### B. Reason for Database Management
A database is needed instead of an Excel file due to the fact that insertions are needed for this database. Every day, new traffic stop receipts are issued, and an efficient mechanism is needed for the insertion of this information. In addition, as more traffic receipts are issued, trends amongst the data may change over time. A database is necessary to effectively capture and analyze such changes over time, as new data streams in daily.

### C. Background and Significance of Problem
Poverty has had a grip on the City of Buffalo for decades, characterized by lower standards of living, high crime rates, food insecurity, inadequate access to healthcare, and significant economic and education deficiencies and gaps for a substantial proportion of those who live in the region’s neighborhoods. Rates of poverty are greater among children and minority individuals. This is a significant problem because such issues revolving around poverty greatly hinder individuals’ abilities to navigate their daily lives and provide for themselves and families. People are living paycheck to paycheck and, frankly, are working just to live. Those individuals deserve equal access to services that the other percentage of the population does not have to worry about not having access to, and understanding underlying issues contributing to this issue would allow for government officials to pinpoint regions and/or sub-populations of need.

### D. Potential For Project Contribution to Problem Domain
This project has the potential to catalyze government and city officials to focus on areas or sub-populations that may not have been of primary concern in the past as it relates to curbing poverty rates in the City of Buffalo. While it is important to address crime and access to education, healthcare, and food, there is also an importance in addressing other smaller-scale issues that over time may have added up and also contributed to the problem as a whole. There is potential to make significant improvements for the sub-populations of interest and supporting those individuals in an effort to make sure they rise above the poverty line, and do not fall below it in the future. Government response to such dire issues can be the difference between life and death for some. Thus, stating that the analysis of such data is crucial is an understatement. Strides can be made in addressing public safety by deploying resources to areas that need aid, by means of welfare programs, and as it directly relates to the traffic stop receipt database, educating individuals through driver education programs, or fixing erroneous road conditions that lead to traffic stops as a result of insufficient city infrastructure and failure to meet safety standards.

## III. Target User

### A. Database Users
The database can be utilized by several groups of people. City and government officials that wish to analyze various demographic and regional trends can use this database to pinpoint sub-populations and areas of interest to provide better programs to curb violations, which in turn can curb poverty rates. Also, databases of this nature are publicly available, as the name of the person that a traffic stop receipt is issued to is not accessible. This database may be used to examine demographic trends, rather than individual and personal information for a specific individual. Thus, politicians and those running for government office may find this information useful in campaigning to voters as to how they can tackle outstanding issues as it relates to traffic violations and poverty, and how they intend on solving those problems, whether it be by implementing welfare programs or improving city infrastructure. In addition, those who simply wish to educate themselves on community demographic trends in the City of Buffalo can use this database. People who live in the City of Buffalo that are not issued traffic stop receipts, but still may be concerned about the safety of the area they live in, or activists that wish to lobby city officials and politicians based on public safety and its potential effect on city poverty levels may also intend to use this database.

### B. Database Administrators
The database will be administered by a select group of city officials and clerks. Typically, the New York State Attorney General’s office would be in charge of matters such as traffic stop receipts and updating records on a daily basis. Beyond this, the Buffalo Police Department may administer the database, as officers directly issue receipts to individuals. Thus, as it directly relates to this specific database regarding traffic stop receipts issued in the City of Buffalo, city officials and clerks, specifically those in the New York State Attorney General’s office downtown, as well as the Buffalo Police Department will administer the database.

### C. Scenarios of Database Management

**Scenario 1: Traffic Stop Incident and Insertion of Records**

A police officer in the City of Buffalo is monitoring the University Heights neighborhood and encounters an individual blowing through a stop sign. The officer pulls the individual over and gathers the individual’s information from their driver’s license and vehicle registration. After the traffic stop is completed, that information is relayed to the Attorney General’s office, where a clerk or other official inserts records into the database on a daily basis. The fields inserted into the database include, but are not limited to, a traffic stop identification number, reason for the stop, date and time of issuance, location of traffic stop, and the race, ethnicity, and age of the individual issued the receipt.

**Scenario 2: Use of Database to Analyze Demographic and Location Data**

A political campaign for a candidate running for city mayor wishes to understand the frequency of traffic stop receipts issued over the past 5 years based on race, age bins, and which neighborhoods traffic stop receipt issues are greatest. After querying data for the time period of interest, it is discovered that there is a greater proportion of traffic stop receipts issued to individuals of minority races, individuals 16-25 years of age make up the most speeding violations, and the most receipts are issued in University Heights and Broadway-Fillmore of the thirty-five neighborhoods that make up the city. As a result, that government hopeful focuses their campaign on how they would solve those problems by ensuring public safety and curbing poverty if elected, in an effort to appeal to voters.

## IV. Entity-Relationship Diagram

### A. Figure

The figure below depicts the entity-relationship diagram for the traffic stop database.
![Entity-Relationship Diagram](/ERdiagram.png)

### B. Relationships Between Tables

The “TrafficStop” table relates to the “Person” table by means of an attribute “Involving”. That is, the “TrafficStop” table that contains the main information regarding the incident, including, but not limited to, a foreign key “Person Id”, reason for the traffic stop, and date and time details, relates to the “Person” table, where the “Person Id” is the primary key, and contains tuples pertaining to the individual involved in that traffic incident. This is a one-to-one relationship, as one traffic stop pertains to exactly one person, and conversely, one individual on record (each entry is a unique incident with no identifiable information for the individual recorded) pertains to exactly one traffic incident. While a “TSR ID” uniquely identifies a person and record, a separate table for “Person” is created for organizational purposes.

The “TrafficStop” table relates to the “Location” table by means of an attribute “At”. That is, the “TrafficStop” table that contains the main information regarding the incident, including, but not limited to, a foreign key that is a composite key consisting of “Latitude” and “Longitude”, reason for the traffic stop, and date and time details, relates to the “Location” table, where the “Latitude” and “Longitude” is the primary key, and contains tuples pertaining to the location at which a traffic receipt was issued. This is a many-to-one relationship, as many traffic stops can occur at one location (in the event that latitude and longitude are the same for different receipts issued), and conversely, one location can relate to many traffic stop incidents.

### C. Functional Dependencies, and Assurance of Boyce-Codd Normal Form For Each Relation

All relations of the database are in Boyce-Codd Normal Form. This is justified for each of the relations as follows:

**“TrafficStop” functional dependencies:**

- TSR ID → Person ID, Latitude, Longitude, Reason, BodyCam, DateIssued, DayOfWeek, HourOfDay
- Person ID → TSR ID, Latitude, Longitude, Reason, BodyCam, DateIssued, DayOfWeek, HourOfDay

For all non-trivial functional dependencies holding in “TrafficStop”, that is the one above, TSR ID and Person ID are candidate keys. This is true as both TSR ID and Person ID on their own can uniquely identify all details of a traffic stop, namely all other attributes in the relation.

**“Person” functional dependencies:**

- Person ID → Race, Age, Sex, Ethnicity

For all non-trivial functional dependencies holding in “Person”, that is the one above, Person ID is a candidate key. This is true as Person ID uniquely identifies all details related to a person involved in the traffic stop.

**“Location” function dependencies:**

- Latitude, Longitude → Address, ZipCode, Neighborhood, CouncilDistrict, PoliceDistrict

For all non-trivial functional dependencies holding in “Location”, that is the one above, Latitude, Longitude is a candidate key. This is true as Latitude and Longitude uniquely identify all location-based details related to a traffic stop.

### D. Transformation from Initial Schema to Boyce-Codd Normal Form

The initial schema was taken from Open Data Buffalo, a public repository of data sets related to the City of Buffalo (https://data.buffalony.gov/Public-Safety/Traffic-Stop-Receipts/8mqs-6g9h). The data set originally contained 14.3K rows and 32 columns. For the purposes of this project, three relations were created by taking subsets of columns from the data set to create an organized and coherent database. For each of the three relations, the primary key uniquely determines all other attributes, with no other functional dependencies present, as each record is a unique instance. Thus, for each of the relations, there is a functional dependency that is nontrivial, in which the primary key determines all other attributes. That is the primary key is a candidate key. Thus, all relations are Boyce-Codd Normal Form.

## V. Database Specifics: Relations and Their Attributes

**Relation 1: TrafficStop**
TrafficStop(TSR ID, Person ID, Reason, BodyCam, DateIssued, DayOfWeek, HourOfDay, Latitude, Longitude)

**Primary Key:**
- TSR ID - unique identifier for a traffic stop

**Foreign Keys:**
- Person ID references Person: ON DELETE CASCADE and ON UPDATE CASCADE are employed where all rows referenced in the child table (Person) are deleted/updated when the corresponding row is deleted/updated from the parent table (TrafficStop).
- Latitude, Longitude references Location: No action is taken with regards to the deletion of rows in the child table (Location) when a corresponding row in the parent table (TrafficStop) is deleted, as although rare, a specific location still may be relevant for other traffic stops in the database

**Attributes:**
- TSR ID (integer, not null): unique number for a traffic stop
- Person ID (integer, not null): unique number for a person involved at a traffic stop
- Reason (varchar, not null): brief description of why a traffic stop receipt was issued
- BodyCam (boolean, default null): true or false value as to whether the officer issuing a traffic stop receipt had a body camera on person
- DateIssued (timestamp, not null): date and time the traffic stop receipt was issued
- DayOfWeek (varchar, default null): day of the week the traffic stop receipt was issued
- HourOfDay (varchar, default null): hour of the day the traffic stop receipt was issued
- Latitude (double precision, not null): latitude where the traffic stop receipt was issued
- Longitude (double precision, not null): longitude where the traffic stop receipt was issued

**Relation 2: Person**
Person(Person ID, Race, Age, Sex, Ethnicity)

**Primary Key:**
- Person ID - unique identifier for a person involved in a traffic stop

**Foreign Keys:**
- None

**Attributes:**
- Person ID (integer, not null) - unique number for a person involved in a traffic stop
- Race (varchar, default ‘UNKNOWN’) - race of the person who received the traffic stop receipt
- Age (integer, not null) - age of the person at the time of receiving the traffic stop receipt
- Sex (char(1), not null) - sex of the person who received the traffic stop receipt
- Ethnicity (varchar, default ‘UNKNOWN’) - ethnicity of the person who received the traffic stop receipt

**Relation 3: Location**
Location(Address, ZipCode, Neighborhood, CouncilDistrict, PoliceDistrict, Latitude, Longitude)

**Primary Key:**
- Latitude, Longitude - unique identifier for a specific place at which a traffic stop receipt is issued

**Foreign Keys:**
- None

**Attributes:**
- Address (varchar, not null) - approximate address where the traffic stop receipt was issued
- ZipCode (varchar, default ‘UNKNOWN’) - zip code where the traffic stop receipt was issued
- Neighborhood (varchar, default ‘UNKNOWN’) - neighborhood where the traffic stop receipt was issued
- CouncilDistrict (varchar, default ‘UNKNOWN’) - council district where the traffic stop receipt was issued
- PoliceDistrict (varchar, default ‘UNKNOWN’) - police district where the traffic stop receipt was issued
- Latitude (double precision, not null) - latitude where the traffic stop receipt was issued
- Longitude (double precision, not null) - longitude where the traffic stop receipt was issued

## VI. Dataset Imports into PostgreSQL

In terms of handling the copy and importing of data sets from our local machine upon downloading from the Open Data Buffalo public repository, problems arose when it came to granting permissions to PostgreSQL, the database management system used for this project, to read the CSV files of data. In an attempt to solve this issue, proper permissions were given by navigating to the local machine’s system preferences, and adjusting the security settings appropriately. Beyond this, a few separate terminal commands were needed to enable proper reading and importing of data into the three relations. In terms of adopting indexing concepts, such was not necessary. No lazy loading of data was needed, and imports of data from the CSV files into the relations were quick and efficient as the amount of data being copied into the table was not large enough to amount to any issues. In terms of the number of rows in each relation specifically, the TrafficStop and Person relations contain 4,323 rows, while the Location relation contains 2,719 rows.

One other problem that came up upon copying data from the three CSV files into the relations of the database dealt with the Location relation and its primary key of (Latitude, Longitude). Since the latitude and longitude coordinates uniquely identify a row in that relation, when two rows with the same primary key appear, namely the same latitude and longitude coordinates, the other values in the row should match. But, even after adjusting the CSV file to remove duplicate rows for the purposes of our database, copying errors arose due to the fact that some rows, while having the same primary key, had values in other columns that did not match. For instance, two rows may have matched on all columns, except for their address, where one entry’s address was inputted as “Corner of Street A Street B”, and the other’s was inputted as “Corner of Street B Street A”. Thus, while the location of the traffic stop receipt issuance was the same, import errors arose due to the way information was inputted. There were very few instances in which such an error occurred when importing the data into the relations (less than five cases), and in each case PostgreSQL helpfully provided the row number of the discrepancy, and that corresponding row was deleted from the CSV file, and thus was not imported into the database.


