# 18. ornekteki kodu test etmek icin, verdigimiz harfleri rastgele
# kullanarak bizim belirledigimiz uzunlukta bir string uretecek
import random
from example_18 import consecutive_repeat_1, consecutive_repeat_2

letters = ["a", "b", "c"]
str_length = 10000000

output_str = ""
for _ in range(str_length):
    selected_index = random.randint(0, len(letters) - 1)
    output_str += letters[selected_index]

print(consecutive_repeat_1(output_str))
print(consecutive_repeat_2(output_str))