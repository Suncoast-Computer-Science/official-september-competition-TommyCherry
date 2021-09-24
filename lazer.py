players = int(input())
indivScores = []
teamScores = []
e = players
f = players
while e > 0:
  a = int(input())
  indivScores.append(a)
  e -= 1

while f > 0:
  teamScores.append(indivScores[1] + indivScores[0])
  del indivScores[0:2]
  f -= 2
  

teamScores.sort()
print(teamScores)
