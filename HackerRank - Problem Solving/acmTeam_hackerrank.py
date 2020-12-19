
def acmTeam(n,m,topic):
    maxKnown = 0
    teamsCnt = 0
    for i in range(n-1): 
        for j in range(i+1, n):
            knownForThisCombo = 0
            for t in range(m):
                if topic[i][t] == '1' or topic[j][t] == '1':
                    knownForThisCombo += 1
            if knownForThisCombo > maxKnown:
                maxKnown = knownForThisCombo;
                teamsCnt = 1;
            elif knownForThisCombo == maxKnown:
                teamsCnt += 1;
     
    return maxKnown, teamsCnt

nm = input().split()

n = int(nm[0])

m = int(nm[1])

topic = []

for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

result = acmTeam(n,m,topic)
print(result)

