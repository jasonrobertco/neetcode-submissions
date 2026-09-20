class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix) #get rows height
        cols = len(matrix[0]) #get cols width
        top = 0
        bot = rows-1
        left = 0
        right = cols-1
        total = rows * cols
        answer =[]

        while len(answer) < total:
        #move right
            for y in range (left, right + 1): #start, stop doesnt include itself so need +1 , step none here
                answer.append(matrix[top][y])
            top += 1 #moves downward
        #move down
            for x in range (top, bot + 1): #top should be 1 here, stop at bottom needs +1 ie 0, 1, 2, stop at 3
                answer.append(matrix[x][right])
            right -= 1 #moves left
            #in exmaple of 4 cols 4-1 = 3 and then ehre we -1 so 2 and go from[2] to [0]
        #move left
            if top <= bot:
                for y in range (right, left - 1, -1): #start, stop doesnt include itself so need -1 , step -1
                    answer.append(matrix[bot][y])
                bot -= 1 #moves up
        #move up
            if left <= right:
                for x in range (bot, top-1, -1): #in example 3 rows top is 0 then top is 1
                #bottom is rows-1 3-1 =2 and then we are on the 2nd row and go tot hte 1st row to [2] to [1]
                    answer.append(matrix[x][left])
                left += 1 #moves right
        return answer