def solution(price, money, count):
    #등비수열의 합
    total_price = (price + price*count) * count / 2
    return money < total_price and total_price - money or 0