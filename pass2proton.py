#!/usr/bin/env python3

import sys
from pathlib import Path, PosixPath

if len(sys.argv) < 2:
    print("Usage: pass2proton.py <path/to/password-store>")
    sys.exit(1)

password_store = Path(sys.argv[1])
if not password_store.exists():
    print(f"Could not find the password store at {password_store}")
    sys.exit(1)


def find_files(dir: PosixPath):
    files = []

    for item in dir.glob("*"):
        if item.name.startswith("."):
            print(f"Skipping hidden item: {item}", file=sys.stderr)
            continue

        if item.is_dir():
            files.extend(find_files(item))
            continue

        files.append(item)

    return files

# TODO
def get_password_data(file: PosixPath) -> dict:
    import subprocess

    # Convert file path to the pass key name
    key = str(file.relative_to(password_store)).replace(".gpg", "")

    # First line is password and additional lines are notes
    output = subprocess.run(["pass", key], stdout=subprocess.PIPE)
    output = output.stdout.decode("utf-8").splitlines()

    # TODO: Parse out URLs and usernames
    return {
        "key": key,
        "url": "",
        "username": "",
        "password": output[0],
        "notes": "\n".join(output[1:])
    }

def main():
    import csv
    writer = csv.writer(sys.stdout, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)

    # Header row
    writer.writerow(["Title", "URL", "Username", "Password", "Notes", "OTPAuth"])

    files = find_files(password_store)
    for file in files[0:10]:  # TODO: Remove temp limit
        data = get_password_data(file)
        print(data)
        writer.writerow([data["key"], data.get("url", ""), data.get("username", ""), data["password"], data.get("notes", ""), ""])


if __name__ == "__main__":
    main()
