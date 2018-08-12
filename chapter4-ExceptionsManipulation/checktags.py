class InvalidEntityError(Exception): pass
class InvalidNumericEntityError(InvalidEntityException): pass
class InvalidAlphaEntityError(InvalidEntityException): pass
class InvalidTagContentError(Exception): pass

fh = None
try:
    fh = open(filename, encoding="utf8")
    errors = False
    for lino, line in enumerate(fh, start=1):
        for column, c in enumerate(line, start=1):
            try: