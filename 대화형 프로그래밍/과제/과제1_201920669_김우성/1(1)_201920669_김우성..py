print("[주차 요금 계산 프로그램]") # 주차 요금 계산 프로그램 201920669 김우성
input_month=int(input("입차월: ")) # 입차날짜와 출차 날짜를 입력받는다.
input_day=int(input("입차일: "))
output_month=int(input("출차월: "))
output_day=int(input("출차일: "))

input=(input_month-1)*30+input_day # 각각의 날짜를 1월 1일을 기준으로 몇일인지 바꾼다.
if(input_month%2==0): # 홀수 달은 31일이므로 월을 고려해 날짜를 추가한다. 
    input=input+input_month/2
else:
    input=input+input_month/2-1

output=(output_month-1)*30+output_day # 입차일과 같은 방식으로 구한다.

if(output_month%2==0):
    output=output+output_month/2
else:
    output=output+output_month/2-1

day=int(output-input+1) # 입차일과 출차일의 차이에 1일을 더하여 총 주차 기간을 구한다.

if(day>=200): # 주차 기간이 200일이 넘은 경우를 조건문을 이용해 나누어 계산한다. 
    result=(day-199)*3000*0.9+199*3000
else:
    result=day*3000
result=int(result)

print("총 주차 기간은 {} 일이고,\n주차 요금은 {} 원입니다.".format(day,result))
