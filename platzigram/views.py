from django.http import HttpResponse, JsonResponse
from datetime import datetime

def hello_world(request):
    #now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi" Current server time is {}'.format(
        datetime.now().strftime('%b %dth, %Y - %H:%M hrs')    
    ))
    #return HttpResponse('Oh, hi" Current server time is {}'.format(str(now)))
    
def sorted_integers(request):      
      #numbers = request.GET['numbers'].split(',')
      #numbers_in_list = [int(num) for num in request.GET['numbers'].split(',')]
      sorted_numbers = sorted([int(num) for num in request.GET['numbers'].split(',')])
      #sorted_numbers = sorted(numbers_in_list)
      #import pdb; pdb.set_trace()
      return JsonResponse({ "sorted_numbers": sorted_numbers })

def say_hi(request, name, age):
      if age < 12:
            message = 'Sorry {}, you are not allowed here'.format(name)
      else:
            message = '{} welcome to Platzigram'.format(name)
      
      return HttpResponse(message)