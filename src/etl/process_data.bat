echo off
title Pull and clean Chicago crime data
:: Runs all py files to clean and organize data files

echo NOTICE: data storage requires about 7 gigs on local drive. 
echo Please kill script if insufficient storage available.
echo Checking and installing requirements..
REM pip install -r requirements.txt

python get_requs.py

echo .
echo .
echo .
echo Querying crime data (2001 to current) from City of Chicago by year...
echo Please be patient :)

python pull_raw_data.py

echo .
echo .
echo .
echo Raw data imported successfully! 
echo Available in data/raw/
echo .
echo .
echo .
echo Aggregating data into complete data set...

python aggregate_data.py

echo .
echo .
echo .
echo Aggregation complete! 
echo Available in data/interim/
echo .
echo .
echo .
echo Cleaning data and processing model requirements...

python clean.py

echo .
echo .
echo . 
echo Data processing complete! :)
echo Available in data/processed
echo .
echo .
echo .
echo crime.csv = final data set, x_counts = model_requs
echo .
echo .
echo .
echo Creating MySQL Storage and uploading...

python load_into_sql.py

echo .
echo .
echo .
echo SQL storage successful!
echo .
echo .
echo .
echo ALL DONE! Have a good day :)