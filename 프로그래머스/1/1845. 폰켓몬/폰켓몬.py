def solution(nums):
    max_value = int(len(nums)/2)
    ans = len(set(nums))
    if ans>max_value:
        answer = max_value
    else :
        answer = ans
    
    return answer