from django.shortcuts import render
from django.contrib import messages
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



