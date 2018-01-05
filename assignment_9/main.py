# group - 6
# Anna Piunova - 362130
# Qianwen Yuan - 383028
# Sara Rezaee Tamasok - 382800

import word_phoneme_models as wpm

# -------------------------- (b) ----------------------------
observations_count_wm = wpm.num_obersvations_word('alignment.word')
wpm.plot(observations_count_wm)

# -------------------------- (c) ----------------------------
wpm.word_to_phoneme('alignment.word', 'alignment.phoneme')
observations_count_phm = wpm.num_obersvations_phoneme('alignment.phoneme')
wpm.plot(observations_count_phm)

# -------------------------- (d) ----------------------------
ordered_triphones = wpm.count_triphones_from_phoneme_alignment('alignment.phoneme')
wpm.assign_indices_and_triphone_models(ordered_triphones)
wpm.plot_triphone(ordered_triphones)

# -------------------------- (e) ---------------------------
ordered_triphones = wpm.count_triphones_from_phoneme_alignment('alignment.phoneme')
mix_align = wpm.mixed_alignment('alignment.phoneme', ordered_triphones)