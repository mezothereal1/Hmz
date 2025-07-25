import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname="ecommerce_nigeria",
    user="postgres",
    password="mot_de_passe_ici",
    host="localhost",
    port="5432"
)

df = pd.read_sql("SELECT * FROM sales", conn)

df["Total"] = df["quantity"] * df["price"]
Total_Profit = df["Total"].sum()
Best_Selling_Product = df.groupby("product")["quantity"].sum().idxmax()
Best_customer = df.groupby("customer_id")["total"].sum().idxmax()

print(f"Analysis")
print(f"{Total_Profit} $")
print(f"{Best_Selling_Product}")
print(f"{Best_customer}")

conn.close()
