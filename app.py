import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

np.random.seed(150)

st.title('Travis Weston - DSBA 5122')
st.header('Homework 1')
st.subheader(
    '''
    Streamlit Homework 1 for DSBA 5122
    ''')


st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)


st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

st.caption('Question 1 Completed code.')
st.code('''
        x_limit = 101

x_axis = np.arange(0,x_limit)
y_data = np.random.randint(100,size=101)

df = pd.DataFrame({'x':x_axis,
                   'y':y_data})
        ''')


x_limit = 101

x_axis = np.arange(0,x_limit)
y_data = np.random.randint(100,size=101)

df = pd.DataFrame({'x':x_axis,
                   'y':y_data})

st.dataframe(data=df)

st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)

st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')

scatter = alt.Chart(df).mark_point(size=45).encode(x='x',
                                                   y='y')
st.altair_chart(scatter, use_container_width = True)

st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)
max_index = df['y'].idxmax()
min_index = df['y'].idxmin()
rng= ['red','green']
flag = 'https://cdn-icons-png.flaticon.com/512/2107/2107961.png'
df_minmax = df.loc[[min_index,max_index],]
df_minmax['img'] = flag
scatter = alt.Chart(df).mark_circle(size=30).encode(x='x',
                                                   y='y',
                                                   size='y',
                                                   color =alt.Color('y', scale=alt.Scale(range=rng)))
max_min = alt.Chart(df_minmax).mark_image(width=25,height=25).encode(
    x='x',
    y='y',
    url='img'
)
text = alt.Chart(df_minmax).mark_text(dx=-15,dy=3,color='white').encode(
    x='x',
    y='y',
    text=alt.Text('y')
)
scatt_maxmin = scatter+max_min+text

st.altair_chart(scatt_maxmin.interactive().configure_axis(
    grid=False
), use_container_width=True)
st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Added color based off of the y value
- Added size based on the y value
- Made the chart interactive
- Removed gridlines on the chart and added text on min/max
- Layered the chart with an image scatter plot and added a flag on the min and max values
""")



st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)
from vega_datasets import data

np.random.seed(42)
x = np.linspace(0, 10)
y = x - 5 + np.random.randn(len(x))

df = pd.DataFrame({'x': x, 'y': y})

chart = alt.Chart(df).mark_point().encode(
    x='x',
    y='y',
    tooltip = ['x','y']
)
with st.container():
    st.altair_chart(chart + chart.transform_regression('x', 'y').mark_line(), use_container_width=True)
    st.caption('Original Chart')

st.markdown("""
The changes I made were:

- Switched to the vegas dataset seattle weather and set the points color to the weather
- Switched to LOcally Estimated Scatterplot Smoothing
- Created two drop downs to update the chart axis
"""
)
st.caption('Must install jsonschema<4.0')

with st.container():
    if "x_axis" not in st.session_state:
        st.session_state.x_axis = "temp_max"
    if "y_axis" not in st.session_state:
        st.session_state.y_axis = "temp_min"

    source = data.seattle_weather()
    

    chart = alt.Chart(source).mark_point().encode(
            x=st.session_state.x_axis,
            y=st.session_state.y_axis,
            color ='weather'
        )
    regression_line = chart + chart.transform_loess(st.session_state.x_axis, st.session_state.y_axis).mark_line()
    with st.container():
        st.altair_chart(regression_line, use_container_width=True)
        st.caption('Updated Chart')


    st.session_state.x_axis = st.selectbox('Select X Variable:',options=source.columns, index =list(source.columns).index(str(st.session_state.x_axis)))
    st.session_state.y_axis = st.selectbox('Select Y Variable:',options=source.columns, index =list(source.columns).index(str(st.session_state.y_axis)))
