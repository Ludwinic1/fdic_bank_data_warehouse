import subprocess

# define the paths to the scripts
script1 = './scripts/sql_server_connection.py'
script2 = './scripts/data_extraction.py'
script3 = './scripts/create_dimensions.py'
script4 = './scripts/dimensions_to_sql_server.py'
script5 = './scripts/create_fact_table.py'

# execute the scripts using subprocess
subprocess.run(['python', script1])
subprocess.run(['python', script2])
subprocess.run(['python', script3])
subprocess.run(['python', script4])
subprocess.run(['python', script5])