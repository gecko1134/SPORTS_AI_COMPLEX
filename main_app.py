import streamlit as st
from ai_modules import demand_forecasting

TOOLS = {
    "📊 Demand Forecast": demand_forecasting
}

def main():
    st.set_page_config(page_title="SportAI Tools", layout="wide")
    st.sidebar.title("⚙️ SPORTAI Toolkit")
    selection = st.sidebar.selectbox("Choose a Tool", list(TOOLS))
    if selection:
        TOOLS[selection].run()

if __name__ == "__main__":
    main()