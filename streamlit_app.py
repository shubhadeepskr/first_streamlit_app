import streamlit
streamlit.title('Cafe Menu')
streamlit.header('Breakfast Menu')
streamlit.text('>>Omega 3 & Blueberry Oatmeal')
streamlit.text('>>Kale, Spinach & Rocket Smoothie')
streamlit.text('>>Hard-Boiled Free-Range Egg')

streamlit.header('Build your own smoothie!')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado', 'Grapes'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
