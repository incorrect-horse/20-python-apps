import streamlit as st
import plotly.express as px
from backend import get_data

#print(f"\nScript Running\n")

st.title("1-5 Day Weather Forecast")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecast days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky View"))
st.subheader(f"{option} for the next {days} days in {place}.")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            #temps = [dict["main"]["temp"] /10 for dict in filtered_data] # for celcius
            temps = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temps, labels={"x": "Date", "y": "Temperature(F)"})
            st.plotly_chart(figure)

        if option == "Sky View":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                    "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            img_lst = [images[i] for i in sky_conditions]
            st.image(img_lst, width=88)
            st.write("Each row represents one day's forecast at three-hour intervals.")

    except KeyError:
        st.write(f"{place.upper()} is not a valid location. Please try again.")
