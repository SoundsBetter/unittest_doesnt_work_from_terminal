def anagram(text: str) -> str:
    words = text.split(' ')
    reversed_words = []
    for word in words:
        letters = [char for char in word if char.isalpha()]
        reversed_word = ''.join(letters.pop() if char.isalpha() else char for char in word)
        reversed_words.append(reversed_word)
    reversed_text = ' '.join(reversed_words)
    return reversed_text
