echo off
title Updates Chicago crime data
:: Runs all py files to clean and organize updated data

echo Updating crime data based on last import or update.
echo Please wait ;)

python updater.py

echo .
echo .
echo .
echo Data Successfully updated!
echo Available in data/interim/aggregate_data.csv, Old version labeled BACKUP-previous_version.
echo .
echo .
echo .
echo Cleaning new version of data and processing model requirements...

python clean.py
python clean_new_data.py
echo .
echo .
echo . 
echo Data processing complete! :)
echo Available in data/processed
echo .
echo .
echo .
echo crime.csv = final data set, [detail_level]_counts = model_requs
echo .
echo .
echo .
echo Inserting new files into MySQL storage...

python update_sql.py

echo .
echo .
echo .
echo SQL storage successful!
echo .
echo .
echo .
echo ALL DONE! Have a good day :)