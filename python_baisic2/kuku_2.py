# 行数と列数の入力
rows = int(input("行数を入力してください: "))
cols = int(input("列数を入力してください: "))

# 掛け算表の出力
for kuku in range(1, cols + 1):
    for i in range(1, rows + 1):
        result = i * kuku

        if result < 10:
            print(f"{i} x {kuku} =  {result} |", end=' ')

        elif result < 100:
            print(f"{i} x {kuku} = {result} |", end=' ')

        else:
            print(f"{i} x {kuku} = {result} |", end=' ')

    print()


