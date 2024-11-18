n=int(input())
scores=[]

for _ in range(n):
    total_points,passed_cases=map(int,input().split())
    points_per_case=total_points//10
    scores.append(passed_cases*points_per_case)
for score in scores:
    print(score)
