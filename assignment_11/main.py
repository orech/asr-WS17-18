import copy
from PhonemeVoc import PhonemeVoc
from TriphoneVoc import TriphoneVoc
from CartTriphoneVoc import CartTriphoneVoc
from CartStateVoc import CartStateVoc
from LexicalTree import PrefixTreeNode
from lxml import etree


vocabulary = PhonemeVoc()
vocabulary_triphones = TriphoneVoc()
vocabulary_cart_triphones = CartTriphoneVoc()
vocabulary_cart_triphone_states = CartStateVoc()
prefix_tree_root_phonemes = PrefixTreeNode()
prefix_tree_root_triphones = PrefixTreeNode()
prefix_tree_root_cart_triphones = PrefixTreeNode()
prefix_tree_root_cart_triphone_states = PrefixTreeNode()
tree = etree.parse("lexicon.xml")
root = tree.getroot()
lemmaList = root.findall(".//lemma")

num_words = 1
num_phonemes = 1
word_ends_2_phoneme_gen, word_ends_3_phoneme_gen = 0, 0

#adding silence word:
prefix_tree_root_phonemes.add_word([vocabulary.index(lemmaList[0].find('phon').text)])

# Task 11.1 (a, b) : generating lexical prefix tree
# we don't need silence, sentence-end and unknown here
for word in lemmaList[4:]:
    curr_phoneme_ids = []
    curr_words = word.findall('phon')
    for word in curr_words:
      num_words += 1
      curr_word_phonemes = word.text.strip().split(' ')
      for phoneme_id, phoneme in enumerate(curr_word_phonemes):
        num_phonemes += 1
        curr_phoneme_id = vocabulary.index(phoneme)
        curr_phoneme_ids.append(curr_phoneme_id)
      if len(curr_word_phonemes) == 2:
        word_ends_2_phoneme_gen += 1
      if len(curr_word_phonemes) == 3:
        word_ends_3_phoneme_gen += 1
      prefix_tree_root_phonemes.add_word(curr_phoneme_ids)


# adding silence word:
prefix_tree_root_triphones.add_word([vocabulary_triphones.index('#' + lemmaList[0].find('phon').text + '#')])
prefix_tree_root_cart_triphones.add_word([vocabulary_cart_triphones.index('#' + lemmaList[0].find('phon').text + '#')])
prefix_tree_root_cart_triphone_states.add_word([vocabulary_cart_triphone_states.index('#' + lemmaList[0].find('phon').text + '#' + '0')])
num_triphones = 0

# Task 11.1 (c, d, e) : generating lexical prefix tree with triphones
for word in lemmaList[4:]:
    word_variantions = word.findall('phon')
    for word in word_variantions:
      current_triphone_ids = []
      current_cart_triphone_ids = []
      current_cart_triphone_state_ids = []
      num_words += 1
      # add word boundary context in the beginning and in the end
      curr_string_phonemes = ['#']
      curr_string_phonemes += word.text.strip().split(' ')
      curr_string_phonemes.append('#')

      for phoneme_id in range(len(curr_string_phonemes) - 1):
          if phoneme_id != 0:
            num_triphones += 1
            curr_triphone_id = vocabulary_triphones.index(curr_string_phonemes[phoneme_id - 1] +
                                                          curr_string_phonemes[phoneme_id] +
                                                          curr_string_phonemes[phoneme_id + 1])
            curr_cart_triphone_id = vocabulary_cart_triphones.index(curr_string_phonemes[phoneme_id - 1] +
                                                                    curr_string_phonemes[phoneme_id] +
                                                                    curr_string_phonemes[phoneme_id + 1])
            curr_cart_triphone_state_id_0 = vocabulary_cart_triphone_states.index(curr_string_phonemes[phoneme_id - 1] +
                                                                                  curr_string_phonemes[phoneme_id] +
                                                                                  curr_string_phonemes[phoneme_id + 1] + '0')
            curr_cart_triphone_state_id_1 = vocabulary_cart_triphone_states.index(curr_string_phonemes[phoneme_id - 1] +
                                                                                  curr_string_phonemes[phoneme_id] +
                                                                                  curr_string_phonemes[phoneme_id + 1] + '1')
            curr_cart_triphone_state_id_2 = vocabulary_cart_triphone_states.index(curr_string_phonemes[phoneme_id - 1] +
                                                                                  curr_string_phonemes[phoneme_id] +
                                                                                  curr_string_phonemes[phoneme_id + 1] + '2')
            current_triphone_ids.append(curr_triphone_id)
            current_cart_triphone_ids.append(curr_cart_triphone_id)
            current_cart_triphone_state_ids.append(curr_cart_triphone_state_id_0)
            current_cart_triphone_state_ids.append(curr_cart_triphone_state_id_1)
            current_cart_triphone_state_ids.append(curr_cart_triphone_state_id_2)

      prefix_tree_root_triphones.add_word(current_triphone_ids)
      prefix_tree_root_cart_triphones.add_word(current_cart_triphone_ids)
      prefix_tree_root_cart_triphone_states.add_word(current_cart_triphone_state_ids)


total_num_words = prefix_tree_root_phonemes.count
compFactor2 = (total_num_words * 2) / prefix_tree_root_phonemes.get_num_of_children()
compFactor3 = (total_num_words * 3) / prefix_tree_root_phonemes.get_num_of_children()
compFactor = (total_num_words * 1) / prefix_tree_root_phonemes.get_num_of_children()

compFactorTriphone2 = (total_num_words * 2) / prefix_tree_root_triphones.get_num_of_children()
compFactorTriphone3 = (total_num_words * 3) / prefix_tree_root_triphones.get_num_of_children()
compFactorTriphone = (total_num_words) / prefix_tree_root_triphones.get_num_of_children()

compFactorCartPhone2 = (total_num_words * 2) / prefix_tree_root_cart_triphones.get_num_of_children()
compFactorCartPhone3 = (total_num_words * 3) / prefix_tree_root_cart_triphones.get_num_of_children()
compFactorCartPhone = (total_num_words) / prefix_tree_root_cart_triphones.get_num_of_children()

compFactorCartStatePhone2 = (total_num_words * 2) / prefix_tree_root_cart_triphone_states.get_num_of_children()
compFactorCartStatePhone3 = (total_num_words * 3) / prefix_tree_root_cart_triphone_states.get_num_of_children()
compFactorCartStatePhone = (total_num_words) / prefix_tree_root_cart_triphone_states.get_num_of_children()

print("Number of word variations in the lexicon: ", prefix_tree_root_phonemes.count)
print('\n')
print("Results for monophones : ")
print("Number of arcs in the lexicon prefix tree : ", prefix_tree_root_phonemes.get_num_of_children())
print("Total number of phonemes in the lexicon: ", num_phonemes)
print("Compression factor for the whole tree: ", compFactor)
print("Compression factor for the first two phoneme generations : ", compFactor2)
print("Compression factor for the first three phoneme generations: ", compFactor3)
print('\n')
print("Results for triphones : ")
print("Number of arcs in the triphone prefix tree : ", prefix_tree_root_triphones.get_num_of_children())
print("Compression factor for the whole tree: ", compFactorTriphone)
print("Compression factor for the first two phoneme generations : ", compFactorTriphone2)
print("Compression factor for the first three phoneme generations: ", compFactorTriphone3)
print('\n')
print("Results for cart_triphones:")
print("Number of arcs in the cart_triphone prefix tree : ", prefix_tree_root_cart_triphones.get_num_of_children())
print("Compression factor for the whole tree: ", compFactorCartPhone)
print("Compression factor for the first two phoneme generations : ", compFactorCartPhone2)
print("Compression factor for the first three phoneme generations: ", compFactorCartPhone3)
print('\n')
print("Results for cart_triphone_states:")
print("Number of arcs in the triphone prefix tree : ", prefix_tree_root_cart_triphone_states.get_num_of_children())
print("Compression factor for the whole tree: ", compFactorCartStatePhone)
print("Compression factor for the first two phoneme generations : ", compFactorCartStatePhone2)
print("Compression factor for the first three phoneme generations: ", compFactorCartStatePhone3)