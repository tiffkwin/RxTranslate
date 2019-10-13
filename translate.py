# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

def trans( input2, language):
    print(u'Text: \n{}\n'.format(input2))
    translation2 = translate_client.translate(input2,target_language=language)
    print(u'Translation: \n{}\n'.format(translation2['translatedText']))

# trans('hello,world', 'es')

#
# The text to translate
#text = u'Hello, world!'
# The target language
#target = 'ru'
#target2 = 'es'

# Translates some text into Russian
#translation = translate_client.translate(
#    text,
#    target_language=target)

#translate2 = translate_client.translate(text, target_language=target2)

#print(u'Text: {}'.format(text))
#print(u'Translation: {}'.format(translation['translatedText']))
#print(u'Translation: {}'.format(translate2['translatedText']))


