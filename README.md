# Airflow Data Pipeline Project in Sparkify

Project 5: Data Pipeline 

# Project Overview

The learning outcome of this project is about how to use Apache Airflow running automation under a regular basis, including instant time to time, hourly, daily, weekly, monthly or yearly. The basis of running an Airflow are highly referred from running an ETL pipeline first to deliver the data through AWS cloud, and re-structral the data precisely which enable the data analyst the run the analysis more effectively. 

As mentioned briefly, the song and log data under JSON format were loaded from Udacity publicly accessible S3 bucket via ETL, and processes the data under a star schema into the AWS Redshift. Once the data are run regularly the scheduled ETL, a data quality check will be implemented to ensure the data are run smoothly under the regular monitoring process.

# Configuration 
- AWS credentials must be filled in probably under the connection menu in Airflow, more importantly, access them via the Secret Access Key ID and Secret access Key, ensuring that the user has full adminaccess under 'AmazonRedshiftFullAccess' and 'AmazonS3ReadOnlyAccess'. 

- Redshift Connection via Postgres Database application, ensuring the host is the endpoint of redshift must be filled, along with your schema name, name and password of the redshift login and the port must be 5439.  

# Structure and process

The steps should be followed under similar to the graph. 

The frame under each procedure should be turn into green as long as they are run sucessfully. 

<img src="images/pipeline_graph.PNG">
 
### 1.Creating table and run the ETL 
- ```create_table.sql``` a SQL queries from Project 3 in DataWarehouse in order to create structural schema in AWS redshift. 


- ```sql_queries.sql``` a SQL queries to process the data under ETL. More importantly, this will transform all the unstructural data from S3 to a required structural into the new star schema table. 


The directory as follows are placed under ```plugins/operators``` directory of the Airflow installation: 
### 2.copying the data from S3 to redshift AWS. 

- ```stage_redshift.py``` copies Json data from S3 to Redshift data warehouse into the staging tables, which was operated under ```StageToRedshiftOperator``` in ```dag``` file.

### 3.Loading the data into the structural tables set by the SQL files above  
- ```load_dimension.py``` loads a dimension tables from data in the staging tables, which was operated under ```LoadDimensionOperator``` in ```dag``` file. 

- ```load_fact.py``` loads a fact table from data in the staging tables, which was operated under ```LoadFactOperator``` in ```dag``` file. 

### 4.Running the quality check against the SQL queries. 

- ```data_quality.py``` runs a quality check passing the SQL query and ensure that the results match the arguments, or this step will be regarded as 'failure' under the graph. 

### 5.Ensuring all the coding are written correctly prior running the airflows. 

- ```udac_example_dag.py``` the task file to run the whole process of the airflow which provides the entire connectivities with all the plugins and operators from S3 > Redshift > the airflow. 


# Result of the project

Once if all the steps are successfully run, all the spot under the tree diagram should be turn into green. 

<img src="images/tree_graph.PNG">




