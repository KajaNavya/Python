# Read n (not used in this specific logic for finding runner-up, but part of problem input)
n = int(input()) 

# Read the scores as a list of integers
scores = list(map(int, input().split()))

# Remove duplicates and sort in ascending order
unique_sorted_scores = sorted(list(set(scores)))

# The runner-up score is the second-to-last element
runner_up_score = unique_sorted_scores[-2]

# Print the runner-up score
print(runner_up_score)
