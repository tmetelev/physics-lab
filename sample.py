from lab import *

# Setup
f = Formula("F")

# Set first row
f.add("x", 2, 0.1)
f.add("y", 2, 0.2)

# Set formula
f.formula = "x ** y"
f.count_all()                   # Count all values
f.add_to_exel()                 # Add to table

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