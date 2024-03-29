import sys
Zero = ["   ***   ", " *     * ", "*       *", "*       *", "*       *", " *     * ", "   ***   "]
One = [" * ", "** ", " * "," * "," * "," * ","***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = ["***** ", "     *", "    * ", "***   ", "    * ", "     *", "***** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "****  ", "    *", "    *", "**** "]
Six = ["*    ", "*    ", "*    ", "**** ", "*   *", "*   *", "**** "]
Seven = ["*****", "    * ", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    #digits = sys.argv[1]
    digits = input("Digite um número: ")
    row = 0
    while row < 7:
        line = ""
        column = 0
        nova = ""
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for char in digit[row]:
                if char == "*":
                    nova += str(number)
                else:
                    nova += " "
            line += nova + " "
            column += 1
            nova = ""
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)