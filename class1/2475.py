# 검증 수 (C로 작성됨)


# include <stdio.h>

# int main(void)
# {
#
#     int num[5];
#     int sum = 0;
#     for (int i = 0; i < 5; i++)
#     {
#         scanf("%d", & num[i]);
#         sum += (num[i] * num[i]);
#     }
#     int result = sum % 10;
#     printf("%d", result);
#
#     return 0;
# }