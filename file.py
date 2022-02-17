import random
import string

alph  = string.ascii_lowercase
numbers  = [str(n) for n in range (10)]
all = alph+ "".join(numbers)
password = "".join(random.sample(all,10))
print(f"New password:{password}")