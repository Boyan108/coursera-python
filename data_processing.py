# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        colon = line.find(':')
        count += 1
        total += float(line[colon+1:].strip())
    else:
        continue

average = total / count
print(f"Average spam confidence: {average}")
