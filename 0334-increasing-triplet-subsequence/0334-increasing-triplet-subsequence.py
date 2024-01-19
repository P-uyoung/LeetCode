class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        fst, sec = [nums[0]],[]
        for n in nums[1:]:
            if len(fst) == 1:
                if not sec:
                    if n > fst[0]: 
                        sec.append(n)
                    elif n < fst[0]:
                        fst[0] = n
                elif sec[0] < n:
                    return True
                elif fst[0] < n and sec[0] > n:
                    sec[0] = n
                elif fst[0] > n:
                    fst.append(n)
            else:
                if sec[0] < n:
                    return True
                elif fst[1] < n:
                    fst = [fst[1]]
                    sec = [n]
        return False
                    