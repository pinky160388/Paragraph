import re

paragraph = '''  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''
paragraph = re.sub(r'\biZ\b', 'is', paragraph, flags=re.IGNORECASE)

# Calculate the number of whitespace characters in the text
num_whitespace = len(re.findall(r'\s', paragraph))

# Add a sentence with the last words of each existing sentence to the end of the paragraph
last_words = re.findall(r'\b\w+\b[.!?]', paragraph)
new_sentence = " ".join([word.strip('.,!?') for word in last_words])
paragraph += " " + new_sentence

print("Updated Paragraph:")
print(paragraph)
print()

print(f"Number of whitespace characters in the text: {num_whitespace}")
