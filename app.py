from email.policy import default
from optparse import Option

import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
model=pickle.load(open('flight_rf.pkl','rb'))
st.title("Flight Fare Prediction System:")

# DATE OF JOURNEY
date_dep=st.date_input("Enter Your Departure Date:")
Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT").day)
Journey_Month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT").month)
# print(Journey_day,Journey_Month)
#  DEPARTURE TIME
dep_time=st.time_input("Enter Your Departure Time:")
Dept_hrs = int(pd.to_datetime(dep_time, format="%H:%M:%S").hour)
Dept_min = int(pd.to_datetime(dep_time, format="%H:%M:%S").minute)
print(Dept_min,Dept_hrs)

date_arriv=st.time_input("Enter Your Arrival Time:")
Arrival_hrs = int(pd.to_datetime(date_arriv, format="%H:%M:%S").hour)
Arrival_mins = int(pd.to_datetime(date_arriv, format="%H:%M:%S").minute)
print(Arrival_hrs,Arrival_mins)

Duration_hours = abs(Arrival_hrs - Dept_hrs)
Duratiom_mins = abs(Arrival_mins - Dept_min)
# print("Duration : ", dur_hour, dur_min)
# abs-> absolute value

Total_Stops=st.selectbox("Enter the Total no of Stops:",["0","1","2","3","4"])
print(Total_Stops)
airline=st.selectbox("From Which Airline do you want to travel:",['Airline_Jet Airways','Airline_IndiGo','Airline_Air India','Airline_Multiple carriers','Airline_SpiceJet','Airline_Vistara','Airline_GoAir','Airline_Multiple carriers Premium economy','Airline_Jet Airways Business','Airline_Vistara Premium economy','Airline_Trujet'])



if (airline == 'Airline_Jet Airways'):
    Airline_Jet_Airways = 1
    Airline_IndiGo = 0
    Airline_Air_India = 0
    Airline_Multiple_carriers = 0
    Airline_SpiceJet = 0
    Airline_Vistara = 0
    Airline_GoAir = 0
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_Jet_Airways_Business = 0
    Airline_Vistara_Premium_economy = 0
    Airline_Trujet = 0

elif (airline == 'Airline_IndiGo'):
    Airline_Jet_Airways = 0
    Airline_IndiGo = 1
    Airline_Air_India = 0
    Airline_Multiple_carriers = 0
    Airline_SpiceJet = 0
    Airline_Vistara = 0
    Airline_GoAir = 0
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_Jet_Airways_Business = 0
    Airline_Vistara_Premium_economy = 0
    Airline_Trujet = 0
elif (airline == 'Airline_Air India'):
    Airline_Jet_Airways = 0
    Airline_IndiGo = 0
    Airline_Air_India = 1
    Airline_Multiple_carriers = 0
    Airline_SpiceJet = 0
    Airline_Vistara = 0
    Airline_GoAir = 0
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_Jet_Airways_Business = 0
    Airline_Vistara_Premium_economy = 0
    Airline_Trujet = 0

elif (airline == 'Airline_Multiple carriers'):
    Airline_Jet_Airways = 0
    Airline_IndiGo = 0
    Airline_Air_India = 0
    Airline_Multiple_carriers = 1
    Airline_SpiceJet = 0
    Airline_Vistara = 0
    Airline_GoAir = 0
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_Jet_Airways_Business = 0
    Airline_Vistara_Premium_economy = 0
    Airline_Trujet = 0

elif (airline == 'Airline_SpiceJet'):
    Airline_Jet_Airways = 0
    Airline_IndiGo = 0
    Airline_Air_India = 0
    Airline_Multiple_carriers = 0
    Airline_SpiceJet = 1
    Airline_Vistara = 0
    Airline_GoAir = 0
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_Jet_Airways_Business = 0
    Airline_Vistara_Premium_economy = 0
    Airline_Trujet = 0

elif (airline == 'Airline_Vistara'):
    Jet_Airways = 0
    IndiGo = 0
    Air_India = 0
    Multiple_carriers = 0
    SpiceJet = 0
    Vistara = 1
    GoAir = 0
    Multiple_carriers_Premium_economy = 0
    Jet_Airways_Business = 0
    Vistara_Premium_economy = 0
    Trujet = 0

elif (airline == 'Airline_GoAir'):
    Airline_Jet_Airways = 0
    Airline_IndiGo = 0
    Airline_Air_India = 0
    Airline_Multiple_carriers = 0
    Airline_SpiceJet = 0
    Airline_Vistara = 0
    Airline_GoAir = 1
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_Jet_Airways_Business = 0
    Airline_Vistara_Premium_economy = 0
    Airline_Trujet = 0

elif (airline == 'Airline_Multiple carriers Premium economy'):
    Airline_Jet_Airways = 1
    Airline_IndiGo = 0
    Airline_Air_India = 0
    Airline_Multiple_carriers = 0
    Airline_SpiceJet = 0
    Airline_Vistara = 0
    Airline_GoAir = 0
    Airline_Multiple_carriers_Premium_economy = 1
    Airline_Jet_Airways_Business = 0
    Airline_Vistara_Premium_economy = 0
    Airline_Trujet = 0

elif (airline == 'Airline_Jet Airways Business'):
    Airline_Jet_Airways = 0
    Airline_IndiGo = 0
    Airline_Air_India = 0
    Airline_Multiple_carriers = 0
    Airline_SpiceJet = 0
    Airline_Vistara = 0
    Airline_GoAir = 0
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_Jet_Airways_Business = 1
    Airline_Vistara_Premium_economy = 0
    Airline_Trujet = 0
elif (airline == 'Airline_Vistara Premium economy'):
    Airline_Jet_Airways = 0
    Airline_IndiGo = 0
    Airline_Air_India = 0
    Airline_Multiple_carriers = 0
    Airline_SpiceJet = 0
    Airline_Vistara = 0
    Airline_GoAir = 0
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_Jet_Airways_Business = 0
    Airline_Vistara_Premium_economy = 1
    Airline_Trujet = 0

elif (airline == 'Airline_Trujet'):
    Airline_Jet_Airways = 0
    Airline_IndiGo = 0
    Airline_Air_India = 0
    Airline_Multiple_carriers = 0
    Airline_SpiceJet = 0
    Airline_Vistara = 0
    Airline_GoAir = 0
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_Jet_Airways_Business = 0
    Airline_Vistara_Premium_economy = 0
    Airline_Trujet = 1

else:
    Airline_Jet_Airways = 0
    Airline_IndiGo = 0
    Airline_Air_India = 0
    Airline_Multiple_carriers = 0
    Airline_SpiceJet = 0
    Airline_Vistara = 0
    Airline_GoAir = 0
    Airline_Multiple_carriers_Premium_economy = 0
    Airline_Jet_Airways_Business = 0
    Airline_Vistara_Premium_economy = 0
    Airline_Trujet = 0

# SOURCE
Source =st.selectbox("Select The Source City",['Source_Delhi','Source_Kolkata','Source_Mumbai','Source_Chennai','Source_Banglore'],value=None)
if (Source == 'Source_Delhi'):
    Source_Delhi = 1
    Source_Kolkata = 0
    Source_Mumbai = 0
    Source_Chennai = 0

elif (Source == 'Source_Kolkata'):
    Source_Delhi = 0
    Source_Kolkata = 1
    Source_Mumbai = 0
    Source_Chennai = 0

elif (Source == 'Source_Mumbai'):
    Source_Delhi = 0
    Source_Kolkata = 0
    Source_Mumbai = 1
    Source_Chennai = 0
elif (Source == 'Source_Chennai'):
    Source_Delhi = 0
    Source_Kolkata = 0
    Source_Mumbai = 0
    Source_Chennai = 1

else:
    Source_Delhi = 0
    Source_Kolkata = 0
    Source_Mumbai = 0
    Source_Chennai = 0



# Destination
# Banglore = 0 (not in column)
Source=st.selectbox("Enter the Destination City:",['Destination_Cochin','Destination_Delhi','Destination_New_Delhi','Destination_Hyderabad','Destination_Kolkata','Destination_Banglore'])
if (Source == 'Destination_Cochin'):
    Destination_Cochin = 1
    Destination_Delhi = 0
    Destination_New_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0

elif (Source == 'Destination_Delhi'):
    Destination_Cochin = 0
    Destination_Delhi = 1
    Destination_New_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0

elif (Source == 'Destination_New_Delhi'):
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_New_Delhi = 1
    Destination_Hyderabad = 0
    Destination_Kolkata = 0

elif (Source == 'Destination_Hyderabad'):
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_New_Delhi = 0
    Destination_Hyderabad = 1
    Destination_Kolkata = 0

elif (Source == 'Destination_Kolkata'):
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_New_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 1

else:
    Destination_Cochin = 0
    Destination_Delhi = 0
    Destination_New_Delhi = 0
    Destination_Hyderabad = 0
    Destination_Kolkata = 0

prediction = model.predict([[
        Total_Stops,
        Journey_day,
        Journey_Month,
        Dept_hrs,
        Dept_min,
        Arrival_hrs,
        Arrival_mins,
        Duration_hours,
        Duratiom_mins,
        Airline_Air_India,
        Airline_GoAir,
        Airline_IndiGo,
        Airline_Jet_Airways,
        Airline_Jet_Airways_Business,
        Airline_Multiple_carriers,
        Airline_Multiple_carriers_Premium_economy,
        Airline_SpiceJet,
        Airline_Trujet,
        Airline_Vistara,
        Airline_Vistara_Premium_economy,
        Source_Chennai,
        Source_Delhi,
        Source_Kolkata,
        Source_Mumbai,
        Destination_Cochin,
        Destination_Delhi,
        Destination_Hyderabad,
        Destination_Kolkata,
        Destination_New_Delhi
    ]])

if st.button("Predict"):
    query = np.array([[  Total_Stops,
        Journey_day,
        Journey_Month,
        Dept_hrs,
        Dept_min,
        Arrival_hrs,
        Arrival_mins,
        Duration_hours,
        Duratiom_mins,
        Airline_Air_India,
        Airline_GoAir,
        Airline_IndiGo,
        Airline_Jet_Airways,
        Airline_Jet_Airways_Business,
        Airline_Multiple_carriers,
        Airline_Multiple_carriers_Premium_economy,
        Airline_SpiceJet,
        Airline_Trujet,
        Airline_Vistara,
        Airline_Vistara_Premium_economy,
        Source_Chennai,
        Source_Delhi,
        Source_Kolkata,
        Source_Mumbai,
        Destination_Cochin,
        Destination_Delhi,
        Destination_Hyderabad,
        Destination_Kolkata,
        Destination_New_Delhi]])


    st.title("The Predicted Price Of Flight is:" + str(np.round(float(model.predict(query)[0]),2)))
