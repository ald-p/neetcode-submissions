class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        currentMax = -1
        n = len(arr)
        res = [0] * n

        for i in range(n - 1, -1, -1):
            res[i] = currentMax

            if arr[i] > currentMax:
                currentMax = arr[i]

        return res


        