''' Created: 04/01/2024 '''

class CaesarCipher:

    def __init__(self, key: str, text: str, sequence: str = 'abcdefghijklmnopqrstuvwxyz'):
        self.validate = False
        self.update_sequence(sequence), self.update_key(key), self.update_text(text)
        self.validate = True
        self._handle_validation()

    def update_text(self, text: str) -> None:
        self.text = text.strip().lower().replace(' ', '')
        self._handle_validation()

    def update_key(self, key: str) -> None:
        self.key = key.lower()
        self._handle_validation()

    def update_sequence(self, sequence: str) -> None:
        self.sequence = sequence.lower()
        self.sequence_length = len(sequence)
        self._char_to_index = {char: idx for idx, char in enumerate(self.sequence)}
        self._handle_validation()

    def encrypt(self) -> str:
        return self._shift_text(self._get_shift(), self.text)

    def decrypt(self) -> str:
        return self._shift_text(-self._get_shift(), self.text)

    def _handle_validation(self) -> None:
        if self.validate:
            self._validate_state()
    
    def _validate_state(self) -> None:
        if self.sequence_length != len(set(self.sequence)):
            raise ValueError('Sequence must be unique set of characters')
        if self.key not in self.sequence or len(self.key) > 1:
            raise ValueError(f'Key must be one character from: {self.sequence}')
        for character in set(self.text):
            if character not in self.sequence:
                raise ValueError(f'Text must only contain characters: {self.sequence}')

    def _shift_text(self, shift: int, text: str) -> str:
        shifted_text = []
        for character in text:
            index = self._char_to_index.get(character, -1)
            shifted_index = (index + shift) % self.sequence_length
            new_character = self.sequence[shifted_index]
            shifted_text.append(new_character)
        return ''.join(shifted_text)
    
    def _get_shift(self) -> int:
        return self.sequence.index(self.key)

if __name__ == '__main__':
    caeser_cipher = CaesarCipher('C', 'hello worldz')
    ciphertext = caeser_cipher.encrypt()
    caeser_cipher.update_text(ciphertext)
    plaintext = caeser_cipher.decrypt()
    print(ciphertext, plaintext)
