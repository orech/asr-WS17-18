from lxml import etree
class TriphoneVoc:
    def __init__(self):
        self.id_by_triphone = {}
        self.triphone_by_id = {}
        self.curr_id = -1
        tree = etree.parse("lexicon.xml")
        root = tree.getroot()
        phonemeList = root.findall(".//phoneme")
        for phLeft in phonemeList:
            for phMiddle in phonemeList:
                for phRight in phonemeList:
                    self.addSymbol(phLeft.find('symbol').text + phMiddle.find('symbol').text +
                                   phRight.find('symbol').text)
                self.addSymbol('#' + phMiddle.find('symbol').text +
                                phLeft.find('symbol').text)
                self.addSymbol(phLeft.find('symbol').text + phMiddle.find('symbol').text +
                                '#')
            self.addSymbol('#' + phLeft.find('symbol').text + '#')
    def size(self):
        return self.curr_id + 1
    def addSymbol(self, triphone):
        if triphone not in self.id_by_triphone:
            self.curr_id += 1
            self.id_by_triphone[triphone] = self.curr_id
            self.triphone_by_id[self.curr_id] = triphone
        return self.id_by_triphone[triphone]
    def symbol(self, ID):
            return self.triphone_by_id[ID]
    def index(self, word):
            return self.id_by_triphone[word]