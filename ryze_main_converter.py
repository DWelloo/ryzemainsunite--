import time

# Get English Text from the User
englishText = input()

# Convert the English Text to the Ryze Language
ryzeText = englishText.replace("e", "e(q)").replace("E", "E(Q)").replace("q", "(e)q").replace("Q", "(E)Q")

# Print the Ryze Language Text to the User
print(ryzeText)

time.sleep(100)