# Python3 implementation for the above approach
import numpy as np

# Define the dp table globally
dp = np.zeros((505,505))
choose = np.zeros((502,502))

# Recursive function to calculate the dp
# values for range [L, R]
def calc(l, r, s) :

	# The range is odd length
	if (abs(r - l) % 2 == 0) :
		return 0

	if (l > r) :
		dp[l][r] = 1
		return dp[l][r]

	# The state is already calculated
	if (dp[l][r] != -1) :
		return dp[l][r]

	# If the length is 2
	if ((r - l) == 1) :
		if (s[l] == s[r]) :
			dp[l][r] = 1
		
		else :
			dp[l][r] = 0
		
		return dp[l][r]
	
	# Total answer for this state
	ans = 0
	
	for k in range(l + 1, r + 1, 2) :

		# Variable to store the current answer.
		temp = 1

		# Remove characters s[l] and s[i].
		if (s[l] == s[k]) :
			temp = calc(l + 1, k - 1, s) * calc(k + 1, r, s) * choose[(r - l + 1) // 2][(r - k) // 2]
			ans += temp
		
	
	dp[l][r] = ans
	return dp[l][r]

def waysToClearString(S) :


	# Initialize all the states of dp to -1
	#memset(dp, -1, sizeof(dp));
	
	for i in range(505):
		for j in range(505) :
			dp[i][j] = -1

	# Calculate all Combinations
	n = len(S)
	choose[0][0] = 1
	for i in range(1, (n // 2) + 1) :
		choose[i][0] = 1
		for j in range(1, i + 1) :
			choose[i][j]= choose[i - 1][j] + choose[i - 1][j - 1];
	
	return calc(0, n - 1, S)

# Driver Code
if __name__ == "__main__" :

	S = "aabccb"

	print(waysToClearString(S))

	# This code is contributed by AnkThon
