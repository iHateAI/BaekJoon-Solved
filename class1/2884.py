# # include <stdio.h>
#
# int
# main(void)
# {
#
#     int
# H, M;
# scanf("%d %d", & H, & M);
# int
# result_M = 0;
# int
# result_H = 0;
# if (M < 45)
# {
#     result_M = M + 15;
# result_H = H - 1;
# if (result_H < 0)
# {
#     result_H = 23;
# }
# }
# else {
#     result_H = H;
# result_M = M - 45;
# }
#
# printf("%d %d", result_H, result_M);
#
# return 0;
#
# }