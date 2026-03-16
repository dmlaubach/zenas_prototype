import streamlit
import snowflake.connector

streamlit.title("Zena's Athleisure Catalog")

# Connect to Snowflake using the secrets you'll set up in Streamlit
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# This is the line we talked about - it pulls from your NEW view
my_cur.execute("SELECT * FROM CATALOG_FOR_WEBSITE")
my_catalog = my_cur.fetchall()

# This part displays the data on the website
import pandas as pd
df = pd.DataFrame(my_catalog)

# Putting the data into a nice table on the screen
streamlit.write("Check out our latest styles:")
streamlit.dataframe(df)
