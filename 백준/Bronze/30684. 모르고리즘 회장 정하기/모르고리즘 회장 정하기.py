N,*L = list(open(0).read().split())
CandidatesList = [ ]
for name in L:
  if len(name) == 3:
    CandidatesList.append(name)
CandidatesList.sort()

print(CandidatesList[0])
