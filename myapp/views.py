from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Inex page accessed')
    return HttpResponse("Hello world")

def index2(request):
    try:
        result = 1/0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse(f'Oops, something went wrong')
    else:
        logger.debug('About page accesed')
        return HttpResponse('This is about page')


# Create your views here.
