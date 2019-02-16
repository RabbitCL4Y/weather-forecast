import random
import sys
import time
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
mengetik('EXIT IN MY TOOLS')
mengetik('Follow Me On The Social Media')
mengetik('My Github     : https://github.com/RabbitCL4Y')
mengetik('My Instagram  : https://www.instagram.com/muhammadrafli_337')
mengetik('Contact Me    : RabbitCL4Y123@gmail.com')
mengetik('Every successful person must have a failure. Do not be afraid to fail because failureis a part of success')

