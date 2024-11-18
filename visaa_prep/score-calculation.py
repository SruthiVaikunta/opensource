n=int(input())
scores=[]
for _ in range(1,n+1):
    total_points,passed_tc=map(int,input().split())
    points_per_tc=total_points//10
    scores.append(passed_tc*points_per_tc)
    
for score in scores:
    print(score)
