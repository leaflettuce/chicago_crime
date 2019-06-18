echo off
title Updated chicaho crime data and runs new model/visuals
:: Runs all py files to clean and organize updated data

call activate tensorflow

echo --------------------
echo RUNNING DATA UPDATER
echo --------------------

cd ./etl
call update_data.bat

echo ------------------------------------------------------------
echo DATA SUCCESSFULLY PULLED, FITTING MODEL AND PRINTING VISUALS
echo ------------------------------------------------------------

cd ../model
call get_preds_and_visuals.bat

echo --------------------
echo SYSTEM FULLY UPDATED
echo --------------------

echo -------------------
echo PUSHING TO WEBSITE
echo -------------------

call robocopy E:\projects\chi_crime\reports\visuals\updated E:\projects\DSblog\content\img\chi_crime /e

cd ../..


call git add .
call git commit -m "Weekly Update."
call git push origin master


cd ../dsblog

call activate pelican1
call pelican content -s publishconf.py

call git add .
call git commit -m "Weekly Chicago Crime Visual Update."
call git push origin master

cd output
call activate root
call aws s3 sync . s3://andrewtrick.com

echo "Update Complete. <(^.^<) <(^.^)> (>^.^)>"