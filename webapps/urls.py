from django.contrib import admin
from django.urls import path

import helloweb.views as helloweb_views
import emaillist.views as emaillist_views
import guestbook.views as guestbook_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloweb/hello', helloweb_views.hello),   # 실행이 아니기 때문에 hello() 안씀
    path('helloweb/tags', helloweb_views.tags),
    path('helloweb/join', helloweb_views.join),


    path('emaillist/', emaillist_views.index),
    path('emaillist/form', emaillist_views.form),
    path('emaillist/add', emaillist_views.add),


    path('guestbook/', guestbook_views.index),
    path('guestbook/deleteform', guestbook_views.deleteform),
    path('guestbook/add', guestbook_views.add),
    path('guestbook/delete', guestbook_views.delete),

]
