def solution(price, money, count):
    n = count*(count+1)/2
    total_price = n*price
    answer = total_price-money
    if answer>0:
        return answer
    else:
        return 0