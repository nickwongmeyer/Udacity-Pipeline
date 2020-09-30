# Airflow Data Pipeline Project in Sparkify

Project 5: Data Pipeline 

# Project Overview

The learning outcome of this project is about how to use Apache Airflow running automation under a regular basis, including instant time to time, hourly, daily, weekly, monthly or yearly. The basis of running an Airflow are highly referred from running an ETL pipeline first to deliver the data through AWS cloud, and re-structral the data precisely which enable the data analyst the run the analysis more effectively. 

As mentioned briefly, the song and log data under JSON format were loaded from Udacity publicly accessible S3 bucket via ETL, and processes the data under a star schema into the AWS Redshift. Once the data are run regularly the scheduled ETL, a data quality check will be implemented to ensure the data are run smoothly under the regular monitoring process.

# Configuration 
- AWS credentials must be filled in probably under the connection menu in Airflow, more importantly, access them via the Secret Access Key ID and Secret access Key, ensuring that the user has full adminaccess under 'AmazonRedshiftFullAccess' and 'AmazonS3ReadOnlyAccess'. 

- Redshift Connection via Postgres Database application, ensuring the host is the endpoint of redshift must be filled, along with your schema name, name and password of the redshift login and the port must be 5439.  

#Structure 





# Result of the project

Once if all the steps are successfully run, all the spot under the tree diagram should be turn into green. 

<img src="images/tree_graph.PNG">



The frame under each procedure should be turn into green as long as they are run sucessfully. 

<img src="images/pipeline_graph.PNG">
