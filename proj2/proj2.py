import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu
from subprocess import call
import pandas as pd
import os
import sys
os.system('cls')


with st.sidebar:
    selected=option_menu(
        menu_title=None,
        options=["Home", "Bulk Convert", "Contact","About"],
        icons=["house","collection-fill","envelope","book"],
        menu_icon="cast", default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "#495057"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)


if selected=="Home":
    st.subheader("Hi, Let's begin with creating ultimate Web based Interface")
    st.title("Python: Project 2")
    uploaded_files = st.file_uploader("Upload excel files", accept_multiple_files=True)
    st.caption('''Make sure that current working directory doesn't has a folder named "input". If present kindly rename it.''')
    form=st.form("mod", clear_on_submit=False)
    mod=form.text_input("mod")
    submit=form.form_submit_button()
    my_bar = st.progress(0)
    if submit:
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'input')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        final_directory = os.path.join(current_directory, r'output')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        for file in uploaded_files:
            print(file.name)
            filename=file.name
            try:
                df=pd.read_excel(file)
                df.to_excel('./input/%s'%filename,index=False)
            except Exception as e:
                print('Error: ' + str(e))
        # print(mod)
        src=".\input"
        call(["python", "tut07.py", str(mod), src])
        my_bar.progress(100)
        st.success('This is a success message!', icon="✅")


elif selected=="Bulk Convert":
    st.subheader("Hi, Let's begin with creating ultimate Web based Interface")
    st.title("Python: Project 2")
    form=st.form("Input the folder path:", clear_on_submit=False)
    src=form.text_input("Input the folder path:")
    st.caption('''For Example: "C:\\Users\\Dell Vostro 3491\\OneDrive\\Documents\\fluid".[without double quotes]''')
    submit=form.form_submit_button()
    form=st.form("mod:", clear_on_submit=False)       
    mod=form.text_input("mod")
    submit=form.form_submit_button()
    my_bar = st.progress(0)
    if(submit):
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'output')
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        call(["python", "tut07.py", str(mod), src])
        my_bar.progress(100)
        st.success('This is a success message!', icon="✅")


elif selected=="Contact":
    st.subheader('Deepanshu Chaudhary:')
    st.write('deepanshu_2001me21@iitp.ac.in')
    st.subheader('Nitesh Srivastava:')
    st.write('nitesh_2001me42@iitp.ac.in')
    

elif selected=="About":
    st.title('About Project')
    # st.text("This is our project 2, developed by Nitesh Srivastava[2001ME42] and Deepanshu Chaudhary[2001ME21]. We have two types of conversions: Normal and Bulk Convert. Normal Convert is in Home Tab. Here the user can directly upload .xlsx files and value of mod and then get result. Bulk Convert is a bit different. Here the User has to manually input the path of the folder which contains all .xlsx files alongwith mod value. All the output is stored in an output folder which is located(in not present then created) in the current working directory.")
    loooong_text = ' '.join(["This is our project 2, developed by Nitesh Srivastava[2001ME42] and Deepanshu Chaudhary[2001ME21].\nWe have two types of conversions: Normal and Bulk Convert. Normal Convert is in Home Tab. Here the user can directly upload .xlsx files and value of mod and then get result. Bulk Convert is a bit different. Here the User has to manually input the path of the folder which contains all .xlsx files alongwith mod value. All the output is stored in an output folder which is located(in not present then created) in the current working directory."])
    st.markdown(loooong_text)
