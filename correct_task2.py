# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
import re

def count_valid_emails(emails):
    # Simple regex for email validation (not perfect, but practical)
    email_pattern = re.compile(r"^[^@]+@[^@]+\.[^@]+$")
    count = 0
    
    for email in emails:
        if isinstance(email, str) and email_pattern.match(email):
            count += 1
    
    return count


