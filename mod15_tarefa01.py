
# Esse documento apresenta 20 possíveis elementos do streamlit dentre tantos existentes.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

### 1. Faz modificações no layout da página

st.set_page_config(
   page_title="Ex-stream-ly Cool App",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)
#------------------------------------------------------------------------------------------#

### 2. Escreve o título 
st.title('Uber pickups in NYC')
#------------------------------------------------------------------------------------------#

### 3. Função que importa os dados de um data frame
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
#------------------------------------------------------------------------------------------#

### 4. Testando a função

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")
#------------------------------------------------------------------------------------------#

### 5. Colocando uma linha de divisão

st.divider()
#------------------------------------------------------------------------------------------#

### 6. Inspecionando os dados

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
#------------------------------------------------------------------------------------------#

### 7. Desenhando um histograma

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

st.divider()
#------------------------------------------------------------------------------------------#

### 8. Plotando os dados em mapa

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

st.divider()
#------------------------------------------------------------------------------------------#

### 9. Exemplos de map e scatterplot

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

st.map(df, size=20, color='#0044ff')

df = pd.DataFrame({
    "col1": np.random.randn(1000) / 50 + 37.76,
    "col2": np.random.randn(1000) / 50 + -122.4,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
})

st.map(df,
    latitude='col1',
    longitude='col2',
    size='col3',
    color='col4')

st.divider()
#------------------------------------------------------------------------------------------#

### 10. Gráficos de área

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

st.divider()
#------------------------------------------------------------------------------------------#

### 11. Destaque em dataframe

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

st.divider()
#------------------------------------------------------------------------------------------#

### 12. Métricas

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.divider()
#------------------------------------------------------------------------------------------#

### 13. Gráfico de barras

chart_data = pd.DataFrame(
   {"col1": list(range(20)), "col2": np.random.randn(20), "col3": np.random.randn(20)}
)

st.bar_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)

st.divider()
#------------------------------------------------------------------------------------------#

### 14. Gráfico de linha

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])

st.line_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)


st.divider()
#------------------------------------------------------------------------------------------#

### 15. Mapa de dispersão

chart_data = pd.DataFrame(np.random.randn(20, 4), columns=["col1", "col2", "col3", "col4"])

st.scatter_chart(
    chart_data,
    x='col1',
    y=['col2', 'col3'],
    size='col4',
    color=['#FF0000', '#0000FF'],  # Optional
)

st.divider() 
#------------------------------------------------------------------------------------------#

### 16. Figuras do pyplot

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

st.divider()
#------------------------------------------------------------------------------------------#

### 17. Botão

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.divider()
#------------------------------------------------------------------------------------------#

### 18. Data

d = st.date_input("When's your birthday", value=None)
st.write('Your birthday is:', d)

st.divider()
#------------------------------------------------------------------------------------------#

### 19. Selectbox

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

st.divider()
#------------------------------------------------------------------------------------------#

### 20. Editor de dados

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
#------------------------------------------------------------------------------------------#