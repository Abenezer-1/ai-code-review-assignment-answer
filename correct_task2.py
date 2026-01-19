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

email_list = [
    "test@example.com",
    "hello@world.org",
    "invalid-email",
    "another@test.co",
    12345,  # not a string, will be ignored
]

valid_count = count_valid_emails(email_list)
print(f"Number of valid emails: {valid_count}")

