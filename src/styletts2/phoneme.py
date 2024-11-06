from gruut import sentences
from collections.abc import Iterable
import phonemizer


class PhonemeConverter:
    def phonemize(self, text):
        pass


class GruutPhonemizer(PhonemeConverter):
    def phonemize(self, text, lang='en-us'):
        phonemized = []
        for sent in sentences(text, lang=lang):
            for word in sent:
                if isinstance(word.phonemes, Iterable):
                    phonemized.append(''.join(word.phonemes))
                elif isinstance(word.phonemes, str):
                    phonemized.append(word.phonemes)
        phonemized_text = ' '.join(phonemized)
        return phonemized_text

class EspeakPhonemizer(PhonemeConverter):
    def __init__(self):
        self.phonemizer = phonemizer.backend.EspeakBackend(language='en-us', preserve_punctuation=True,  with_stress=True)
    def phonemize(self, text, lang='en-us'):
        return self.phonemizer.phonemize([text])[0]






# class YourPhonemizer(Phonemizer):
#     def phonemize(self, text):
#         ...


class PhonemeConverterFactory:
    @staticmethod
    def load_phoneme_converter(name: str, **kwargs):
        if name == 'gruut':
            return GruutPhonemizer()
        elif name == 'espeak':
            return EspeakPhonemizer()
        else:
            raise ValueError("Invalid phoneme converter.")
