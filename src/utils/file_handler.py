from typing import Union
import pandas as pd

def read_excel(file_path: str) -> Union[pd.DataFrame, None]:
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

def read_csv(file_path: str) -> Union[pd.DataFrame, None]:
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None