from data import boxes as data, sumToReach

SUM_TO_REACH = sumToReach

def rotate(row):
    element = row.pop(0)
    row.append(element)
    return row

def displaySolution(solution):
    print(solution)

def checkSolution(solution):
    # print('checkSolution')
    sums = [0, 0, 0, 0]
    for row in solution:
        for i in range(4):
            # print(i)
            sums[i] += row[i]
    return (sums[0] == SUM_TO_REACH and
        sums[1] == SUM_TO_REACH and
        sums[2] == SUM_TO_REACH and
        sums[3] == SUM_TO_REACH)

def recuringSolve(data, currentSol):
    # print('==============')
    # print(data)
    # print(currentSol)
    if len(data) == 0:
        if checkSolution(currentSol):
            displaySolution(currentSol)
        return

    row = data.pop(0)
    for i in range(4):
        # print(i)
        currentSol.append(row)
        recuringSolve(data, currentSol)
        currentSol.pop()
        row = rotate(row)
    data.insert(0, row)

def solve(data):
    currentSol = [data.pop(0)]
    recuringSolve(data, currentSol)

if __name__ == "__main__":
    solve(data)
