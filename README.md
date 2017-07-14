# News Database Log Report Generator

A program for gathering information from database logs

Basic useful feature list:

 * Report 3 most popular articles and viewcount
 * Reoport most popular authors and viewcount
 * Report high connection error days (>1%)

## Installation

* Fork guthub repo and dowload files
* Place files in the shared folder of your VM if using virtual machine
* Populate database: ` psql -d news -f newsdata.sql `
* Run program: ` python3 logsproject.py `

## Output

The program should execute and print to Terminal in the following format:

(This is example text for the database in its current form, updates may change values)

Most Popular Articles:  
"Candidate is jerk, alleges rival" - 338647 views  
"Bears love berries, alleges bear" - 253801 views  
"Bad things gone, say good people" - 170098 views  

Most Popular Authors:  
Ursula La Multa - 507594 views  
Rudolf von Treppenwitz - 423457 views  
Anonymous Contributor - 170098 views  
Markoff Chaney - 84557 views  

High Error Days:  
July 17, 2016 - 2.26% error  

