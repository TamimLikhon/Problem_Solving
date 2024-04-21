score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2



sorted_Score = sorted(score, key=lambda x: x[k], reverse= True)

print(sorted_Score)