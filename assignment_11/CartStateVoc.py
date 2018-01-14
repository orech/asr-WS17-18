class CartStateVoc:
    def __init__(self):
        self.id_by_triphone = {}
        self.triphone_by_id = {}
        self.curr_id = -1
        # Initialize the vocabulary mappings
        cart = open('cart.state', 'r')
        for line in cart:
            leftPhoneme = line.split('{')[1].split('+')[0]
            middlePhoneme = line.split('{')[0]
            rightPhoneme =  line.split('{')[1].split('+')[1].split('}')[0]
            stateIdx = line.split('{')[1].split('+')[1].split('}')[1][1:2]
            clusterIdx = int(line.split('{')[1].split('+')[1].split('}')[1][3:])
            self.addSymbol(leftPhoneme + middlePhoneme + rightPhoneme + stateIdx, clusterIdx)
    def size(self):
        return self.curr_id + 1
    def addSymbol(self, triphone, clusterIdx):
        if triphone not in self.id_by_triphone:
            self.curr_id += 1
            self.id_by_triphone[triphone] = clusterIdx
            self.triphone_by_id[clusterIdx] = triphone
        return self.id_by_triphone[triphone]
    def symbol(self, ID):
            return self.triphone_by_id[ID]
    def index(self, word):
            return self.id_by_triphone[word]