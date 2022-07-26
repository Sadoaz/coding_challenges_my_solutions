def solution(args):
    
    result = []
    temp = []
    print(args)
    for x in range(1, len(args)):
        temp.append(args[x-1])
        
        if abs(args[x] - args[x-1]) > 1:
            result.append(temp)
            temp = []
        elif x == len(args) -1: result.append(temp)

    if abs(args[-1] - result[-1][-1]) > 1:result.append([args[-1]])
    else: result[-1].append(args[-1])
    
    return ",".join(["-".join(map(str, [x[0], x[-1]])) if len(x) >= 3 else ",".join(map(str, x))  for x in result])