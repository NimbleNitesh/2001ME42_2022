import pandas as pd
from datetime import datetime
start_time = datetime.now()

#Customized sort function to find the ranl of various Octant IDs based on their frequency
#If two Octant IDs have same frequency then their rank would also be same
def customsort(l2):
    l1=['Rank of +1', 'Rank of -1', 'Rank of +2', 'Rank of -2', 'Rank of +3', 'Rank of -3', 'Rank of +4', 'Rank of -4']
    #cnt_one=cnt_minus_one=cnt_two=cnt_minus_two=cnt_three=cnt_minus_three=cnt_four=cnt_minus_four=0
    pairlist=list(zip(l1, l2))
    pairlist.sort(key=lambda x: x[1])
    pairlist.reverse()
    cur_rank=1
    thisdict={
        'Rank of +1':0, 'Rank of -1':0, 'Rank of +2':0, 'Rank of -2':0, 'Rank of +3':0,  'Rank of -3':0, 'Rank of +4':0, 'Rank of -4':0
    }
    i=0
    while i<8:
        curval=pairlist[i][1]
        thisdict[pairlist[i][0]]=cur_rank
        j=i+1
        while j<8:
            if pairlist[j][1]==curval:
                thisdict[pairlist[i][0]]=cur_rank
                j+=1
            else:
                break
        i=j
        cur_rank+=1
#     print(pairlist)    
#     print(thisdict)
    return thisdict



#Help https://youtu.be/N6PBd4XdnEw
def octant_range_names(mod=5000):
    #reading excel file
    df=pd.read_excel(r"C:\Users\Dell Vostro 3491\OneDrive\Documents\GitHub\2001ME42_2022\tut05\octant_input.xlsx")
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
    U_list=df["U'=U - U avg"].tolist()
    V_list=df["V'=V - V avg"].tolist()
    W_list=df["W'=W - W avg"].tolist()
    df.insert(len(df.columns), column="Octant", value="")
    n=len(U_list)
    cnt_one=cnt_minus_one=cnt_two=cnt_minus_two=cnt_three=cnt_minus_three=cnt_four=cnt_minus_four=0
    #Finding the Octant ID based on U, V and W values
    #Also maintaing count of all the Octants
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
    #Inserting New columns
    df.insert(len(df.columns), column=" ", value="")
    df[' '][1]="User Input"
    df.insert(len(df.columns), column="Octant ID", value="")
    df.insert(len(df.columns), column="+1", value="")
    df.insert(len(df.columns), column="-1", value="")
    df.insert(len(df.columns), column="+2", value="")
    df.insert(len(df.columns), column="-2", value="")
    df.insert(len(df.columns), column="+3", value="")
    df.insert(len(df.columns), column="-3", value="")
    df.insert(len(df.columns), column="+4", value="")
    df.insert(len(df.columns), column="-4", value="")
    df.insert(len(df.columns), column="Rank of +1", value="")
    df.insert(len(df.columns), column="Rank of -1", value="")
    df.insert(len(df.columns), column="Rank of +2", value="")
    df.insert(len(df.columns), column="Rank of -2", value="")
    df.insert(len(df.columns), column="Rank of +3", value="")
    df.insert(len(df.columns), column="Rank of -3", value="")
    df.insert(len(df.columns), column="Rank of +4", value="")
    df.insert(len(df.columns), column="Rank of -4", value="")
    df.insert(len(df.columns), column="Rank 1 Octant ID", value="")
    df.insert(len(df.columns), column='Octant Name', value="")
    #Dictionary to store the name of Octant IDs
    OctantName={
        '+1':'Internal outward interaction',
        '-1':'External outward interaction',
        '+2':'External Ejection',
        '-2':'Internal Ejection',
        '+3':'External inward interaction',
        '-3':'Internal inward interaction',
        '+4':'Internal sweep',
        '-4':'External sweep'
    }
    df.at[0, 'Octant ID']="Overall Count"
    df.at[0, '+1']=cnt_one
    df.at[0, '-1']=cnt_minus_one
    df.at[0, '+2']=cnt_two
    df.at[0, '-2']=cnt_minus_two
    df.at[0, '+3']=cnt_three
    df.at[0, '-3']=cnt_minus_three
    df.at[0, '+4']=cnt_four
    df.at[0, '-4']=cnt_minus_four
    l2=[cnt_one, cnt_minus_one, cnt_two, cnt_minus_two, cnt_three, cnt_minus_three, cnt_four, cnt_minus_four]
    rank1=''
    thisdict=customsort(l2)
    #print(thisdict)
    #Finding the Octant with rank 1
    #if many such Octant are their then storing any one of them
    for i in thisdict:
        df.at[0, i]=thisdict[i]
        if thisdict[i]==1 and rank1=='':
            rank1=i[8]+i[9]
    df.at[0, 'Rank 1 Octant ID']=rank1
    df.at[0, 'Octant Name']=OctantName[rank1]
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
    #A dictionary to store the frequency of getting Rank 1
    countdict={
        '+1':0,
        '-1':0,
        '+2':0,
        '-2':0,
        '+3':0,
        '-3':0,
        '+4':0,
        '-4':0
    }
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
        l2=[cnt_one, cnt_minus_one, cnt_two, cnt_minus_two, cnt_three, cnt_minus_three, cnt_four, cnt_minus_four]
        thisdict=customsort(l2)
        rank1=''
        for i in thisdict:
            df.at[cur_pos, i]=thisdict[i]
            if thisdict[i]==1 and rank1=='':
                rank1=i[8]+i[9]
        df.at[cur_pos, 'Rank 1 Octant ID']=rank1
        df.at[cur_pos, 'Octant Name']=OctantName[rank1]
        countdict[rank1]+=1
        cur_pos+=1

        
    cur_pos=11
    df.at[cur_pos, '+1']='Octant ID'
    df.at[cur_pos, '-1']='Octant Name'
    df.at[cur_pos, '+2']='Count of Rank 1 Mod Values'
    cur_pos+=1
    for i in countdict:
        df.at[cur_pos, '+1']=i
        df.at[cur_pos, '-1']=OctantName[i]
        df.at[cur_pos, '+2']=countdict[i]
        cur_pos+=1
    #Exporting Data
    df.to_excel(r'C:\Users\Dell Vostro 3491\OneDrive\Documents\GitHub\2001ME42_2022\tut05\octant_output_ranking_excel.xlsx', encoding='utf-8', index=False)
    #print(countdict)
    
    #octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}

###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


mod=5000 
octant_range_names(mod)



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
