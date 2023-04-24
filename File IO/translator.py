
from translate import Translator
translator = Translator(to_lang= 'ja')

try:
    with open('./text_for_translation.txt', encoding='UTF-8') as my_file:
        txt_to_scan = my_file.read()
        translation = translator.translate(txt_to_scan)
        print(translation)
        with open('./translated.txt', mode='w', encoding='UTF-8') as my_file2:
            my_file2.write(translation)
except:
    print('error occured')

