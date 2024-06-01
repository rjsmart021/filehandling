import os.path
import re
from typing import Optional, Match


def is_email(text: str) -> Optional[Match[str]]:
    email_re_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_re_pattern, text) is not None


def extract_emails(filename):
    file_content = ""
    unique_emails = set()
    try:
        f = open(filename)
        file_content = f.read()
        words = file_content.split()

        for word in words:
            if is_email(word):
                unique_emails.add(word)

    except FileNotFoundError:
        print(f"File Not found. Verify path: {filename}")
        exit(0)
    return unique_emails


file_path = input("Enter file path: ")
emails = extract_emails(file_path)
print("Emails extracted are: ", emails)
