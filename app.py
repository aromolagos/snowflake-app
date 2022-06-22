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


#crear un filtrado con multiples selecciones
my_fruit_list = my_fruit_list.set_index('Fruit')

#Seleccion multiple
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

#Filtro a nivel de tabla
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Tabla filtrada frutas con informacion nutricional
streamlit.dataframe(fruits_to_show)
