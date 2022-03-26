#Пример локализации для Ивана
import locale
import gettext
def setlocale(loc=None):
	if loc is None:
		l = locale.getdefaultlocale()[0]
	else:
		l = loc
	lc = gettext.translation('base', localedir='locales', languages=[l])
	lc.install()
	return lc.gettext, lc.ngettext
	# _ = lc.gettext
	# ngettext = lc.ngettext

def print_hello():

    return _("Привет мир!\nИван лучший архитектор проектов в мире!\nА меня зовут Арнольд")

def print_formatted(num, ngettext):

    return ngettext("У меня {0} яблоко", "У меня {0} яблок" , num).format(num)

if __name__=='__main__':
    _, ngettext = setlocale('uk')
    print(print_hello())
    print(print_formatted(1, ngettext))
    print(print_formatted(5, ngettext))
