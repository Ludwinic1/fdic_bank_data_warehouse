# fdic_bank_data_warehouse
Data Engineering project that builds an entire star schema data warehouse from scratch. 

Python script builds the star schema data warehouse from scratch and completes the following:
- Extracts data from several CSV files containing 5 years of FDIC (Federal Deposit Insurance Corporation) public banking data (**CSV files located in the data folder**) from thousands of banks across the country.
- Combines and cleans the files including reducing the memory footprint significantly.
- Creates all of the dimension tables and the fact table in order to form an OLAP star schema structure.  
- Loads the newly created tables into SQL Server (**creates the tables in SQL Server as well**) using the SQL Alchemy module.
- Creates the primary keys for the dimension tables and the composite primary key for the fact table.
- Creates the foreign key constraints between the tables.  
- Data is loaded from SQL Server into Power BI to visualize the data and compare banks over different time periods or search for details on a particular bank.  

 # Tech Stack:
- Programming languages:  Python and SQL.  Python packages/modules used:  Pandas and SQL Alchemy.
- DBMS:  SQL Server.
- Visualization platform:  Power BI.  

Below is the finished star schema design once the data gets loaded into Power BI:

![](/Star%20Schema.PNG)


