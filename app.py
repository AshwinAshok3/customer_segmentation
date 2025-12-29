import streamlit as st
from inference.predictor import predict_customer_segment

st.title("Customer Segmentation Predictor")

recency = st.number_input("Recency (days)", min_value=0)
frequency = st.number_input("Frequency", min_value=0)
monetary = st.number_input("Monetary Value", min_value=0.0)
quantity = st.number_input("Total Quantity", min_value=0)
unique_products = st.number_input("Unique Products", min_value=0)

if st.button("Predict Segment"):
    input_data = {
        "Recency": recency,
        "Frequency": frequency,
        "Monetary": monetary,
        "TotalQuantity": quantity,
        "UniqueProducts": unique_products
    }

    result = predict_customer_segment(input_data)

    st.success(f"KMeans Cluster: {result['kmeans_cluster']}")
    st.info(f"GMM Cluster: {result['gmm_cluster']}")
    st.write(f"GMM Confidence: {result['gmm_confidence']}")
