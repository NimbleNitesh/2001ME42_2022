import pandas as pd
#Help https://youtu.be/H37f_x4wAC0
def octant_longest_subsequence_count_with_range():
    try:
        df=pd.read_excel(r"input_octant_longest_subsequence_with_range.xlsx")
    except:
        print('Error in reading Excel file')
        exit()
    U_Avg=df['U'].mean()
    U_Avg=round(U_Avg, 8)#setting precision to 8
    V_Avg=df['V'].mean()
    V_Avg=round(V_Avg, 9)
    W_Avg=df['W'].mean()
    W_Avg=round(W_Avg, 8)
    U_Avg=str(U_Avg)
    V_Avg=str(V_Avg)
    W_Avg=str(W_Avg)
    try:
        df.insert(len(df.columns), column="U Avg", value="")
        df.insert(len(df.columns), column="V Avg", value="")
        df.insert(len(df.columns), column="W Avg", value="")
    except:
        print('Error in inserting new columns')
        exit()
    df.at[0, 'U Avg'] = U_Avg
    df.at[0, 'V Avg'] = V_Avg
    df.at[0, 'W Avg'] = W_Avg
    try:
        U_Avg=float(U_Avg)
        V_Avg=float(V_Avg)
        W_Avg=float(W_Avg)
    except:
        print('Error in data type conversion')
        exit()
    df.insert(len(df.columns), column="U'=U - U avg", value="")
    df["U'=U - U avg"]=df['U']-U_Avg
    df.insert(len(df.columns), column="V'=V - V avg", value="")
    df["V'=V - V avg"]=df['V']-V_Avg
    df.insert(len(df.columns), column="W'=W - W avg", value="")
    df["W'=W - W avg"]=df['W']-W_Avg
    df["Time"] = df["Time"].apply(lambda x: format(float(x),".2f"))
    #using lamda function
    df["U"] = df["U"].apply(lambda x: format(float(x),".2f"))
    df["V"] = df["V"].apply(lambda x: format(float(x),".2f"))
    df["W"] = df["W"].apply(lambda x: format(float(x),".2f"))
    df["U'=U - U avg"] = df["U'=U - U avg"].apply(lambda x: format(float(x),".9f"))
    df["V'=V - V avg"] = df["V'=V - V avg"].apply(lambda x: format(float(x),".9f"))
    df["W'=W - W avg"] = df["W'=W - W avg"].apply(lambda x: format(float(x),".9f"))
    #df.head()
    try:
        U_list=df["U'=U - U avg"].tolist()
        V_list=df["V'=V - V avg"].tolist()
        W_list=df["W'=W - W avg"].tolist()
    except:
        print('Error in converting dataframe to python list')
        exit()
    df.insert(len(df.columns), column="Octant", value="")
    n=len(U_list)
    try:
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
        print('Error in calculating Octants')
        exit()
    #df.head()
    try:
        O_list=df['Octant'].tolist()
        n=len(O_list)
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

        newdict={
            '+1':[],
            '-1':[],
            '+2':[],
            '-2':[],
            '+3':[],
            '-3':[],
            '+4':[],
            '-4':[]
        }
        i=0
        while i<n:
            cur_val=O_list[i]
            cur_freq=1
            j=i+1
            while j<n :
                if O_list[j]!=cur_val:
                    break
                cur_freq+=1
                j+=1
        #     txt="cur_val={} and cur_freq={}"
        #     txt=txt.format(cur_val, cur_freq)
        #     print(txt)
            if thisdict[cur_val][0]==cur_freq:
                thisdict[cur_val][1]+=1
                newdict[cur_val].append(i)
            elif thisdict[cur_val][0]<cur_freq:
                newdict[cur_val].clear()
                newdict[cur_val].append(i)
                thisdict[cur_val][1]=1
                thisdict[cur_val][0]=cur_freq
            i=j
    except:
        print('ERROR in finding Longest Subsequence Count for every Octant along with range')
        exit()
    # print(newdict)
    # print(len(df.columns))
    df.insert(len(df.columns), column=" ", value="")
    print(len(df.columns))
    df.insert(len(df.columns), column="Octant ID", value="")
    df.insert(len(df.columns), column="Longest Subsquence Length", value="")
    df.insert(len(df.columns), column="Count", value="")
    try:
        j=0
        for i in thisdict:
            df['Octant ID'][j]=i
            df['Longest Subsquence Length'][j]=thisdict[i][0]
            df['Count'][j]=thisdict[i][1]
            j+=1
        df.insert(len(df.columns), column="  ", value="")
        df.insert(len(df.columns), column="Count_2", value="")
        df.insert(len(df.columns), column="Longest Subsquence Length_2", value="")
        df.insert(len(df.columns), column="Count_3", value="")
        cur_row=0
        for i in newdict:
            df['Count_2'][cur_row]=i
            df['Longest Subsquence Length_2'][cur_row]=thisdict[i][0]
            df['Count_3'][cur_row]=thisdict[i][1]
            cur_row+=1
            df['Count_2'][cur_row]='Time'
            df['Longest Subsquence Length_2'][cur_row]='From'
            df['Count_3'][cur_row]='To'
            cur_row+=1
            for j in newdict[i]:
                df['Longest Subsquence Length_2'][cur_row]=df['Time'][j]
                df['Count_3'][cur_row]=df['Time'][j+thisdict[i][0]-1]
                cur_row+=1
    except:
        print('Error in adding the calculated values to the dataframe')
        exit()
    #df.head(10)
    try:
        df.to_excel(r"output_octant_longest_subsequence_with_range.xlsx", encoding='utf-8', index=False)#storing final excel file to octant_output
    except:
        print('Error in exporting the dataframe to excel file')
        exit()
    ###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


octant_longest_subsequence_count_with_range()
