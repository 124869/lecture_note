print("[항공권 요금 계산 프로그램]")# 항공권 요금 계산 프로그램  (사이버보안학과 201920669 김우성)
print("출국일은 10월 15일입니다.") # 출국 날짜를 월과 일로 구분하여 입력받는다.
month=int(input("예약월: "))
day=int(input("예약일: "))
print("도착지 번호: 1. 미국, 2.영국, 3.중국") # 도착지 나라의 번호를 입력받아 저장한다. 
country=int(input("도착지 번호 입력: "))

depart=31+29+31+30+31+30+31+31+30+15 # 출국일을 1월1일 이후 경과일로 변환한다. 
reservation=0
if month==1: # 예약일로 출국일과 같은 방식으로 변환한다. 
    reservation=reservation+day
elif month==2:
    reservation=reservation+31+day
elif month==3:
    reservation=reservation+31+29+day
elif month==4:
    reservation=reservation+31+29+31+day
elif month==5:
    reservation=reservation+31+29+31+30+day
elif month==6:
    reservation=reservation+31+29+31+30+31+day
elif month==7:
    reservation=reservation+31+29+31+30+31+30+day
elif month==8:
    reservation=reservation+31+29+31+30+31+30+31+day
elif month==9:
    reservation=reservation+31+29+31+30+31+30+31+31+day
elif month==10:
    reservation=reservation+31+29+31+30+31+30+31+31+30+day

days=depart-reservation # 예약일과 출국일의 차이를 계산하여 남은 날짜를 계산한다.

if days>=200: # 남은 날짜에 따른 할인율을 계산한다. 
    discount=0.1
elif days>=100:
    discount=0.05
elif days>=50:
    discount=0.03
else:
    discount=0

if country==1: # 도착 나라의 번호로 항공권 요금을 정한다. 
    cost=1000000
elif country==2:
    cost=800000
elif country==3:
    cost=500000

cost=cost*(1-discount) # 요금에 할인율을 적용하여 실제 요금을 구한다. 

print("{} 월 {} 일에 예약하면 \n{} 일 전으로 할인율은 {} (%)입니다. \n항공권 요금은 {} 원입니다.".format(month,day,days,int(discount*100),int(cost)))

