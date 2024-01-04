''' Created: 04/01/2024 '''

class CaesarCipher:

    def __init__(self, key: str, text: str, sequence: str = 'abcdefghijklmnopqrstuvwxyz'):
        self._validation_enabled = False
        self.set_sequence(sequence)
        self.set_key(key)
        self.set_text(text)
        self._validation_enabled = True
        self._check_validation()

    def set_text(self, text: str) -> None:
        self.text = text.strip().lower().replace(' ', '')
        self._check_validation()

    def set_key(self, key: str) -> None:
        self.key = key.lower()
        self._check_validation()

    def set_sequence(self, sequence: str) -> None:
        self.sequence = sequence.lower()
        self.sequence_length = len(sequence)
        self._character_map = {character: index for index, character in enumerate(self.sequence)}
        self._check_validation()

    def encrypt(self) -> str:
        return self._shift_text(self._get_shift(), self.text)

    def decrypt(self) -> str:
        return self._shift_text(-self._get_shift(), self.text)

    def _check_validation(self) -> None:
        if self._validation_enabled:
            self._validate_state()
    
    def _validate_state(self) -> None:
        if self.sequence_length != len(set(self.sequence)):
            raise ValueError(f'Sequence must be unique set of characters, not {self.sequence}')
        if self.key not in self.sequence or len(self.key) > 1:
            raise ValueError(f'Key must be character from sequence: {self.sequence}, not {self.key}...')
        for character in set(self.text):
            if character not in self.sequence:
                raise ValueError(f'Text must only contain characters from: {self.sequence}, not {character}...')

    def _shift_text(self, shift: int, text: str) -> str:
        shifted_text = []
        for character in text:
            index = self._character_map[character]
            shifted_index = (index + shift) % self.sequence_length
            new_character = self.sequence[shifted_index]
            shifted_text.append(new_character)
        return ''.join(shifted_text)
    
    def _get_shift(self) -> int:
        return self.sequence.index(self.key)
    
    def __str__(self):
        attributes = vars(self)
        return ', '.join([f'{key}="{value}"' for key, value in attributes.items()])

if __name__ == '__main__':
    caeser_cipher = CaesarCipher('k', 'hello world')
    ciphertext = caeser_cipher.encrypt()
    caeser_cipher.set_text(ciphertext)
    plaintext = caeser_cipher.decrypt()
    print(ciphertext, plaintext)
