import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec egestas mi. Vivamus iaculis sem eu odio 
scelerisque pellentesque. Phasellus blandit sem a ex tincidunt, ac mattis dui hendrerit. Cras commodo purus ut felis 
eleifend tristique. Cras iaculis sapien ac suscipit faucibus. Maecenas tincidunt ipsum at ipsum tempor vehicula. 
"""

st.write(content)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data.csv')

with col1:
    for index, row in df[0:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image(f"images/{row['image']}")