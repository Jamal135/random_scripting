''' Created: 21/01/2024 '''

def decode(message_file: str) -> str:
    with open(message_file, 'r') as textfile:
        data = textfile.read()
    word_dictionary = {}
    for line in data.split('\n'):
        if line.strip():
            key, word = line.split(' ')
            word_dictionary[int(key)] = word
    message_words = []
    key, increment = 1, 2
    while True:
        if key in word_dictionary:
            message_words.append(word_dictionary[key])
            key += increment
            increment += 1
        else:
            break
    return ' '.join(message_words)

if __name__ == '__main__':
    print(decode('scripts/coding_qual_input.txt'))
