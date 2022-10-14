class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    # def books(self, A, B):

#in this question we are getting the ranges that is it a valid range to get all the elements in that range or not?
#if this is valid store that into result and think of that 
#can we get some more low limits?
#Prefer AADITYA VERMA VIDEO
    def isValid(self, barrier, B, arr):

        no_of_stud = 1

        pages = 0


        # if B greater than len(arr) simply return False

        # Edge case

        if B > len(arr):

            return False


        for i in range(len(arr)):

            # if pages greater than barrier we cannot allocate

            if arr[i] > barrier:

                return False


            if pages + arr[i] > barrier:

                no_of_stud += 1

                pages = arr[i]

            else:

                pages += arr[i]


        # print(no_of_stud)

        if (no_of_stud > B):

            return False

        else:

            return True


    def books(self, A, B):

        # Eg: A = [12,13,14,15]. B = 4.. then min value is 12 which is min(A)

        l = min(A)

        # Eg: A = [12,13,14,15]. B = 1.. then min value is Sum(A) where all books gets allocated to the student 1

        h = sum(A)

        # we have defined our search space

        # now for each value in the search space see if we can allocate books to required no of students and find the minimum value


        res = -1

        while l<=h:

            mid = l + (h-l)//2

            # print(l,h,mid)

            if(self.isValid(mid,B,A)):

                res = mid

                h = mid - 1

            else:

                l = mid + 1


        return res
