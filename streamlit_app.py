import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd

from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommender_agent import RecommenderAgent
from utils.preprocessing import load_customer_data, load_product_data

# Load Data
try:
    customer_data = load_customer_data("data/customer_data_collection.csv")
    product_data = load_product_data("data/product_recommendation_data.csv")
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Validate customer_id column
if "customer_id" not in customer_data.columns:
    st.error("❌ 'customer_id' column is missing in customer_data_collection.csv. Please fix the CSV.")
    st.stop()

# App UI
st.title("🛍️ SmartShoppers: Personalized Product Recommendations")

customer_ids = customer_data["customer_id"].unique()
selected_id = st.selectbox("Select a customer ID", customer_ids)

# Create agents
cust_agent = CustomerAgent(customer_data)
prod_agent = ProductAgent(product_data)
recom_agent = RecommenderAgent(cust_agent, prod_agent)

# Show recommendations
if st.button("🔍 Get Recommendations"):
    recs = recom_agent.recommend(selected_id)
    if isinstance(recs, pd.DataFrame) and not recs.empty:
        st.success(f"Recommended products for customer {selected_id}:")
        st.dataframe(recs)
    elif isinstance(recs, list) and len(recs) > 0:
        st.success(f"Recommended products for customer {selected_id}:")
        st.write(recs)
    else:
        st.warning("No recommendations available for this customer.")
