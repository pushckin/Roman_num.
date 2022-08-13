num = int(input())
rom = {1 : "I", 2 : "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX", 10 : "X"}
if num < 0 or num > 10:
    print("ошибка")
else:
    print(rom[num])