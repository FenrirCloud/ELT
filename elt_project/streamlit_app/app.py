import streamlit as st
import duckdb
import pandas as pd
import os

def get_project_root() -> str:
    """Returns the project root directory."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    st.title('Olist Brazilian E-Commerce Dashboard')

    # Path to the DuckDB database
    project_root = get_project_root()
    db_path = os.path.join(project_root, 'data', 'ecommerce.duckdb')

    try:
        # Connect to DuckDB
        con = duckdb.connect(database=db_path, read_only=True)

        # Query the fct_orders table
        query = "SELECT * FROM fct_orders"
        
        # Execute the query and fetch the results into a Pandas DataFrame
        df = con.execute(query).fetchdf()

        st.subheader('Raw Data')
        st.write(df)

        # Example: Show total revenue
        total_revenue = df['total_value'].sum()
        st.metric(label="Total Revenue", value=f"R$ {total_revenue:,.2f}")

        # Example: Show orders by status
        st.subheader('Orders by Status')
        order_status_counts = df['order_status'].value_counts()
        st.bar_chart(order_status_counts)

    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        if 'con' in locals() and con:
            con.close()

if __name__ == "__main__":
    main()