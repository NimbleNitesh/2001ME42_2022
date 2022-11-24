import pandas as pd
from datetime import datetime
#starting the datatime module to find executiontime

start_time = datetime.now()
try:
    def ballsToOver(balls):
        val1=balls//6
        val2=balls%6
    #     print(val2)
        if val2==0:
            return str(val1)
        s=str(val1)+'.'+str(val2)
        return s
except:
    print('Error in ballsToOver function')
    exit()

#Help
def scorecard():
    ind_bt={}
    ind_ball={}
    pak_bt={}
    pak_ball={}
    ind_list=[]
    pak_list=[]
    try:
        with open("teams.txt", 'r') as file_data:
            line_no=0
            for line in file_data:
                line_no+=1
                data = line.split()
                if line_no==1 or line_no==3:
                    for i in range(3, len(data), 2):
                        s=data[i]+' '+data[i+1]
                        if s[len(s)-1]==',':
                            s=s[:-1]
                        if data[0]=='Pakistan':
                            pak_bt[s]=[0, 0, 0, 0, '']#run, ball, 4, 6, how out
                            pak_ball[s]=[0, 0, 0, 0, 0, 0, 0]#balls, maiden, run, wicket, wide, byes, leg
                        else:
                            ind_bt[s]=[0, 0, 0, 0, '']#run, ball, 4, 6, how out
                            ind_ball[s]=[0, 0, 0, 0, 0, 0, 0]#balls, maiden, run, wicket, wide, byes, leg
        # print(pak_bt)
    except:
        print('Error in working on teams.txt')
        exit()


    try:
        line_no=0
        ind_gen={
            'Bhuvneshwar':'Bhuvneshwar Kumar',
            'Chahal':'Yuzvendra Chahal',
            'Jadeja':'Ravindra Jadeja',
            'Rohit':'Rohit Sharma(c)',
            'Rahul':'KL Rahul',
            'Kohli':'Virat Kohli',
            'Karthik':'Dinesh Karthik(w)',
            
        }
        pak_gen={
            'Rizwan':'Mohammad Rizwan(w)',
            'Dahani':'Shahnawaz Dahani',
            'Khushdil':'Khushdil Shah',
            'Babar Azam':'Babar Azam(c)'
        }
        cur_score_pak=0
        cur_wicket_pak=0
        cur_ball_pak=0
        p_run_pak=0
        with open("pak_inns1.txt", 'r') as file_data:
            for line in file_data:
                line_no+=1
                if line_no&1==0:
                    continue
                data=line.split()
        #         print(data[1:])
                to_index=-1
                cur_ball_pak=data[0]
                baller_ind=-1
                for i in range(len(data)):
                    if data[i]=='to':
                        to_index=i
                        break
                for i in range(len(data)):
                    if data[i][-1]==',':
                        baller_ind=i
                        data[i]=data[i][:-1]
                        break
                if data[baller_ind+1][-1]==',':
                    data[baller_ind+1]=data[baller_ind+1][:-1]
                if data[baller_ind+1]=='FOUR':
                    data[baller_ind+1]=4
                elif data[baller_ind+1]=='no':
                    data[baller_ind+1]=0
                elif data[baller_ind+1]=='SIX':
                    data[baller_ind+1]=6
        #         if to_index+1==baller_ind:
        #             data[baller_ind]=pak_gen[data[baller_ind]]
                bowler=''#data[1:to_index]
                for i in range(1, to_index):
                    bowler=bowler+data[i]+' ';
                bowler=bowler[:-1]
                if bowler in ind_gen.keys():
                    bowler=ind_gen[bowler]
        #         batsman=data[to_index+1:baller_ind+1]
                batsman=''
                for i in range(to_index+1, baller_ind+1):
                    batsman=batsman+data[i]+' ';
                batsman=batsman[:-1]
                if batsman in pak_gen.keys():
                    batsman=pak_gen[batsman]
                res=data[baller_ind+1]
                if res=='out':
                    cur_wicket_pak+=1
        #             cur_ball_pak+=1
                    i=len(data)-1
                    while 1:
                        if data[i][-1]=='.' or data[i][-1]=='!':
                            break
                        i-=1
        #             print(data[i+1:])
                        v=0
                        s=''
                        for j in range(i+2, len(data)):
                            if data[j]!='b' and data[j]!='c' and data[j]!='lbw' and v==0:
                                v=1
                                continue
                            if(data[j][-1]==')' or data[j][-1]==']'):
                                break
                            s=s+data[j]+' '
                    ind_ball[bowler][3]+=1
                    s=s[:-1]
                    pak_bt[batsman][-1]=s
                    l=[]
                    l.append(cur_score_pak)
                    l.append(cur_wicket_pak)
                    l.append(batsman)
                    l.append(data[0])
                    pak_list.append(l)
        #             print(s)
        #         print(batsman)
        #         print(res)
                if res!='wide' and res!='byes' and res!='out' and res!='leg':
                    res=int(res)
        #             print(res)
        #             print(type(res))
                    cur_score_pak+=res
                    pak_bt[batsman][0]+=res
                    ind_ball[bowler][2]+=res
                if res=='byes':
                    ind_ball[bowler][-2]+=1
                    cur_score_pak+=1
                if res=='leg':
                    ind_ball[bowler][-1]+=1
                    cur_score_pak+=1
                if res=='wide':
                    ind_ball[bowler][-3]+=1
                    ind_ball[bowler][2]+=1
                    cur_score_pak+=1
                if res==4:
                    pak_bt[batsman][2]+=1
                if res==6:
                    pak_bt[batsman][3]+=1
                if res!='wide':
        #             cur_ball_pak+=1
                    ind_ball[bowler][0]+=1
                    pak_bt[batsman][1]+=1
                    if res!='out':
                        pak_bt[batsman][-1]='Not Out'
        #         print(type(cur_ball_pak))
                if cur_ball_pak=='5.6':
        #             print(cur_score_pak)
                    p_run_pak=cur_score_pak
        # print(ind_ball)
        # print(pak_bt) 
        # print(pak_list)
    except:
        print('Error in working on pak_inns1.txt')
        exit()


    try:
        # print(ind_bt)
        line_no=0
        cur_score_ind=0
        cur_wicket_ind=0
        cur_ball_ind=0
        p_run_ind=0
        with open("india_inns2.txt", 'r') as file_data:
            for line in file_data:
                line_no+=1
                if line_no&1==0:
                    continue
                data=line.split()
        #         print(data[1:])
                cur_ball_ind=data[0]
                to_index=-1
                baller_pak=-1
                for i in range(len(data)):
                    if data[i]=='to':
                        to_index=i
                        break
                next=''
                for i in range(len(data)):
                    if data[i][-1]==',':
                        baller_pak=i
                        next=data[i+2]
                        data[i]=data[i][:-1]
                        break
        #         print(next)
                if data[baller_pak+1][-1]==',':
                    data[baller_pak+1]=data[baller_pak+1][:-1]
                if data[baller_pak+1]=='FOUR':
                    data[baller_pak+1]=4
                elif data[baller_pak+1]=='no':
                    data[baller_pak+1]=0
                elif data[baller_pak+1]=='SIX':
                    data[baller_pak+1]=6
        #         if to_index+1==baller_ind:
        #             data[baller_pak]=pak_gen[data[baller_pak]]
                bowler=''#data[1:to_index]
                for i in range(1, to_index):
                    bowler=bowler+data[i]+' ';
                bowler=bowler[:-1]
                if bowler in pak_gen.keys():
                    bowler=pak_gen[bowler]
        #         batsman=data[to_index+1:baller_ind+1]
                batsman=''
                for i in range(to_index+1, baller_pak+1):
                    batsman=batsman+data[i]+' ';
                batsman=batsman[:-1]
                if batsman in ind_gen.keys():
                    batsman=ind_gen[batsman]
                res=data[baller_pak+1]
                if res=='out':
                    cur_wicket_ind+=1
                    i=len(data)-1
                    while 1:
                        if data[i][-1]=='.' or data[i][-1]=='!':
                            break
                        i-=1
        #             print(data[i+1:])
                        s=''
                        v=0
                        for j in range(i+2, len(data)):
                            if data[j]!='b' and data[j]!='c' and data[j]!='lbw' and v==0:
                                v=1
                                continue
                            if(data[j][-1]==')' or data[j][-1]==']'):
                                break
                            s=s+data[j]+' '
                    pak_ball[bowler][3]+=1
                    pak_ball[bowler][0]+=1
                    s=s[:-1]
                    ind_bt[batsman][-1]=s
        #             print(s)
                    ind_bt[batsman][1]+=1
                    l=[]
                    l.append(cur_score_ind)
                    l.append(cur_wicket_ind)
                    l.append(batsman)
                    l.append(data[0])
                    ind_list.append(l)
        #balls, maiden, run, wicket, wide, byes, leg
        #run, ball, 4, 6, how out
                elif res=='wide':
        #             pak_ball[bowler][2]+=(res+1)
        #             print(bowler)
                    cur_score_ind+=1
                    pak_ball[bowler][4]+=1
                    pak_ball[bowler][2]+=1
                elif next=='wides,':
                    res=int(res)
        #             print(bowler)
                    cur_score_ind+=res
                    pak_ball[bowler][2]+=res
                    pak_ball[bowler][4]+=res
                elif res=='byes' or res=='leg':
                    res=data[baller_pak+3]
                    if res=='FOUR,':
                        res=4
                    if res=='SIX,':
                        res=6
                    res=int(res)
                    ind_bt[batsman][1]+=res
                    cur_score_ind+=res
                    pak_ball[bowler][0]+=res
                    ind_bt[batsman][-1]='Not Out'
                else:
                    res=int(res)
                    ind_bt[batsman][0]+=res
                    cur_score_ind+=res
                    ind_bt[batsman][1]+=1
                    pak_ball[bowler][0]+=1
                    ind_bt[batsman][-1]='Not Out'
                    pak_ball[bowler][2]+=res
                    if res==4:
                        ind_bt[batsman][2]+=1
                    if res==6:
                        ind_bt[batsman][3]+=1
                if cur_ball_ind=='5.6':
        #             print(cur_score_ind)
                    p_run_ind=cur_score_ind
        #         print(cur_ball_ind, cur_score_ind)
        # print(pak_ball)
        # print(ind_bt)
    except:
        print('Error in working on india_inns2.txt')
        exit()


    try:
        df = pd.DataFrame()
        df = df.reindex(columns = df.columns.tolist() + ['Batter', ' ', 'R', 'B', '4s', '6s', 'SR', '  ', '   '])
    except:
        print('Error in creating python DataFrame')
        exit()


    try:
        df.at[0, 'Batter']='Pakistan Innings'
        df.at[1, 'Batter']='Batter'
        df.at[1, ' ']=''
        df.at[1, 'R']='R'
        df.at[1, 'B']='B'
        df.at[1, '4s']='4s'
        df.at[1, '6s']='6s'
        df.at[1, 'SR']='SR'
        cur_row=2
        wide=bye=leg_bye=0
        for i in pak_bt:
            df.at[cur_row, 'Batter']=i
            df.at[cur_row, ' ']=pak_bt[i][-1]
            df.at[cur_row, 'R']=pak_bt[i][0]
            df.at[cur_row, 'B']=pak_bt[i][1]
            df.at[cur_row, '4s']=pak_bt[i][2]
            df.at[cur_row, '6s']=pak_bt[i][3]
            sr=pak_bt[i][0]/pak_bt[i][1]*100
            sr=round(sr, 2)
            df.at[cur_row, 'SR']=sr
            cur_row+=1
        #wide, byes, leg
        for i in ind_ball:
            wide+=ind_ball[i][-3]
            bye+=ind_ball[i][-2]
            leg_bye+=ind_ball[i][-1]
        df.at[cur_row, 'Batter']='Extras'
        txt='{} (b {}, lb {}, w {}, nb {}, p {})'
        txt=txt.format(wide+bye+leg_bye, bye, leg_bye, wide, 0, 0)
        df.at[cur_row, 'R']=txt
        df.at[cur_row, 'Batter']='Total'
        txt='{} ({} wkts, {} Ov)'
        # print(cur_ball_pak)
        txt=txt.format(cur_score_pak, cur_wicket_pak, cur_ball_pak)
        df.at[cur_row, 'R']=txt
        cur_row+=1
        df.at[cur_row, 'Batter']='Fall of Wickets'
        cur_row+=1
        txt=''
        for i in pak_list:
            ano='{}-{} ({}, {})'
            ano=ano.format(i[0], i[1], i[2], i[3])
            txt=txt+ano+' '
        # print(txt)
        df.at[cur_row, 'Batter']=txt
        cur_row+=1
        df.at[cur_row, 'Batter']='Bowler'
        df.at[cur_row, 'R']='O'
        df.at[cur_row, 'B']='M'
        df.at[cur_row, '4s']='R'
        df.at[cur_row, '6s']='W'
        df.at[cur_row, 'SR']='NB'
        df.at[cur_row, '  ']='WD'
        df.at[cur_row, '   ']='ECO'
        cur_row+=1
        for i in ind_ball:
            if ind_ball[i][0]==0:
                continue
            df.at[cur_row, 'Batter']=i
            df.at[cur_row, 'R']=ballsToOver(ind_ball[i][0])
            df.at[cur_row, 'B']=ind_ball[i][1]
            df.at[cur_row, '4s']=ind_ball[i][2]
            df.at[cur_row, '6s']=ind_ball[i][3]
            df.at[cur_row, 'SR']=0
            df.at[cur_row, '  ']=ind_ball[i][4]
            val=ind_ball[i][2]/ind_ball[i][0]*6
            val=round(val, 2)
            df.at[cur_row, '   ']=val
            cur_row+=1
        df.at[cur_row, 'Batter']='Powerplays'
        df.at[cur_row, 'R']='Overs'
        df.at[cur_row, '   ']='Runs'
        cur_row+=1
        df.at[cur_row, 'Batter']='Mandatory'
        df.at[cur_row, 'R']='0.1-6'
        df.at[cur_row, '   ']=p_run_pak
    except:
        print('Error in working on Pakistan Innings table')
        exit()


    try:
        cur_row+=1
        df.at[cur_row, 'Batter']='India Innings'
        cur_row+=1
        df.at[cur_row, 'Batter']='Batter'
        df.at[cur_row, ' ']=''
        df.at[cur_row, 'R']='R'
        df.at[cur_row, 'B']='B'
        df.at[cur_row, '4s']='4s'
        df.at[cur_row, '6s']='6s'
        df.at[cur_row, 'SR']='SR'
        cur_row+=1
        wide=bye=leg_bye=0
        for i in ind_bt:
            if ind_bt[i][1]==0:
                continue
            df.at[cur_row, 'Batter']=i
            df.at[cur_row, ' ']=ind_bt[i][-1]
            df.at[cur_row, 'R']=ind_bt[i][0]
            df.at[cur_row, 'B']=ind_bt[i][1]
            df.at[cur_row, '4s']=ind_bt[i][2]
            df.at[cur_row, '6s']=ind_bt[i][3]
            sr=ind_bt[i][0]/ind_bt[i][1]*100
            sr=round(sr, 2)
            df.at[cur_row, 'SR']=sr
            cur_row+=1
        #wide, byes, leg
        for i in pak_ball:
            wide+=pak_ball[i][-3]
            bye+=pak_ball[i][-2]
            leg_bye+=pak_ball[i][-1]
        df.at[cur_row, 'Batter']='Extras'
        txt='{} (b {}, lb {}, w {}, nb {}, p {})'
        txt=txt.format(wide+bye+leg_bye, bye, leg_bye, wide, 0, 0)
        df.at[cur_row, 'R']=txt
        df.at[cur_row, 'Batter']='Total'
        txt='{} ({} wkts, {} Ov)'
        # print(cur_ball_pak)
        txt=txt.format(cur_score_ind, cur_wicket_ind, cur_ball_ind)
        df.at[cur_row, 'R']=txt
        cur_row+=1
        df.at[cur_row, 'Batter']='Fall of Wickets'
        cur_row+=1
        txt=''
        for i in ind_list:
            ano='{}-{} ({}, {})'
            ano=ano.format(i[0], i[1], i[2], i[3])
            txt=txt+ano+' '
        # print(txt)
        df.at[cur_row, 'Batter']=txt
        cur_row+=1
        df.at[cur_row, 'Batter']='Bowler'
        df.at[cur_row, 'R']='O'
        df.at[cur_row, 'B']='M'
        df.at[cur_row, '4s']='R'
        df.at[cur_row, '6s']='W'
        df.at[cur_row, 'SR']='NB'
        df.at[cur_row, '  ']='WD'
        df.at[cur_row, '   ']='ECO'
        cur_row+=1
        for i in pak_ball:
            if pak_ball[i][0]==0:
                continue
            df.at[cur_row, 'Batter']=i
            df.at[cur_row, 'R']=ballsToOver(pak_ball[i][0])
            df.at[cur_row, 'B']=pak_ball[i][1]
            df.at[cur_row, '4s']=pak_ball[i][2]
            df.at[cur_row, '6s']=pak_ball[i][3]
            df.at[cur_row, 'SR']=0
            df.at[cur_row, '  ']=pak_ball[i][4]
            val=pak_ball[i][2]/pak_ball[i][0]*6
            val=round(val, 2)
            df.at[cur_row, '   ']=val
            cur_row+=1
        df.at[cur_row, 'Batter']='Powerplays'
        df.at[cur_row, 'R']='Overs'
        df.at[cur_row, '   ']='Runs'
        cur_row+=1
        df.at[cur_row, 'Batter']='Mandatory'
        df.at[cur_row, 'R']='0.1-6'
        df.at[cur_row, '   ']=p_run_ind
    except:
        print('Error in working on Indian Innings table')
        exit()


    try:
        df.to_csv('Scorecard.csv', index=False)
    except:
        print('Error in exporting csv file')
        exit()

###Code

from platform import python_version
ver = python_version()

if ver == "3.8.10":
	print("Correct Version Installed")
else:
	print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


scorecard()



#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
