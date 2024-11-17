def send_email(message, recipient, *, sender="university.help@gmail.com"):
    r_tail = False
    s_tail = False
    tails = ('@', '.com', '.ru', '.net')
    for domen in tails:
        if domen == '@':
            if not ('@' in recipient) or not ('@' in sender):
                return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        else:
            str_rec = recipient[len(recipient) - len(domen):]
            str_send = sender[len(sender) - len(domen):]
            if domen == str_rec:
                r_tail = True
            if domen == str_send:
                s_tail = True
    if not r_tail or not s_tail:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if sender == recipient:
        return print('Нельзя отправить письмо самому себе!')
    if sender == 'university.help@gmail.com':
        return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
