import streamlit as st

# innitialize connection
conn = st.experimental_connection('mysql',type='sql')
# perform query
df = conn.query('SELECT * FROM pets;', ttl=600)

for row in df.itertuples():
    st.write(f'{row.name} has a :{row.pet}:')