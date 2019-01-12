# logs Analysis

# In this project:

I will create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database. which is answering three qustions:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Needed skils in this project:

- joining tables
- The select ...where statement
- Select clauses
- Writing code with DB-API
- Views

### you'll need:

- Ddatabase software (provided by a Linux virtual machine) and the data to analyze.
- Vagrant https://www.vagrantup.com/downloads.html.
- Virtual machine from https://www.virtualbox.org/wiki/Downloads .
- Download	a	FSND	virtual	machine https://github.com/udacity/fullstack-nanodegree-vm .
- Download newsdata.sql https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip	.
- To bring the virtual machine online (with ```bash vagrant up```), do so now. Then log into it with ```bash vagrant ssh ``` from the same locate ```bash Vagrantfile``` directory.
- Install psycopg2 package from the	terminal/git bash ```bash pip3 install psycopg2 ```.
- Install ```bash pip3 install pycodestyle ```  from the	terminal/git bash.

## How to start the work?

- On terminal/git bash
```bash cd vagrant
vagrant up
vagrant ssh
cd /vagrant
mkdir log-analysis-project
cd log-analysis-project 
```
- Move	the	“newsdata.sql”	to project	folder	“log-analysis-project”

- On terminal/git bash ```bash psql -d news -f newsdata.sql ``` then connect	to database	using ```bash psql -d news``` and explore	the	Data.

- Create	a	Python	File	and	Output	Text	File.

## Queries  and Python file:
- ```python import psycopg2```on python file.
- Defining database connection & running querye method.
- Defining queries  & printing results methods.

## How to run the project?
- on terminal/git bash while vagrant is connected run ```bash python loganalysisdb.py```.
