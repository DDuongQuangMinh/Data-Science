# api/load_csv.py

import pandas as pd
from .models import Customer  # adjust if model is in a different path

def run():
    df = pd.read_csv('/home/akd/Desktop/data_science/Data-Science/WA_Fn-UseC_-Telco-Customer-Churn.xls')
    df = df.fillna('')  # handle missing values

    for _, row in df.iterrows():
        Customer.objects.update_or_create(
            customerID=row['customerID'],
            defaults=row.to_dict()
        )
