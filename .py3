import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()
    
    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            print("Data loaded successfully!")
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def summarize_data(self):
        if self.data is not None:
            print("Data Summary:")
            print(self.data.describe())
            print("\nMissing Values:")
            print(self.data.isnull().sum())
        else:
            print("No data to summarize.")

    def visualize_data(self):
        if self.data is not None:
            # Example: Histogram for numerical features
            num_cols = self.data.select_dtypes(include=['float64', 'int64']).columns
            for col in num_cols:
                plt.figure(figsize=(8, 4))
                sns.histplot(self.data[col], bins=30, kde=True)
                plt.title(f'Distribution of {col}')
                plt.xlabel(col)
                plt.ylabel('Frequency')
                plt.show()
        else:
            print("No data to visualize.")

    def correlation_matrix(self):
        if self.data is not None:
            plt.figure(figsize=(10, 8))
            sns.heatmap(self.data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
            plt.title('Correlation Matrix')
            plt.show()
        else:
            print("No data 
