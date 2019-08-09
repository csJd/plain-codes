#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (34.97%)
# Likes:    2491
# Dislikes: 134
# Total Accepted:    364K
# Total Submissions: 1M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note:
#
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
#
#

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length+1)
        # dp[i] represents to wordBreak(s[:i], wordDict)
        dp[0] = True
        for i in range(length):
            if dp[i]:
                for word in wordDict:
                    if(s[i:i+len(word)] == word):
                        dp[i+len(word)] = True
        return dp[length]


# def main():
#     solu = Solution()
#     print(solu.wordBreak(s="catsandog", wordDict=[
#           "cats", "dog", "sand", "and", "cat"]))
#     print(solu.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))


# if __name__ == "__main__":
#     main()