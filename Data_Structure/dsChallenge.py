text = input("Enter your text:")
count = {c: text.count(c)for c in text}

"""unique = []
for t in count:
    if t not in unique:
        unique.append(t)

count = unique
# print(unique)
count.sort(key=lambda item: item[1], reverse=True)"""
count_sorted = sorted(count.items(), key=lambda item: item[1], reverse=True)
print("the most used character in your text is:", count_sorted[0])
