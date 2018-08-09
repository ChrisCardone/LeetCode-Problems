# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Example 1:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
#
# Example 2:
# Input: J = "z", S = "ZZ"
# Output: 0

#My initial solution

def numJewelsInStones1(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_count = 0
        for jewel_type in list(J):
            for rock in list(S):
                if jewel_type == rock:
                    jewel_count += 1
        return jewel_count

#Best solution
def numJewelsInStones2(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([i in J for i in S])

#Results
test_input_1 = "aA"
test_input_2 = "aAAbbbb"

print("My solution: " + str(numJewelsInStones1(test_input_1, test_input_2)))
print("Best solution: " + str(numJewelsInStones2(test_input_1, test_input_2)))
