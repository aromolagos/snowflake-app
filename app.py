import streamlit
import pandas

streamlit.title("Listado de comida")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

#Agregar una seccion para crear tu batido
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Cargar un listado de datos en formato csv para mostrarlo en la applicacion
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
