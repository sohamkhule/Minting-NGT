from collections import defaultdict

# Sample input data
text_data = [
    "hello world",
    "hello again world",
    "hello world world"
]

# Map step: Split each line into words and emit (word, 1)
def map_function(line):
    words = line.strip().split()
    return [(word, 1) for word in words]

# Shuffle and sort step: Group by word
def shuffle_and_sort(mapped_data):
    grouped_data = defaultdict(list)
    for word, count in mapped_data:
        grouped_data[word].append(count)
    return grouped_data

# Reduce step: Sum counts for each word
def reduce_function(grouped_data):
    reduced_data = {}
    for word, counts in grouped_data.items():
        reduced_data[word] = sum(counts)
    return reduced_data

# Main MapReduce execution
def map_reduce(text_data):
    # Map
    mapped = []
    for line in text_data:
        mapped.extend(map_function(line))

    # Shuffle and Sort
    grouped = shuffle_and_sort(mapped)

    # Reduce
    reduced = reduce_function(grouped)

    return reduced

# Run the program
if __name__ == "__main__":
    word_count = map_reduce(text_data)
    for word, count in word_count.items():
        print(f"{word}: {count}")
