"""the best fizzbuzz in the world nothing can compete dont even bother"""
words = {
    3: "\033[94mFizz\033[0m",
    5: "\033[93mBuzz\033[0m",
}
for n in range(100):
    prod = "".join(v for k, v in words.items() if n % k == 0)
    print(prod if len(prod) > 0 else n)
