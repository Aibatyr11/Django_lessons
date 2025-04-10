from django.shortcuts import render

def test_cookie(request):
    # if request.method == 'POST':
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        print('Test cookie deleted')

    else:
        print('Test cookie not deleted')

    request.session.set_test_cookie()
    return render(request, 'testapp/test_cookie.html')
