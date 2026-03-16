import streamlit
import snowflake.connector
import pandas as pd

streamlit.title("Zena's Amazing Athleisure Catalog")

# Connect to Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# 1. Pull the data from your special website view
my_cur.execute("SELECT * FROM CATALOG_FOR_WEBSITE")
my_catalog = my_cur.fetchall()
df = pd.DataFrame(my_catalog)

# 2. Add column names so we can refer to them easily
df.columns = ['Color', 'Price', 'File_Name', 'URL', 'Size_List', 'Upsell']

# 3. Create the Dropdown (The "Pick a sweatsuit" box)
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(df['Color']))

# 4. Filter the dataframe to just the one color selected
selection = df.loc[df['Color'] == option]

# 5. Display the "Hero" Image
streamlit.image(selection['URL'].iloc[0], width=400)

# 6. Display the Details
streamlit.write(f"Our warm, comfortable, {option} sweatsuit!")
streamlit.write(f"**Price:** {selection['Price'].iloc[0]}")
streamlit.write(f"**Sizes Available:** {selection['Size_List'].iloc[0]}")
streamlit.write(f"**BONUS:** {selection['Upsell'].iloc[0]}")
