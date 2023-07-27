import streamlit as st
import pandas as pd 
import os
import csv
import datetime



class Prediction_input:
    def my_title_page(self):
        """_
        It is the program just for creating the webpage 
        from where i can take inputs from web and predict the vaue 
        based on my trained model
        run input webpage seprately on app.py
        and run main.py seprately. Also first run app.py and create a df will be the best option
        as i am yet to handle many exceptions with time will do it for now it is what is .  
        it will create the df that you want to predict the values after 
        training and creating our model 
        """
        if st.button("Terminate App", key="terminate_btn"):
            st.warning("Stopping the Streamlit app...")
            os._exit(0)
            
        st.title("AIRLINE PRICE PREDICTION")        
        Date_of_Journey= st.text_input("Date_of_Journey plz choose year 2019 ex: '18/05/2019' format(DD/MM/YYYY)", key = "DATE",)
##############################################################     1
        Airline = st.selectbox(" Airline" , (list(["None",'Jet Airways','IndiGo','Air India','Multiple carriers','SpiceJet','Vistara','Air Asia','GoAir','Multiple carriers Premium economy','Jet Airways Business','Vistara Premium economy','Trujet'])), key = "AIRLINE")
        if Airline == "Air Asia":
            Source = st.selectbox("Select Source/Boarding", (['None', 'Bangalore', 'Kolkata', 'Delhi']), key="Airasia")

            if Source == 'Bangalore':
                Destination = st.selectbox("Destination", (['None', 'New Delhi', 'Delhi']), key="Bangalore")
                if Destination == 'Delhi':
                    Route = st.selectbox("Route", (['None', 'BLR → DEL']))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")

                if Destination == 'New Delhi':
                    Route = st.selectbox("Route", (['None', 'BLR → DEL']))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")

            if Source == 'Kolkata':
                Destination = st.selectbox("Destination", (['None', 'Bangalore']), key="Kolkata")
                if Destination == 'Bangalore':
                    Route = st.selectbox("Route", (['None', 'CCU → BLR', 'CCU → DEL → BLR', 'CCU → BBI → BLR', 'CCU → IXR → DEL → BLR']))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")

            if Source == "Delhi":
                Destination = st.selectbox("Destination", (['None', 'Cochin']), key="Delhi")
                if Destination == 'Cochin':
                    Route = st.selectbox("Route", (['None', 'DEL → BLR → COK']))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")

######################################################         2          
                    
        if Airline == "Air India":
            
            Source= st.selectbox("Select Source/Boarding", (list(['None','Kolkata', 'Delhi', 'Chennai', 'Banglore', 'Mumbai'])), key = "AirIndia")
        
            if Source == 'Banglore':
                Destination = st.selectbox("Destination", (list(['None','New Delhi', 'Delhi'])), key = "Banglore")
                if Destination == 'Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → DEL'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")
                if Destination == 'New Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → COK → DEL', 'BLR → BOM → DEL', 'BLR → BOM → AMD → DEL','BLR → MAA → DEL', 'BLR → DEL', 'BLR → BOM → JDH → DEL','BLR → CCU → DEL', 'BLR → HYD → DEL', 'BLR → CCU → GAU → DEL','BLR → BOM → BHO → DEL', 'BLR → AMD → DEL', 'BLR → VGA → DEL','BLR → BOM → IDR → DEL', 'BLR → BBI → DEL','BLR → CCU → BBI → DEL', 'BLR → BOM → NAG → DEL','BLR → CCU → BBI → HYD → DEL', 'BLR → GAU → DEL','BLR → GOI → DEL', 'BLR → HYD → VGA → DEL','BLR → VGA → HYD → DEL', 'BLR → BOM → IDR → GWL → DEL','BLR → TRV → COK → DEL', 'BLR → BOM → UDR → DEL','BLR → VGA → VTZ → DEL', 'BLR → HBX → BOM → BHO → DEL','BLR → HBX → BOM → AMD → DEL', 'BLR → HBX → BOM → NAG → DEL','BLR → BOM → IXC → DEL', 'BLR → CCU → BBI → HYD → VGA → DEL'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")

            if Source == 'Kolkata' :
                Destination = st.selectbox("Destination", (list(['None', 'Banglore'])), key = "Kolkata" )
      
                if Destination == 'Banglore':
                    Route = st.selectbox("Route", (list(['None','CCU → IXR → BBI → BLR', 'CCU → GAU → DEL → BLR', 'CCU → BLR','CCU → HYD → BLR', 'CCU → BOM → BLR', 'CCU → MAA → BLR','CCU → BBI → BOM → BLR', 'CCU → JAI → BOM → BLR','CCU → BBI → BLR', 'CCU → IXR → DEL → BLR','CCU → BOM → COK → BLR', 'CCU → BOM → GOI → BLR','CCU → DEL → AMD → BLR', 'CCU → DEL → COK → BLR','CCU → DEL → BLR', 'CCU → BOM → AMD → BLR','CCU → BBI → IXR → DEL → BLR', 'CCU → JAI → DEL → BLR','CCU → VNS → DEL → BLR', 'CCU → BBI → HYD → BLR','CCU → GAU → BLR', 'CCU → DEL → VGA → BLR','CCU → DEL → COK → TRV → BLR', 'CCU → BOM → TRV → BLR','CCU → BOM → HBX → BLR', 'CCU → IXZ → MAA → BLR','CCU → GAU → IMF → DEL → BLR', 'CCU → IXB → DEL → BLR'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")
            if Source == "Delhi":
                Destination = st.selectbox("Destination", (list(['None', 'Cochin'])), key= "Delhi")
                if Destination == 'Cochin':
                    Route = st.selectbox("Route", (list(['None','DEL → BLR → COK', 'DEL → AMD → BOM → COK','DEL → CCU → BOM → COK', 'DEL → MAA → COK','DEL → BHO → BOM → COK', 'DEL → JDH → BOM → COK','DEL → BOM → COK', 'DEL → GOI → BOM → COK', 'DEL → COK','DEL → TRV → COK', 'DEL → UDR → BOM → COK','DEL → HYD → MAA → COK', 'DEL → JAI → BOM → COK','DEL → RPR → NAG → BOM → COK', 'DEL → HYD → BOM → COK','DEL → NAG → BOM → COK', 'DEL → LKO → BOM → COK'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")               
            if Source == "Chennai":
                Destination = st.selectbox("Destination", (list(['None', 'Kolkata'])), key= "Delhi")
                if Destination == 'Kolkata':
                    Route = st.selectbox("Route", (list(['None','MAA → CCU'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")               
            if Source == "Mumbai":
                Destination = st.selectbox("Destination", (list(['None', 'Hyderabad'])), key= "Delhi")
                if Destination == 'Hyderabad':
                    Route = st.selectbox("Route", (list(['None','BOM → HYD', 'BOM → JDH → DEL → HYD', 'BOM → AMD → ISK → HYD','BOM → BHO → DEL → HYD', 'BOM → DEL → HYD','BOM → JDH → JAI → DEL → HYD', 'BOM → COK → MAA → HYD','BOM → CCU → HYD', 'BOM → GOI → PNQ → HYD','BOM → BLR → CCU → BBI → HYD', 'BOM → MAA → HYD','BOM → RPR → VTZ → HYD', 'BOM → IDR → DEL → HYD','BOM → BLR → HYD', 'BOM → JAI → DEL → HYD', 'BOM → BBI → HYD'])))        
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")   
 ##########################################            3       
        if Airline == "GoAir":
            
            Source= st.selectbox("Select Source/Boarding", (list(['None', 'Delhi','Banglore', 'Kolkata'])), key = "GOAir")
        
            if Source == 'Banglore':
                Destination = st.selectbox("Destination", (list(['None','Delhi', 'New Delhi'])), key = "Banglore")
                if Destination == 'Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → DEL'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")
                if Destination == 'New Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → DEL', 'BLR → GOI → DEL'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")
 
            if Source == 'Kolkata' :
                Destination = st.selectbox("Destination", (list(['None', 'Banglore'])), key = "Kolkata" )
        
                if Destination == 'Banglore':
                    Route = st.selectbox("Route", (list(['None','CCU → BOM → BLR', 'CCU → AMD → BLR', 'CCU → BLR','CCU → HYD → BLR'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")

            if Source == "Delhi":
                Destination = st.selectbox("Destination", (list(['None', 'Cochin'])), key= "Delhi")
                if Destination == 'Cochin':
                    Route = st.selectbox("Route", (list(['None','DEL → BOM → COK', 'DEL → AMD → COK', 'DEL → HYD → COK'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")
                    
############################################# 4
        if Airline == "Jet Airways":
            
            Source= st.selectbox("Select Source/Boarding", (list(['None','Delhi', 'Banglore', 'Kolkata', 'Mumbai'])), key = "Jet Airways")
            
            if Source == 'Banglore':
                Destination = st.selectbox("Destination", (list(['None','New Delhi', 'Delhi'])), key = "Banglore")
                if Destination == 'Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → DEL'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")
                if Destination == 'New Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → DEL'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")
                            

            if Source == 'Kolkata' :
                Destination = st.selectbox("Destination", (list(['None', 'Banglore'])), key = "Kolkata" )

                if Destination == 'Banglore':
                    Route = st.selectbox("Route", (list(['None','CCU → BOM → BLR', 'CCU → DEL → BLR', 'CCU → GAU → BLR','CCU → BOM → PNQ → BLR'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")

            if Source == "Mumbai":
                Destination = st.selectbox("Destination", (list(['None', 'Hyderabad'])), key= "Mumbai")
                if Destination == 'Hyderabad':
                    Route = st.selectbox("Route", (list(['None','BOM → HYD', 'BOM → DED → DEL → HYD', 'BOM → DEL → HYD','BOM → BDQ → DEL → HYD', 'BOM → UDR → DEL → HYD','BOM → JDH → DEL → HYD', 'BOM → IDR → DEL → HYD','BOM → VNS → DEL → HYD'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")
            if Source == "Delhi":
                
                    Destination = st.selectbox("Destination", (list(['None', 'Cochin'])), key= "Delhi")
                    if Destination == 'Cochin':
                        Route = st.selectbox("Route", (list(['None','DEL → LKO → BOM → COK', 'DEL → BOM → COK','DEL → IDR → BOM → COK', 'DEL → NAG → BOM → COK','DEL → AMD → BOM → COK', 'DEL → COK', 'DEL → JAI → BOM → COK','DEL → ATQ → BOM → COK', 'DEL → BDQ → BOM → COK','DEL → JDH → BOM → COK', 'DEL → UDR → BOM → COK','DEL → BHO → BOM → COK', 'DEL → DED → BOM → COK','DEL → MAA → BOM → COK', 'DEL → IXC → BOM → COK','DEL → CCU → BOM → COK'])))     
                        if Route:
                            length = len(Route.split(" → "))
                            if length == 2:
                                Total_Stops = 'non-stop'
                                st.write(Total_Stops)
                            elif length == 3:
                                Total_Stops = '1 stop'
                                st.write(Total_Stops)
                            elif length == 4:
                                Total_Stops = '2 stops'
                                st.write(Total_Stops)
                            elif length == 5:
                                Total_Stops = '3 stops'
                                st.write(Total_Stops)
                            elif length == 6:
                                Total_Stops = '4 stops'
                                st.write(Total_Stops)
                            else:
                                st.write("Please Select the Route")     

 ##########################################          5         
        if Airline == "IndiGo":
            
            Source= st.selectbox("Select Source/Boarding", (list(['None', 'Banglore', 'Kolkata', 'Delhi', 'Chennai', 'Mumbai'])), key = "Indigo")
        
            if Source == 'Banglore':
                Destination = st.selectbox("Destination", (list(['None','Delhi', 'New Delhi'])), key = "Banglore")
                if Destination == 'Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → DEL'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")  
                if Destination == 'New Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → DEL', 'BLR → NAG → DEL', 'BLR → HYD → DEL','BLR → LKO → DEL', 'BLR → BOM → DEL', 'BLR → IDR → DEL','BLR → GOI → DEL', 'BLR → MAA → DEL', 'BLR → STV → DEL','BLR → AMD → DEL'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")  

            if Source == 'Kolkata' :
                Destination = st.selectbox("Destination", (list(['None', 'Banglore'])), key = "Kolkata" )
         
                if Destination == 'Banglore':
                    Route = st.selectbox("Route", (list(['None','CCU → NAG → BLR', 'CCU → BLR', 'CCU → PNQ → BLR','CCU → HYD → BLR', 'CCU → MAA → BLR', 'CCU → BBI → BLR','CCU → PAT → BLR', 'CCU → GAU → BLR', 'CCU → RPR → HYD → BLR','CCU → VTZ → BLR', 'CCU → IXA → BLR', 'CCU → BOM → BLR'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")  
            if Source == "Delhi":
                Destination = st.selectbox("Destination", (list(['None', 'Cochin'])), key= "Delhi")
                if Destination == 'Cochin':
                    Route = st.selectbox("Route", (list(['None','DEL → LKO → COK', 'DEL → BOM → COK', 'DEL → BLR → COK','DEL → MAA → COK', 'DEL → HYD → COK', 'DEL → COK','DEL → HYD → MAA → COK', 'DEL → PNQ → COK', 'DEL → AMD → COK','DEL → BBI → COK', 'DEL → TRV → COK'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")  
            if Source == "Chennai":
                Destination = st.selectbox("Destination", (list(['None', 'Kolkata'])), key= "Delhi")
                if Destination == 'Kolkata':
                    Route = st.selectbox("Route", (list(['None','MAA → CCU'])))  
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")   
                        
            if Source == "Mumbai":
                Destination = st.selectbox("Destination", (list(['None', 'Hyderabad'])), key= "Delhi")
                if Destination == 'Cochin':
                    Route = st.selectbox("Route", (list(['None','BOM → HYD', 'BOM → HYD, BOM → GOI → HYD'])))    
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")   
################################################## 6
        if Airline == "Jet Airways Business":
            
            Source= st.selectbox("Select Source/Boarding", (list(['None', 'Banglore', 'Delhi'])), key = "Jet Airways Buisness")
        
            if Source == 'Banglore':
                Destination = st.selectbox("Destination", (list(['None','New Delhi'])), key = "Banglore")
                if Destination == 'Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → DEL'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")   
                if Destination == 'New Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → BOM → DEL', 'BLR → MAA → DEL'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")   
                        
            
            if Source == "Delhi":
                Destination = st.selectbox("Destination", (list(['None', 'Cochin'])), key= "Delhi")
                if Destination == 'Cochin':
                    Route = st.selectbox("Route", (list(['None','DEL → ATQ → BOM → COK'])))  
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")                    
##################################################### 7
        if Airline == "Multiple carriers":
            
            Source= st.selectbox("Select Source/Boarding", (list(['None','Delhi'])), key = "Multiple carriers")
            if Source == "Delhi":
                Destination = st.selectbox("Destination", (list(['None', 'Cochin'])), key= "Delhi")
                if Destination == 'Cochin':
                    Route = st.selectbox("Route", (list(['None','DEL → BOM → COK', 'DEL → HYD → COK', 'DEL → IXU → BOM → COK','DEL → IDR → BOM → COK', 'DEL → HYD → MAA → COK','DEL → GWL → IDR → BOM → COK'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")  
###################################################################### 8

        if Airline == "Multiple carriers Premium economy":
            
            Source= st.selectbox("Select Source/Boarding", (list(['None','Delhi'])), key = "Multiple carriers Premium economy")
            if Source == "Delhi":
                Destination = st.selectbox("Destination", (list(['None', 'Cochin'])), key= "Delhi")
                if Destination == 'Cochin':
                    Route = st.selectbox("Route", (list(['None','DEL → BOM → COK'])))
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")  
             
############################################################################    9                
        #complete done
        if Airline == "SpiceJet":
                
                Source= st.selectbox("Select Source/Boarding", (list(['None','Kolkata','Delhi','Banglore','Chennai','Mumbai'])), key = "SpiceJet")
                #done
                if Source == 'Banglore':
                    Destination = st.selectbox("Destination", (list(['None','Delhi','New Delhi'])), key = "Banglore")
                    if Destination == 'Delhi':
                        Route = st.selectbox("Route", (list(['None','BLR → DEL'])))
                        if Route:
                            length = len(Route.split(" → "))
                            if length == 2:
                                Total_Stops = 'non-stop'
                                st.write(Total_Stops)
                            elif length == 3:
                                Total_Stops = '1 stop'
                                st.write(Total_Stops)
                            elif length == 4:
                                Total_Stops = '2 stops'
                                st.write(Total_Stops)
                            elif length == 5:
                                Total_Stops = '3 stops'
                                st.write(Total_Stops)
                            elif length == 6:
                                Total_Stops = '4 stops'
                                st.write(Total_Stops)
                            else:
                                st.write("Please Select the Route")  
                    if Destination == 'New Delhi':
                        Route = st.selectbox("Route", (list(['None','BLR → DEL', 'BLR → PNQ → DEL', 'BLR → HYD → DEL'])))
                        if Route:
                            length = len(Route.split(" → "))
                            if length == 2:
                                Total_Stops = 'non-stop'
                                st.write(Total_Stops)
                            elif length == 3:
                                Total_Stops = '1 stop'
                                st.write(Total_Stops)
                            elif length == 4:
                                Total_Stops = '2 stops'
                                st.write(Total_Stops)
                            elif length == 5:
                                Total_Stops = '3 stops'
                                st.write(Total_Stops)
                            elif length == 6:
                                Total_Stops = '4 stops'
                                st.write(Total_Stops)
                            else:
                                st.write("Please Select the Route")  
                    
                #done
                if Source == 'Kolkata' :
                    Destination = st.selectbox("Destination", (list(['None', 'Banglore'])), key = "Kolkata" )
                
                    if Destination == 'Banglore':
                        Route = st.selectbox("Route", (list(['None','CCU → BLR', 'CCU → MAA → BLR', 'CCU → IXB → BLR','CCU → PNQ → BLR', 'CCU → KNU → BLR']))) 
                        if Route:
                            length = len(Route.split(" → "))
                            if length == 2:
                                Total_Stops = 'non-stop'
                                st.write(Total_Stops)
                            elif length == 3:
                                Total_Stops = '1 stop'
                                st.write(Total_Stops)
                            elif length == 4:
                                Total_Stops = '2 stops'
                                st.write(Total_Stops)
                            elif length == 5:
                                Total_Stops = '3 stops'
                                st.write(Total_Stops)
                            elif length == 6:
                                Total_Stops = '4 stops'
                                st.write(Total_Stops)
                            else:
                                st.write("Please Select the Route")            
                # done
                if Source == "Delhi":
                    Destination = st.selectbox("Destination", (list(['None', 'Cochin'])), key= "Delhi")
                    if Destination == 'Cochin':
                        Route = st.selectbox("Route", (list(['None','DEL → PNQ → COK', 'DEL → MAA → COK', 'DEL → BLR → COK'])))
                        if Route:
                            length = len(Route.split(" → "))
                            if length == 2:
                                Total_Stops = 'non-stop'
                                st.write(Total_Stops)
                            elif length == 3:
                                Total_Stops = '1 stop'
                                st.write(Total_Stops)
                            elif length == 4:
                                Total_Stops = '2 stops'
                                st.write(Total_Stops)
                            elif length == 5:
                                Total_Stops = '3 stops'
                                st.write(Total_Stops)
                            elif length == 6:
                                Total_Stops = '4 stops'
                                st.write(Total_Stops)
                            else:
                                st.write("Please Select the Route")  
                # done       
                if Source == "Chennai":
                    Destination = st.selectbox("Destination", (list(['None', 'Kolkata'])), key= "Delhi")
                    if Destination == 'Kolkata':
                        Route = st.selectbox("Route", (list(['None','MAA → CCU'])))  
                        if Route:
                            length = len(Route.split(" → "))
                            if length == 2:
                                Total_Stops = 'non-stop'
                                st.write(Total_Stops)
                            elif length == 3:
                                Total_Stops = '1 stop'
                                st.write(Total_Stops)
                            elif length == 4:
                                Total_Stops = '2 stops'
                                st.write(Total_Stops)
                            elif length == 5:
                                Total_Stops = '3 stops'
                                st.write(Total_Stops)
                            elif length == 6:
                                Total_Stops = '4 stops'
                                st.write(Total_Stops)
                            else:
                                st.write("Please Select the Route")  
                # done           
                if Source == "Mumbai":
                    Destination = st.selectbox("Destination", (list(['None', 'Hyderabad'])), key= "Delhi")
                    if Destination == 'Hyderabad':
                        Route = st.selectbox("Route", (list(['None','BOM → HYD', 'BOM → JLR → HYD'])))  
                        if Route:
                            length = len(Route.split(" → "))
                            if length == 2:
                                Total_Stops = 'non-stop'
                                st.write(Total_Stops)
                            elif length == 3:
                                Total_Stops = '1 stop'
                                st.write(Total_Stops)
                            elif length == 4:
                                Total_Stops = '2 stops'
                                st.write(Total_Stops)
                            elif length == 5:
                                Total_Stops = '3 stops'
                                st.write(Total_Stops)
                            elif length == 6:
                                Total_Stops = '4 stops'
                                st.write(Total_Stops)
                            else:
                                st.write("Please Select the Route")                
#######################################################       10
        if Airline == "Trujet":
            
            Source= st.selectbox("Select Source/Boarding", (list(['None','Mumbai'])), key = "Trujet")
            #done            
            if Source == "Mumbai":
                Destination = st.selectbox("Destination", (list(['None', 'Hyderabad'])), key= "Delhi")
                if Destination == 'Hyderabad':
                    Route = st.selectbox("Route", (list(['None','BOM → NDC → HYD'])))   
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")                  
##########################################################   11

        if Airline == "Vistara":
            
            Source= st.selectbox("Select Source/Boarding", (list(['None','Mumbai'])), key = "Vistara")
            #done            
            if Source == "Mumbai":
                Destination = st.selectbox("Destination", (list(['None', 'Hyderabad'])), key= "Delhi")
                if Destination == 'Hyderabad':
                    Route = st.selectbox("Route", (list(['None','BOM → NDC → HYD'])))  
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")                 
                    
#########################################            12     
        if Airline == "Vistara Premium economy":
            
            Source= st.selectbox("Select Source/Boarding", (list(['Banglore', 'Chennai'])), key = "Vistara Premium economy")
            #done
            if Source == 'Banglore':
                Destination = st.selectbox("Destination", (list(['None','New Delhi'])), key = "Banglore")
                
                if Destination == 'New Delhi':
                    Route = st.selectbox("Route", (list(['None','BLR → DEL'])))  
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")  
        #done        
            if Source == "Chennai":
                Destination = st.selectbox("Destination", (list(['None', 'Kolkata'])), key= "Delhi")
                if Destination == 'Kolkata':
                    Route = st.selectbox("Route", (list(['None','MAA → CCU'])))  
                    if Route:
                        length = len(Route.split(" → "))
                        if length == 2:
                            Total_Stops = 'non-stop'
                            st.write(Total_Stops)
                        elif length == 3:
                            Total_Stops = '1 stop'
                            st.write(Total_Stops)
                        elif length == 4:
                            Total_Stops = '2 stops'
                            st.write(Total_Stops)
                        elif length == 5:
                            Total_Stops = '3 stops'
                            st.write(Total_Stops)
                        elif length == 6:
                            Total_Stops = '4 stops'
                            st.write(Total_Stops)
                        else:
                            st.write("Please Select the Route")   
                    
##############################################################     

        # Function to format time in "hh:mm" format
        def format_time(time):
            return f"{time // 3600:02d}h {(time // 60) % 60:02d}m"

# Get the departure time from the user using 24-hour clock format
        Dep_time = st.time_input("Departure Time")

        # Get the arrival time from the user using 24-hour clock format
        Arrival_time = st.time_input("Arrival Time")

        # Combine the date with the time to create datetime objects
        # Here, we use a dummy date (e.g., 2023-01-01) as the date since we only care about the time.
        dummy_date = datetime.date(2023, 1, 1)
        Dep_datetime = datetime.datetime.combine(dummy_date, Dep_time)
        Arrival_datetime = datetime.datetime.combine(dummy_date, Arrival_time)

        # Calculate the duration between departure and arrival times and store it in a variable
        if Dep_datetime and Arrival_datetime:
            if Arrival_datetime < Dep_datetime:
                # Add a day to the arrival time if it's less than the departure time (assuming same-day arrival)
                Arrival_datetime += datetime.timedelta(days=1)

            durations = Arrival_datetime - Dep_datetime

            # Format the duration using the custom function
            Duration = format_time(durations.seconds)

            # Display the duration
            st.write("Duration:", Duration)
############## Gett Addditional Info 

        Additional_Info = st.selectbox("Additional_Info", (['No info', 'In-flight meal not included','No check-in baggage included', '1 Short layover', 'No Info','1 Long layover', 'Change airports', 'Business class','Red-eye flight', '2 Long layover']), key= "Additional_info")
        if st.checkbox("Click when all the information is filled"):
            Airline_dictionary = {
                'Airline' : Airline,
                "Date_of_Journey" :Date_of_Journey,
                "Source" : Source,
                "Destination":Destination,
                "Route": Destination,
                "Dep_Time":Dep_time,
                "Arrival_Time":Arrival_time,
                "Duration":Duration,
                "Total_Stops":Total_Stops,
                "Additional_Info":Additional_Info     
            }

            if st.checkbox("Click If you have given all the correct Information"):
                st.write(Airline_dictionary)
                if st.checkbox("write dict values to dataframe"):
                    df = pd.DataFrame([Airline_dictionary])
                    st.write(df)
                    if st.checkbox("create_csv_file"):
                        with open("airline.csv", mode="w", newline="") as csvfile:
                            fieldnames = list(Airline_dictionary.keys())
                            values = list(Airline_dictionary.values())
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerow(Airline_dictionary)
                            st.write("done")
                        
if __name__ == "__main__":
    webpage  = Prediction_input()                
    title_input_page = webpage.my_title_page()











    
    
    
