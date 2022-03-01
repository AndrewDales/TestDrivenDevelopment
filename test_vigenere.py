import pytest
from vigenere import VigenereCipher


class TestVigenereCipher:
    @pytest.fixture()
    def my_cipher(self):
        return VigenereCipher("TRAIN")

    # Test fixture works correctly
    def test_vigenere_cipher(self, my_cipher):
        assert my_cipher.keyword == "TRAIN"

    # Test OK for lower_case key
    def test_init_lower(self):
        my_cipher = VigenereCipher("taxi")
        assert my_cipher.keyword == "TAXI"

    # Test error raised correctly for invalid keywords
    def test_init_invalid(self):
        with pytest.raises(ValueError):
            VigenereCipher("$%FG")
        with pytest.raises(TypeError):
            VigenereCipher(56)

    # Test _combine_character works for ordinary values, including where mod 26 is needed
    def test_combine_character(self, my_cipher):
        assert my_cipher._combine_character("F", "H") == "M"
        assert my_cipher._combine_character("Y", "N") == "L"

    # Test _combine_character works for lower case
    def test_combine_character_lower(self, my_cipher):
        assert my_cipher._combine_character("g", "i") == "O"
        assert my_cipher._combine_character("t", "W") == "P"

    # Test _combine_character raises correct error types
    def test_combine_invalid_string(self, my_cipher):
        with pytest.raises(ValueError):
            my_cipher._combine_character("G", "@")
        with pytest.raises(TypeError):
            my_cipher._combine_character(6, "A")

    # Test _combine_character raises error if characters of incorrect length
    def test_combine_correct_length(self, my_cipher):
        with pytest.raises(ValueError):
            my_cipher._combine_character("AA", "C")
        with pytest.raises(ValueError):
            my_cipher._combine_character("Z", "YY")

    # Test _extend_keyword works correctly
    def test_extend_keyword(self, my_cipher):
        assert my_cipher._extend_keyword(13) == "TRAINTRAINTRA"
        cipher = VigenereCipher("taxi")
        assert cipher._extend_keyword(11) == "TAXITAXITAX"

    # Test _separate_character works for ordinary values, including where mod 26 is needed
    def test_separate_character(self, my_cipher):
        assert my_cipher._separate_character("X", "R") == "G"
        assert my_cipher._separate_character("o", "s") == "W"

    # Test the encode method on normal text
    def test_encode(self, my_cipher):
        assert my_cipher.encode("ENCODEDINPYTHON") == "XECWQXUIVCRKHWA"
        cipher = VigenereCipher("secret")
        assert cipher.encode("Attack the bridge") == "SXVRGDLLGSVBVKG"

    # Test the decode method on normal text
    def test_decode(self, my_cipher):
        assert my_cipher.decode("XECWQXUIVCRKHWA") == "ENCODEDINPYTHON"
        cipher = VigenereCipher("duke")
        assert cipher.decode("ELOENUVIJ") == "BREAKALEG"

    # Test for errors raised with encode
    def test_encode_invalid_characters(self, my_cipher):
        with pytest.raises(TypeError):
            my_cipher.encode(987)
        with pytest.raises(ValueError):
            my_cipher.encode("Hello World!")
