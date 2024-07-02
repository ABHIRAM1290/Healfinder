from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import patient,docter,hospital
from .depfinder import dep
from .locfinder import search
# Create your views here.
def index(request):
    return render(request,"frontp.html")
def booking(request):
    #return HttpResponse("hello")
    if request.method=="POST":
        name=request.POST["patientName"]
        c_no=request.POST["patientContact"]
        date=request.POST["appointmentDate"]
        time=request.POST["apptime"]
        msg=request.POST["message"]
        age=request.POST["patientAge"]
        patloc=request.POST["patloc"]
        fnd=dep(msg)
        dprtmnt=fnd.finding()
        #time.remove(":")
        hos=search(patloc,list(dprtmnt)[0],time,date)
        hosname=hos.searchloc()
        print(hosname,"checking hos name")
        try:
            hos1=hosname[0][-1]#list inside anoher list that contain docter name and last hospital name thats are nearest one
            hosname[0].remove(hos1)
            hos2=hosname[1][-1]#list inside anoher list that contain docter name and last hospital name thats are second nearest one
            hosname[1].remove(hos2)
        except:
            #hosname=f'not found location{hosname}'
            return render(request,"index.html",{"msg":hosname})
        
        data=patient.objects.create(name=name,phone=c_no,date=date,reson=list(dprtmnt)[0],age=age,visit_hos=" ",visit_doc=" ",status=0,pat_time=time,location=patloc)# here i convert the list dict into the list to get the first value 
        data.save()
        data=patient.objects.get(name=name)
        return render(request,"profile.html",{"data":data,"pri_hos":hos1,"sec_hos":hos2,"pri_docs":hosname[0],"sec_docs":hosname[1]})
        
    return render(request,"index.html")#patient registration

def hospitalreg(request):
    if "hs" in request.session:
        hs_name=request.session["hs"]
        patdata=patient.objects.filter(visit_hos=hs_name)
        data=docter.objects.filter(hospital=hs_name)
        return render(request,"hs_profile.html",{"patdetail":patdata,"data":data})
    elif request.method=="POST":
        hs_name=request.POST["hs_name"]
        hs_pass=request.POST["hs_password"]
        cno=request.POST["hs_con"]
        hs_loc=request.POST["hs_loc"]
        #hs_loc_link=request.POST["loc_link"]
        hs_email=request.POST["hs_email"]
        hs_image = request.FILES.get("hs_img")
        rating=5
        lfind=search(hs_name.upper(),"hi","0","0")#here athor 3 atribute are not used so give invalid 0 value
        lonlan=lfind.hosploc()
        print(lonlan)
        data=hospital.objects.create(name=hs_name,password=hs_pass,cno=cno,email=hs_email,location=hs_loc,image=hs_image,rating=rating,long=lonlan[0],lat=lonlan[1])
        data.save()
        return render(request,"hs_login.html")
    return render(request,"hs_reg.html")
def hospitallog(request):
    if "hs" in request.session:
            hs_name=request.session["hs"]
            patdata=patient.objects.filter(visit_hos=hs_name)
            data=docter.objects.filter(hospital=hs_name)
            return render(request,"hs_profile.html",{"patdetail":patdata,"data":data})
    elif request.method=="POST":
        hs_name=request.POST["hs_name"]
        hs_pass=request.POST["hs_pass"]
        try: 
            data=hospital.objects.get(name=hs_name)
            #data={"name":data.name,"hospic"}
            print(data)
            if data.password==hs_pass:
                request.session["hs"]=hs_name
                hs_name=request.session["hs"]
                patdata=patient.objects.filter(visit_hos=hs_name)
                data=docter.objects.filter(hospital=hs_name)
                return render(request,"hs_profile.html",{"patdetail":patdata,"data":data})
            else:
                return render(request,"hs_login.html",{"msg":"login password not matching"})
        except:
            return render(request,"hs_login.html",{"msg":"Hospital Noy Found"})
    return render(request,"hs_login.html")
def admin_login(request):
       return redirect('/admin/')
def docreg(request):
    msg=""
    if request.method=="POST":
     name=request.POST["doc_name"]
     experinace=request.POST["doc_exp"]
     doc_con=request.POST["doc_con"]
     doc_email=request.POST["doc_email"]
     doc_img=request.FILES["doc_img"]
     doc_dpt=request.POST["doc_dpt"]
     st_time=request.POST["st_time"]
     end_time=request.POST["end_time"]
     days=request.POST.getlist("days")#here get list method is used to get data from the html as lst format becs the name have more than one value so used get ist method
     avl_days=""
     for i in days:
        avl_days+=i# here the days are in list format so i use for loop and add eac elemnt from the days and add to avail days as string concantination
     #print(type(st_time),end_time,"hhkhjkh")
     data=docter.objects.create(name=name,dpt=doc_dpt,exp=experinace,img=doc_img,hospital=request.session["hs"],rating=5,con_no=doc_con,st_time=st_time,end_time=end_time,day_avail=avl_days)
     data.save()#date and time are in string format
     msg="logged succesfully"
    return render(request,"docter.html",{"msg":msg})
def logout(request):
    request.session.flush()
    return render(request,"hs_login.html")
def confirm_bk(request):#confirm the hospital and docter
    if request.method=="POST":
        hos= request.POST["hos"]
        doc= request.POST["doc"]
        name= request.POST["name"]
        data=patient.objects.filter(name=name)#get may be cause error while updating
        data.update(visit_hos=hos,visit_doc=doc) 
        k={"ko":0,"data":data}#there need to pass value like this if it need to ckeck the if condtion
        data=patient.objects.get(name=name)
        return render(request,"profile.html",{"data":data})
  

        

