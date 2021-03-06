"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from qa import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.new_questions, name='new-questions'),
    url(r'^login/$', views.login_user),
    url(r'^signup/$', views.signup_user),
    url(r'^question/(?P<id>\d+)/$', views.question_answers, name='question-answers'),
    url(r'^ask/$', views.question_add, name='question-add'),
    url(r'^popular/$', views.popular_questions, name='popular-questions'),
    url(r'^new/$', views.test),
]
