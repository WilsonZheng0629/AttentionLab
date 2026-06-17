import pandas as pd
import sqlite3  

conn = sqlite3.connect('/Users/wilson/AttentionLab/data/attentionlab.db')

# Query the database to check if the data was inserted correctly
query = "SELECT * FROM attentionlab LIMIT 5;"  # Fetch the first
result = pd.read_sql_query(query, conn)
print(result)

# Close the database connection
conn.close()

