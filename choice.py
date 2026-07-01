def choice(text):
    choice = int(input(text))
    return choice

def choicerandom(items):
    index = id(items) % len(items)
    return items[index]

def choicebiggest(numbers):
    return max(numbers)

def choicesmallest(numbers):
    return min(numbers)

def choiceeven(numbers):
    return [x for x in numbers if x % 2 == 0]

def choiceodd(numbers):
    return [x for x in numbers if x % 2 != 0]

def choicesum(numbers):
    return sum(numbers)

def choiceaverage(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def choicemedian(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid-1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def choicemode(numbers):
    return max(set(numbers), key=numbers.count)

def choiceunique(numbers):
    return list(set(numbers))

def choicelongest(strings):
    return max(strings, key=len)

def choiceshortest(strings):
    return min(strings, key=len)

def choicecapitalized(strings):
    return [s for s in strings if s and s[0].isupper()]

def choicecontains(strings, letter):
    return [s for s in strings if letter in s]

def choicepalindromes(strings):
    return [s for s in strings if s == s[::-1]]

def choiceprime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [x for x in numbers if is_prime(x)]

def choicebetween(numbers, low, high):
    return [x for x in numbers if low <= x <= high]

def choiceduplicates(numbers):
    return [x for x in set(numbers) if numbers.count(x) > 1]

def choicesorted(numbers, reverse=False):
    return sorted(numbers, reverse=reverse)

def choicerange(start, end, step=1):
    return list(range(start, end, step))

def choicegreater_than(numbers, threshold):
    return [x for x in numbers if x > threshold]

def choiceless_than(numbers, threshold):
    return [x for x in numbers if x < threshold]

def choiceequal_to(numbers, value):
    return [x for x in numbers if x == value]

def choiceclosest(numbers, target):
    return min(numbers, key=lambda x: abs(x - target))

def choicedifference(numbers):
    return max(numbers) - min(numbers)
def choicefactorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def choicegcd(a, b):
    while b:
        a, b = b, a % b
    return a

def choicelcm(a, b):
    return abs(a * b) // choicegcd(a, b)

def choiceanagrams(words):
    result = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                result.append((words[i], words[j]))
    return result

def choiceremove_duplicates(text):
    return ''.join(dict.fromkeys(text))

def choicecolor():
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

def choiceuuid():
    import uuid
    return str(uuid.uuid4())

def choiceshuffle(items):
    import random
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled

def choicerotate(items, steps=1):
    if not items:
        return []
    steps = steps % len(items)
    return items[-steps:] + items[:-steps]

def choicechunk(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]

def choiceflatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(choiceflatten(item))
        else:
            result.append(item)
    return result

def choiceis_email(text):
    return "@" in text and "." in text

def choiceis_phone(text):
    digits = ''.join(filter(str.isdigit, text))
    return len(digits) >= 10 and len(digits) <= 15

def choiceis_url(text):
    return text.startswith("http://") or text.startswith("https://")

def choiceclean_text(text):
    return ' '.join(text.split())

def choicecount_words(text):
    return len(text.split())

def choicefind_duplicates(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def choicehelp():
    print("Commands:")
    print("choicebiggest")
    print("choicesmallest")
    print("choiceeven")
    print("choiceodd")
    print("choicesum")
    print("choiceaverage")
    print("choicemedian")
    print("choicemode")
    print("choicerange")
    print("choicefactorial")
    print("choicegcd")
    print("choicelcm")
    print("choicelongest")
    print("choiceshortest")
    print("choicecapitalized")
    print("choicecontains")
    print("choicepalindromes")
    print("choiceanagrams")
    print("choiceremove_duplicates")
    print("choicerandom")
    print("choicecolor")
    print("choiceuuid")
    print("choiceshuffle")
    print("choicerotate")
    print("choicechunk")
    print("choiceflatten")
    print("choiceis_email")
    print("choiceis_phone")
    print("choiceis_url")
    print("choiceclean_text")
    print("choicecount_words")
    print("choicefind_duplicates")