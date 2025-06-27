# Data Dashboard

This project is a web application that allows users to upload Excel and CSV files, process the data, and generate visualizations in the form of a dashboard.

## Project Structure

```
data-dashboard
├── src
│   ├── app.py               # Entry point of the application
│   ├── data
│   │   └── processor.py     # Data processing functionalities
│   ├── dashboard
│   │   └── charts.py        # Dashboard and chart generation
│   └── utils
│       └── file_handler.py   # Utility functions for file handling
├── requirements.txt         # Project dependencies
├── config.py                # Configuration settings
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd data-dashboard
   ```

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```
   python src/app.py
   ```

4. **Access the dashboard:**
   Open your web browser and go to `http://localhost:5000`.

## Usage Guidelines

- Upload your Excel or CSV files using the provided interface.
- The application will process the data and generate visualizations based on the uploaded data.
- You can interact with the dashboard to explore the visualizations.

## Dependencies

This project requires the following Python packages:

- Flask
- pandas
- matplotlib

Make sure to check the `requirements.txt` file for the complete list of dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.