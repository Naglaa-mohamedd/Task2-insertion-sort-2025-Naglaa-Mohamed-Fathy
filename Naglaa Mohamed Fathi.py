#Problem:

#We have a list of words of different lengths, and we want to sort them in ascending order based on their length using the Insertion Sort algorithm instead of sorting numbers.

#Solution:

#We will use the Insertion Sort algorithm to sort the list by comparing the lengths of the words and inserting each word into its correct position.

#Python Code:

def insertion_sort_by_length(words):
    """
    This function sorts a list of words based on their length using the Insertion Sort algorithm.
    """
    for i in range(1, len(words)):  # Start from the second element
        key = words[i]  # Current word to be inserted in the correct position
        j = i - 1
        
        # Shift longer words to the right to make space
        while j >= 0 and len(words[j]) > len(key):  
            words[j + 1] = words[j]
            j -= 1
        
        words[j + 1] = key  # Insert the word in its correct position

# Unsorted list of words
words_list = ["apple", "banana", "kiwi", "grape", "watermelon", "fig"]

# Print the list before sorting
print("Before sorting:", words_list)

# Apply the insertion sort algorithm
insertion_sort_by_length(words_list)

# Print the list after sorting
print("After sorting:", words_list)
#Expected Output:

#Before sorting: ['apple', 'banana', 'kiwi', 'grape', 'watermelon', 'fig']
#After sorting: ['fig', 'kiwi', 'apple', 'grape', 'banana', 'watermelon']

#The list is now sorted based on word length, from shortest to longest.