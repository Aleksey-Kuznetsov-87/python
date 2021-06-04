import re

email_parse = ['someone@geekbrains.ru']
RE_EMAIL = re.compile(r'\w+[a-z]\@\w+[a-z].\w+[.*\b]')
for meaning_p in email_parse:
    assert RE_EMAIL.match(meaning_p), f'ошибка в {meaning_p}'
else:
    print("зе бест мыло!")
    RE_GET_PARSER = re.compile(r'(?P<username>\w+)@(?P<domain>\w+(.*\b))')
    print(*map(lambda x: x.groupdict(), RE_GET_PARSER.finditer(*email_parse)), sep=', ')
