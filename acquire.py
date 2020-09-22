import pandas as pd
import numpy as np
from pydataset import data
import matplotlib.pyplot as plt
import seaborn as sns
import os
from env import host, user, password

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_telco_data():
    if os.path.isfile('telco.csv') == False:
        sql_query = """
                    SELECT customer_id,
                    contract_type_id,
                    phone_service,
                    internet_service_type_id,
                    gender,
                    senior_citizen,
                    partner,
                    dependents,
                    tenure,
                    online_security,
                    online_backup,
                    device_protection,
                    tech_support,
                    streaming_tv,
                    streaming_movies,
                    monthly_charges,
                    total_charges,
                    churn
                    FROM customers
                    """
        df = pd.read_sql(sql_query, get_connection('telco_churn'))
        df.to_csv('telco.csv')
        return df
    else:
        df = pd.read_csv('telco.csv', index_col=0)
        return df

def new_telco_data():
    sql_query = """
                SELECT customer_id,
                contract_type_id,
                phone_service,
                internet_service_type_id,
                gender,
                senior_citizen,
                partner,
                dependents,
                tenure,
                online_security,
                online_backup,
                device_protection,
                tech_support,
                streaming_tv,
                streaming_movies,
                monthly_charges,
                total_charges,
                churn
                FROM customers                    """
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    df.to_csv('telco.csv')
    return df