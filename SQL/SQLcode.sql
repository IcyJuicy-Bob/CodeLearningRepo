/*this is a comment in a sql document i will be using this to comment throughout the sql file*/
/*sql stands for structured query language*/
/*
SQL can execute queries against a database
SQL can retrieve data from a database
SQL can insert records in a database
SQL can update records in a database
SQL can delete records from a database
SQL can create new databases
SQL can create new tables in a database
SQL can create stored procedures in a database
SQL can create views in a database
SQL can set permissions on tables, procedures, and views
*/
/*SQL is a ANSI/ISO standard but there are diffrent types of SQL 
to be compliant to the ANSI standard they need to have the major commands
SELECT, UPDATE, DELETE, INSERT, WHERE in a similar manner*/

/*to use a database in a website you need a RDBMS(e.g SQL server/MySQL), a server side language (e.g php)
use sql to get the data you want and html and css to style the website*/

/*RDBMS*/
/*RDBMS stands for Relational Database Management System.*/
/*a RDBMS is the basis of all database systems e.g MySQL*/
/*the data in RDBMS is stored in objects called tables*/
/*a table is a collection of related data entries in collums and rows*/
/*a field is a column of the table going vertically but is like the header like it may say cities and then in each row under is has diffrent city names*/
/*a record is a row of the table going horizontially for every entry for example might hold a name then in another field/column it has age then height ect going horizontally*/
/*going down on this hypothetical table would be other peoples names hights ages ect all in a different record*/
/*a column is just a row going vertically down like record just vertical*/

SELECT * FROM customers;
/*this selects all records from the customers table*/
/*it SELECTs the * means all FROM the customers table*/
/*the semi-colon is the standard way to seperate sql statements if the database system can handle more than one statement in the same call to the server*/

/*databases normally contain more than 1 table*/
/*SQL keywords aren't case sensitive SELECT is the same as select*/

SELECT - /*extracts data from a database*/
UPDATE - /*updates data in a database*/
DELETE - /*deletes data from a database*/
INSERT INTO - /*inserts new data into a database*/
CREATE DATABASE - /*creates a new database*/
ALTER DATABASE - /*modifies a database*/
CREATE TABLE - /*creates a new table*/
ALTER TABLE - /*modifies a table*/
DROP TABLE - /*deletes a table*/
CREATE INDEX - /*creates an index (search key)*/
DROP INDEX - /*deletes an index*/

SELECT town,city FROM customers;
/*same thing as the last select but it doesnt select the whole table just the two fields town and city seperated by a comma*/

SELECT town,city
FROM customers;
/*same thing as the one above the statement ends at the semi-colon ;*/
/*you can write statements over two lines probably more*/
/*town and city are column/field names*/

SELECT * FROM customers;
/* "*"" selects all columns/fields when you want to return all fields*/

/*sometimes a table contains more than one of the same value so we use the distinct statement*/
SELECT DISTINCT * FROM customers;
/*DISTINCT tells it to only return one of each value so if there was 2 of a value it wouldn't be returned*/

SELECT COUNT(DISTINCT towns) FROM customers;
/*this will return the number of unique values in the field "towns"*/
/*this isn't supported by MS access databases*/

/*workaround for MS acess databases*/
SELECT Count(*) AS DistinctCountries
FROM (SELECT DISTINCT Country FROM Customers);
/*idk how to explain this it works tho i think it saves the distinct value as distinct countries or something*/

/*where is used to filter record that fufill a condition*/
WHERE

SELECT (*) FROM Customers
WHERE Country='Mexico'; /*use single quotes most use double but single to be safe*/
/*if you use a number for the where vaulue DONT USE QUOTES*/

SELECT * FROM Customers
WHERE CustomerID > 80;
/*you can use operators in there where command this will filter for all values above 80*/
/*all these operators can be used*/
/*
=	Equal	
>	Greater than	
<	Less than	
>=	Greater than or equal	
<=	Less than or equal	
<>	Not equal. Note: In some versions of SQL this operator may be written as !=	
BETWEEN	Between a certain range	
LIKE	Search for a pattern	
IN	To specify multiple possible values for a column
*/

ORDER by
/*orders the values returned*/

SELECT * FROM Products
ORDER BY Price;
/*orders the records of the table in order by what the values are in the price field it is starting from smallest to biggest*/

SELECT * FROM Products
ORDER BY Price DESC; /*DESC means descending*/
/*orders the records of the table in order by what the values are in the price field it is starting from biggest to smallest*/

SELECT * FROM Products
ORDER BY ProductName;
/*if you order by a field that is made of strings it orders alphabetically*/

SELECT * FROM Products
ORDER BY ProductName DESC;
/*orders alphabetically backwards because its descending*/

SELECT * FROM Products
ORDER BY Price, ProductName DESC;
/*if some items have the same price it then orders by product name*/

SELECT * FROM Products
ORDER BY Price ASC, ProductName DESC;
/*you can use both Ascending and descending in that same order by pretty self explanatory so i wont explain it more*/
