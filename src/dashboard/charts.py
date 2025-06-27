import matplotlib
matplotlib.use('Agg')  # Use backend without display
import matplotlib.pyplot as plt
import os

class Dashboard:
    def create_chart(self, data):
        if data is None or data.empty:
            return None
            
        # Create static folder if it doesn't exist
        static_folder = 'static'
        if not os.path.exists(static_folder):
            os.makedirs(static_folder)
            
        plt.figure(figsize=(10, 5))
        
        # Use the first numeric column if available
        numeric_columns = data.select_dtypes(include=['number']).columns
        if len(numeric_columns) > 0:
            column_name = numeric_columns[0]
            plt.plot(data.index, data[column_name], marker='o')
            plt.ylabel(column_name)
        else:
            # If no numeric columns, just show data info
            plt.text(0.5, 0.5, f'Data loaded: {len(data)} rows, {len(data.columns)} columns', 
                    ha='center', va='center', transform=plt.gca().transAxes)
            
        plt.title('Data Visualization')
        plt.xlabel('Index')
        plt.grid()
        
        chart_path = 'static/chart.png'
        plt.savefig(chart_path)
        plt.close()
        
        return chart_path