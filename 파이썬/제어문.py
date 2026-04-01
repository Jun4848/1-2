#money = True
#if money:
#    print("택시 타고 가세요.") # 조건이 참 일 경우
#else:
#    print("걸어서 가세요.") # 조건이 거짓 일 경우


#if True:
#    print("택시를")
#print(" 타고 ") 들여쓰기 필수
#    print("가라")

#pocket = ["money", "card"]


pocket = ["paper", "cellphone"]
card = True
if "money" in pocket:
    print("택시 타셈")
elif card:
    print("택시 타셈.")
else:
    print("걸어가셈")

score = 60
message = "성공" if score >= 60 else "실패"

print(message)