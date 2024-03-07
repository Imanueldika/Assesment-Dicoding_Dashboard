import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

url1 = "https://raw.githubusercontent.com/Imanueldika/Assesment-Dicoding_Dashboard/main/total_sales_per_category_df.csv"
url2 = "https://raw.githubusercontent.com/Imanueldika/Assesment-Dicoding_Dashboard/main/orders_revenue_df.csv"
url3 = "https://raw.githubusercontent.com/Imanueldika/Assesment-Dicoding_Dashboard/main/rfm_df.csv"

total_sales_per_category_df = pd.read_csv(url1)
orders_revenue_df = pd.read_csv(url2)
rfm_df = pd.read_csv(url3)

st.header('E-Commerce Public Dashboard :sparkles:')

st.subheader("Best and Worts Performing Product")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="total_sales", y="product_category_name_english", data=total_sales_per_category_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Paling Banyak Terjual", loc="center", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)

sns.barplot(x="total_sales", y="product_category_name_english", data=total_sales_per_category_df.sort_values(by="total_sales", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Paling Sedikit Terjual", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)

st.pyplot(fig)


st.subheader("Sales Performance and Revenue")
plt.figure(figsize=(12, 6))
import numpy as np

# Convert DataFrame columns to numpy arrays
order_month_array = orders_revenue_df['order_month'].to_numpy()
order_id_array = orders_revenue_df['order_id'].to_numpy()
price_array = orders_revenue_df['price'].to_numpy()

# Plotting
fig1=plt.figure(figsize=(12, 6))

# Grafik tren jumlah pesanan per bulan
plt.plot(order_month_array, order_id_array, marker='o', color='b', label='Jumlah Pesanan')
plt.title('Tren Jumlah Pesanan dan Pendapatan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pesanan')
plt.xticks(rotation=45)

# Menambahkan sumbu y kedua untuk pendapatan
plt.twinx()
plt.plot(order_month_array, price_array, marker='s', color='r', label='Pendapatan')
plt.ylabel('Pendapatan (Rupiah)')

# Menampilkan legenda
plt.legend(loc='upper left')

st.pyplot(fig1)


st.subheader("Best Customer Based on RFM Parameters")
 
col1, col2, col3 = st.columns(3)
 
with col1:
    avg_recency = round(rfm_df.recency.mean(), 1)
    st.metric("Average Recency (days)", value=avg_recency)
 
with col2:
    avg_frequency = round(rfm_df.frequency.mean(), 2)
    st.metric("Average Frequency", value=avg_frequency)
 
with col3:
    avg_frequency = format_currency(rfm_df.monetary.mean(), "AUD", locale='es_CO') 
    st.metric("Average Monetary", value=avg_frequency)
 
fig2, ax = plt.subplots(nrows=1, ncols=3, figsize=(45, 15))
colors = ["#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9"]

sns.barplot(y="customer_id", x="recency", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("By Recency (days)", loc="center", fontsize=25)
ax[0].tick_params(axis='x', labelsize=15)

sns.barplot(y="customer_id", x="frequency", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("By Frequency", loc="center", fontsize=25)
ax[1].tick_params(axis='x', labelsize=15)

sns.barplot(y="customer_id", x="monetary", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel(None)
ax[2].set_title("By Monetary", loc="center", fontsize=25)
ax[2].tick_params(axis='x', labelsize=15)
plt.subplots_adjust(wspace=0.5)

plt.suptitle("Best Customer Based on RFM Parameters (customer_id)", fontsize=30)
st.pyplot(fig2)


