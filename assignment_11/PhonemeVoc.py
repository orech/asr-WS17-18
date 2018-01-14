from lxml import etree
class PhonemeVoc:
    def __init__(self):
        self.id_by_phoneme = {}
        self.phoneme_by_id = {}
        self.curr_id = -1
        tree = etree.parse("lexicon.xml")
        root = tree.getroot()
        phonemeList = root.findall(".//phoneme")
        for ph in phonemeList:
            self.addSymbol(ph.find('symbol').text)
    def size(self):
        return self.curr_id + 1
    def addSymbol(self, phoneme):
        if phoneme not in self.id_by_phoneme:
            self.curr_id += 1
            self.id_by_phoneme[phoneme] = self.curr_id
            self.phoneme_by_id[self.curr_id] = phoneme
        return self.id_by_phoneme[phoneme]
    def symbol(self, ID):
            return self.phoneme_by_id[ID]
    def index(self, word):
            return self.id_by_phoneme[word]

