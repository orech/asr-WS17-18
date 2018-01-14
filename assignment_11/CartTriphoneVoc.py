class CartTriphoneVoc:
    def __init__(self):
        self.id_by_triphone = {}
        self.triphone_by_id = {}
        self.curr_cluster_id = -1
        cart = open('cart.phone', 'r')
        for line in cart:
            left_ph = line.split('{')[1].split('+')[0]
            middle_ph = line.split('{')[0]
            right_ph =  line.split('{')[1].split('+')[1].split('}')[0]
            cluster_id = int(line.split('{')[1].split('+')[1].split('}')[1][1:])
            self.addSymbol(left_ph + middle_ph + right_ph, cluster_id)
    def size(self):
        return self.curr_cluster_id + 1
    def addSymbol(self, triphone, cluster_id):
        if triphone not in self.id_by_triphone:
            self.id_by_triphone[triphone] = cluster_id
            self.triphone_by_id[cluster_id] = triphone
        return self.id_by_triphone[triphone]
    def symbol(self, ID):
            return self.triphone_by_id[ID]
    def index(self, word):
            return self.id_by_triphone[word]