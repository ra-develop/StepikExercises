base_string = ' abcdefghijklmnopqrstuvwxyz'
input_phrase = ''
output_phrase = ''
while True:
    try:
        secure_key = int(input())
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
while True:
    input_phrase = input()
    if input_phrase:
        break
    else:
        print("Oops!  That was no valid phrase.  Try again...")

input_phrase = input_phrase.strip()
# input_phrase=input_phrase.lstrip()
# input_phrase=input_phrase.rstrip()

for i in range(len(input_phrase)):
    change_chr = input_phrase[i]
    shift = base_string.find(change_chr)+secure_key
    # if shift<28:
    #     shift=(27-shift%27)*-1
    if shift >= 27:
        shift = shift % 27
    else:
        shift = (27-shift % 27)*-1
    output_phrase += base_string[shift]
print('Result: "'+output_phrase+'"')
