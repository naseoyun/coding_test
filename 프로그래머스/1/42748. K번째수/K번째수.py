def solution(array, commands):
    lens= len(commands)
    ans= []
    for i in range(0,lens):
        start= commands[i][0]
        end  = commands[i][1]
        order= commands[i][2]
        new_arr= sorted(array[start-1:end])
        ans.append(new_arr[order-1])
    
    answer = ans
    return answer