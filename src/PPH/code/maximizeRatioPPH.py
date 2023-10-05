import numpy as np

def calculate_R(pairs):
    sum_x = np.sum([pair[0] for pair in pairs])
    sum_y = np.sum([pair[1] for pair in pairs])
    return sum_x / sum_y

def solve_PPH(required_pair, pairs):
    selected_pairs_indices = []
    selected_pairs = [required_pair]
    max_R = calculate_R(np.array(selected_pairs))
    history_R = [max_R]

    change_R = True
    while (change_R and len(selected_pairs) < len(pairs) + 1 ):
      change_R = False
      for i, pair in enumerate(pairs):
          if pair[0] / pair[1] > max_R:
              selected_pairs_indices.append(i)
              selected_pairs.append(pair)
              max_R = calculate_R(np.array(selected_pairs))
              history_R.append(max_R)
              change_R = True


    print(f'R*: {max_R} \n')
    # print(f'S*_indices: {set(selected_pairs_indices)} \n')
    # print(f'R_history: {history_R} \n')
    
    return selected_pairs 

