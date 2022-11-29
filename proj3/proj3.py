import streamlit as st
import pandas as pd
from subprocess import call
from streamlit_option_menu import option_menu
import os
os.system('cls')
with st.sidebar:
    selected=option_menu(
        menu_title=None,
        options=["Home","Contact","About"],
        icons=["house","envelope","book"],
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
    st.title("Python: Project 3")
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)
    current_directory=os.getcwd()
    for file in uploaded_files:
        completeName = os.path.join(current_directory, file.name)
        file1 = open(completeName, "w")
        # cur_data=file.read()
        for line in file:
            line=line.decode()
            file1.write(line)
    with open("input_file_list.txt", 'w') as file_data:
        for file in uploaded_files:
            file_data.write(file.name)
            file_data.write('\n')

    constant_fk2d=st.number_input("constant_fk2d")
    multiplying_factor_3d=st.number_input("multiplying_factor_3d")
    Shear_velocity=st.number_input("Shear_velocity")
    option = st.selectbox('Choose your Filtering Method:', ('1. C','2. S','3. A','4. C & S','5. C & A','6. S & A','7. C & S & A','8. all combine'))
    st.write('You selected:', option)
    corr=SNR=Lambda=k=0
    if option=='1. C':
        corr=st.number_input("Enter thresold value C:")
    elif option=='2. S':
        SNR=st.number_input("Enter thresold value S:")
    elif option=='3. A':
        Lambda = st.number_input('Enter Lambda value for A:')
        k = st.number_input('Enter k value for A:')
    elif option=='4. C & S':
        corr = st.number_input('Enter thresold value C:')
        SNR = st.number_input('Enter thresold value S:')
    elif option=='5. C & A':
        corr = st.number_input('Enter thresold value C:')
        Lambda = st.number_input('Enter Lambda value for A:')
        k = st.number_input('Enter k value for A:')
    elif option=='6. S & A':
        SNR = st.number_input('Enter thresold value S:')
        Lambda = st.number_input('Enter Lambda value for A:')
        k = st.number_input('Enter k value for A:')
    elif option=='7. C & S & A' or option=='8. all combine':
        corr = st.number_input('Enter thresold value C:')
        st.write('corr:', corr)
        SNR = st.number_input('Enter thresold value S:')
        st.write('SNR:', SNR)
        Lambda = st.number_input('Enter Lambda value for A:')
        st.write('Lambda:', Lambda)
        k = st.number_input('Enter k value for A:')
        st.write('k:', k)
    else:
        pass
    corr=int(corr)
    SNR=int(SNR)
    corr=str(corr)
    SNR=str(SNR)
    # print(corr)
    # print(SNR)
    # print(Lambda)
    # print(k)
    # print("Name is Nitesh\n\n\n")
    n_option = st.selectbox('Chose Replacement Method From Below:', ('1. previous point','2. 2*last-2nd_last','3. overall_mean', '4. 12_point_strategy','5. mean of previous 2 point', '6. all seqential','7. all parallel'))
    st.write('You selected:', n_option)
    my_bar = st.progress(0)
    if st.button('Run'):
        #pp_tch, pp_corr, pp_SNR, pp_Lamda, pp_k, pp_sch
        # command = "{} {} {} {} {} {}".format(option, corr, SNR, Lambda, k, n_option) # if you want to pass any arguments
        call(["python", 'psat_v3.py',  "{}".format(option), "{}".format(corr), "{}".format(SNR), "{}".format(Lambda), "{}".format(k), "{}".format(n_option), "{}".format(constant_fk2d), "{}".format(multiplying_factor_3d), "{}".format(Shear_velocity)])
        my_bar.progress(100)
        st.success('This is a success message!', icon="✅")

elif selected=="Contact":
    st.subheader('E-mail:')
    st.write('Deepanshu Chaudhary: deepanshu_2001me21@iitp.ac.in')
    st.write('Nitesh Srivastava: nitesh_2001me42@iitp.ac.in')
    

elif selected=="About":
    st.title('About Project')
    st.write("This is our project 3, developed by Nitesh Srivastava[2001ME42] and Deepanshu Chaudhary[2001ME21]. \n Here the user has to input the data files and then later select the various parameters required for his computation. The program saves the input files in the same directory along with their .csv format having results computed. Also, two more CSV files are computed: Method_timestamp and Results_v2. Former consists of the timestamp of computing the CSV files while the latter consists of all the required results.")