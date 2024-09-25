from collections import defaultdict

def counts_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        result = file.read()
    sum_words = defaultdict(int)
    for line in result.split():
        word = line.lower()  # Convert the word to lowercase
        sum_words[word] += 1
    total_words = sum(sum_words.values())  # Calculate total number of words
    return sum_words, total_words # Return both the dictionary and total word count

file_path = r'C:\python_tmp\pan_tadeusz.txt'
print(file_path)
words_stats, total_words = counts_words(file_path)

# Sort the words by count in descending order and get the top 20
top_20_words = sorted(words_stats.items(), key=lambda item: item[1], reverse=True)[:20]

# Print the total number of words
print(f"Total number of words: {total_words}")

print("\nTop 20 Words:")

# Print the top 20 most occurring words
for word, count in top_20_words:
    print(f"{word}: {count}")
