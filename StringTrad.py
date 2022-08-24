class StringTrad:
    def __init__(self, varname: str, langline: int, language: str = "US", file: str = "lang.language"):
        self.varName = varname
        self.langLine = langline-1
        self.lang = language
        self.file = file

        if self.lang == 'US':
            self.symbol = "0"
        elif self.lang == 'FR':
            self.symbol = "1"

        self.listeOtherSymbol = [str(i) for i in range(2) if str(i) is not self.symbol]
        self.string = self.getTranslated()

    def getTranslated(self):
        langFile = open(self.file, "r")
        ligneLut = langFile.readlines()
        ligneUsefull = ligneLut[self.langLine]
        letterIndiceStart = 0
        while ligneUsefull[letterIndiceStart] != self.symbol:
            letterIndiceStart += 1
        letterIndiceStart += 1
        letterIndiceEnd = letterIndiceStart
        while ligneUsefull[letterIndiceEnd] != "/" and ligneUsefull[letterIndiceEnd] not in self.listeOtherSymbol:
            letterIndiceEnd += 1
        text = ligneUsefull[letterIndiceStart:letterIndiceEnd]
        langFile.close()
        return text

    def __str__(self):
        return self.string


