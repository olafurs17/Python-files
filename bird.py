'''
REmember: The , character after our print statement means that our next print 
statement keeps printing on the same line. Let's filter out the letter 'A' 
from our string.

phrase = "A bird in the hand..."
Do the following for each character in the phrase.
If char is an 'A' or char is an 'a', print 'X', instead of char. Make sure to 
include the trailing comma.
Otherwise (else:), please print char, with the trailing comma.
'''
phrase = "A bird in the hand..."
for char in phrase:
    if char __ 'A' or char == 'a':
        print 'X',
    else:
        print char,