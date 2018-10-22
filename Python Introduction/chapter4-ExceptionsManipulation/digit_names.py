import sys

Language = "en"

ENGLISH = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
PORTUGUESE = {0:"zero",1:"um",2:"dois",3:"três",4:"quatro",5:"cinco",6:"seis",7:"sete",8:"oito",9:"nove"}

def print_digits(digits):
    dictionary = ENGLISH if Language == "en" else PORTUGUESE
    for digit in digits:
        print(dictionary[int(digit)], end=" ")
    print()

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} [en|pt] number".format(sys.argv[0]))
        sys.exit()
    args = sys.argv[1:]
    if args[0] in {"en", "pt"}:
        global Language
        Language = args.pop(0)
    print_digits(args.pop(0))

main()
