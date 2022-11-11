class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        # lis = []

        # -------------- check the not duplicated numbers -------------------------
        # for j in arr1:
        #     if j not in arr2:

        #         lis.sort()
        #         lis.append(j)


        #print(lis) => [7,19] 


        # -------------- check the duplicated numbers ------------------------------------- 
        # for k in arr1:
        #     if k in arr2:
        #         arr1.sort()
        #         lis.append(k)
        # print(lis) => [7, 19, 2, 2, 2, 2, 3, 3, 4, 6, 9]

        # Output array
        output = []

        # Counting Frequency of each
        # number in arr1
        f = Counter(arr1)

        # Iterate over arr2 and append all
        # occurrences of element of
        # arr2 from arr1
        for e in arr2:

            
            # Appending element 'e',
            # f[e] number of times
            output.extend([e]*f[e])

            # Count of 'e' after appending is zero
            f[e] = 0

        # Remaining numbers in arr1 in sorted
        # order (Numbers with non-zero frequency)
        rem = list(sorted(filter(
            lambda x: f[x] != 0, f.keys())))

        # Append them also
        for e in rem:
            output.extend([e]*f[e])

        return output

        print(*solve(arr1, arr2))
