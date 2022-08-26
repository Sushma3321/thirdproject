import requests
import json
def get():
    response = requests.get("http://saral.navgurukul.org/api/courses")
    content=json.loads(response.text)
    with open("courses.json","w")as f:
        json.dump(content,f,indent=8)
        store=content["availableCourses"]
    id=[]
    name=[]
    for i in range (0,len(store)):
        print(i+1,store[i]["name"],store[i]["id"])
 
        id.append(store[i]["id"])
        name.append(store[i]["name"])
    # print(id)
    # global id_number  
    id_number=int(input("enter the id number:"))-1
    api2="http://saral.navgurukul.org/api/courses"+"/"+str(id[id_number])+"/"+"exercises"
    res=requests.get(api2)
    data2=res.json()
    j=0
    l=0
    slug=[]
    while j<len(data2["data"]):
        print(l+1,data2["data"][j]["name"])
        slug.append(data2['data'][j]["slug"])
        l=l+1
        j=j+1
    slugname=int(input("**Enter your slug number:"))-1
    sluglist=requests.get("http://saral.navgurukul.org/api/courses/"+ str(id_number)+"/exercise/getBySlug?slug=" + slug[slugname])
    b=sluglist.json()
    with open("course_id.json","w") as k:
        json.dump(b,k,indent=4)
    with open("course_id.json","r") as k:
        d=json.load(k)
    print(d["name"])
    print(d["slug"])
    print("CONTENT",b["content"])
    pre_next = input("enter the 'n' for next and 'p' previous: ")
    if pre_next == "p":
        i = 0
        while i < len(slug):
            print(slug[slugname-1])
            print(b["content"]) 
            break
            i=i+1
    else:
        print("back")
        
   
get()





    


