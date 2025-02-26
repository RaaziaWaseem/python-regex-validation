import re

def is_valid_email(email):
    """Validate an email address."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_camel_case(string):
    """Check if a string follows CamelCase."""
    camel_case_regex = r'^[A-Z][a-zA-Z0-9]*$'
    return re.match(camel_case_regex, string) is not None

# Test cases
emails = ["test@example.com", "invalid-email@", "user.name@domain.com", "user@.com"]
camel_cases = ["CamelCase", "camelCase", "snake_case", "PascalCase"]

for email in emails:
    print(f"{email} is valid: {is_valid_email(email)}")

for string in camel_cases:
    print(f"{string} is CamelCase: {is_camel_case(string)}")