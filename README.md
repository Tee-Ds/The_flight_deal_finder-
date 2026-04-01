# The_flight_deal_finder-
# Automated API Data Pipeline & Aggregator

##  Overview
This project is a Python-based data pipeline designed to communicate with multiple REST APIs to aggregate, filter, and log complex JSON datasets. It tracks real-time data parameters (flight pricing and availability) and automatically structures the output into cloud-based spreadsheets. 

##  Technical Stack
* **Language:** Python 3.x
* **Libraries:** `requests`, `datetime`, `os`
* **APIs Integrated:** * Amadeus / Tequila API (Data Aggregation & JSON Parsing)
  * Sheety API (Cloud Data Logging via GET/POST requests)
  * Twilio API (Automated Alerting)
* **Key Concepts:** Object-Oriented Programming (OOP), RESTful API Architecture, Environment Variable Security.

##  Core Features
* **Dynamic Data Extraction:** Queries third-party APIs to pull real-time JSON data based on predefined analytical thresholds.
* **Data Structuring:** Parses complex nested dictionaries and lists to extract relevant data points.
* **Automated Logging:** Interfaces with the Sheety API to automatically update and format Google Sheets data.
* **Alert System:** Triggers automated SMS/Email notifications when data criteria (price drops) are met.

##  Security Note
All API keys, authentication tokens, and personal credentials are secured using environment variables (`os.environ`) and are not exposed in this repository.

---
*Developed by David Testimony*
