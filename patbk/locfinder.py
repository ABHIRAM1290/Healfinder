from math import radians, sin, cos, sqrt, atan2
from .models import hospital,docter,hospital
from .str_to_int import time_ch
class search():
    def __init__(self,location,dpt,time,date):
        self.loc=location
        self.dpt=dpt
        self.time=time
        self.date=date
    def searchloc(self):

        def haversine_distance(lat1, lon1, lat2, lon2):
            """
            Calculate the great circle distance between two points
            on the Earth's surface given their latitude and longitude
            in degrees.
            """  
            # Convert latitude and longitude from degrees to radians
            lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
            # Haversine formula
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            earth_radius_km = 6371  # Earth radius in kilometers
            distance = earth_radius_km * c
            return distance
        # Example usage:
        locations = {
            "KOCHI": [9.9312, 76.2673],
            "FORT KOCHI": [9.9647, 76.2422],
            "MATTANCHERRY": [9.9575, 76.2591],
            "ERNAKULAM TOWN": [9.9924, 76.2922],
            "KAKKANAD": [10.0128, 76.3328],
            "TRIPUNITHURA": [9.9392, 76.3431],
            "ALUVA": [10.1076, 76.3511],
            "THRIKKAKARA": [10.0369, 76.3494],
            "EDAPPALLY": [10.0331, 76.3086],
            "VYTTILA": [9.9696, 76.3188],
            "KADAVANTHRA": [9.9610, 76.3026],
            "PALARIVATTOM": [9.9884, 76.3116],
            "KALOOR": [9.9985, 76.3025],
            "PANAMPILLY NAGAR": [9.9627, 76.2996],
            "MARINE DRIVE": [9.9658, 76.2823],
            "THOPPUMPADY": [9.9303, 76.2665],
            "PALLURUTHY": [9.9198, 76.2695],
            "CHERAI": [10.1514, 76.1905],
            "KALAMASSERY": [10.0581, 76.3134],
            "THRIKKAKARA MUNICIPALITY": [10.0320, 76.3373],
            "MUVATTUPUZHA": [9.9757, 76.5733],
            "PERUMBAVOOR": [10.1068, 76.4707],
            "ANGAMALY": [10.2033, 76.3860],
            "NORTH PARAVUR": [10.1410, 76.2133],
            "KODUNGALLUR": [10.2292, 76.1994],
            "KOTHAMANGALAM": [10.0652, 76.6281],
            "PIRAVOM": [9.8665, 76.5679],
            "MULANTHURUTHY": [9.8711, 76.4836],
            "PARAVUR": [9.6849, 76.3375],
            "THIRUVANKULAM": [9.9605, 76.3637],
            "VARAPUZHA": [10.0851, 76.2254],
            "VYPIN ISLAND": [10.1460, 76.2273],
            "MOOTHAKUNNAM": [10.1645, 76.1777],
            "CHERANALLOOR": [10.0082, 76.2902],
            "VAZHAKKALA": [10.0093, 76.3395],
            "MARADU": [9.9492, 76.3190],
            "KADAMAKKUDY": [10.1597, 76.2344],
            "VADUTHALA": [9.9767, 76.2830],
            "THIRUVANIYOOR": [9.9756, 76.2534],
            "PALLIKKARA": [10.0465, 76.3844],
            "KAKKANAD WEST": [10.0150, 76.3297],
            "KIZHAKKAMBALAM": [10.0997, 76.4279],
            "ELAMAKKARA": [10.0246, 76.3165],
            "THRIPUNITHURA TOWN": [9.9381, 76.3414],
            "EDAKOCHI": [9.9403, 76.2785],
            "VAZHAKKULAM": [9.8214, 76.5529],
            "KOOTHATTUKULAM": [9.9029, 76.5828],
            "THRIKKARIYOOR": [9.8362, 76.5021]}
        loc=self.loc.upper()
        if loc in locations:
                
                hos=[]#list of hospital from these criteria from these selected docter by available date time and dpt
                doct=[]# list doc from these criteria vailable docters by time and date and dpt
                hos_near=[]# add nearest hospital
                lon1,lat1 = locations[loc][0], locations[loc][1]  # dic format to enable the list and in the list slect long and lang
                try:
                    doc=docter.objects.filter(dpt=self.dpt)
                    for i in doc:
                        check=time_ch(i.st_time,i.end_time,self.time)#get the starting end time and pat time
                        result=check.convertion()
                        if result==1:
                            check=time_ch(self.date,"0","0",) #check day11
                            check_date=check.date_to_weekday()
                            #print(check_date,"date avail checking")
                            if check_date in i.day_avail:
                            # print(i.hospital,"checking i.hos")
                                doct.append(i.name)#here append doctername create list with that pertcular shceduled docter
                                hos.append(i.hospital)#the selected docter hospital
                                #finally we get the list of all hospital and docter with thsese criteria
                    
                    
                    hos=set(hos)#for avoiding duplication here use set and then
                    hos=list(hos)#convert back it into list
                    for n in range(2):
                        #print(hos,"number counting")
                        dis=1000#make starting distance 1000 to get least distace from the hospital properly
                        for k in hos:#take each and every hospial name from the list
                            d=hospital.objects.get(name=k)
                            lon2,lat2 = d.long, d.lat  # Latitude and longitude of Los Angeles
                            distance = haversine_distance(lat1, lon1, lat2, lon2)
                            if dis>distance:
                                    dis=distance
                                    hs=d.name
                                   # print(hs,dis,"low distance")
                        if hs not in hos_near:#heare it will avoid multiple hospitle name addtion bcs the outer loop stil working
                            hos_near.append(hs)#list of nearest hospital and the nearst one have index value one
                        #print(hos,hos_near,"checking hos")
                        try:#here i use try except bcs the hos may be have only one hospital its only work when its have more than one hospital
                            hos.remove(hs)
                        except:
                            print("met the hospital limit")
                    hos=[]
                    hos1=[]
                    for i in doct:
                        print(hs)
                        docter1=docter.objects.get(name=i)
                        if docter1.hospital==hos_near[0]:
                            print("docter ok")
                            hos.append(docter1.name)
                        if docter1.hospital==hos_near[1]:
                            # print("docter ok")
                            hos1.append(docter1.name)
                    hos.append(hos_near[0])#here we hetall this hospitals available docters
                    hos1.append(hos_near[1])#here we hetall this hospitals available docters 
                    print([hos,hos1])
                    return([hos,hos1])
                except:
                    return("the website under cnstructions")

                
        else:
            return(f"{loc} not found re enter location")
    def hosploc(self):#finding hospital longitude and latiude
        locations = {
            "BALAJI MEDICAL CENTRE": [9.984646, 76.285249],
            "LOURDES HOSPITAL": [10.006647, 76.276862],
            "LISIE HOSPITAL": [9.988574, 76.288604],
            "ERNAKULAM GENERAL HOSPITAL": [9.971564, 76.281531],
            "DOCTOR'S HOSPITAL": [9.999893, 76.306923],
            "RENAI MEDICITY": [10.007812, 76.303760],
            "M.A.J. HOSPITAL": [10.020872, 76.307970],
            "FUTUREACE HOSPITAL": [10.031869, 76.304280],
            "ST.JOSEPH'S HOSPITAL TRUST": [10.060443, 76.301728],
            "GOVT. AYURVEDA DISPENSARY, ELOOR GRAMA PANCHAYAT": [10.052621, 76.304247],
            "ERNAKULAM MEDICAL CENTRE": [9.999455, 76.314206],
            "KOCHI": [9.9312, 76.2673],
            "FORT KOCHI": [9.9647, 76.2422],
            "MATTANCHERRY": [9.9575, 76.2591],
            "ERNAKULAM TOWN": [9.9924, 76.2922],
            "KAKKANAD": [10.0128, 76.3328],
            "TRIPUNITHURA": [9.9392, 76.3431],
            "ALUVA": [10.1076, 76.3511],
            "THRIKKAKARA": [10.0369, 76.3494],
            "EDAPPALLY": [10.0331, 76.3086],
            "VYTTILA": [9.9696, 76.3188],
            "KADAVANTHRA": [9.9610, 76.3026],
            "PALARIVATTOM": [9.9884, 76.3116],
            "KALOOR": [9.9985, 76.3025],
            "PANAMPILLY NAGAR": [9.9627, 76.2996],
            "MARINE DRIVE": [9.9658, 76.2823],
            "THOPPUMPADY": [9.9303, 76.2665],
            "PALLURUTHY": [9.9198, 76.2695],
            "CHERAI": [10.1514, 76.1905],
            "KALAMASSERY": [10.0581, 76.3134],
            "THRIKKAKARA MUNICIPALITY": [10.0320, 76.3373],
            "MUVATTUPUZHA": [9.9757, 76.5733],
            "PERUMBAVOOR": [10.1068, 76.4707],
            "ANGAMALY": [10.2033, 76.3860],
            "NORTH PARAVUR": [10.1410, 76.2133],
            "KODUNGALLUR": [10.2292, 76.1994],
            "KOTHAMANGALAM": [10.0652, 76.6281],
            "PIRAVOM": [9.8665, 76.5679],
            "MULANTHURUTHY": [9.8711, 76.4836],
            "PARAVUR": [9.6849, 76.3375],
            "THIRUVANKULAM": [9.9605, 76.3637],
            "VARAPUZHA": [10.0851, 76.2254],
            "VYPIN ISLAND": [10.1460, 76.2273],
            "MOOTHAKUNNAM": [10.1645, 76.1777],
            "CHERANALLOOR": [10.0082, 76.2902],
            "VAZHAKKALA": [10.0093, 76.3395],
            "MARADU": [9.9492, 76.3190],
            "KADAMAKKUDY": [10.1597, 76.2344],
            "VADUTHALA": [9.9767, 76.2830],
            "THIRUVANIYOOR": [9.9756, 76.2534],
            "PALLIKKARA": [10.0465, 76.3844],
            "KAKKANAD WEST": [10.0150, 76.3297],
            "KIZHAKKAMBALAM": [10.0997, 76.4279],
            "ELAMAKKARA": [10.0246, 76.3165],
            "THRIPUNITHURA TOWN": [9.9381, 76.3414],
            "EDAKOCHI": [9.9403, 76.2785],
            "VAZHAKKULAM": [9.8214, 76.5529],
            "KOOTHATTUKULAM": [9.9029, 76.5828],
            "THRIKKARIYOOR": [9.8362, 76.5021]}
        
        if self.loc in locations:
            lola=locations[self.loc]
            return lola# actually the locations are taken in the form of hospital name not the assigned location


