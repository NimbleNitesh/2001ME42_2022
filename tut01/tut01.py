import pandas as pd
import numpy as np


def octact_identification(mod=5000):
###Code
    df=pd.read_csv(r"octant_input.csv")#reading csv file
    U_Avg=df['U'].mean()
    U_Avg=round(U_Avg, 8)#setting precision to 8
    V_Avg=df['V'].mean()
    V_Avg=round(V_Avg, 9)
    W_Avg=df['W'].mean()
    W_Avg=round(W_Avg, 8)
    U_Avg=str(U_Avg)
    V_Avg=str(V_Avg)
    W_Avg=str(W_Avg)
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
    df["Time"] = df["Time"].apply(lambda x: format(float(x),".2f"))
    #using lamda function
    df["U"] = df["U"].apply(lambda x: format(float(x),".2f"))
    df["V"] = df["V"].apply(lambda x: format(float(x),".2f"))
    df["W"] = df["W"].apply(lambda x: format(float(x),".2f"))
    df["U'=U - U avg"] = df["U'=U - U avg"].apply(lambda x: format(float(x),".9f"))
    df["V'=V - V avg"] = df["V'=V - V avg"].apply(lambda x: format(float(x),".9f"))
    df["W'=W - W avg"] = df["W'=W - W avg"].apply(lambda x: format(float(x),".9f"))
    #df.head()
    U_list=df["U'=U - U avg"].tolist()
    V_list=df["V'=V - V avg"].tolist()
    W_list=df["W'=W - W avg"].tolist()
    df.insert(len(df.columns), column="Octant", value="")
    n=len(U_list)
    cnt_one=cnt_minus_one=cnt_two=cnt_minus_two=cnt_three=cnt_minus_three=cnt_four=cnt_minus_four=0
    for i in range(n):
        U_list_i=float(U_list[i])
        V_list_i=float(V_list[i])
        W_list_i=float(W_list[i])
        if U_list_i>=0.0 and V_list_i>=0.0:
            if W_list_i>0:
                df['Octant'][i]="1"
                cnt_one+=1
            else:
                df['Octant'][i]="-1"
                cnt_minus_one+=1
        elif U_list_i<0.0 and V_list_i>=0.0:
            if W_list_i>0:
                df['Octant'][i]="2"
                cnt_two+=1
            else:
                df['Octant'][i]="-2"
                cnt_minus_two+=1
        elif U_list_i<0.0 and V_list_i<0.0:
            if W_list_i>0:
                df['Octant'][i]="3"
                cnt_three+=1
            else:
                df['Octant'][i]="-3"
                cnt_minus_three+=1
        elif U_list_i>=0.0 and V_list_i<0.0:
            if W_list_i>0:
                df['Octant'][i]="4"
                cnt_four+=1
            else:
                df['Octant'][i]="-4"
                cnt_minus_four+=1
    df.insert(len(df.columns), column=" ", value="")
    df[" "][1]="User Input"
    df.head()
    #adding new column
    df.insert(len(df.columns), column="Octant ID", value="")
    df.insert(len(df.columns), column="1", value="")
    df.insert(len(df.columns), column="-1", value="")
    df.insert(len(df.columns), column="2", value="")
    df.insert(len(df.columns), column="-2", value="")
    df.insert(len(df.columns), column="3", value="")
    df.insert(len(df.columns), column="-3", value="")
    df.insert(len(df.columns), column="4", value="")
    df.insert(len(df.columns), column="-4", value="")
    df.at[0, 'Octant ID']="Overall Count"
    df.at[0, '1']=cnt_one
    df.at[0, '-1']=cnt_minus_one
    df.at[0, '2']=cnt_two
    df.at[0, '-2']=cnt_minus_two
    df.at[0, '3']=cnt_three
    df.at[0, '-3']=cnt_minus_three
    df.at[0, '4']=cnt_four
    df.at[0, '-4']=cnt_minus_four
    #CHANGE THE MOD VALUES FROM HERE
    x=mod
    txt="Mod {}"
    txt=txt.format(x)
    df.at[1, 'Octant ID']=txt
    l=[]
    cur=0;
    row_cnt=len(df.index)
    while cur<=row_cnt:
        l.append(cur)
        cur+=x
    n=len(l)
    cur_pos=2
    for i in range(n):
        low=l[i]
        high=l[i]+x
        if high>row_cnt:
            high=row_cnt
        txt="{}-{}"
        txt=txt.format(low, high-1)
        df.at[cur_pos, 'Octant ID']=txt
        cnt_one=cnt_minus_one=cnt_two=cnt_minus_two=cnt_three=cnt_minus_three=cnt_four=cnt_minus_four=0
        for j in range(low, high):
            if df['Octant'][j]=="1":
                cnt_one+=1;
            elif df['Octant'][j]=="-1":
                cnt_minus_one+=1
            elif df['Octant'][j]=="2":
                cnt_two+=1
            elif df['Octant'][j]=="-2":
                cnt_minus_two+=1
            elif df['Octant'][j]=="3":
                cnt_three+=1
            elif df['Octant'][j]=="-3":
                cnt_minus_three+=1
            elif df['Octant'][j]=="4":
                cnt_four+=1
            elif df['Octant'][j]=="-4":
                cnt_minus_four+=1
            df.at[cur_pos, '1']=cnt_one
            df.at[cur_pos, '-1']=cnt_minus_one
            df.at[cur_pos, '2']=cnt_two
            df.at[cur_pos, '-2']=cnt_minus_two
            df.at[cur_pos, '3']=cnt_three
            df.at[cur_pos, '-3']=cnt_minus_three
            df.at[cur_pos, '4']=cnt_four
            df.at[cur_pos, '-4']=cnt_minus_four 
        cur_pos+=1            
    #print(df.head(5))
    df.to_csv(r"octant_output.csv", encoding='utf-8', index=False)#storing final csv file to octant_output.csv

from platform import python_version
ver = python_version()
if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octact_identification(mod)
