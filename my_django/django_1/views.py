import logging
from django.http import HttpResponse

def index(request):
    logging.info("User visited the home page")
    html = """
        <h1>Добро пожаловать на мой первый Django сайт!</h1>
        <h1>Welcome to my first Django site!</h1>

        <p>Здесь вы можете найти информацию о моем первом проекте Django.</p>
        <p>Here you might find information about my first Django project.</p>
    """
    return HttpResponse(html)

def about(request):
    logging.info("The user visited the about page")
    html = """
        <h1>Обо мне</h1>
        <h1>About me</h1>

        <p>Привет, меня зовут Yury, и я создал этот сайт с помощью Django.</p>
        <p>Hi, my name is Yury and I created this website using Django.</p>
    """
    return HttpResponse(html)
