import streamlit as st
import pandas as pd
import gdown
from tensorflow.python.keras.utils.generic_utils import to_list

st.set_page_config(page_title="23O0513-Time Series Data Analysis and Modelling ", layout="wide")
st.title("Attendance Record")

st.markdown(
            f"<p style='color:cyan; font-size:32px;'>23O0513-Time Series Data Analysis and Modelling </p>",
                        unsafe_allow_html=True
            )

#st.markdown("23O0513-Time Series Data Analysis and Modelling")
# Google Drive file ID
file_id = "19UzTUqx-MTo0cW1cv2uiHiAu-i9LeHlOsV6n56uzZ3M"
download_url = f"https://drive.google.com/uc?id={file_id}"
#download_url = f"https://docs.google.com/spreadsheets/d/19UzTUqx-MTo0cW1cv2uiHiAu-i9LeHlOsV6n56uzZ3M/edit?usp=sharing={file_id}"

# Load data once
@st.cache_data(ttl=600)
def load_data():
    sheet_id = "19UzTUqx-MTo0cW1cv2uiHiAu-i9LeHlOsV6n56uzZ3M"
    sheet_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
    df = pd.read_csv(sheet_url)
    return df

st.write("Attendance have been finalized till Aug 15. It is being updated soon")

df = load_data()

# Input box for Roll Number
roll_number = st.text_input("Enter Roll Number:")
#g1 = df.groupby('Unnamed: 1')


# Button to trigger query
if st.button("Fetch Student Details"):
    if roll_number:
        # Make sure the column name matches exactly what’s in your sheet
        filtered_df = df[df["Unnamed: 1"].astype(str).str.strip() == roll_number.strip()]
        #print(filtered_df)
        if not filtered_df.empty:
            st.success(f"✅ Found details for Roll Number {roll_number}")
            st.dataframe(filtered_df, use_container_width=True)

            result2 = df.loc[df["Unnamed: 1"] == roll_number, "15"]
            #st.caption("Total: "+str(df['15']) )
            # Equivalent query
            #result1 = df.loc[df["Unnamed: 1"].astype(str).str.strip() == roll_number, df['15']]
            if(result2.values[0]=="A"):
                st.write('NOTE: You were absent on the concerned day: SCROLL THE TABLE FOR ATTENDANCE %')
            else:

                st.write('Total Classes(till updated): '+ str(result2.name))
                st.write('Attended: '+ str((result2.values[0])))

                percent1 = int(result2.values[0])/int(result2.name)
                #st.write('Attendance % : '+str(percent1*100))
                #st.markdown("## Attendance % : "+str(percent1*100),
                #"<h2 style='text-align: center; color: blue;'>Custom Font Size Text</h2>",
                #unsafe_allow_html = True)
                if percent1*100 < 65:
                    st.markdown(
                        f"<p style='color:red; font-size:22px;'>Attendance % : {percent1*100} </p>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f"<p style='color:limegreen; font-size:22px;'>Attendance % : {percent1 * 100} </p>",
                        unsafe_allow_html=True
                    )


        else:
            st.error(f"No records found for Roll Number {roll_number}")
    else:
        st.warning("Please enter a Roll Number before clicking Fetch Student Details.")
else:
    st.info("Enter a Roll Number and click the button to see details.")
    #st.dataframe(df.head(10), use_container_width=True)

print(df)
print(df.columns)


#print(df['Unnamed: 1'].head(10))