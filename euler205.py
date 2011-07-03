dices_Peter = [a+b+c+d+e+f+g+h+i for a in range(1,5) for b in range(1,5) for c in range(1,5) for d in range(1,5) for e in range(1,5) for f in range(1,5) for g in range(1,5) for h in range(1,5) for i in range(1,5)]
dices_Colin = [a+b+c+d+e+f for a in range(1,7) for b in range(1,7) for c in range(1,7) for d in range(1,7) for e in range(1,7) for f in range(1,7)]

scores_Peter = set(dices_Peter)
scores_Colin = set(dices_Colin)
all_cases = len(dices_Peter) * len(dices_Colin)

probability = 0.0
for scoreP in scores_Peter:
    for scoreC in scores_Colin:
        if not scoreP > scoreC:
            break
        probability +=  dices_Peter.count(scoreP) * dices_Colin.count(scoreC) / all_cases

print(probability.__round__(7))
