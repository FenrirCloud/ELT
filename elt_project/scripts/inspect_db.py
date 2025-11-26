import duckdb

def inspect_columns(db_path, table_name):
    """
    Connects to a DuckDB database and prints the column names of a table.

    Args:
        db_path (str): The path to the DuckDB database file.
        table_name (str): The name of the table to inspect.
    """
    try:
        con = duckdb.connect(database=db_path, read_only=True)
        # Use PRAGMA to get table info
        columns = con.execute(f"PRAGMA table_info('{table_name}')").fetchall()
        
        if columns:
            print(f"Columns in '{table_name}':")
            for col in columns:
                print(f"- {col[1]} ({col[2]})") # Print name and type
        else:
            print(f"Table '{table_name}' not found or has no columns.")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'con' in locals() and con:
            con.close()

if __name__ == "__main__":
    database_path = 'd:/ELT/elt_project/data/ecommerce.duckdb'
    table_to_inspect = 'olist_classified_public_dataset'
    inspect_columns(database_path, table_to_inspect)