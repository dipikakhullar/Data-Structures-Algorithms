def solution(A):
    # write your code in Python 3.6
    valid_words = delete_internal_duplicates(A)
    print(valid_words)
    word_sets = []
    for word in valid_words:
        word_set = set(word)
        word_sets.append(word_set)

    power_set = subsets(valid_words)
    print("power set:  ", power_set)
    output = delete_internal_duplicates(power_set)
    max_concat = 0
    for word in output:
        if len(word) > max_concat:
            max_concat = len(word)
    return max_concat


def subsets(valid_words):
    output = [""]
    for n in (valid_words):
        subs_with_n = []
        for subset in output:
            new_subset = subset + n
            subs_with_n.append(new_subset)
        output.extend(subs_with_n)
    return output

    # return 5
    

def delete_internal_duplicates(arr):
    output = []
    for word in arr:
        seen = set()
        contains_duplicates = False
        for letter in word:
            if letter in seen:
                contains_duplicates = True
                break
            else:
                # print(seen)
                seen.add(letter)
        if not contains_duplicates:
            output.append(word)
    return output

# a = ['eva', 'jqw', 'tyn', 'jan']
# solution = solution(a)
# print(solution)


def n_k(N, K):
    if N == 0:
        return [""]
    result = []
    for p in n_k(N - 1, K - 1):
        for l in 'abc':
            if p[-1:] != l:
                result += [p + l]
    return result[:K]


s = n_k(0,0)
print(s)