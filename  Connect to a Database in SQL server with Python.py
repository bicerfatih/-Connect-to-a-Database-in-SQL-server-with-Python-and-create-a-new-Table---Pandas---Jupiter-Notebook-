#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pyodbc
import pandas as pd 
pyodbc.drivers()

conn = pyodbc.connect(
    
    'Driver={ODBC Driver 18 for SQL Server};'
    'Server=tcp:localhost,1433;'
    'Database=AdventureWorks2017;'
    'Encrypt=yes;'
    'TrustServerCertificate=YES;'
    'UID=sa;'
    'PWD=anypassword;'

)

cursor = conn.cursor()




# In[6]:


df = pd.read_csv("/Users/f/Desktop/data_example/data_example.csv")
df.head()


# In[7]:


df.columns


# In[ ]:





# In[12]:


cursor.execute('''
                CREATE TABLE TABLE2
                (
                
                id int primary key, first_name nvarchar(50), last_name nvarchar(50), email nvarchar(50), gender nvarchar(50), ip_address nvarchar(50),
       city nvarchar(50)
                
                )             
                
                ''')


for row in df.itertuples():
    cursor.execute('''
    INSERT INTO AdventureWorks2017.dbo.TABLE2 ( id, first_name, last_name, email, gender, ip_address,
       city)
    VALUES(?,?,?,?,?,?,?)
    
    ''',
                    
                    row.id,
                    row.first_name,
                    row.last_name,
                    row.email,
                    row.gender,
                    row.ip_address,
                    row.city,
    
    )
    
    conn.commit()


# In[ ]:




