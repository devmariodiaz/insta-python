#from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

posts = [
      {
         'title': 'Mont Blanc',
         'user':{
               'name':'Yesica Cortés',
               'picture': 'https://i.picsum.photos/id/1027/60/60.jpg'
          },
         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
         'photo': 'https://i.picsum.photos/id/1036/200/200.jpg'
      },
      {
         'title': 'Via Lactea',
         'user':{
               'name': 'C. Vander',
               'picture': 'https://i.picsum.photos/id/1005/60/60.jpg'
          },
         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
         'photo': 'https://i.picsum.photos/id/903/200/200.jpg'
      },
      {
         'title': 'Nuevo Auditorio',
         'user': {
               'name': 'Thespianarist',
               'picture': 'https://i.picsum.photos/id/883/60/60.jpg'
          },
         'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
         'photo': 'https://i.picsum.photos/id/1076/200/200.jpg'
      },
]

def list_posts(request):
      return render(request, 'feed.html', { 'posts': posts})

      
#def list_posts(request):
#           content = []
#           
#           for post in posts:
#                  content.append("""
#                              <p><strong>{name}</strong></p>
#                              <p><small>{user} - <i>{timestamp}</i></small></p>
#                              <figure><img src="{picture}" /></figure>
#                              """.format(**post))
#            return HttpResponse('<br />'.join(content))
#      """