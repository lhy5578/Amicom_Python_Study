import sys 

N = int(input())
coupons = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

def get_coupons(N):
    count = 0
    for coupon in coupons:
        count += N // coupon
        N = N % coupon
    return count

print(get_coupons(N))