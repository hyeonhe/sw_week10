def 짝수_확인(숫자):
    return 숫자 % 2 == 0

# 사용 예시
입력_숫자 = int(input("숫자를 입력하세요: "))

def add_numbers(num1, num2):
    return num1 + num2

# 예제 사용
result = add_numbers(3, 5)
print(result)
if 짝수_확인(입력_숫자):
    print(f"{입력_숫자}는 짝수입니다.")
else:
    print(f"{입력_숫자}는 홀수입니다.")


def 두_수의_합(숫자1, 숫자2):
    합 = 숫자1 + 숫자2
    return 합

# 사용 예시
입력_숫자1 = float(input("첫 번째 숫자를 입력하세요: "))
입력_숫자2 = float(input("두 번째 숫자를 입력하세요:"))

결과 = 두_수의_합(입력_숫자1, 입력_숫자2)
print(f"두 수의 합: {결과}")

def concatenate_strings(str1, str2):
    return str1 + str2

# 예제 사용
string1 = "Hello, "
string2 = "world!"
concatenated_string = concatenate_strings(string1, string2)
print(concatenated_string)
