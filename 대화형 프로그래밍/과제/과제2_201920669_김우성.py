"""
 Author : 사이버보안학과 201920669 김우성

 Details : 모양 출력 프로그램

 Input  :  모양 번호, 크기 

 Output  : 결과 모양

 File Name  : 과제2.py

 History  : 2020/05/29

"""
def alphabet(n):  # 알파벳 함수
    if (n%2==1): # 홀수인 경우
        star=n
        space=0
        for i in range(int(n/2)+1): # 윗부분 출력
            a=65
            for j in range(space):
                print("  ",end="")
            for j in range(star):
                print(chr(a)+" ",end="")
                if j<star/2-1:
                    a=a+1
                else:
                    a=a-1
            space=space+1
            star=star-2
            print()
            
        star=3
        space=int(n/2)-1
        for i in range(int(n/2)): # 아랫 부분 출력
            a=65
            for j in range(space):
                print("  ",end="")
            for j in range(star):
                print(chr(a)+" ",end="")
                if j<star/2-1:
                    a=a+1
                else:
                    a=a-1
            space=space-1
            star=star+2
            print()
    else: # 짝수인 경우 
        star=n
        space=0
        for i in range(int(n/2)): # 윗부분 출력
            a=65
            for j in range(space): # 빈칸과 알파벳을 각각 for문으로 출력한다.
                print("  ",end="")
            for j in range(star):
                print(chr(a)+" ",end="")
                if j==star/2-1: # 알파벳을 조건에 따라 변경하며 출력한다.
                    a=a
                elif j<star/2-1:
                    a=a+1
                else:
                    a=a-1
            space=space+1
            star=star-2
            print()
        star=2
        space=int(n/2)-1
        
        for i in range(int(n/2)): # 아랫부분 출력
            a=65
            for j in range(space): # 빈칸과 알파벳을 각각 for문으로 출력한다.
                print("  ",end="")
            for j in range(star):
                print(chr(a)+" ",end="")
                if j==star/2-1: # 알파벳을 조건에 따라 변경하며 출력한다.
                    a=a
                elif j<star/2-1:
                    a=a+1
                else:
                    a=a-1
            space=space-1
            star=star+2
            print()
            
    return 0
def number(n): # 숫자 함수 
    
    if (n%2 == 1): # 홀수인 경우 
        n=n*2-1
        star=2
        space=n-star
        for i in range(int(n/2)): # 윗부분 출력 
            a=1
            for j in range(int(star/2)): # 왼쪽 숫자 출력 
                print(str(a)+" ",end="")
                a=a+1
            for j in range(space): # 가운데 빈칸 출력
                print("  ",end="")
            a=a-1
            for j in range(int(star/2)): # 오른쪽 숫자 출력
                print(str(a)+" ",end="")
                a=a-1
            star=star+2
            space=n-star
            print()

            
        a=1  
        for i in range(n): # 중간 한줄 출력 파트
            print(str(a)+" ",end="")
            if (i<n/2-1):
                a=a+1
            else:
                a=a-1
        print()
        
        star=n-1
        space=n-star
        for i in range(int(n/2)): # 아랫 부분 출력 파트
            a=1
            for j in range(int(star/2)): # 왼쪽 숫자 출력 
                print(str(a)+" ",end="")
                a=a+1
            for j in range(space): # 가운데 빈칸 출력
                print("  ",end="")
            a=a-1
            for j in range(int(star/2)): # 오른쪽 숫자 출력
                print(str(a)+" ",end="")
                a=a-1
            star=star-2
            space=n-star
            print()
    else: # 짝수인 경우 
        n=n*2
        star=2
        space=n-star
        for i in range(int(n/2)): # 윗부분 출력
            a=1
            for j in range(int(star/2)): # 왼쪽 숫자
                print(str(a)+" ",end="")
                a=a+1
            for j in range(space): # 공백
                print("  ",end="")
            a=a-1
            for j in range(int(star/2)): # 오른쪽 숫자
                print(str(a)+" ",end="")
                a=a-1
            star=star+2
            space=n-star
            print()

            
        a=1  
        for i in range(n):  # 가운데 출력
            print(str(a)+" ",end="")
            if (i==n/2-1):
                a=a
            elif (i<n/2-1):
                a=a+1
            else:
                a=a-1
        print()
        
        star=n-1
        space=n-star
        for i in range(int(n/2)): # 아래 파트 출력
            a=1
            for j in range(int(star/2)):# 왼쪽 숫자
                print(str(a)+" ",end="")
                a=a+1
                
            space=space+1
            for j in range(space): # 가운데 숫자 
                print("  ",end="")
            a=a-1
            for j in range(int(star/2)): # 오른쪽 숫자
                print(str(a)+" ",end="")
                a=a-1
            star=star-2
            space=n-star
            print()

while(1):
    print("[모양 출력 프로그램]")
    print("[모양 번호: 1.알파벳 모래시계, 2. 숫자 리본]")
    
    a = int(input("출력할 모양을 선택하세요: "))
    if (a!=1 and a!=2):
        print("잘못 입력했습니다.")
        continue
    
    b = int(input("크기를  입력하세요: "))

    if (a==1):
        alphabet(b)
    elif(a==2):
        number(b)
    break
