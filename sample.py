from lab import *

# Setup
f = Formula("F")

# Set first row
f.add("x", 2, 0.1)
f.add("y", 2, 0.2)

# Set formula
f.formula = "x ** y"
# Count all values
f.count_all()
# Add to table
f.add_to_exel()

# Second row
f.rewrite_values([2, 3])
f.count_all()
f.add_to_exel()

# Third row
f.rewrite_values([3, 3])
f.rewrite_thresholds([2, 2])
f.count_all()
f.add_to_exel()

# Out put LaTex formula
f.print_all_tex()
# Build Excel file
f.write_excel("sample")