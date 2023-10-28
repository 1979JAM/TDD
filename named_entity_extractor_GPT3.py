import spacy


class NamedEntityExtractor:
    def __init__(self, model_name='uk_core_news_sm'):
        self.nlp = self.load_model(model_name)

    def get_extract_entities(self, text):
        """
        Extract named entities and their types from the input text.

        :param text: Input text.
        :return: A dictionary with named entities as keys and their types as values.
        """
        if not isinstance(text, str):
            raise TypeError("Input text must be a string")

        doc = self.nlp(text)
        entities = {ent.text: ent.label_ for ent in doc.ents}
        return entities

    @staticmethod
    def load_model(model_name):
        try:
            model = spacy.load(model_name)
            return model
        except OSError:
            return None
