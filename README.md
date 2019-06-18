# Chicago Crime Analysis and Forecaster
Data life-cycle project using Chicago crime data to better understand crime trends in the city and to predict future crime rates for 2019. Conducted for SNHU Data Analytics capstone project.

## Goals
```
- Identify outliers and trends within Chicago's crime data through eda
- Map out crime rates by area of city (ward)
- Identify peak hours for Chicago crime to occur.
- Model time-series of hourly crime rates to create forecaster
- Create visuals which impart time-series and hourly trends in crime. 
- Form a final report and presentation to impart Business Value of project to stakeholders
```

## Business Questions
```
- Can hourly crime rates be accurately predicted?
- Are there any temporal trends in the data? 
- Can predictions be split by neighborhood to specifically identify resource needs?
```

## Hypothesis
```
- Crime rates can be estimated based upon time of hour and day of week..
- There is a downward trend (excluding seasonality and cycle) in overall annual crime rates.
- Certain hours are more likely to have higher rates of crime than others.
- Some neighborhoods have higher variability in crime rates than others.

```

## Overall Process
 
```
1 - [X] Import Data
2 - [X] Clean, Process, and Load (ETL)
3 - [X] EDA FTW
5 - [X] Build Time-Series Models
6 - [X] Bring in External Data
7 - [X] Complete Ensemble Model
8 - [X] Visualize and Report Results
9 - [X] Format into a presentation.
```

## Loading Data
```
(1) Connect to crime data set
	|--> Data located at www.cityofchicago.org
	|--> To load data through bat file, request API credentials
	|--> Set API credentials into env variables 
	|----> key: CHI_API_TOKEN 

(2) Set up storage environment
	|--> Assumes MySQL Server 8.0 on localhost
	|--> User defaults to 'root (change in load_into_sql.py if needed)
	|--> Set MySQL root user password into env variables 
	|----> pass: MYSQL_PASS

(3) RUN ./src/etl/process_data.bat
	|--> Give up to 35 minutes to run
	|--> Cleaned files will write to /data/processed/
	|--> Data also be loaded into MySQL DB
	|----> DB: chicago_crime, TABLE: crime
```

## Updating Data
```
  RUN ./src/etl/update_data.bat
	|--> Give up to 15 minutes to run
	|--> Cleaned files will write to /data/processed/
	|--> Previous data set will store as data/interim/BACKUP-previous_version.csv
	|--> MySQL DB will auto-update and insert the new data
```

## Model Overview
```
Rough Idea
  (1) Seasonal ARIMA model based on weekly rates
  (2) Proportion table of percent of crime per community per day-of-week per hour_bin
  (3) Multiple (1) by (2) to create forecast matrix to schedule by!
  
Model Evaluation
   o - ARIMA model will first be evaluated with AIC and RMSE
   o - Custom Loss function: Sum of Squared elements in Error Matrix
   |--> Error Matrix = M(pred) - M(actual)
   |--> Optimize ARIMA model by minimizing loss.
   
Model Results
   o - SARIMAX best fit: (1, 1, 2)(1, 0, 1)52 
   |--> RSME of around 350,  6.8% error rate average
   o - Prediction Matrix = SARIMAX forecast * avg_prop_table
   |--> SSE average of 323
   |--> Average error per location x time intersect = 0.2
```

## Running Forecaster
```
  RUN ./src/model/get_preds_and_visuals.bat
    |--> Forecasts 6 crime rates 6 months out.
	|--> Give up to 5 minutes to run.
	|--> Predicted values will write to /data/processed/predictions.csv
	|--> Forecast and heatmap visuals will save to reports/visuals/updated/
	
  NOTE update.bat current version set for personal dir and live updating
       Edit this manually or can instead run following to update:
    |--> (1) ./etl/update_data.bat
	|--> (2) ./model/get_preds_and_visuals.bat
```

## Results
```
o -
o -
o -
o -
o -
```
