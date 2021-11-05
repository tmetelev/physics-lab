from lab import *

# Setup
f = Formula("g")

# Set first row
f.add("P", 3.14, 0.005)
f.add("l", 0.15, 0.2)
f.add("T", 0.75, 0.005)

# Set formula
f.formula = "(4 * P ** 2 * l) / (T ** 2)"
f.count_all()
f.add_to_exel()

f.rewrite_values([3.14, 0.2, 0.81])
f.count_all()
f.add_to_exel()

f.rewrite_values([3.14, 0.25, 0.92])
f.count_all()
f.add_to_exel()

f.write_excel("walues")
print(f.result_value, f.threshold_value)
f.print_all_tex()

# Count all values