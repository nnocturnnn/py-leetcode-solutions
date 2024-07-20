# Read from the file file.txt and output all valid phone numbers to stdout.
while IFS= read -r line; do
  # Process the line here (e.g., print it)
  echo "$line"
done < "file.txt"