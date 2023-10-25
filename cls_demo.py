import collections
import inspect

def make_oneline(string):
    return string.replace('\n ', ' ').replace('\n', ' ').strip()

demo1 = """
But I must explain to you how all this mistaken idea of denouncing pleasure 
and praising pain was born and I will give you a complete account of the 
system, and expound the actual teachings of the great explorer of the truth, 
the master-builder of human happiness. No one rejects, dislikes, or avoids 
pleasure itself, because it is pleasure, but because those who do not know 
how to pursue pleasure rationally encounter consequences that are extremely 
painful. Nor again is there anyone who loves or pursues or desires to obtain 
pain of itself, because it is pain, but because occasionally circumstances 
occur in which toil and pain can procure him some great pleasure. To take a 
trivial example, which of us ever undertakes laborious physical exercise, 
except to obtain some advantage from it? But who has any right to find fault 
with a man who chooses to enjoy a pleasure that has no annoying 
consequences, or one who avoids a pain that produces no resultant pleasure?
"""
demo2 = """
O lovely maidens, fall in love,
But not with Muscovites [2],
For Muscovites are foreign folk,
They do not treat you right.
A Muscovite will love for sport,
And laughing go away;
He’ll go back to his Moscow land 
And leave the maid a prey 
To grief and shame... 
"""
a = int(input("What text do you want to check? "))

def symbols_count(txt):
    """Build mapping counting number of entries of each symbol.

    ...
    """
    syms = set(txt)
    res = dict()
    for sym in sorted(syms):
        res[sym] = txt.count(sym)
    return res
    # or
    # return {sym: txt.count(sym) for sym in sorted(set(txt))}

def count_characters_in_code():
    code = inspect.getsource(inspect.currentframe())
    character_counter = collections.Counter(code)
    return character_counter

class Text:
    def __init__(self, obj=''):
        self.str = str(obj)
        self.oneline = make_oneline(self.str)

    def __repr__(self):
        lim = self.oneline[:16]
        ext = '...' if len(self.oneline) > 16 else ''
        return f'{type(self).__name__}({repr(lim)}{ext})'

    def __str__(self):
        return self.str

    def symbols_count(self):
        """... same as above ..."""
        return {sym: self.oneline.count(sym)
                for sym in sorted(set(self.oneline))}
    

if a == 1:

    text1 = Text(demo1)
    print(text1)
    symbol_count = text1.symbols_count()
    print(symbol_count)
elif a == 2:
    text2 = Text(demo2)
    print(text2)
    symbol_count = text2.symbols_count()
    print(symbol_count)
elif a == 3:
        code_character_count = count_characters_in_code()
        print("Number of characters in the program code:")
        for char, count in code_character_count.items():
            print(f"'{char}': {count}")
else:
    print("You entered something wrong")



