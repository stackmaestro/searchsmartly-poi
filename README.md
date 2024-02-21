# Points of Interest (PoI) Data Management Service

## Stack Versions

- **Python**: 3.10 or above
- **Django**: 3.2 or later
- **Database**: SQLite (default with Django for development)
- **Additional Python Packages**: Refer to `requirements.txt`

## Setup Guide

1. **Clone the repository**:
   `git clone https://github.com/stackmaestro/searchsmartly-poi`

2. **Navigate to the project directory**:
   `cd path/to/project`

3. **Create and activate a virtual environment**:

   - macOS/Linux:
     `python -m venv venv`
     `source venv/bin/activate`
   - Windows:
     `python -m venv venv`
     `venv\Scripts\activate`

4. **Install the required dependencies**:
   `pip install -r requirements.txt`

5. **Apply the database migrations**:
   `python manage.py migrate`

6. **Create a superuser account** (optional but recommended for accessing the Django admin site):
   `python manage.py createsuperuser`

## Importing Data

To import Points of Interest (PoI) data from CSV, JSON, or XML files:

`python manage.py import_pois path/to/datafile`

- Replace `path/to/datafile` with the actual path to your CSV, JSON, or XML file containing the PoI data.
- Ensure the data file adheres to the specified format for each type.

## Run the App

To start the Django development server and access the web application:

`python manage.py runserver`

- The application will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
- Access the Django admin site at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with your superuser credentials to manage PoIs.

## Ideas for Improving

### Parallel Data Processing

Implementing parallel processing for large CSV files to reduce import times, leveraging multi-core processors by splitting files and processing them in parallel using Python's multiprocessing or concurrent.futures modules.

### Utilization of Data Processing Libraries

Incorporating libraries like Pandas for efficient data manipulation and bulk database operations, enhancing performance and simplifying data transformation.

### External API Integration

Extending functionality to fetch and synchronize data from external APIs, enriching the PoI dataset with up-to-date information and expanding data sources.

### Expanded File Support

Adding support for more file formats (e.g., Excel, Google Sheets) to increase the application's versatility in handling diverse data inputs.

### Microservices for Data Integration

Adopting a microservices architecture for scalable and flexible data ingestion, transforming data from varied API sources for database compatibility.
