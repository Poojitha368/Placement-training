# 🗓️ 7-Day Dynamic Programming Plan
# ✅ Ground Rule:
# Each day, spend 1–2 hours:
# ✏️ 30 mins understanding the concept +
# 🧠 1+ hour solving 2–3 problems.

# 📅 Day 1: Understand Recursion + Memoization
# Goal: Build the foundation of DP using recursion.

# 🧠 Learn:

# Recursion (base case + recursive case)

# Memoization (top-down DP)

# 📚 Problems:

# Fibonacci Numbers

# Climbing Stairs

# House Robber

# 📅 Day 2: Tabulation (Bottom-Up DP)
# Goal: Convert recursive DP to iterative (faster) version.

# 🧠 Learn:

# How to build a DP table

# Iterative thinking

# 📚 Problems:

# Tabulate Fibonacci

# Tabulate Climbing Stairs

# Min Cost Climbing Stairs

# 📅 Day 3: 0/1 Knapsack Pattern
# Goal: Learn how to pick or skip items.

# 🧠 Learn:

# Binary decision DP

# 2D DP array

# 📚 Problems:

# 0/1 Knapsack (GFG)

# Subset Sum

# Target Sum

# 📅 Day 4: Longest Common Subsequence (LCS)
# Goal: Learn sequence-based DP.

# 🧠 Learn:

# Comparing characters

# 2D DP with string indices

# 📚 Problems:

# Longest Common Subsequence

# Longest Palindromic Subsequence

# Edit Distance (Hard)

# 📅 Day 5: Grid DP
# Goal: Move in a matrix with dynamic choices.

# 🧠 Learn:

# DP on rows and columns

# Optimal paths

# 📚 Problems:

# Unique Paths

# Minimum Path Sum

# Dungeon Game (Hard)

# 📅 Day 6: Longest Increasing Subsequence (LIS)
# Goal: Work with sequences and constraints.

# 🧠 Learn:

# Using loops to compare elements

# DP with sequences

# 📚 Problems:

# LIS (Leetcode)

# Patience Sorting Version (Advanced)

# Max Sum Increasing Subsequence (GFG)

# 📅 Day 7: Review & Solve Mixed Problems
# Goal: Apply everything you’ve learned.

# 🧠 Practice:

# Review failed or difficult problems

# Try solving without help

# Focus on time/space optimization

# 📚 Mixed Problems:

# Partition Equal Subset Sum

# Coin Change

# Palindrome Partitioning II

# 🎁 Bonus Resources:
# 📘 NeetCode DP Playlist (YouTube)

# 🔗 Leetcode DP Pattern List


#coin change
coin = [2,3,4,5]
amount = 13
dp = [[0]*(amount+1) for _ in range(len(coin))]
for i in range(len(coin)):
    dp[i][0]=1
    dp[i][coin[i]]=1
for i in range(1,len(coin)):
    for j in range(1,amount+1):
        if j<coin[i]:
            dp[i][j] = dp[i-1][j]
        if dp[i-1][j] == 1:
            dp[i][j]=1
        else:
            if dp[i-1][j-coin[i]]==1:
                dp[i][j] = dp[i-1][j-coin[i]]
                
print(dp[-1][-1] == 1)  # Output: 1 if possible, 0 if not possible
# This code snippet implements a dynamic programming solution to the coin change problem.




# dynamic programming solution to the coin change problem using a 1D array.
#min coins using coin repetition
coin = [2,3,4,5]
amount = 12
dp = [0]*(amount+1)

for i in range(len(coin)):
    for j in range(1,amount+1):
        if j == coin[i]:
            dp[j]=1
        if dp[j-coin[i]] > 0:
            if dp[j] == 0:
                dp[j]=dp[j-coin[i]]+1
            else:
                dp[j] = min(dp[j-coin[i]]+1,dp[j])
print(dp[-1])
            
        
    