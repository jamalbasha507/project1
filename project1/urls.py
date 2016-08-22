from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'application.views.index'),
    
    # url(r'^idea/','application.views.jamal')

    # url(r'^idea/','application.views.cal'),
    # # url(r'^calender/','application.views.cal'),
    # url(r'^home1/','application.views.sign_up')
    # url(r'^abc/','application.views.login'),
    # url(r'^basha/', 'application.views.jamal'),
    # url(r'^sign_up/','Products.views.sign_up'),
    # url(r'^sign_up_user/','Products.views.sign_up_user'),
    # url(r'^test_login/','Products.views.test_login'),

]