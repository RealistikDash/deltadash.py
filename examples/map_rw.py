# deltadash.py map reading example
from deltadash.maps.difficulty import Difficulty

# Read a .dd file
diff = Difficulty.from_file("test_res/debug.dd")

# Print the difficulty's full name
print(diff.full_name)

# Change the difficulty name
diff.name = "New Name"

# Write the difficulty to a new file
diff.into_file("test_res/debug_new.dd")
