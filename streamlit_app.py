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

streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado', 'Grapes'])
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
