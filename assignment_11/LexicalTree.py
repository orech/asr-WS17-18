import sys
sys.setrecursionlimit(1000)
class PrefixTreeNode:
    def __init__(self):
        self.children = None
        self.count = 0

    def add_word(self, word):
        # word: vector of phoneme ids (integers)
        self.count += 1
        if len(word) == 0:
            return
        if self.children == None:
            self.children = {}
        next_phoneme_id = word[0]
        # next phoneme is not yet among current node children
        if next_phoneme_id not in self.children:
            self.children[next_phoneme_id] = PrefixTreeNode()
        # current phoneme is already a child of a current node
        child_node = self.children[next_phoneme_id]
        child_node.add_word(word[1:])

    def get_num_of_children(self):
        if self.children != None:
            num_of_childern = len(self.children)
            for id in self.children:
                num_of_childern += self.children[id].get_num_of_children()
            return num_of_childern
        else:
            return 0
