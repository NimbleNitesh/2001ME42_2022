import pandas as pd
import datetime
from Send_Mail import main_mail

start_time = datetime.datetime.now()


full={}
    
def isValidDate(date, roll_no):
#     print(date.weekday())
    start=datetime.datetime.strptime('2022-07-28', '%Y-%m-%d').date()
#     start=start.strftime('%Y-%m-%d')
    end=datetime.datetime.strptime('2022-09-29', '%Y-%m-%d').date()
#     end=end.strftime('%Y-%m-%d')
    if date<start or date>end:
        return False
    if date.weekday()==0 or date.weekday()==3:
        return True
    return False


def isValidTime(x):
    start=datetime.time(14, 0, 0)
    end=datetime.time(15, 0, 0)
    return start <= x <= end

def attendance_report():     
    #main
    df=pd.read_csv(r'C:\Users\Dell Vostro 3491\OneDrive\Documents\GitHub\2001ME42_2022\tut06\input_registered_students.csv')
    roll_list=df['Roll No'].tolist()
    name_list=df['Name'].tolist()
    valid_dates=[]
    start=datetime.datetime.strptime('2022-07-28', '%Y-%m-%d')
    end=datetime.datetime.strptime('2022-09-29', '%Y-%m-%d')
    step1=datetime.timedelta(days=4)
    step2=datetime.timedelta(days=3)
    n=1
    while start<=end:
        t=start.strftime('%Y-%m-%d')
        valid_dates.append(t)
        if n&1:
            start+=step1
        else:
            start+=step2
        n+=1
    # print(valid_dates)
    n=len(roll_list)
    for i in range(n):
        full[roll_list[i]] = {}
    #     full[roll_list[i]][name_list[i]] = 1
        for j in range(len(valid_dates)):
            full[roll_list[i]][valid_dates[j]]=[0, 0, 0]
    # print(full)        
    df1=pd.read_csv(r'C:\Users\Dell Vostro 3491\OneDrive\Documents\GitHub\2001ME42_2022\tut06\input_attendance.csv')
    df1['Timestamp'] = pd.to_datetime(df1['Timestamp'], format='%d-%m-%Y %H:%M')
    df1['Dates'] = pd.to_datetime(df1['Timestamp']).dt.date
    df1['Time'] = pd.to_datetime(df1['Timestamp']).dt.time
    date_list=df1['Dates'].tolist()
    time_list=df1['Time'].tolist()
    n=len(date_list)
    # for i in range(n):
    #     print(date_list[i])    
    for i in range(n):
        roll_no=df1['Attendance'][i][:8]
        name=df1['Attendance'][i][9:]
    #     txt='{} {}'
    #     txt=txt.format(roll_no, name)
    #     print(txt)
    #     if isValidDetail(roll_no, name)==False:
    #         continue
        date=str(date_list[i])
        if isValidDate(date_list[i], roll_no)==False:
            continue
        curtime=time_list[i]
        if isValidTime(curtime)==False:
            full[roll_no][date][2]+=1
            continue
        if full[roll_no][date][0]==0:
            full[roll_no][date][0]=1
        else:
            full[roll_no][date][1]+=1
    # print(full['2001ME42'])

    final_col=['Roll', 'Name']
    for i in range(len(valid_dates)):
        final_col.append(str(valid_dates[i]))
    final_col.append('Actual Lecture Taken')
    final_col.append('Total Real')
    final_col.append('% Attendance')
    # print(final_col)
    df_final=pd.DataFrame(columns=final_col)
    cur=1
    for i in range(len(roll_list)):
        df_final.at[cur, 'Name']=name_list[i]
        df_final.at[cur, 'Roll']=roll_list[i]
        ctr=0
        for j in range(len(valid_dates)):
            if full[roll_list[i]][valid_dates[j]][0]==1:
                df_final.at[cur, valid_dates[j]]='P'
                ctr+=1
            else:
                df_final.at[cur, valid_dates[j]]='A'
        df_final.at[cur, 'Actual Lecture Taken']=ctr
        df_final.at[cur, 'Total Real']=len(valid_dates)
        percent=ctr/len(valid_dates)*100
        percent=round(percent, 2)
        df_final.at[cur, '% Attendance']=percent
        cur+=1
    # print(df_final.head(10))
    df_final.to_excel('C:/Users/Dell Vostro 3491/OneDrive/Documents/GitHub/2001ME42_2022/tut06/output/attendance_report_consolidated.xlsx', encoding='utf-8', index=False)

    n=len(roll_list)
    for i in range(n):
        df_cur=pd.DataFrame(columns=['Date', 'Roll', 'Name', 'Total Attendance Count', 'Real', 'Duplicate', 'Invalid', 'Absent'])
        cur=0
        df_cur.at[cur, 'Roll']=roll_list[i]
        df_cur.at[cur, 'Name']=name_list[i]
        cur+=1
        for j in full[roll_list[i]]:
            #j is date
            df_cur.at[cur, 'Date']=j
            df_cur.at[cur, 'Real']=full[roll_list[i]][j][0]
            df_cur.at[cur, 'Duplicate']=full[roll_list[i]][j][1]
            df_cur.at[cur, 'Invalid']=full[roll_list[i]][j][2]
            df_cur.at[cur, 'Total Attendance Count']=full[roll_list[i]][j][0]+full[roll_list[i]][j][1]+full[roll_list[i]][j][2]
            if full[roll_list[i]][j][0]==1:
                df_cur.at[cur, 'Absent']=0
            else:
                df_cur.at[cur, 'Absent']=1
            cur+=1
        Path='C:/Users/Dell Vostro 3491/OneDrive/Documents/GitHub/2001ME42_2022/tut06/output/'
        File=roll_list[i]+'.xlsx'
        df_cur.to_excel((Path+File), encoding='utf-8', index=False)
    ###Code


from platform import python_version
ver = python_version()
if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")



attendance_report()
#Add to receiver mail address in string to. For example, to='nitesh620137@gamil.com'
to=''
main_mail(to)



#This shall be the last lines of the code.
end_time = datetime.datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
