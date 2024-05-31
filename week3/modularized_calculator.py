#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def read_multiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1


def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def read_left_kakko(line, index):
    token = {'type': 'LEFT_KAKKO'}
    return token, index + 1

def read_right_kakko(line, index):
    token = {'type': 'RIGHT_KAKKO'}
    return token, index + 1

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_multiply(line, index)
        elif line[index] == '/':
            (token, index) = read_divide(line, index)
        elif line[index] == '(':
            (token, index) = read_left_kakko(line, index)
        elif line[index] == ')':
            (token, index) = read_right_kakko(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def evaluate(tokens):

    def evaluate_1(tokens):
        new_tokens = []
        index = 0
        while index < len(tokens):
            if tokens[index]['type'] == 'MULTIPLY':
                new_tokens[-1]['number'] = new_tokens[-1]['number'] * tokens[index + 1]['number']
                index += 2
            elif tokens[index]['type'] == 'DIVIDE':
                new_tokens[-1]['number'] = new_tokens[-1]['number'] / tokens[index + 1]['number']
                index += 2
            else:
                new_tokens.append(tokens[index])
                index += 1
        return new_tokens

    def evaluate_2(tokens):
        answer = 0
        tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
        index = 1
        while index < len(tokens):
            if tokens[index]['type'] == 'NUMBER':
                if tokens[index - 1]['type'] == 'PLUS':
                    answer += tokens[index]['number']
                elif tokens[index - 1]['type'] == 'MINUS':
                    answer -= tokens[index]['number']
            index += 1
        return answer
    
    def get_kakko_tokens(tokens, index):
        kakko_tokens = []
        while index < len(tokens):
            if tokens[index]['type'] == 'RIGHT_KAKKO':
                break
            else:
                kakko_tokens.append(tokens[index])
                index += 1
        return kakko_tokens

    new_tokens = []
    index = 0
    while tokens[index] < len(tokens):
        if tokens[index]['type'] == 'LEFT_KAKKO':
            if tokens[index+1:]['type'] != 'LEFT_KAKKO':

            else:
                new_tokens.append(tokens[index])
        else:
            new_tokens.append(tokens[index])
        index += 1

    return answer


def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("3.0+4*2-1/5")
    test("(3.0+4.0*(2-1))/5")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
