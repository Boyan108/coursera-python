# Write a program to read through the mbox-short.txt and count the distribution of the hour of the day for each of the messages. You can pull the hour out from the 'From ' lines by finding the time and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    hour = words[5].split(":")[0]
    counts[hour] = counts.get(hour, 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)