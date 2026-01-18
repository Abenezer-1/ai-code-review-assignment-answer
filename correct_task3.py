# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    total = 0.0
    count = 0

    for v in values:
        if v is not None:
            try:
                total += float(v)
                count += 1
            except (ValueError, TypeError):
                # Skip invalid entries that cannot be converted to float
                continue

    if count == 0:
        return None  # or raise ValueError("No valid measurements")
    
    return total / count
