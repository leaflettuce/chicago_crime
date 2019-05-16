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
2 - [ ] Clean, Process, and Load (ETL)
3 - [ ] EDA FTW
5 - [ ] Explore Time-Series Models
6 - [ ] Bring in External Data
7 - [ ] Build Ensemble Model
8 - [ ] Visualize and Report Results
9 - [ ] Format into a presentation.
```

## Loading Data
```
(1) Connect to crime data set
	|--> Data located at www.cityofchicago.org
	|--> To load data through bat file, request API credentials
	|--> Set API credentials into env variables 
	|----> app: CHI_API_TOKEN     key: CHI_SECRET_TOKEN

(2) RUN ./src/etl/process_data.bat
	|--> Give up to 30 minutes to run
	|--> Cleaned files will write to /data/processed/
```

## Updating Data
```
  RUN ./src/etl/update_data.bat
	|--> Give up to 15 minutes to run
	|--> Cleaned files will write to /data/processed/
	|--> Previous data set will store as data/interim/BACKUP-previous_version.csv
```

## Model Overview
```

```

## Results
```

```
