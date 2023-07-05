This is a case study that I have worked on as a part of assessment process in an organization. 

The dataset folder contains CSV files containing vehicle trails. Each file contains the trail of a unique vehicle.
The parameters inside each of these csv files are as follows:

fk_asset_id : unique identifier for the vehicle
lic_plate_no : registration number of the vehicle
lat : latitude of the point
lon : longitude of the point
lname : geocoded location name of the point
tis : epoch timestamp in UTC 0:00:00
spd : speed in kmph
harsh_acceleration : boolean flag representing if harsh acceleration occured at the point
hbk : boolean flag representing if harsh braking occured at the point
osf : boolean flag representing if overspeeding occured at the point

Any other parameters present in the file can be ignored.



The file "Trip-Info.csv" contains information related to trips completed by all the vehicles.
The parameters inside "Trip-Info.csv" file are as follows:

trip_id : unique identifier for the trip
transporter_name: name of the transport company to which the vehicle belongs.
quantity: quantity of material carried for a trip
vehicle_number : registration number of the vehicle
date_time : timestamp of trip creation in YYYYMMDDHHMMSS format


You need to build an API to generate an asset report in excel format.
The API needs to take start time and end time in epoch format as input parameters.

The report must contain the following columns:
License plate number | Distance | Number of Trips Completed | Average Speed | Transporter Name | Number of Speed Violations

Each row in the report should represent a unique vehicle. The computation of the above mentioned columns will have to be done for the 
period between the start time and end time passed in the API call.
The API should send a suitable error response if there is no data available for the time period mentioned by the user.


Resultant reports are present in datasets/asset_report directory(NOT present in the repository because of huge size, available in the link below)

All trail datasets, asset report and Trip_Info csv files present in the datasets folder. Click [here](https://drive.google.com/file/d/1Dl7NhvStj_xgqvRJAI7pQ6UxsmF92zZa/view?usp=drive_link)
to access datasets folder

-- **assumptions that I have made**

-- Lat and long values assumed to be in degrees, hence have converted into radians before calculating distance

-- Aggregated distance values in kilometers

-- Report generated between time periods end_time = 1519842815 and start_time = 1519964409

-- If only start time is  mentioned, api will generate report from start date till max date available in the csv trail reports

-- -- If only end time is  mentioned, api will generate report from min date till end time available in the csv trail reports

-- If both end time and start times are not mentioned, api iterates through all trail data and gives aggregated report

-- Use uvicorn apis:app --reload to start fastapi server

-- use local url --> http://localhost:8000/api/generate_report?start_time=1525145685&end_time=1526543776 to call API from Postman

-- ignore both starttime and end time params in url if you want to keep both none

-- If date range entered does not exist, message "Data not available for given daterange" appears

-- Please find report in datasets/asset_report directory

-- For distance calculation -- trail reports have 0 and null values present in lat long columns, this creates problem in calculating correct distance value, hence while calculating distance, latitude and longitude columns with null and zero rows are ignored
