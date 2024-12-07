scores=[]

for i in range(3):
    score=int(input("Num: "))
    scores.append(score)
    scores += [score]

average=sum(scores)/len(scores)

print(f"{average}")