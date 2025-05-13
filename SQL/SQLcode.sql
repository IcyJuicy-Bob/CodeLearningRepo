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
