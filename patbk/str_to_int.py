from datetime import datetime
class time_ch:
    def __init__(self,s_time,e_time,p_time):
        self.stime=s_time
        self.etime=e_time
        self.ptime=p_time
        self.date=s_time
    def convertion(self):
        ltim=[str(self.stime),str(self.etime),str(self.ptime)+"00"]#here i add 00 to the patient time bcs the time not take from datbase so the seconds value is not there only have hr and minute value thats why ad 00 by making its in string bcs its in time format in in string
        a=" "
        l=[]
        #print(ltim,"times from st to int")
        for i in ltim:
            for k in str(i):
                #print(k,"str to int.py checking the stime")
                if k!=":":
                    a+=k
            l.append(a)
            #print(l,"from str to int")
            a=""
        if int(l[0])>int(l[1]):
            if int(l[1])>int(l[2]):#here it will check that the time is in am zone or pm zone if this is am zone and its less than the end time of doc thenif its pm zone then there no need to add one on the starting of the pt time its greater than the starttime and less than end time by giving 1 at starting of end time
                s="1"+l[2]
                l[2]=s
            s="1"+l[1]
            l[1]=s
            
        #print(int(l[0]),int(l[1]),int(l[2]),"from time checker in st to int")

        if int(l[0])<int(l[2]) and int(l[2])<int(l[1]):
            return(1)
        else:
            return(0)
    def date_to_weekday(self):
        # Convert the date string to a datetime object
        date_object = datetime.strptime(self.date, '%Y-%m-%d')
        
        # Get the full name of the weekday
        weekday = date_object.strftime('%A')
        
        weekday_dict = {
            "Monday": "1",
            "Tuesday": "2",
            "Wednesday": "3",
            "Thursday": "4",
            "Friday": "5",
            "Saturday": "6",
            "Sunday": "7"
        }
        #print(weekday_dict[weekday],"checking weekday")
        return(weekday_dict[weekday])


