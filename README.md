<# ETL Coding Test

This project is an ETL (Extract, Transform, Load) coding test designed to process data from a given URL, which is stored in various formats. The goal is to perform ETL, modeling, and visualization techniques to organize and analyze the data effectively.

## Table of Contents
- [Installation and Setup](#installation-and-setup)
- [Features](#features)
- [Functions and Reasoning for Each Feature](#functions-and-reasoning-for-each-feature)

## Installation and Setup

To install and set up the project, follow these steps:

1. Go to bash and clone the git repo: `git clone git@github.com:Hsaehyn/Abyres_ETL_Test.git`
2. Navigate to the project directory: `cd Abyres_ETL_Test`
3. Open a new terminal or on bash, create a virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
    Install dependencies after you activate the virtual environment: `pip install -r requirements.txt`
4. Fill in the credentials for `.env` file to connect to your SQL server.
5. Execute the code in `main.ipynb` and read through the explanations in the markdown section.

## Features

- Data Extraction: Extract data from the given URL.
- Data Transformation: Transform the data into a structured/tabular format suitable for analysis.
- Data Loading: Load the transformed data into a database for storage.
- Data Modeling: Model the data to establish relationships and ensure data integrity.
- Data Visualization: Visualize the data using Excel by exporting them into a .csv file.


## Functions and Reasoning for Each Feature

### Data Extraction:

Function: `extract_data(url)`

Reasoning: This function retrieves data from the specified URL, Each URL leads to a different data storing format, I have selected to collect data from the JSON file and save a copy of the .json file to my local desktop under the data directory

### Data Transformation:

Function: `transform_data(raw_data)`

Reasoning: This function processes the raw data obtained from the extraction step. It focus on data integrity and reduce redundancy when querying to make it suitable for analysis. This step involve handling missing and dupliated values, converting data types, , and possibly performing other transformations like renaming and indexing.

### Data Loading:

Function: `load_data(transformed_data)`

Reasoning: This function loads the transformed data into a database or data warehouse for storage. It ensures that the data is persistently stored and can be accessed for further analysis or reporting.

### Data Modeling:

Function: `model_data(data)`

Reasoning: This function defines the structure of the data model, including tables, columns, primary keys, and foreign keys. It establishes relationships between different entities to maintain data integrity and optimize query performance.

### Data Visualization:

Function: `visualize_data(data)`

Reasoning: This function generates visualizations that can be directlyy view by users to help them  understand the data better. It provides insights into trends, patterns, and relationships within the data, facilitating data-driven decision-making.

By implementing these features, the ETL coding test aims to demonstrate proficiency in data processing, modeling, and visualization techniques.
