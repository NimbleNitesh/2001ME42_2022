import pandas as pd

from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count():
#reading excel file
    try:
        df=pd.read_excel(r"input_octant_longest_subsequence.xlsx")
    except:
        print("ERROR in reading file\n")
        exit()
    U_Avg=df['U'].mean()
#setting precision to 8
    U_Avg=round(U_Avg, 8)
    V_Avg=df['V'].mean()
    V_Avg=round(V_Avg, 9)
    W_Avg=df['W'].mean()
    W_Avg=round(W_Avg, 8)
    U_Avg=str(U_Avg)
    V_Avg=str(V_Avg)
    W_Avg=str(W_Avg)
    try:
#inserting new column
        df.insert(len(df.columns), column="U Avg", value="")
        df.insert(len(df.columns), column="V Avg", value="")
        df.insert(len(df.columns), column="W Avg", value="")
        df.at[0, 'U Avg'] = U_Avg
        df.at[0, 'V Avg'] = V_Avg
        df.at[0, 'W Avg'] = W_Avg
        U_Avg=float(U_Avg)
        V_Avg=float(V_Avg)
        W_Avg=float(W_Avg)
        df.insert(len(df.columns), column="U'=U - U avg", value="")
        df["U'=U - U avg"]=df['U']-U_Avg
        df.insert(len(df.columns), column="V'=V - V avg", value="")
        df["V'=V - V avg"]=df['V']-V_Avg
        df.insert(len(df.columns), column="W'=W - W avg", value="")
        df["W'=W - W avg"]=df['W']-W_Avg
    except:
        print("ERROR in creating new column\n")
        exit()
    df["Time"] = df["Time"].apply(lambda x: format(float(x),".2f"))
#using lamda function
    df["U"] = df["U"].apply(lambda x: format(float(x),".2f"))
    df["V"] = df["V"].apply(lambda x: format(float(x),".2f"))
    df["W"] = df["W"].apply(lambda x: format(float(x),".2f"))
    df["U'=U - U avg"] = df["U'=U - U avg"].apply(lambda x: format(float(x),".9f"))
    df["V'=V - V avg"] = df["V'=V - V avg"].apply(lambda x: format(float(x),".9f"))
    df["W'=W - W avg"] = df["W'=W - W avg"].apply(lambda x: format(float(x),".9f"))
    try:
        U_list=df["U'=U - U avg"].tolist()
        V_list=df["V'=V - V avg"].tolist()
        W_list=df["W'=W - W avg"].tolist()
        df.insert(len(df.columns), column="Octant", value="")
        n=len(U_list)
        for i in range(n):
            U_list_i=float(U_list[i])
            V_list_i=float(V_list[i])
            W_list_i=float(W_list[i])
            if U_list_i>=0.0 and V_list_i>=0.0:
                if W_list_i>0:
                    df['Octant'][i]="+1"
                else:
                    df['Octant'][i]="-1"
            elif U_list_i<0.0 and V_list_i>=0.0:
                if W_list_i>0:
                    df['Octant'][i]="+2"
                else:
                    df['Octant'][i]="-2"
            elif U_list_i<0.0 and V_list_i<0.0:
                if W_list_i>0:
                    df['Octant'][i]="+3"
                else:
                    df['Octant'][i]="-3"
            elif U_list_i>=0.0 and V_list_i<0.0:
                if W_list_i>0:
                    df['Octant'][i]="+4"
                else:
                    df['Octant'][i]="-4"
    except:
        print("ERROR in finding Octants\n")
        exit()
    try:
        O_list=df['Octant'].tolist()
        n=len(O_list)
#creating a dictionary to store the maximum length and its frequency for each Octant ID
        thisdict={
            '+1':[0, 0],
            '-1':[0, 0],
            '+2':[0, 0],
            '-2':[0, 0],
            '+3':[0, 0],
            '-3':[0, 0],
            '+4':[0, 0],
            '-4':[0, 0]
        }
        i=0
#Iterating through the Octant list and storing the current length of continous segment
#If this length is greater than max length then updating maxlength and setting its
#frequency to 1 else if this length is equal to max lemgth the incrementing the max
#length frequency
        while i<n:
            cur_val=O_list[i]
            cur_freq=1
            j=i+1
            while j<n :
                if O_list[j]!=cur_val:
                    break
                cur_freq+=1
                j+=1
            if thisdict[cur_val][0]==cur_freq:
                thisdict[cur_val][1]+=1
            elif thisdict[cur_val][0]<cur_freq:
                thisdict[cur_val][1]=1
                thisdict[cur_val][0]=cur_freq
            i=j
        df.insert(len(df.columns), column=" ", value="")
        df.insert(len(df.columns), column="Octant ID", value="")
        df.insert(len(df.columns), column="Longest Subsquence Length", value="")
        df.insert(len(df.columns), column="Count", value="")
#storing dicionary thisdict in dataframe df
        j=0
        for i in thisdict:
            df['Octant ID'][j]=i;
            df['Longest Subsquence Length'][j]=thisdict[i][0]
            df['Count'][j]=thisdict[i][1]
            j+=1
    except:
        print("ERROR in finding Longest Subsequence Count for every Octant.\n")
        exit()
    try:
        df.to_excel(r"output_octant_longest_subsequence.xlsx", encoding='utf-8', index=False)#storing final excel file to octant_output
    except:
        print("ERROR in exporting Excel file\n")
#Code

#Checkin Python Version
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count()


#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
