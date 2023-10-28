import spacy


class NamedEntityExtractor:
    """
    Клас для визначення іменованих сутностей з тексту.
    """

    def __init__(self, model_name='uk_core_news_sm'):
        """
        Ініціалізація об'єкта класу з моделлю, яка використовується для витягування сутностей.
        """
        self.model = self.load_model(model_name)

    @staticmethod
    def load_model(model):
        """
        Статичний метод для завантаження моделі.
        """
        try:
            return spacy.load(model)
        except Exception as e:
            print(f"An error occurred while loading the model: {e}")
            return None

    def get_extract_entities(self, text):
        """
        Метод для визначення іменованих сутностей з тексту.
        """
        if not isinstance(text, str):
            raise TypeError('text must be a string')
        else:
            doc = self.model(text)
            return {ent.text: ent.label_ for ent in doc.ents}
