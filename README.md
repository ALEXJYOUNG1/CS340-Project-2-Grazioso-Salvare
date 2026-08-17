# CS340-Project-2-Grazioso-Salvare
Interactive MongoDB dashboard for Grazioso Salvare that filters Austin Animal Center data for search-and-rescue training candidates.

# CS340 Project 2 - Grazioso Salvare Dashboard

## Project Overview

This project is an interactive client/server dashboard developed for **Grazioso Salvare**, an organization that identifies dogs with characteristics suitable for search-and-rescue training. The dashboard uses animal shelter data from the **Austin Animal Center Outcomes** dataset and provides an intuitive interface for identifying potential rescue-training candidates.

The application connects a **MongoDB** database to a Python-based **Dash** web application. Users can filter available dogs according to the breed, sex, and age requirements established by Grazioso Salvare for different types of rescue work.

The dashboard supports the following rescue categories:

* **Water Rescue**
* **Mountain or Wilderness Rescue**
* **Disaster Rescue or Individual Tracking**
* **Reset**, which restores the complete dataset

When a rescue category is selected, the dashboard dynamically updates the **data table, breed distribution chart, and geolocation map** to display only animals matching the selected criteria.

## Dashboard Features

The dashboard includes:

* Grazioso Salvare branding and logo
* Interactive rescue-type filtering
* Searchable and sortable animal data table
* Pagination for easier navigation through large datasets
* Dynamic breed distribution pie chart
* Interactive geolocation map
* Individual animal selection and location display
* MongoDB-backed filtering using the Project One CRUD module

## Rescue Animal Filtering Criteria

### Water Rescue

Dogs are selected using the following criteria:

* Labrador Retriever Mix
* Chesapeake Bay Retriever
* Newfoundland
* Intact Female
* 26 to 156 weeks old

### Mountain or Wilderness Rescue

Dogs are selected using the following criteria:

* German Shepherd
* Alaskan Malamute
* Old English Sheepdog
* Siberian Husky
* Rottweiler
* Intact Male
* 26 to 156 weeks old

### Disaster Rescue or Individual Tracking

Dogs are selected using the following criteria:

* Doberman Pinscher
* German Shepherd
* Golden Retriever
* Bloodhound
* Rottweiler
* Intact Male
* 20 to 300 weeks old

## Technologies Used

### MongoDB

MongoDB serves as the **model** portion of the application's MVC architecture. The Austin Animal Center data is stored as MongoDB documents, allowing the application to efficiently query animals according to breed, sex, age, and other attributes.

MongoDB was appropriate for this project because its document-oriented structure works well with the shelter dataset and integrates directly with Python through the **PyMongo** library.

### Python

Python provides the primary application logic and connects the different components of the system. The `AnimalShelter` CRUD class developed during Project One provides the interface between the dashboard and MongoDB.

### Dash and JupyterDash

Dash provides the **view and controller** portions of the dashboard. Dash components are used to construct the user interface, while callbacks respond to user selections and dynamically update the displayed information.

### pandas

pandas is used to convert MongoDB query results into DataFrames. These DataFrames are then supplied to the interactive Dash data table and visualization components.

### Plotly Express

Plotly Express is used to generate the dashboard's breed distribution pie chart. The visualization automatically changes as the rescue filter changes.

### Dash Leaflet

Dash Leaflet is used to create the geolocation map. Latitude and longitude values contained in the Austin Animal Center dataset allow the dashboard to display the location associated with a selected animal.

## Application Architecture

The application follows a **Model-View-Controller (MVC)** design.

* **Model:** MongoDB database and `AnimalShelter` CRUD module
* **View:** Dash data table, filtering controls, pie chart, and geolocation map
* **Controller:** Dash callback functions that process user selections and update dashboard components

The separation of these responsibilities makes the application easier to understand, maintain, and modify.

## Project Files

* `ProjectTwoDashboard.ipynb` - Main Grazioso Salvare dashboard
* `animal_shelter.py` - MongoDB CRUD module developed during Project One
* `Grazioso Salvare Logo.png` - Client branding used by the dashboard
* `README.md` - Project documentation

## Running the Project

1. Start the MongoDB service.
2. Confirm that the Austin Animal Center Outcomes dataset has been imported into the `aac` database and `animals` collection.
3. Ensure that `animal_shelter.py` is available in the project directory.
4. Open `ProjectTwoDashboard.ipynb` in Jupyter.
5. Install any required Python packages if they are not already available.
6. Run the notebook cells.
7. Launch the Dash application.
8. Select a rescue category to filter the available animals.
9. Select an animal from the table to view its location on the map.

Required Python libraries include:

```bash
pip install pymongo pandas dash jupyter-dash plotly dash-leaflet
```

## Dashboard Testing

The application was tested using each of the required rescue filters. The data table, breed distribution chart, and geolocation map dynamically update based on the selected rescue category.

### Reset / Unfiltered Dashboard

*Insert Reset dashboard screenshot here.*

### Water Rescue

The Water Rescue filter displays intact female dogs of the preferred water-rescue breeds within the required training-age range.

*Insert Water Rescue screenshot here.*

### Mountain or Wilderness Rescue

The Mountain or Wilderness Rescue filter displays intact male dogs from the preferred mountain-rescue breeds between 26 and 156 weeks old.

*Insert Mountain or Wilderness Rescue screenshot here.*

### Disaster Rescue or Individual Tracking

The Disaster Rescue or Individual Tracking filter displays intact male dogs from the preferred tracking and disaster-rescue breeds between 20 and 300 weeks old.

*Insert Disaster Rescue or Individual Tracking screenshot here.*

## Challenges and Solutions

One challenge was ensuring that MongoDB records could be displayed correctly by the Dash DataTable. MongoDB automatically creates an `_id` field using the `ObjectId` data type, which cannot be directly serialized by the Dash table. This was resolved by removing the `_id` column from the pandas DataFrame before providing the records to the dashboard.

Another challenge was keeping multiple dashboard components synchronized. Each rescue filter needed to update the data table while also causing the breed chart and geolocation map to reflect the same filtered dataset. Dash callbacks were used to connect the components so that changes in the selected rescue type propagate throughout the dashboard.

The geolocation map originally relied on numerical DataFrame column positions. Using explicit column names such as `location_lat`, `location_long`, `breed`, and `name` made the implementation more reliable and easier to maintain.

## Resources

* [MongoDB Documentation](https://www.mongodb.com/docs/)
* [PyMongo Documentation](https://pymongo.readthedocs.io/)
* [Dash Documentation](https://dash.plotly.com/)
* [Plotly Python Documentation](https://plotly.com/python/)
* [pandas Documentation](https://pandas.pydata.org/docs/)
* [Jupyter Documentation](https://jupyter.org/)

## Data Source

Austin Animal Center. (2020). *Austin Animal Center Outcomes* [Data set]. City of Austin, Texas Open Data Portal.

## Author

**Alex**
CS 340 - Client/Server Development

