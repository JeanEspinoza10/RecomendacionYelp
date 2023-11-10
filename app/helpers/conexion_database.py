import pyodbc
import pandas as pd
from dotenv import load_dotenv
import os

def conexionSQLServer():
    '''
    return: archivo, codigo
    '''
    try:
        
        load_dotenv()

        server = os.environ.get("SERVER")
        database = os.environ.get("DATABASE")
        driver = os.environ.get("DRIVER")
        user = os.environ.get("USER")
        pwd = os.environ.get("PASSWORD")

        

        

        conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={pwd}'
        conn = pyodbc.connect(conn_str)

        df_tip = pd.read_sql("SELECT * FROM tip_users_busines", conn)
        
        
        # Grabando el archivo
    
        
        return df_tip, 200
    
    except Exception as e:
        return None, 404
