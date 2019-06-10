echo off
title Updates Chicago crime data
:: Runs all py files to clean and organize updated data

echo Running model, forecatsing, and cooking up visuals
echo Please wait ;)

python get_predictions.py

echo .
echo .
echo .
echo Forecaster Complete!
echo Forecast chart created and stored.. Heatmap time!


cd ../visuals
python matrix_map.py 

echo .
echo .
echo .Heatmap complete and stored! 
echo ALL DONE! Have a good day :)