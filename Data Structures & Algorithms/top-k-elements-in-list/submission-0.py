class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            answer = {}
            #return k most freq elements
            #for num in enumerate(nums): #provides index (0,1)
            for num in (nums): #takes value (1)
                #add to a count and sort
                if num in answer:
                    answer[num] += 1;
                else:
                    answer[num] = 1;
            #sortnums based on k
            answerformat = sorted(answer.items(), key=lambda x: x[1], reverse=True)
            return [x[0] for x in answerformat[:k]]
            #lst[start : stop : step]

            #sorted returns a list
                # the first k elemnet sof the list .sort()
                # answer.items() (number, counts)
                # lambda x: x[1] returns counts
                    # lambda x: x[0] returns nums
                #reverse=True is a named argument of the sorted()
                
        