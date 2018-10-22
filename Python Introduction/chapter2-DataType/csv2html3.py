import sys
import xml.sax.saxutils

def main():
    maxwidth, format = process_options()
    if maxwidth is not None:
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth)
                count += 1
            except EOFError:
                break
        print_end()

def process_options():
    maxwidth = 100
    format = ".0f"
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
            print("usage: {0} [maxwidth:int] [format:str] < infile.csv > outfile.html".format(sys.argv[0]))
            #print("usage: {0[0]} [string]".format(sys.argv))
            print("\nmaxwidth é uma integer opcional; se especificado, configura o " +
                  "número máximo de caracteres que podem entrar no campo da string, " +
                  "do contrário, o padrão de 100 caracteres é usado.")
            print("\nformat é o formatação usada para números; se não especificado o padrão é \".0f\".")
        #elif sys.argv[sys.argv[1].index(" ")+1:sys.argv[1].index(" ")+9] == "maxwidth":
        elif sys.argv[1][:9] == "maxwidth=" or sys.argv[2][:9] == "maxwidth=":
            try:
                maxwidth = int(sys.argv[1][sys.argv[1].index("=")+1:])
            except ValueError as err:
                pass
        elif sys.argv[1][:7] == "format=" or sys.argv[2][:7] == "format=":
            format = str(sys.argv[1][sys.argv[1].index("=")+1:])
        else:
            return maxwidth, format
    return maxwidth, format

def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth):
    print("<tr bgcolor='{0}'>".format(color))
    numberFormat = "<td align='right'>{{0:{0}}}</td>".format(format)
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print(numberFormat.format(x))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(
                            xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")

def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None: # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c    # other quote inside quoted string
            continue
        if quote is None and c == ",": # end of a field
            fields.append(field)
            field = ""
        else:
            field += c        # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


'''def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text
'''

def print_end():
    print("</table>")

main()
