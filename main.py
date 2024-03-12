# =========================================================================================

# 1] -----------------------------------------------------------------
#
# k = int(input("k kiriting: "))
#
# n = int(input("n kiriting (0 dan kotta bolsin): "))
#
# for i in range(n):
#     print(k)

# 2] -----------------------------------------------------------------
#
# a = int(input("a  kiriting: "))
# b = int(input("b  kiriting: "))
#
# print(f"a va b orasidegi hamma butun sonla:")
# for i in range(a, b + 1):
#     print(i)
#
# count = b - a + 15
# print(f"Chiqqan sonla soni: {count}")

# 3] -----------------------------------------------------------------
#
# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))
#
# print(f"a va b orasidegi hamma butun sonla kamayiw tartibida:")
# for i in range(b - 1, a, -1):
#     print(i)
#
# count = b - a - 1
# print(f"Chiqqan sonla soni: {count}")

# 4] -----------------------------------------------------------------
#
# narx_per_kg = float(input("Bir kilogram wkalad narxini kiriting: "))
#
# narx_1kg = narx_per_kg
# narx_2kg = narx_per_kg * 2
# narx_10kg = narx_per_kg * 10
#
# print("1 kg wkalad narxi:", narx_1kg)
# print("2 kg wkalad narxi:", narx_2kg)
# print("10 kg wkalad narxi:", narx_10kg)

# 5] -----------------------------------------------------------------
#
# o = "hello world"
#
# big_letter = ''.join(letter.upper() for letter in o)
#
# print(big_letter)

# 6] -----------------------------------------------------------------
#
# s = "Hello wORID"
#
# kotta_harflar = ''.join(letter for letter in s if letter.isupper())
# kichik_harflar = ''.join(letter for letter in s if letter.islower())
#
# print("Kotta harflar:", kotta_harflar)
# print("Kichik harflar:", kichik_harflar)

# 7] -----------------------------------------------------------------
#
# darajalar = [x ** 3 for x in range(1, 21)]
#
# print(darajalar)

# 8] -----------------------------------------------------------------
#
# juft_sonlar = [x // 2 for x in range(2, 21, 2)]
#
# print(juft_sonlar)

# 9] -----------------------------------------------------------------
#
# raqamlar_dict = {x: x ** 2 for x in range(1, 11)}
#
# print(raqamlar_dict)

# 10] -----------------------------------------------------------------
#
# word = "salom dunyo"
# word_dict = {letter.lower(): letter.upper() for letter in word if letter.islower()}
#
# print(word_dict)

# =================================================================================================





