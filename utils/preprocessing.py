import pandas as pd

def load_customer_data(filepath):
    return pd.read_csv(filepath)

def load_product_data(filepath):
    return pd.read_csv(filepath)
