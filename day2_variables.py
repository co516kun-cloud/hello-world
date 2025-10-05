a = 10
b = 3.14
name = "Taro"
is_adult = True
print(a + b)
print("Hello" + name)
print(is_adult)
print(type(a),type(b),type(name),type(is_adult))

#簡易練習
try:
    age = int(input("あなたの年齢は？"))
    if age >= 20:
        print("成人です")
    else:
        print("未成年です")

except ValueError:
    print("数字を入力してください")
