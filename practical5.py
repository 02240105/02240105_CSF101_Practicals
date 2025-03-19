def read_file (filename):
    with open(filename, 'r') as file:
        return file.read()
    
content = read_file('sample.txt')
print(content[:100]) 

def count_lines(content):
    return len(content.split('\n'))
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}") 

def count_words(content):
    return len(content.split())
num_words = count_words(content)
print(f"Number of words: {num_words}")

from collections import Counter
def most_common_words(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]
common_words, count = most_common_words(content)
print(f"Most common words: '{common_words}' (appears {count} times)")

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)
avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

def unique_words(content):
    word = content.lower().split()
    unique_word_count = len(set(word))
    return unique_word_count
num_unique_words = unique_words(content)
print(f"Number of unique words: {num_unique_words}")

def longest_word(content):
    words = content.lower().split()
    return max(words, key=len)
longest = longest_word(content)
print(f"Longest word: '{longest}'")

def count_specific_word(content, word):
    words = content.lower().split()
    return words.count(word)
specific_word = 'python'
specific_word_count = count_specific_word(content, specific_word)
print(f"Number of times '{specific_word}' appears: {specific_word_count}")

def percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words)) * 100
percentage_longer = percentage_longer_than_average(content)
print(f"Percentage of words longer than average length: {percentage_longer:.2f}%")

def analyze_file(filename):
    content = read_file(filename)   
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_words, count = most_common_words(content)
    avg_length = average_word_length(content)
    num_unique_words = unique_words(content)
    longest = longest_word(content)
    specific_word_count = count_specific_word(content, specific_word)
    percentage_longer = percentage_longer_than_average(content)
    

    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common words: '{common_words}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Longest word: '{longest}'")
    print(f"Number of times '{specific_word}' appears: {specific_word_count}")
    print(f"Percentage of words longer than average length: {percentage_longer:.2f}%")

analyze_file('sample.txt')    

