import pyperclip
from googletrans import Translator
import time

translator = Translator()

oldText = pyperclip.paste()

while True:
    try:
        language = input('Введите язык на который хотите переводить скопированный текст(en, ru и тд.): ')
        
        check = translator.translate(oldText, dest=language)
        
        print('Программа запущена, можете копировать и при вставке получать перевод')
        
        break
    except:
        print('Нету такого языка, введите заново')

while True:
    time.sleep(0.25)
    newText = pyperclip.paste()
    if newText != oldText:
        result = translator.translate(newText, dest=language)
        pyperclip.copy(result.text)
        oldText = result.text
