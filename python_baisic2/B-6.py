import random

# ユーザーから入力を受け取る
N = int(input("サイコロの面数を入力してください（例: 6）: "))
M = int(input("振る回数を入力してください（例: 10）: "))

# M回サイコロを振る
print(f"\n{N}面サイコロを{M}回振った結果:")
for i in range(M):
    roll = random.randint(1, N)
    print(f"{i + 1}回目: {roll}")
