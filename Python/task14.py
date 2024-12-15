# Count word frequency in a paragraph. 
# Input: "apple banana apple orange banana banana" 
# Output: 
# apple: 2 
# banana: 3 
# orange: 1

from collections import Counter

def count_word_in_paragraph(paragraph):
    words = paragraph.split()
    
    word_count = Counter(words)
    
    for word, count in word_count.items():
        print(f"{word} : {count}")
        
paragraph = "apple banana apple orange banana banana"
count_word_in_paragraph(paragraph)