def solution(s):
    ans=''
    if len(s)%2==0:
        a= len(s)//2
        ans= s[a-1:a+1]
        print(ans)
    elif len(s)%2==1:
        a= len(s)//2
        ans= s[a]
        print(ans)
    return ans