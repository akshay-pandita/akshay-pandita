"""
Algorithm:

1. Traverse the string and push each new character into a dictionary
2. Two possibilities exist now:
  2a. We hit a character which is already in our dictionary
      2a1. Figure out the difference between the current index and the start_index(this is 0 at the start).
           If this is greater than max_non_repeating_length(this is also 0 at start), then assign (current_index-start_index)
           to it.
      2a2. One case that we want to handle(in the 2a1 condition block) here is where the dictionary has a repeating character but it occurred before
            the start_index in the string. In this case (i-start_index) would be one less than the max.
            So we increment 1 to the (i-start_index). For ref on this case check out test case: tmmzuxt.
      2a3. Now we need to look at modifying the start_index. The imp point is that the start_index needs to be only
           modified when the current character was at an index which was >= start_index in the string.
           We do not worry about the charaters which are repeating but are anyways before the start_index.
      2a4. Finally we update the dictionary with the new index of the repeating charater for correct calculations when
           the next occurence of this character comes.
  2b. We never hit a repeating character
    2b1. Whenever we reach the end of the string i.e the current_index = length(string) - 1.
         We need to calculate the max_non_repeating_length as (current_index-start_index).
         Because of the way indexes work, we need to add 1 to the number we get to get the accurate length.
3. Keep repeating step 2 for each new character that we come across.


Important test cases, corner cases for this problem:
aabaab!bb
tmmzuxt
bbbb
pwwkew
wobgrovw

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_dict = {}
        max_non_repeating = 0
        start_index = 0
        for i in range(len(s)):
            if s[i] not in temp_dict:
                temp_dict[s[i]] = i
                if i == len(s) - 1:
                    if (i - start_index) >= max_non_repeating:
                        max_non_repeating = i - start_index + 1
            else:
                if (i - start_index) >= max_non_repeating:
                    max_non_repeating = i - start_index
                    if temp_dict[s[i]] < start_index:
                        max_non_repeating = max_non_repeating + 1
                if temp_dict[s[i]] >= start_index:
                    start_index = temp_dict[s[i]] + 1
                temp_dict[s[i]] = i

        return max_non_repeating
