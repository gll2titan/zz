import streamlit as st
import pandas as pd

tab1, tab2, tab3 = st.tabs(["# 周工作表1", "# 周工作表2", "# 周工作表3"])


def insert_data(data, file_name):
    df = pd.DataFrame(data, columns=["Name", "Age", "Phone Number"])
    df.to_csv(file_name, mode="a", header=False, index=False)


with tab1:
    name_1 = st.text_input("Name1")
    age_1 = st.number_input("Age1")
    phone_number_1 = st.text_input("Phone Number1")

    if st.button("Submit1"):
        data1 = [[name_1, age_1, phone_number_1]]
        file_name1 = "form_data1.csv"
        insert_data(data1, file_name1)
        st.write("Form submitted successfully!")
        data11 = pd.read_csv(file_name1)
        st.write(data11)
    else:
        st.write("Form not submitted!")

with tab2:
    name_2 = st.text_input("Name2")
    age_2 = st.number_input("Age2")
    phone_number_2 = st.text_input("Phone Number2")
    if st.button("Submit2"):
        data2 = [[name_2, age_2, phone_number_2]]
        file_name2 = "form_data2.csv"
        insert_data(data2, file_name2)
        st.write("Form submitted successfully!")
        data12 = pd.read_csv(file_name2)
        st.write(data12)
    else:
        st.write("Form not submitted!")


with tab3:
    name_3 = st.text_input("Name3")
    age_3 = st.number_input("Age3")
    phone_number_3 = st.text_input("Phone Number3")
    if st.button("Submit3"):
        data3 = [[name_3, age_3, phone_number_3]]
        file_name3 = "form_data3.csv"
        insert_data(data3, file_name3)
        st.write("Form submitted successfully!")
        data13 = pd.read_csv(file_name3)
        st.write(data13)
    else:
        st.write("Form not submitted!")
