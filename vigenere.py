class VigenereCipher:
    def __init__(self, keyword):
        if not isinstance(keyword, str):
            raise TypeError("Keyword must be a string")
        if not keyword.isalpha():
            raise ValueError("Keyword must include only alphabetic characters (a-z or A-Z")
        self.keyword = keyword.upper()

    @staticmethod
    def _combine_character(plain_chr: str, key_chr: str) -> str:
        """
        combines two alpha characters into a cipher character
        :param plain_chr: single alpha character - plain text letter
        :param key_chr: single alpha character - key code letter
        :return: cipher_chr - returns a cipher character from combining plain text and key characters
        """
        # Input validation
        if not (isinstance(plain_chr, str) and isinstance(key_chr, str)):
            raise TypeError("Both inputs must be strings")
        if not (plain_chr.isalpha() and key_chr.isalpha()):
            raise ValueError("Both inputs must be a-z or A-Z")
        if len(plain_chr) > 1 or len(key_chr) > 1:
            raise ValueError("Both inputs must be single characters")
        # Main program
        plain_number = ord(plain_chr.upper()) - ord('A')
        key_number = ord(key_chr.upper()) - ord('A')
        cipher_number = (plain_number + key_number) % 26 + 65
        cipher_chr = chr(cipher_number)
        return cipher_chr

    @staticmethod
    def _separate_character(cipher_chr, key_chr):
        cipher_num = ord(cipher_chr.upper()) - ord('A')
        keyword_num = ord(key_chr.upper()) - ord('A')
        plain_num = (cipher_num - keyword_num) % 26
        return chr(plain_num + ord('A'))

    def _extend_keyword(self, msg_length: int) -> str:
        """
        extends keyword to the length of msg_length by repeating copies of the keyword
        :param msg_length: integer representing the total message length
        :return: str representing the repeated key word
        """
        d, m = divmod(msg_length, len(self.keyword))
        return self.keyword * d + self.keyword[:m]

    def encode(self, plaintext) -> str:
        """
        method takes a plaintext message, removes all spaces and converts to a coded
        message using the instance keyword
        :param plaintext:
        :return: ciphertext message
        """
        return self._encode(plaintext, self._combine_character)

    def decode(self, ciphertext) -> str:
        """
        method takes a ciphertext message, removes all spaces and converts to a plaintext
        message using the instance keyword
        :param ciphertext:
        :return:
        """
        return self._encode(ciphertext, self._separate_character)

    def _encode(self, text, encoding_func):
        """
        method takes a ciphertext message, removes all spaces and converts to a plaintext
        message using the instance keyword
        :param ciphertext:
        :return:
        """
        if not isinstance(text, str):
            raise TypeError("Ciphertext must be a string")
        text_msg = text.replace(" ", "")
        if not text_msg.isalpha():
            raise ValueError("Ciphertext must include only alphabetic characters (a-z or A-Z")
        output_letters = [encoding_func(p, k)
                          for p, k in zip(text_msg, self._extend_keyword(len(text_msg)))]
        return "".join(output_letters)
