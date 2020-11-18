# fdic_bank_data_warehouse
Data Engineering project to build a star schema data warehouse from scratch. 

Python script builds a star schema data warehouse from scratch by combining several CSV files containing 5 years of FDIC public banking data from thousands of banks across the country and does the following:

-Combines and cleans the files including reducing the memory footprint significantly.
-Creates the different dimension tables and fact table in order to form an OLAP star schema format.  
-Loads the newly created tables into SQL Server (creates the tables in SQL Server as well) using the SQL Alchemy package and adds the primary and foreign keys.    
-Data is loaded from SQL Server into Power BI to visualize the data and compare banks over different time periods or search for details on a particular bank.  

Tech stack used:
-Programming languages:  Python, SQL.  Python packages used:  Pandas and SQL Alchemy
-DBMS:  Sql Server
-Visualization platform:  Power BI.  

Below is the finished star schema format once the new structure gets loaded into Power BI:

![](/Star%20Schema.PNG)


