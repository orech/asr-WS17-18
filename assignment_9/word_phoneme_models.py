import numpy as np
import matplotlib.pyplot as plt
import collections

def plot(num_oberservations):
    separated_tuples = list(zip(*num_oberservations))
    print(separated_tuples)
    counter = 0
    x_range = []
    for elem in separated_tuples[0]:
        x_range.append(counter)
        counter += 1
    print(x_range)


    plt.title('Number of observation per mixture')
    plt.xlabel('Mixture')
    plt.ylabel('Number of observations')
    plt.xticks(x_range, separated_tuples[0])
    plt.plot(x_range, separated_tuples[1])
    plt.plot(x_range, separated_tuples[1], 'or')
    plt.show()

def model_read(model_file):
  model = open(model_file, 'r')
  model_dict = {}
  start_indices = []

  for word in model:
    word = word.replace('\t', ' ')
    line = np.array(word.split(' '))
    model_dict[line[0]] = []
    for idx in line[1:]:
      if idx != '':
        model_dict[line[0]].append(int(idx))

  for key, values in model_dict.items():
    start_indices.append(values[0])

  return model_dict, start_indices

def num_obersvations_word(align_file):
    word_alignment = open(align_file, 'r')
    model, start_indices = model_read('whole-word.models')
    observations_count = {'silence': 0, 'zero': 0, 'one': 0, 'two': 0, 'three': 0, 'four': 0, 'five': 0, 'six': 0,
                        'seven': 0, 'eight': 0, 'nine': 0, 'oh': 0}

    for utterance in word_alignment:
        line_int = np.fromstring(utterance, dtype=int, sep=' ')
        curr_prefix = line_int[0]
        for elem in line_int:
            if elem in start_indices and curr_prefix != elem:
                curr_prefix = elem
                if elem == 1:
                    observations_count['zero'] += 1
                elif elem == 13:
                    observations_count['one'] += 1
                elif elem == 22:
                    observations_count['two'] += 1
                elif elem == 28:
                    observations_count['three'] += 1
                elif elem == 37:
                    observations_count['four'] += 1
                elif elem == 46:
                    observations_count['five'] += 1
                elif elem == 55:
                    observations_count['six'] += 1
                elif elem == 67:
                    observations_count['seven'] += 1
                elif elem == 82:
                    observations_count['eight'] += 1
                elif elem == 88:
                    observations_count['nine'] += 1
                elif elem == 97:
                    observations_count['oh'] += 1
            # count each silence state as word
            elif elem == 0 and curr_prefix != elem:
                curr_prefix = elem
                observations_count['silence'] += 1
    # close file
    word_alignment.close()
    # write count to file
    num_observations_sorted = sorted(observations_count.items(), key=lambda x: x[1], reverse=True)
    count = open('num_observations_per_mixture.word', 'w')
    for elem in num_observations_sorted:
        count.write(str(elem[0]) + ' ' + str(elem[1]) + '\n')

    count.close()
    return num_observations_sorted

def num_obersvations_phoneme(align_file):
    word_alignment = open(align_file, 'r')
    model, start_indices = model_read('phoneme.models')
    num_observations = {'silence': 0, 'ah': 0, 'ax': 0, 'ay': 0, 'f': 0, 'eh': 0, 'ey': 0, 'ih': 0, 'iy':0, 'k': 0, 'n': 0,
                        'ow': 0, 's': 0, 'r':0, 't':0, 'th':0, 'uw':0, 'v':0, 'w':0, 'z':0}


    for line in word_alignment:
        line_int = np.fromstring(line, dtype=int, sep=' ')
        current_prefix = line_int[0]
        for elem in line_int:
            if elem in start_indices and current_prefix != elem:
                current_prefix = elem
                if elem == 1:
                    num_observations['ah'] += 1
                elif elem == 4:
                    num_observations['ax'] += 1
                elif elem == 7:
                    num_observations['ay'] += 1
                elif elem == 10:
                    num_observations['f'] += 1
                elif elem == 13:
                    num_observations['eh'] += 1
                elif elem == 16:
                    num_observations['ey'] += 1
                elif elem == 19:
                    num_observations['ih'] += 1
                elif elem == 22:
                    num_observations['iy'] += 1
                elif elem == 25:
                    num_observations['k'] += 1
                elif elem == 28:
                    num_observations['n'] += 1
                elif elem == 31:
                    num_observations['ow'] += 1
                elif elem == 34:
                    num_observations['s'] += 1
                elif elem == 37:
                    num_observations['r'] += 1
                elif elem == 40:
                    num_observations['t'] += 1
                elif elem == 43:
                    num_observations['th'] += 1
                elif elem == 46:
                    num_observations['uw'] += 1
                elif elem == 49:
                    num_observations['v'] += 1
                elif elem == 52:
                    num_observations['w'] += 1
                elif elem == 55:
                    num_observations['z'] += 1
                elif elem == 0:
                    num_observations['silence'] += 1

            elif elem == 0 and current_prefix != elem:
                current_prefix = elem
                num_observations['silence'] += 1

    word_alignment.close()
    num_observations_sorted = sorted(num_observations.items(), key=lambda x: x[1], reverse=True)
    count = open('num_observations_per_mixture.phoneme', 'w')
    for elem in num_observations_sorted:
        count.write(str(elem[0]) + ' ' + str(elem[1]) + '\n')

    count.close()
    return num_observations_sorted

def translate_word_to_phoneme(word):

    if len(word) == 0:
      return []

    result = []
    # Oh
    if word[0] == 97:
        phoneme_state = 31
        result.append(phoneme_state)
        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                phoneme_state += 1
            result.append(phoneme_state)
    # Two
    elif word[0] == 22:
        phoneme_state = 40
        result.append(phoneme_state)
        t = True
        uw = False
        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                if abs(word[0] - word[i]) > 2 and not uw:
                    phoneme_state = 46
                    uw = True
                else:
                    phoneme_state += 1
            result.append(phoneme_state)
    # Eight
    elif word[0] == 82:
        phoneme_state = 16
        result.append(phoneme_state)
        ey = True
        t = False
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                if abs(word[0] - word[i]) > 2 and not t:
                    phoneme_state = 40
                    t = True
                else:
                    phoneme_state += 1
            result.append(phoneme_state)

    # One
    elif word[0] == 13:
        w = True
        ah = False
        n  = False
        phoneme_state = 52
        result.append(phoneme_state)
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                if abs(word[0] - word[i]) > 2 and not ah:
                    phoneme_state = 1
                    ah = True
                elif abs(word[0] - word[i]) > 5 and not n:
                    phoneme_state = 28
                    n = True
                else:
                    phoneme_state += 1
            result.append(phoneme_state)
    # Three
    elif word[0] == 28:
        phoneme_state = 43
        result.append(phoneme_state)
        th = True
        r = False
        iy = False
        for i in range(1, len(word)):
            if word[i] != word[i-1]:
                if abs(word[0] - word[i]) > 2 and not r:
                    phoneme_state = 37
                    r = True
                elif abs(word[0] - word[i]) > 5 and not iy:
                    phoneme_state = 22
                    iy = True
                else:
                    phoneme_state += 1
            result.append(phoneme_state)
    # Four
    elif word[0] == 37:
        phoneme_state = 10
        result.append(phoneme_state)
        f = True
        ow = False
        r = False
        for i in range(1, len(word)):
              if word[i] != word[i - 1]:
                  if abs(word[0] - word[i]) > 2 and not ow:
                      phoneme_state = 31
                      ow = True
                  elif abs(word[0] - word[i]) > 5 and not r:
                      phoneme_state = 37
                      r = True
                  else:
                      phoneme_state += 1
              result.append(phoneme_state)
    # Five
    elif word[0] == 46:
        phoneme_state = 10
        result.append(phoneme_state)
        f = True
        ay = False
        v = False
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                if abs(word[0] - word[i]) > 2 and not ay:
                    phoneme_state = 7
                    ay = True
                elif abs(word[0] - word[i]) > 5 and not v:
                    phoneme_state = 49
                    v = True
                else:
                    phoneme_state += 1
            result.append(phoneme_state)
    # Nine
    elif word[0] == 88:
        phoneme_state = 28
        result.append(phoneme_state)
        n = True
        ay = False
        n2 = False
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                if abs(word[0] - word[i]) > 2 and not ay:
                    phoneme_state = 7
                    ay = True
                elif abs(word[0] - word[i]) > 5 and not n2:
                    phoneme_state = 28
                    n2 = True
                else:
                    phoneme_state += 1
            result.append(phoneme_state)

    # Zero
    elif word[0] == 1:
        phoneme_state = 55
        result.append(phoneme_state)
        z = True
        ih = False
        r = False
        ow = False
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                if abs(word[0] - word[i]) > 2 and not ih:
                    phoneme_state = 19
                    ih = True
                elif abs(word[0] - word[i]) > 5 and not r:
                    phoneme_state = 37
                    r = True
                elif abs(word[0] - word[i]) > 8 and not ow:
                    phoneme_state = 31
                    ow = True
                else:
                    phoneme_state += 1
            result.append(phoneme_state)
    # Six
    elif word[0] == 55:
        phoneme_state = 34
        result.append(phoneme_state)
        s = True
        ih = False
        k = False
        s2 = False
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                if abs(word[0] - word[i]) > 2 and not ih:
                    phoneme_state = 19
                    ih = True
                elif abs(word[0] - word[i]) > 5 and not k:
                    phoneme_state = 25
                    k = True
                elif abs(word[0] - word[i]) > 8 and not s2:
                    phoneme_state = 34
                    s2 = True
                else:
                    phoneme_state += 1
            result.append(phoneme_state)
    # Seven
    elif word[0] == 67:
        s = True
        eh = False
        v  = False
        ax = False
        n  = False
        phoneme_state = 34
        result.append(phoneme_state)
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                    if abs(word[0] - word[i]) > 2 and not eh:
                        phoneme_state = 13
                        eh = True
                    elif abs(word[0] - word[i]) > 5 and not v:
                        phoneme_state = 49
                        v = True
                    elif abs(word[0] - word[i]) > 8 and not ax:
                        phoneme_state = 4
                        ax = True
                    elif abs(word[0] - word[i]) > 11 and not n:
                        phoneme_state = 28
                        n = True
                    else:
                        phoneme_state += 1
            result.append(phoneme_state)
    return result

def word_to_phoneme(src_file, target_file):
    word_alignment = open(src_file, 'r')
    phoneme_alignment = open(target_file, 'w')
    start_indices = [0, 1, 13, 22, 28, 37, 46, 55, 67, 82, 88, 97]

    all_words = []
    for line in word_alignment:
        current_word = []
        line_int = np.fromstring(line, dtype=int, sep=' ')
        current_prefix = line_int[0]
        for elem in line_int:
            # new word
            if elem in start_indices and current_prefix != elem:
                current_prefix = elem
                # translate current word into corresponding phoneme states
                phonemes = translate_word_to_phoneme(current_word)
                all_words.append(current_word)
                current_word = []
                if phonemes:
                    for phoneme in phonemes:
                        phoneme_alignment.write(str(phoneme) + ' ')

                if elem == 0:
                    phoneme_alignment.write('0 ')
                else:
                    current_word.append(elem)
            # write zero to file if we have more than one zero
            elif elem == 0:
                phoneme_alignment.write('0 ')
            # save state for the current word
            else:
                current_word.append(elem)
        phoneme_alignment.write('\n')

    # close files
    word_alignment.close()
    phoneme_alignment.close()

def assign_indices_and_triphone_models(ordered_triphones):
    output = open('triphone.models', 'w')
    starting_index = 58
    for elem in ordered_triphones:
        output.write(elem + '\t' + str(starting_index) + ' ' + str(starting_index + 1) + ' ' + str(starting_index + 2) + '\n')
        starting_index +=3
    output.close()

def plot_triphone(observations):
    for elem in observations.items():
        print(str(elem[0]) + ' ' + str(elem[1]))

def determine_phoneme(state):
    phoneme_prefix    = {0: 'silence', 1: 'ah', 4: 'ax', 7: 'ay', 10: 'f', 13: 'eh', 16: 'ey', 19: 'ih', 22: 'iy',
                         25: 'k', 28: 'n', 31: 'ow', 34: 's', 37: 'r', 40: 't', 43: 'th', 46: 'uw', 49: 'v', 52: 'w',
                         55: 'z'}
    try:
        return phoneme_prefix[state]
    except:
        return None

def count_triphones_from_phoneme_alignment(alignment_file):
    phoneme_alignment = open(alignment_file, 'r')
    triphones = {}
    for line in phoneme_alignment:
        line_int = np.fromstring(line, dtype=int, sep=' ')

        left_   = str()
        middle_ = str()
        right_  = str()

        current_phoneme = 0
        # iterate over all phonemes to count occurences of all triphones
        for i in range(len(line_int)):
            i = current_phoneme
            if i < len(line_int) and line_int[i] != 0:
                # fix left phoneme
                left_ = determine_phoneme(line_int[i])
                # find middle phoneme
                for j in range(i, len(line_int)):
                    if abs(line_int[i] - line_int[j]) > 2 and line_int[j] != 0:
                        middle_ = determine_phoneme(line_int[j])
                        # fix middle phoneme to make it left_ for the next triphone
                        current_phoneme = j
                        # find right context
                        for k in range(j, len(line_int)):
                            if abs(line_int[j] - line_int[k]) > 2 and line_int[k] != 0:
                                right_ = determine_phoneme(line_int[k])
                                break
                        break
            if None not in (left_, middle_, right_):
                if str(middle_) + '{' + str(left_) + ',' + str(right_) + '}' in triphones:
                    triphones[str(middle_) + '{' + str(left_) + ',' + str(right_) + '}'] += 1
                else:
                    triphones[str(middle_) + '{' + str(left_) + ',' + str(right_) + '}'] = 1
            if current_phoneme == i:
                current_phoneme += 1

    ordered_triphones =  collections.OrderedDict(sorted(triphones.items()))

    return ordered_triphones

def determine_triphone_indices(phoneme_sequence, curr_triphone):
    triphone_prefix, start_indices = model_read('triphone.models')
    result = []

    curr_phoneme = 0
    for idx, elem in enumerate(phoneme_sequence):
        result.append(triphone_prefix[curr_triphone][0] + curr_phoneme)
        if abs(elem - phoneme_sequence[curr_phoneme]) > 2 and elem != 0:
            curr_phoneme = idx

    return result

def mixed_alignment(phoneme_alignment_file, triphone_counts):
    phoneme_alignment = open(phoneme_alignment_file, 'r')
    mixed_alignment_file = open('mixed.alignment', 'w')

    mixed_alignment_arr = []

    for line_id, line in enumerate(phoneme_alignment):
        line_int = np.fromstring(line, dtype=int, sep=' ')
        mixed_alignment_arr.append([])
        left_ = str()
        middle_ = str()
        right_ = str()

        current_phoneme = 0
        for i in range(len(line_int)):
            i = current_phoneme
            if i < len(line_int) and line_int[i] != 0:
                left_phoneme_start_id = i
                left_ = determine_phoneme(line_int[i])
                for j in range(i, len(line_int)):
                    if abs(line_int[i] - line_int[j]) > 2 and line_int[j] != 0:
                        middle_ = determine_phoneme(line_int[j])
                        current_phoneme = j
                        middle_phoneme_start_id = current_phoneme
                        for k in range(j, len(line_int)):
                            if abs(line_int[j] - line_int[k]) > 2 and line_int[k] != 0:
                                right_ = determine_phoneme(line_int[k])
                                for e in range(k, len(line_int)):
                                    if abs(line_int[k] - line_int[e]) > 2 and line_int[e] != 0:
                                        right_phoneme_last_id = e
                                        break
                                break
                        break
            if None not in (left_, middle_, right_):
                triphone = str(middle_) + '{' + str(left_) + ',' + str(right_) + '}'
                if triphone in triphone_counts.keys():
                    if triphone_counts[triphone] > 300:
                        triphone_mixture_ind = determine_triphone_indices(line_int[left_phoneme_start_id:right_phoneme_last_id], triphone)
                        mixed_alignment_arr[line_id].extend(triphone_mixture_ind)
                    else:
                        mixed_alignment_arr[line_id].extend(line_int[left_phoneme_start_id:middle_phoneme_start_id - 1])
            if current_phoneme == i:
                current_phoneme += 1

        mixed_alignment_file.write(' '.join(str(x) for x in mixed_alignment_arr[line_id]))
        mixed_alignment_file.write('\n')


    return mixed_alignment_arr
