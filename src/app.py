from flask import Flask, request, render_template
from data.processor import DataProcessor
from dashboard.charts import Dashboard

app = Flask(__name__)
data_processor = DataProcessor()
dashboard = Dashboard()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    file_path = f"./uploads/{file.filename}"
    file.save(file_path)
    
    data = data_processor.load_data(file_path)
    processed_data = data_processor.process_data(data)
    charts = dashboard.create_chart(processed_data)
    
    return render_template('dashboard.html', charts=charts)

if __name__ == '__main__':
    app.run(debug=True)