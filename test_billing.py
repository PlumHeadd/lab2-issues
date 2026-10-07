from billing import discount, total

assert round(total(100), 2) == 119.0
assert discount(100, 10) == 90, f"discount(100, 10) gave {discount(100, 10)}"
print("ok")
