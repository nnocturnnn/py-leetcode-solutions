# Read from the file file.txt and output all valid phone numbers to stdout.
pattern="(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})"
grep -oE "$pattern" file.txt