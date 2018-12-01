import sys

def _change_freq(current_freq, value):
    if value[0] == '+':
        current_freq += int(value[1:])         
    else:
        current_freq -= int(value[1:])         

    return current_freq

def calculate_output(input_list):
    start = 0
    
    for input in input_list:
        start = _change_freq(start, input)

    return start

def find_first_repeat_freq(input_list):
    start = 0
    current_idx = 0
    seen_freqs = set([0])

    while(True):
        if current_idx == len(input_list):
            current_idx = 0

        start = _change_freq(start, input_list[current_idx])
        if start in seen_freqs:
            return start

        seen_freqs.add(start)

        current_idx += 1

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        inputs = [line.strip() for line in f.readlines()]
        print('OUTPUT PART 1', calculate_output(inputs))
        print('OUTPUT PART 2', find_first_repeat_freq(inputs))

