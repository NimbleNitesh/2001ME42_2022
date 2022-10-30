import pandas as pd

def octant_transition_count(mod=5000):
###Code
    #importing xlsx file to create a dataframe
    try:
        df=pd.read_excel(r"input_octant_transition_identify.xlsx")
    except:
        print('ERROR IN READING FILE')
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
    df.insert(len(df.columns), column="U Avg", value="")
    df.insert(len(df.columns), column="V Avg", value="")
    df.insert(len(df.columns), column="W Avg", value="")
    df.at[0, 'U Avg'] = U_Avg
    df.at[0, 'V Avg'] = V_Avg
    df.at[0, 'W Avg'] = W_Avg
    U_Avg=float(U_Avg)
    V_Avg=float(V_Avg)
    W_Avg=float(W_Avg)
    try:
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
    except:
        print("ERROR in computing U', V' or W' ")
        exit()
    try:
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
                    df['Octant'][i]="+1"
                    cnt_one+=1
                else:
                    df['Octant'][i]="-1"
                    cnt_minus_one+=1
            elif U_list_i<0.0 and V_list_i>=0.0:
                if W_list_i>0:
                    df['Octant'][i]="+2"
                    cnt_two+=1
                else:
                    df['Octant'][i]="-2"
                    cnt_minus_two+=1
            elif U_list_i<0.0 and V_list_i<0.0:
                if W_list_i>0:
                    df['Octant'][i]="+3"
                    cnt_three+=1
                else:
                    df['Octant'][i]="-3"
                    cnt_minus_three+=1
            elif U_list_i>=0.0 and V_list_i<0.0:
                if W_list_i>0:
                    df['Octant'][i]="+4"
                    cnt_four+=1
                else:
                    df['Octant'][i]="-4"
                    cnt_minus_four+=1
    except:
        print("ERROR in computing Octant Values ")
        exit()
    df.insert(len(df.columns), column=" ", value="")
    df[" "][1]="User Input"
    #df.head()
    #adding new column
    df.insert(len(df.columns), column="Octant ID", value="")
    df.insert(len(df.columns), column="+1", value="")
    df.insert(len(df.columns), column="-1", value="")
    df.insert(len(df.columns), column="+2", value="")
    df.insert(len(df.columns), column="-2", value="")
    df.insert(len(df.columns), column="+3", value="")
    df.insert(len(df.columns), column="-3", value="")
    df.insert(len(df.columns), column="+4", value="")
    df.insert(len(df.columns), column="-4", value="")
    try:
        df.at[0, 'Octant ID']="Overall Count"
        df.at[0, '+1']=cnt_one
        df.at[0, '-1']=cnt_minus_one
        df.at[0, '+2']=cnt_two
        df.at[0, '-2']=cnt_minus_two
        df.at[0, '+3']=cnt_three
        df.at[0, '-3']=cnt_minus_three
        df.at[0, '+4']=cnt_four
        df.at[0, '-4']=cnt_minus_four
        #CHANGE THE MOD VALUES FROM HERE
        x=mod
        txt="Mod {}"
        txt=txt.format(x)
        df.at[1, 'Octant ID']=txt
        l=[]
        cur=0
        row_cnt=len(df.index)
        while cur<=row_cnt:
            l.append(cur)
            cur+=x
        n=len(l)
        cur_pos=2
        total_cnt_one=total_cnt_minus_one=total_cnt_two=total_cnt_minus_two=total_cnt_three=total_cnt_minus_three=total_cnt_four=total_cnt_minus_four=0
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
                if df['Octant'][j]=="+1":
                    cnt_one+=1;
                elif df['Octant'][j]=="-1":
                    cnt_minus_one+=1
                elif df['Octant'][j]=="+2":
                    cnt_two+=1
                elif df['Octant'][j]=="-2":
                    cnt_minus_two+=1
                elif df['Octant'][j]=="+3":
                    cnt_three+=1
                elif df['Octant'][j]=="-3":
                    cnt_minus_three+=1
                elif df['Octant'][j]=="+4":
                    cnt_four+=1
                elif df['Octant'][j]=="-4":
                    cnt_minus_four+=1
                df.at[cur_pos, '+1']=cnt_one
                df.at[cur_pos, '-1']=cnt_minus_one
                df.at[cur_pos, '+2']=cnt_two
                df.at[cur_pos, '-2']=cnt_minus_two
                df.at[cur_pos, '+3']=cnt_three
                df.at[cur_pos, '-3']=cnt_minus_three
                df.at[cur_pos, '+4']=cnt_four
                df.at[cur_pos, '-4']=cnt_minus_four 
            cur_pos+=1
            total_cnt_one+=cnt_one
            total_cnt_minus_one+=cnt_minus_one
            total_cnt_two+=cnt_two
            total_cnt_minus_two+=cnt_minus_two
            total_cnt_three+=cnt_three
            total_cnt_minus_three+=cnt_minus_three
            total_cnt_four+=cnt_four
            total_cnt_minus_four+=cnt_minus_four
        n+=2
        df.at[n, 'Octant ID']="Verified"
        df.at[n, '+1']=total_cnt_one
        df.at[n, '-1']=total_cnt_minus_one
        df.at[n, '+2']=total_cnt_two
        df.at[n, '-2']=total_cnt_minus_two
        df.at[n, '+3']=total_cnt_three
        df.at[n, '-3']=total_cnt_minus_three
        df.at[n, '+4']=total_cnt_four
        df.at[n, '-4']=total_cnt_minus_four 
        n+=3
    except:
        print('ERROR in computing Overall Octant Count')
        exit()
    try:
        df.at[n, 'Octant ID']="Overall Transition Count"
        n+=1
        df.at[n, '+1']="To"
        n+=1
        df.at[n, 'Octant ID']="Count"
        df.at[n, '+1']="+1"
        df.at[n, '-1']="-1"
        df.at[n, '+2']="+2"
        df.at[n, '-2']="-2"
        df.at[n, '+3']="+3"
        df.at[n, '-3']="-3"
        df.at[n, '+4']="+4"
        df.at[n, '-4']="-4"
        df.at[n+1, 'Octant ID']="+1"
        df.at[n+2, 'Octant ID']="-1"
        df.at[n+3, 'Octant ID']="+2"
        df.at[n+4, 'Octant ID']="-2"
        df.at[n+5, 'Octant ID']="+3"
        df.at[n+6, 'Octant ID']="-3"
        df.at[n+7, 'Octant ID']="+4"
        df.at[n+8, 'Octant ID']="-4"
        n+=1
        df.at[n, ' ']="From"
        thislist=['+1', '-1', '+2', '-2', '+3', '-3', '+4', '-4']
        #nested loop to initialise the table element
        for i in range(len(thislist)):
            for j in range(len(thislist)):
                df.at[n+i, thislist[j]]=0
        #computing the Transition counts
        for i in range(row_cnt):
            if i+1==row_cnt:
                break
            if df.at[i, 'Octant']=='+1':
                df.at[n, df['Octant'][i+1]]+=1
            elif df.at[i, 'Octant']=='-1':
                df.at[n+1, df['Octant'][i+1]]+=1
            elif df.at[i, 'Octant']=='+2':
                df.at[n+2, df['Octant'][i+1]]+=1
            elif df.at[i, 'Octant']=='-2':
                df.at[n+3, df['Octant'][i+1]]+=1
            elif df.at[i, 'Octant']=='+3':
                df.at[n+4, df['Octant'][i+1]]+=1
            elif df.at[i, 'Octant']=='-3':
                df.at[n+5, df['Octant'][i+1]]+=1
            elif df.at[i, 'Octant']=='+4':
                df.at[n+6, df['Octant'][i+1]]+=1
            elif df.at[i, 'Octant']=='-4':
                df.at[n+7, df['Octant'][i+1]]+=1
        n+=8
    except:
        print('ERROR in computing Overall Transitions Count')
        exit()
    try:
        ch=True
        while ch:
            l_size=len(l)
            #nested loop to compute modular transition counts
            for i in range(l_size):
                n+=2
                df.at[n, 'Octant ID']="Mod Transition Count"
                low=l[i]
                high=l[i]+x
                if high>row_cnt:
                    high=row_cnt
                    ch=False
                txt="{}-{}"
                txt=txt.format(low, high-1)
                n+=1
                df.at[n, 'Octant ID']=txt
                df.at[n, '+1']="To"
                n+=1
                df.at[n, 'Octant ID']="Count"
                df.at[n+1, ' ']="From"
                for iii in range(len(thislist)):
                    df.at[n, thislist[iii]]=thislist[iii]
                df.at[n+1, 'Octant ID']="+1"
                df.at[n+2, 'Octant ID']="-1"
                df.at[n+3, 'Octant ID']="+2"
                df.at[n+4, 'Octant ID']="-2"
                df.at[n+5, 'Octant ID']="+3"
                df.at[n+6, 'Octant ID']="-3"
                df.at[n+7, 'Octant ID']="+4"
                df.at[n+8, 'Octant ID']="-4"
                n+=1
                for ii in range(len(thislist)):
                    for j in range(len(thislist)):
                        df.at[n+ii, thislist[j]]=0
                for j in range(low, high):
                    if j+1==row_cnt:
                        break
                    if df.at[j, 'Octant']=='+1':
                        df.at[n, df['Octant'][j+1]]+=1
                    elif df.at[j, 'Octant']=='-1':
                        df.at[n+1, df['Octant'][j+1]]+=1
                    elif df.at[j, 'Octant']=='+2':
                        df.at[n+2, df['Octant'][j+1]]+=1
                    elif df.at[j, 'Octant']=='-2':
                        df.at[n+3, df['Octant'][j+1]]+=1
                    elif df.at[j, 'Octant']=='+3':
                        df.at[n+4, df['Octant'][j+1]]+=1
                    elif df.at[j, 'Octant']=='-3':
                        df.at[n+5, df['Octant'][j+1]]+=1
                    elif df.at[j, 'Octant']=='+4':
                        df.at[n+6, df['Octant'][j+1]]+=1
                    elif df.at[j, 'Octant']=='-4':
                        df.at[n+7, df['Octant'][j+1]]+=1
                n+=8
    except:
        print('ERROR in computing Modular Transitions Count')
        exit()
    #Exporting to xlsx file
    df.to_excel(r"output_octant_transition_identify.xlsx", encoding='utf-8', index=False)#storing final csv file to octant_output



from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octant_transition_count(mod)
