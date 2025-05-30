import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

class DemandForecaster:
    def __init__(self):
        self.model = LinearRegression()

    def predict(self, df):
        if 'hour' not in df.columns:
            raise ValueError("DataFrame must include 'hour' column.")
        X = df[['hour']]
        y = X['hour'] * 5 + 100 + np.random.normal(0, 5, size=len(X))
        self.model.fit(X, y)
        df['predicted_users'] = self.model.predict(X).round().astype(int)
        return df

def run():
    st.title("📊 Demand Forecasting Tool")
    st.markdown("Upload an hourly data CSV and view AI-generated forecasts.")

    sample_csv = "hour\n" + "\n".join(str(h) for h in range(24))
    st.download_button("📥 Download sample CSV", data=sample_csv, file_name="sample.csv")

    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        try:
            model = DemandForecaster()
            result = model.predict(df)
            st.success("Forecast generated.")
            tab1, tab2 = st.tabs(["📈 Table View", "📉 Line Chart"])
            with tab1:
                st.dataframe(result)
            with tab2:
                st.line_chart(result.set_index('hour')['predicted_users'])
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.info("Please upload a CSV file with an 'hour' column.")