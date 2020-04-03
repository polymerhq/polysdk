class MaskedData:
    __text = ''

    def __init__(self, text):
        if text is '':
            raise Exception("text is empty.")

        self.__text = text

    def get_text(self):
        return self.__text;