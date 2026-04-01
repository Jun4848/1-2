#treehit = 0
#while treehit < 10:
#    treehit += 1
##    print("나무를 %d번 찍었습니다." % treehit)
#    if treehit == 10:
#        print("나무가 쓰러집니다.")
#----------------------------------------------
#    1. add
#    2. del
#    3. list
#    4. quit
#
#
#    Enter number = """
#hum1 = 0 
#while hum1 != 4:
#    print(prompt)
#    hum1 = int(input())
#----------------------------------------------
#co = 10
#mo = 300
#while mo:
#    if co != 0:
#        print("커피를 한잔 드리겠습니다.")
#        co -= 1
#        print("남은 커피는 %s잔 입니다." % co)
#    else:
#        print("남은 커피가 없습니다")
#        break
#----------------------------------------------
#a = 0
#while a < 10:
#    a += 1
#    if a % 2 == 0 :
#        continue # while 문 맨 위로 감
#    else:
#        print(a)
#----------------------------------------------
#lists = [100, 59, 95, 55, 71]
#num = 0
#for i in lists:
#    num += 1
#    if i >=60 :
#        print("%d번째 학생 ㅊㅋㅊㅋㅊㅋ" % num)
#    else:
#        continue
#----------------------------------------------
#a = 0
#for i in range(1,11):
#    a += i
#print(a)
#----------------------------------------------
for i in range(2,10):
    print()
    for j in range(1,10):
        c = i * j
        print("%d X %d = %d"%(i,j,c))