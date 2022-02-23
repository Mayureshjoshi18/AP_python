

day=[]; km=[]; hr=[]; speed=[]

def TimeToHr(time_str):
    # Get Seconds from time
    h, m, s = time_str.split(':')
    seconds = int(h) * 3600 + int(m) * 60 + int(s)
    return round(seconds/3600,2)

def StepToKm(steps):
    km = steps/1400
    return round(km,2)

def Average(lst):
    return round(sum(lst) / len(lst),2)

def BMI(w,h):
    bmi=weight/((height/100)**2)
    if(bmi<18.5):
        print("Your BMI is:",round(bmi, 1),". Try to put on some weight!!")
    elif(18.5<=bmi<=24.9):
        print("Your BMI is:",round(bmi, 1),". You are healthy, maintain it!!")
    elif(25.0<=bmi<=29.9):
        print("Your BMI is:",round(bmi, 1),". You are overweight, do exercise!!")
    else:
        print("Your BMI is:",round(bmi, 1),". You are obese, alert!!")


def remove_items(test_list, item):    
    # remove the item for all its occurrences
    global award
    award=7
    for i in test_list:
        if(i == item):
            award=award-1
            test_list.remove(i)
  
    return test_list


name=input("Name: ")
sex=input("Sex: ")
age=int(input("Age (years): "))
weight=float(input("Weight (Kg): "))
height=float(input("Height (cms): "))
while(1):
    duration=input("Please specify the duration week/month: ")
    if(duration.lower()=="week"):
        no=int(input("Enter the No. of Week for which you want to insert data: "))
        duration=1
        break
    elif(duration.lower()=="month"):
        no=int(input("Enter the No. of Month for which you want to insert data: "))
        duration=4
        break
    else:
        print("Please enter valid input")
for j in range(no):
    for i in range(0,duration):
        while(1):
            str = input("")
            i=str.split(', ')
            if(i[0] >= '8' or i[0] <= '0'):
                print("Alert! Please give day input between 1-7")
                continue
            elif(i[0] == '7'):
                day.append(int(i[0]))
                km.append(StepToKm(int(i[1])))
                hr.append(TimeToHr(i[2]))
                break
            else:
                day.append(int(i[0]))
                km.append(StepToKm(int(i[1])))
                hr.append(TimeToHr(i[2]))

for i in range(len(day)):
    if(hr[i]==0.0):
        speed.append(0)
    else:
        speed.append(km[i]/hr[i])

remove_items(speed,0)
remove_items(km,0.0)

print("Hi,",name)
BMI(weight,height)
print("Your Weekly achievement is as follows:")
if(award==7):
    print("No breakout in Sessions: You get a 7/7 award")
else:
    print("You have a breakout in Sessions: You get a ",award,"/7 award", sep='')
print("Your Fastest Speed is:",round(max(speed),2),"km/hr")
print("Your Longest Distance is:",max(km),"km")
print("Your Slowest Speed is:",round(min(speed),2),"km/hr")
print("Your Shortest Distance is:",min(km),"km")
print("Your Weekly Average Speed is:",Average(speed),"Km/hr")
print("Your Weekly Average Distance is:",Average(km),"Km")


