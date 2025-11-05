sum_value_one_to_ten = 0
# 간단한 콘솔 기반 계산기 기능 구현
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    """
    Multiply two numeric values.

    Args:
        x (int | float): The first multiplicand.
        y (int | float): The second multiplicand.

    Returns:
        int | float: The product of x and y. The return type will match the input numeric types
        (e.g., int if both inputs are ints, float if either input is a float).

    Raises:
        TypeError: If either x or y is not an int or float.

    Examples:
        >>> multiply(2, 3)
        6
        >>> multiply(2.5, 4)
        10.0
    """
    return x * y

def divide(x, y):
    if y == 0:
        return '0으로 나눌 수 없습니다.'
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        return '0으로 나눌 수 없습니다.'
    return x % y

def sqrt(x):
    if x < 0:
        return '음수의 제곱근은 계산할 수 없습니다.'
    return math.sqrt(x)

def main():
    print("간단한 계산기입니다.")
    print("원하는 연산을 선택하세요:")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")
    print("5. 제곱")
    print("6. 나머지")
    print("7. 제곱근")

    while True:
        choice = input("연산 선택(1/2/3/4/5/6/7, 종료하려면 q): ")
        if choice == 'q':
            print("계산기를 종료합니다.")
            break
        if choice not in ('1', '2', '3', '4', '5', '6', '7'):
            print("잘못된 입력입니다. 다시 선택하세요.")
            continue
        try:
            if choice == '7':
                num1 = float(input("숫자를 입력하세요: "))
            else:
                num1 = float(input("첫 번째 숫자를 입력하세요: "))
                num2 = float(input("두 번째 숫자를 입력하세요: "))
        except ValueError:
            print("숫자를 입력하세요.")
            continue

        if choice == '1':
            print(f"결과: {add(num1, num2)}")
        elif choice == '2':
            print(f"결과: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"결과: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"결과: {divide(num1, num2)}")
        elif choice == '5':
            print(f"결과: {power(num1, num2)}")
        elif choice == '6':
            print(f"결과: {modulo(num1, num2)}")
        elif choice == '7':
            print(f"결과: {sqrt(num1)}")

if __name__ == "__main__":
    main()