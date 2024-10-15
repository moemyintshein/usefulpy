from googletrans import Translator
import os

while True:
    # Create a Translator object.
    translator = Translator()
    words = input("From detect language: ")
    country_code = input("To language(Burmese-my/Thailand-th): ")
    tran_text = translator.translate(words, dest=country_code).text
    os.system('clear')
    print(f"From  > %s" % words)
    print(f"To {country_code} > {tran_text}\n")