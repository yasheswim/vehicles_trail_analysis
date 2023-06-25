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


Resultant reports are present in datasets/asset_report directory

All trail datasets and Trip_Info csv files present in the datasets folder. Click [here](https://drive.google.com/file/d/1h3YtP91jBETg_rAdETIiLQi6yly18dFb/view?usp=sharing)
to access datasets folder
