import random

# ユーザーから入力を受け取る
N = int(input("サイコロの面数を入力してください（例: 6）: "))
M = int(input("振る回数を入力してください（例: 10）: "))

# M回サイコロを振る
results = [random.randint(1, N) for _ in range(M)]

# 結果を表示（カンマ区切りで[]内に）
print(results)
