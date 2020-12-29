class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) >= 3 and arr[0] < arr[1]:
            climax = False
            for i, item in enumerate(arr[1:], 0):
                if (item > arr[i] and not climax) or (item < arr[i] and climax):
                    continue
                elif item < arr[i] and not climax:
                    climax = True
                elif item == arr[i] or (item > arr[i] and climax):
                    return False
            if climax:
                return True
            else:
                return False
                
        else:
            return False
