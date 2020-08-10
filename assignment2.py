def best_score(arr1,arr2):
    memo = [0]*(len(arr1)+1)
    for i in range(len(arr1)+1):
        memo[i] = [0]*(len(arr2)+1)
    for i in range(len(arr1)+1):
        for j in range(len(arr2)+1):
            if i == 0:
                if j == 0:
                    memo[i][j] = (0,0)
                elif j == 1:
                    memo[i][j] = (arr2[j-1],0)
                elif j >= 2:
                    m = memo[i][j-2][0] + arr2[j-1]
                    n = (memo[i][j-1][1]+memo[i][j-1][0])+arr2[j-1]-m
                    memo[i][j] = (m,n)
            elif i > 0 and j == 0:
                if i == 1 and j == 0:
                    memo[i][j] = (arr1[i-1],0)
                if j == 0 and i>1:
                    m = memo[i-2][j][0] + arr1[i-1]
                    n = memo[i-1][j][1]+memo[i-1][j][0]+arr1[i-1]-m
                    memo[i][j] = (m,n)
            else: # when j > 0 and i > 0:
                sum_coins = (memo[0][j][0]+memo[0][j][1])+(memo[i][0][0]+memo[i][0][1])
                m = sum_coins-min(memo[i-1][j][0],memo[i][j-1][0])
                n = sum_coins-m
                memo[i][j] = (m,n)
    sequence = []
    m = len(arr1)
    n = len(arr2)
    while m >= 0 and n >= 0:
        target = (m, n)
        check = min(memo[target[0]-1][n][0],memo[m][target[1]-1][0])
        if m ==0 and n==0:
            break
        elif check == memo[m][target[1]-1][0]:
            sequence.append(2)
            n -= 1
        else:
            m -= 1
            sequence.append(1)
    return (memo[len(arr1)][len(arr2)][0],sequence)

def is_in(grid,word):
    memo = []
    for i in range(len(word)):
        memo.append([])

    success = False
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == word[0]:
                test = available_choice(grid,memo,(i,j),0,word)
                if test is not False:
                    success = True
                    break

    if success:
        return test
    else:
        return success

def available_choice(grid, memo, target, index, word): # target is (i,j)
    count = 0
    while True:
        # make sure the search is valid and the target is in bound
        if index+1 < len(word) and target[0] >= 0 and target[0] <= len(grid)and target[1] >= 0 and target[1] <= len(grid):
            if target[0]-1 >= 0:
                # i am finding if there is NEXT possible move
                if grid[target[0] - 1][target[1]] == word[index+1]: # i-1,j
                    count += 1
                    test = available_choice(grid,memo,(target[0] - 1,target[1]),index+1,word)
                    if test is True:
                        memo[index].append((target[0],target[1]))
                    break

                if target[1]-1 >= 0:  # within border
                    if grid[target[0] - 1][target[1] - 1] == word[index+1]:  # i-1,j-1
                        count += 1
                        test = available_choice(grid, memo, (target[0] - 1,target[1] - 1), index + 1, word)
                        if test is True:
                            memo[index].append((target[0], target[1]))
                        break
                if target[1]+1 < len(grid):  # within border
                    if grid[target[0] - 1][target[1] + 1] == word[index+1]:  # i-1, j+1
                        count += 1
                        test = available_choice(grid, memo, (target[0] - 1,target[1] + 1), index + 1, word)
                        if test is True:
                            memo[index].append((target[0], target[1]))
                        break

            if target[1]-1 >= 0:  # within border
                if grid[target[0]][target[1] - 1] == word[index+1]:  # i, j-1
                    count += 1
                    test = available_choice(grid, memo, (target[0],target[1] - 1), index + 1, word)
                    if test is True:
                        memo[index].append((target[0], target[1]))
                    break
            if target[1]+1 < len(grid):  # within border
                if grid[target[0]][target[1] + 1] == word[index+1]:  # i,j+1
                    count += 1
                    test = available_choice(grid, memo, (target[0],target[1] + 1), index + 1, word)
                    if test is True:
                        memo[index].append((target[0], target[1]))
                    break
            if target[0]+1 < len(grid):
                if grid[target[0] + 1][target[1]] == word[index+1]:  # i+1,j
                    count += 1
                    test = available_choice(grid, memo, (target[0] + 1,target[1]), index + 1, word)
                    if test is True:
                        memo[index].append((target[0], target[1]))
                    break
                if target[1]-1 >= 0:
                    if grid[target[0] + 1][target[1] - 1] == word[index+1]:  # i+1,j-1
                        count += 1
                        test = available_choice(grid, memo, (target[0] + 1,target[1] - 1), index + 1, word)
                        if test is True:
                            memo[index].append((target[0], target[1]))
                        break
                if target[1]+1 < len(grid):
                    if grid[target[0] + 1][target[1] + 1] == word[index+1]:  # i+1,j+1
                        count += 1
                        test = available_choice(grid, memo, (target[0] + 1,target[1] + 1), index + 1, word)
                        if test is True:
                            memo[index].append((target[0], target[1]))
                        break
                # no match is found
                if count == 0:
                    return False
                    # break
        # already find the last letter to the word, no need to recurse anymore
        elif index+1 == len(word):
            memo[index].append(target)
            break
    # when search still needs to continue
    if index+1 < len(word):
        # found match
        if count > 0:
            # if its not the first recursion
            if index >= 1:
                return True
            else:  # when its back to the first function call (completed the search)
                return memo
        else:
            return False
    # found the whole word
    else:
        return True

if __name__ == "__main__":
    #check best_score
    arr1 = [5, 8, 2, 4, 1, 10, 2]
    arr2 = [6, 2, 4, 5, 6, 9, 8]
    best_score(arr1, arr2)

    arr3 = [20, 5]
    arr4 = [1]
    best_score(arr3, arr4)

    arr5 = [1, 2, 3]
    arr6 = [1]
    best_score(arr5, arr6)
    # print(best_score([],[])) # check for boundary cases

    #check is_in
    grid = [['a', 'b', 'c', 'd'],
            ['e', 'a', 'p', 'f'],
            ['e', 'p', 'g', 'h'],
            ['l', 'i', 'j', 'k']]
    word1 = "apple"
    word2 = "xylophone"
    is_in(grid, word1)