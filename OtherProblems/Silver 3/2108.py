# # 통계학
# # 구현
#
#
# n = int(input())
# data = []
# for _ in range(n):
#     data.append(int(input()))
#
# dict = {}
#
# # 산술평균
# print(round(sum(data) / len(data)))
#
# # 중앙값
# print(sorted(data)[len(data) // 2])
#
# # 최빈값
# for num in data:
#     if num in dict.keys():
#         dict[num] += 1
#     else:
#         dict[num] = 1
#
#
#
# print(dict)
#
# # 범위
# print(max(data) - min(data))