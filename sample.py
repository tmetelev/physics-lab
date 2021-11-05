from lab import *

# Setup
f = Formula("\Alpha")

# Set first row
f.add("w", 2, 0.005)
f.add("v", 3.14, 0.2)
f.add("t", 4, 0.005)
f.add("Xm", 5, 0.1)

# Set formula
f.formula = "Xm * sin(w * t + v)"
f.close_units = True
f.count_all()
f.add_to_exel()

print(f.result_value, f.threshold_value)

f.generate_tex()
f.change_symbol("w", "\omega")
f.change_symbol("v", "\phi")
f.print_all_tex()