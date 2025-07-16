class DataProcessor:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        import pandas as pd
        if file_path.endswith('.csv'):
            self.data = self.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            self.data = self.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")
        # print(f"Data loaded successfully from {file_path}. Shape: {self.data.shape}")
        return self.data

    def read_csv(self, file_path):
        import pandas as pd
        return pd.read_csv(file_path)

    def read_excel(self, file_path):
        import pandas as pd
        return pd.read_excel(file_path)

    def process_data(self):
        if self.data is None:
            raise ValueError("No data loaded. Please load data before processing.")
        # Example processing: drop missing values
        self.data = self.data.dropna()
        return self.data