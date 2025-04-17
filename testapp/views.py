from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage, get_connection, EmailMultiAlternatives, send_mail, send_mass_mail
from django.template.loader import render_to_string


def test_cookie(request):
    # if request.method == 'POST':
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        print('Test cookie deleted')
        messages.success(request, "Test cookie was deleted.")

    else:
        print('Test cookie not deleted')
        messages.warning(request, "Test cookie did not work")

    request.session.set_test_cookie()
    return render(request, 'testapp/test_cookie.html')





def email(request):
    #em = EmailMessage(subject="Test", body="Test", to=['user@domain.kz'])
    # em.send()

    # var 1

    # em = EmailMessage(subject="Ваш новый пароль",
    #                   body="Ваш новый пароль тут",
    #                   attachments=[('password.txt', '12345678', 'text/plain')],
    #                   to=['user@domain.kz'])
    #
    # em.send()

    # var 2
    # em = EmailMessage(subject="Запрошенный вами файл",
    #                   body="Получите Запрошенный вами файл",
    #                   to=['user@domain.kz'])
    #
    # em.attach_file(r'C:\work\file.txt')
    # em.send()



    #var 3
    # context = {'user': "asd"}
    # s = render_to_string('email/letter.txt', context)
    #
    # em = EmailMessage(subject='Оповещение', body=s, to=['asd@domain.kz'])
    #
    # em.send()

    #var4

    # con = get_connection()
    # con.open()
    #
    # em1 = EmailMessage(subject="Запрошенный вами файл",
    #                   body="Получите Запрошенный вами файл",
    #                   to=['user@domain.kz'],
    #                   connection=con)
    # em1.send()
    #
    # em2 = EmailMessage(subject="Запрошенный вами файл",
    #                    body="Получите Запрошенный вами файл",
    #                    to=['user@domain.kz'],
    #                    connection=con)
    # em2.send()
    #
    # con.close()


    # var5
    # con = get_connection()
    # con.open()
    # em1 = EmailMessage(...)
    # em2 = EmailMessage(...)
    # em3 = EmailMessage(...)
    # con.send_messages([em1, em2, em3])
    # con.close()

    # em = EmailMultiAlternatives(subject='Test',
    #                             body='Test',
    #                             to=['user@supersite.kz'])
    #
    # em.attach_alternative('<h1>Test</h1>', 'text/html')
    # em.send()


    ###Высокоуровневые###
    #var1
    # send_mail('Test mail', 'Test!!!', 'webmaster@supersite.kz',
    #         ['user@othersite.kz'], html_message='<h1>Test!!!</h1>')

    # msg1 = ('Подписка', 'asd',
    #         'sub@sub.kz',
    #         ['user@othersite.kz', 'user@othersite.kz'])
    #
    # msg2 = ('Подписка', 'asd',
    #         'sub@sub.kz',
    #         ['user@othersite.kz', 'user@othersite.kz'])
    #
    # send_mass_mail((msg1, msg2))

    return render(request, 'testapp/test_cookie.html')



