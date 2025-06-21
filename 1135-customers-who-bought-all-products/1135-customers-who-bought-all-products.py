import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    total_products = product['product_key'].nunique()

    customer_product_counts = customer.groupby('customer_id')['product_key'].nunique().reset_index()

    result = customer_product_counts[customer_product_counts['product_key'] == total_products]



    return result[['customer_id']]
