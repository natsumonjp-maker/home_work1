# 行数と列数の入力を受け取る
rows = int(input("行数を入力してください: "))
cols = int(input("列数を入力してください: "))

# 掛け算の表を出力
for i in range(1, rows + 1):
    for kuku in range(1, cols + 1):
        print(i * kuku, end=' ')
    print()
