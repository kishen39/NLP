def min_edit_distance(source, target, sub_cost, ins_cost, del_cost):
    n = len(source)
    m = len(target)
    # Initialize DP table with dimensions (n+1) x (m+1)
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # Base cases: converting to/from empty string
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] + del_cost  # Deleting all characters from source
    for j in range(1, m+1):
        dp[0][j] = dp[0][j-1] + ins_cost  # Inserting all characters to form target
        
    # Fill the DP table
    for i in range(1, n+1):
        for j in range(1, m+1):
            if source[i-1] == target[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No cost if characters match
            else:
                # Consider substitution, insertion, deletion
                substitute = dp[i-1][j-1] + sub_cost
                insert = dp[i][j-1] + ins_cost
                delete = dp[i-1][j] + del_cost
                dp[i][j] = min(substitute, insert, delete)
                
    return dp[n][m]

# Word pair
source = "Sunday"
target = "Saturday"

# Model A: sub=1, ins=1, del=1
distA = min_edit_distance(source, target, 1, 1, 1)
print(f"Model A distance: {distA}")

# Model B: sub=2, ins=1, del=1
distB = min_edit_distance(source, target, 2, 1, 1)
print(f"Model B distance: {distB}")