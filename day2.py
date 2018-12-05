import sys 

from collections import defaultdict

def _has_amount(input_line, number):
    count = 0
    prev = ''

    char_counts = defaultdict(int)

    for char in input_line:
        char_counts[char] += 1

    for char, count in char_counts.items():
        if count == number:
            return True

    return False

def _has_twos(input_line):
    return _has_amount(input_line, 2) 
    
    

def _has_threes(input_line):
    return _has_amount(input_line, 3)


def get_twos_and_threes(input_list):
    twos = 0
    threes = 0

    (twos, threes) = zip(*[
        (_has_twos(input_line), _has_threes(input_line))
        for input_line in input_list
    ])

    return sum(twos) * sum(threes)

def get_common_letters_in_box_ids(input_list):
    sorted_inputs = sorted(input_list)

    def array_diff(a, b):
        return [
            (letter_a is not letter_b, letter_a if letter_a is letter_b else None)
                for letter_a, letter_b 
                in zip(a, b)
            ]

    for i in range(len(sorted_inputs) - 1):
        first_input = sorted_inputs[i]
        second_input = sorted_inputs[i+1]

        number_of_different_chars = array_diff(first_input, second_input)

        if sum([is_diff[0] for is_diff in number_of_different_chars]) == 1:
            print(number_of_different_chars)
            return ''.join([is_diff[1] for is_diff in number_of_different_chars
                if is_diff[1] is not None])

    return ''

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        inputs = [line.strip() for line in f.readlines()]
        # print('OUTPUT 1', get_twos_and_threes(inputs))
        print('OUTPUT 2', get_common_letters_in_box_ids(inputs))
