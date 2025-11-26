import duckdb
import os

def load_csv_to_duckdb(csv_dir, db_path):
    """
    Loads all CSV files from a directory into a DuckDB database.

    Args:
        csv_dir (str): The directory containing the CSV files.
        db_path (str): The path to the DuckDB database file.
    """
    con = duckdb.connect(database=db_path, read_only=False)

    csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]

    for csv_file in csv_files:
        file_path = os.path.join(csv_dir, csv_file)
        table_name = os.path.splitext(csv_file)[0].replace('-', '_')
        print(f"Loading {csv_file} into table {table_name}...")
        con.execute(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM read_csv_auto('{file_path}')")

    print(f"\nAll CSV files have been loaded into {db_path}")
    
    con.close()

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_directory = os.path.join(project_root, 'data')
    database_path = os.path.join(project_root, 'data', 'ecommerce.duckdb')

    load_csv_to_duckdb(data_directory, database_path)