import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('netflix_titles.csv')
# df.fillna('Not Specified', inplace=True)
df.drop('show_id', axis=1,inplace=True)
df.drop('title', axis=1,inplace=True)
df.drop('description', axis=1,inplace=True)

country_cnt= df.country.dropna().reset_index(name='countries').groupby('countries').size().sort_values(ascending=False).head(10).reset_index(name='Total count')
graph = px.bar(country_cnt,x= 'countries', y= 'Total count', title='Content by Countries',  color_discrete_sequence=px.colors.qualitative.Set3)

rating_count=df.groupby(df.rating).size().sort_values(ascending=False).reset_index(name='counts')

pie_chart  = px.pie(rating_count, values='counts', names='rating', title='Distribution of Content', color_discrete_sequence=px.colors.qualitative.Set3)

st.set_page_config(page_title='Netflix Analysis',
    layout='wide')
st.title(' Netflix Dashboard')
feature = st.selectbox('Select Column', df.columns)
left_col, right_col = st.columns(2)
if feature == 'country' or feature == 'cast' or feature == 'director' or feature == 'listed_in':
    z = df[f'{feature}'].str.split(', ', expand=True).stack().reset_index(name=f'{feature}').groupby(f'{feature}').size().sort_values(ascending=False)[:15]
    with left_col:
        st.dataframe(z, use_container_width=True)
    with right_col:
        graph = px.bar(z, title=f'Content by {feature}',  color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(graph,use_container_width=True )
else:
    z=df.groupby(f'{feature}').size().sort_values(ascending=False)[:15]
# st.plotly_chart(pie_chart, use_container_width=True)
    with left_col:
        st.dataframe(z, use_container_width=True)
    with right_col:
        graph = px.bar(z, title=f'Content by {feature}',  color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(graph,use_container_width=True)





