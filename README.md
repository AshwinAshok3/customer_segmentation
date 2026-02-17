# 🛍️ AI-Powered Customer Segmentation

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A professional-grade Machine Learning application that segments retail customers based on their purchasing behavior. By analyzing transaction history, this tool identifies distinct customer groups—from high-value VIPs to at-risk churners—enabling businesses to launch targeted marketing campaigns with precision.

---

## 🌟 Key Features

*   **RFM Analysis**: Automatically calculates Recency, Frequency, and Monetary value for every customer.
*   **Smart Clustering**: Uses K-Means clustering to group customers with similar behaviors.
*   **Dynamic Labeling**: Intelligently labels clusters (e.g., "💎 Loyal", "⚠️ At-Risk") based on their statistical profiles, solving the common "label switching" problem in ML.
*   **Interactive Dashboard**: A beautiful Streamlit interface to visualize segments, explore data, and export results.
*   **Business-Ready**: Handles real-world retail data issues like cancellations, missing IDs, and returns.

---

## 📂 Project Structure

This project is organized for scalability and clarity. Here's a look under the hood:

```plaintext
customer_segmentation/
├── app.py                  # 🚀 The main Streamlit application entry point
├── requirements.txt        # 📦 List of python dependencies
├── data/                   # 💾 Folder for storing raw CSV/Excel data
│   └── customer_segmentation.csv (Example data)
├── pipeline/               # ⚙️ The Engine Room: Training & Processing
│   ├── train_model.py      # Script to retrain the ML model
│   └── feature_engineering.py # Logic for cleaning & RFM calculation
├── inference/              # 🔮 Prediction Logic
│   └── batch_predictor.py  # Class to load model & predict on new data
├── utils/                  # 🛠️ Helper Utilities
│   └── io.py               # Robust file loading (CSV/Excel)
├── artifacts/              # 🏺 Saved Models (Created after training)
│   ├── kmeans.pkl          # Trained K-Means model
│   ├── scaler.pkl          # Standard Scaler for normalization
│   └── feature_schema.json # Ensures data consistency
└── notebooks/              # 📓 Jupyter Notebooks for experimentation
```

---

## 🚀 Getting Started

Follow these steps to get the project running on your local machine.

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Installation
Clone the repository and install the required packages:

```bash
# Install dependencies
pip install -r requirements.txt
```

### 3. Training the Model (Optional)
The project comes with a pre-trained model structure, but if you want to retrain it on your own data:
1.  Place your training data in `data/customer_segmentation.csv`.
2.  Run the training pipeline:

```bash
python pipeline/train_model.py
```
*This will generate new model files in the `artifacts/` directory.*

### 4. Running the App
Launch the interactive dashboard:

```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`.

---

## 💡 How It Works

### The Workflow
1.  **Data Ingestion**: You upload a transaction file (CSV/Excel) containing `InvoiceNo`, `StockCode`, `Quantity`, `InvoiceDate`, `UnitPrice`, and `CustomerID`.
2.  **Preprocessing**: The app cleans the data (removing returns, null IDs) and aggregates it to the customer level.
3.  **Feature Engineering**: We calculate 5 core metrics for each customer:
    *   **Recency**: Days since last purchase.
    *   **Frequency**: Number of unique purchases.
    *   **Monetary**: Total money spent.
    *   **Total Quantity**: Total items bought.
    *   **Unique Products**: Variety of products purchased.
4.  **AI Segmentation**: The pre-trained K-Means model groups customers into 4 clusters based on these metrics.
5.  **Insight Generation**: The system analyzes the clusters and assigns human-readable labels (e.g., "Recent Low Spenders" vs "High-Value Loyal") so you can take action immediately.

---

## 📊 Sample Data Format

Your input file needs to look something like this:

| InvoiceNo | StockCode | Description | Quantity | InvoiceDate | UnitPrice | CustomerID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 536365 | 85123A | HEART LIGHT HOLDER | 6 | 12/1/2010 8:26 | 2.55 | 17850 |
| 536365 | 71053 | WHITE METAL LANTERN | 6 | 12/1/2010 8:26 | 3.39 | 17850 |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](issues) if you want to contribute.

---

*Built with ❤️ for intelligent retail analytics.*
