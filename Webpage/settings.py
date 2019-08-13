Last login: Tue Jul 30 13:22:44 on ttys000
Jonathans-MacBook-Pro:webpage2 jonathanposo$ ls
Webpage			db.sqlite3		node_modules		requirements.txt
apps			manage.py		package-lock.json
Jonathans-MacBook-Pro:webpage2 jonathanposo$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
July 30, 2019 - 21:03:11
Django version 1.10, using settings 'Webpage.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[30/Jul/2019 21:03:26] "GET / HTTP/1.1" 200 16684
[30/Jul/2019 21:03:26] "GET /static/personal_page/vendor/fontawesome-free/css/all.min.css HTTP/1.1" 200 54456
[30/Jul/2019 21:03:26] "GET /static/personal_page/vendor/jquery/jquery.min.js HTTP/1.1" 200 86927
[30/Jul/2019 21:03:26] "GET /static/personal_page/python.png HTTP/1.1" 200 14934
[30/Jul/2019 21:03:26] "GET /static/personal_page/vendor/jquery-easing/jquery.easing.min.js HTTP/1.1" 200 2532
[30/Jul/2019 21:03:26] "GET /static/personal_page/js/resume.min.js HTTP/1.1" 200 738
[30/Jul/2019 21:03:26] "GET /static/personal_page/img/me.jpeg HTTP/1.1" 200 270483
[30/Jul/2019 21:03:26] "GET /static/personal_page/vendor/bootstrap/js/bootstrap.bundle.min.js HTTP/1.1" 200 78635
[30/Jul/2019 21:03:26] "GET /static/personal_page/vendor/bootstrap/css/bootstrap.min.css HTTP/1.1" 200 155760
[30/Jul/2019 21:03:26] "GET /static/personal_page/resume.min.css HTTP/1.1" 200 3223
[30/Jul/2019 21:03:26] "GET /static/personal_page/django.png HTTP/1.1" 200 13646
[30/Jul/2019 21:03:26] "GET /static/personal_page/resume-icon.png HTTP/1.1" 200 3758
[30/Jul/2019 21:03:26] "GET /static/personal_page/JavaScript-logo.png HTTP/1.1" 200 11088
[30/Jul/2019 21:03:26] "GET /static/personal_page/html.png HTTP/1.1" 200 9955
[30/Jul/2019 21:03:26] "GET /static/personal_page/mySQL.png HTTP/1.1" 200 17267
[30/Jul/2019 21:03:26] "GET /static/personal_page/flask.png HTTP/1.1" 200 8768
[30/Jul/2019 21:03:26] "GET /static/personal_page/bootstrap-logo.png HTTP/1.1" 200 22154
[30/Jul/2019 21:03:26] "GET /static/personal_page/fire.png HTTP/1.1" 200 11915
[30/Jul/2019 21:03:26] "GET /static/personal_page/iOS.png HTTP/1.1" 200 7050
[30/Jul/2019 21:03:26] "GET /static/personal_page/git.png HTTP/1.1" 200 12913
[30/Jul/2019 21:03:26] "GET /static/personal_page/materialize.png HTTP/1.1" 200 18828
[30/Jul/2019 21:03:26] "GET /static/personal_page/github.png HTTP/1.1" 200 6568
[30/Jul/2019 21:03:26] "GET /static/personal_page/mongoDB.png HTTP/1.1" 200 18575
[30/Jul/2019 21:03:26] "GET /static/personal_page/node.png HTTP/1.1" 200 13850
[30/Jul/2019 21:03:26] "GET /static/personal_page/postgresql-logo.png HTTP/1.1" 200 16816
[30/Jul/2019 21:03:26] "GET /static/personal_page/swift.png HTTP/1.1" 200 12017
[30/Jul/2019 21:03:26] "GET /static/personal_page/squile.png HTTP/1.1" 200 19770
[30/Jul/2019 21:03:26] "GET /static/personal_page/typescript.png HTTP/1.1" 200 10597
[30/Jul/2019 21:03:26] "GET /static/personal_page/ruby.png HTTP/1.1" 200 18870
[30/Jul/2019 21:03:26] "GET /static/personal_page/angular.png HTTP/1.1" 200 13080
[30/Jul/2019 21:03:26] "GET /static/personal_page/amazon.png HTTP/1.1" 200 12429
[30/Jul/2019 21:03:26] "GET /static/personal_page/json.png HTTP/1.1" 200 71492
[30/Jul/2019 21:03:26] "GET /static/personal_page/vendor/fontawesome-free/webfonts/fa-brands-400.woff2 HTTP/1.1" 200 72112
[30/Jul/2019 21:03:26] "GET /static/personal_page/vendor/fontawesome-free/webfonts/fa-solid-900.woff2 HTTP/1.1" 200 74348
[30/Jul/2019 21:03:26] "GET /static/personal_page/vendor/fontawesome-free/webfonts/fa-regular-400.woff2 HTTP/1.1" 200 13592
[30/Jul/2019 21:04:59] "GET / HTTP/1.1" 200 16684
Not Found: /accomodations
[30/Jul/2019 21:05:01] "GET /accomodations HTTP/1.1" 404 2762
[30/Jul/2019 21:05:01] "GET /admin HTTP/1.1" 200 5232
Not Found: /favicon.ico
[30/Jul/2019 21:05:01] "GET /favicon.ico HTTP/1.1" 404 2756
test INFO #1
asdasd
asdasfdsfa
[30/Jul/2019 21:05:12] "POST /run HTTP/1.1" 302 0
[30/Jul/2019 21:05:12] "GET /admin HTTP/1.1" 200 5232
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x10c1fcb18>
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Library/Python/2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Library/Python/2.7/site-packages/django/core/management/base.py", line 385, in check
    include_deployment_checks=include_deployment_checks,
  File "/Library/Python/2.7/site-packages/django/core/management/base.py", line 372, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Library/Python/2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Library/Python/2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Library/Python/2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Library/Python/2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Library/Python/2.7/site-packages/django/urls/resolvers.py", line 310, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Library/Python/2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Library/Python/2.7/site-packages/django/urls/resolvers.py", line 303, in urlconf_module
    return import_module(self.urlconf_name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/jonathanposo/Desktop/Code/my_environments/Webpage2/Webpage/urls.py", line 20, in <module>
    url(r'^', include('apps.personal_page.urls')),
  File "/Library/Python/2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/jonathanposo/Desktop/Code/my_environments/Webpage2/apps/personal_page/urls.py", line 9, in <module>
    url(r'^portfolio$', views.portolfio),
AttributeError: 'module' object has no attribute 'portolfio'
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x1036e5b18>
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Library/Python/2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Library/Python/2.7/site-packages/django/core/management/base.py", line 385, in check
    include_deployment_checks=include_deployment_checks,
  File "/Library/Python/2.7/site-packages/django/core/management/base.py", line 372, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Library/Python/2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Library/Python/2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Library/Python/2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Library/Python/2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Library/Python/2.7/site-packages/django/urls/resolvers.py", line 310, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Library/Python/2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Library/Python/2.7/site-packages/django/urls/resolvers.py", line 303, in urlconf_module
    return import_module(self.urlconf_name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/jonathanposo/Desktop/Code/my_environments/Webpage2/Webpage/urls.py", line 20, in <module>
    url(r'^', include('apps.personal_page.urls')),
  File "/Library/Python/2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/jonathanposo/Desktop/Code/my_environments/Webpage2/apps/personal_page/urls.py", line 9, in <module>
    url(r'^portfolio$', views.portolfio),
AttributeError: 'module' object has no attribute 'portolfio'
Performing system checks...

Unhandled exception in thread started by <function wrapper at 0x104656b18>
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/Library/Python/2.7/site-packages/django/core/management/commands/runserver.py", line 121, in inner_run
    self.check(display_num_errors=True)
  File "/Library/Python/2.7/site-packages/django/core/management/base.py", line 385, in check
    include_deployment_checks=include_deployment_checks,
  File "/Library/Python/2.7/site-packages/django/core/management/base.py", line 372, in _run_checks
    return checks.run_checks(**kwargs)
  File "/Library/Python/2.7/site-packages/django/core/checks/registry.py", line 81, in run_checks
    new_errors = check(app_configs=app_configs)
  File "/Library/Python/2.7/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/Library/Python/2.7/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    for pattern in resolver.url_patterns:
  File "/Library/Python/2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Library/Python/2.7/site-packages/django/urls/resolvers.py", line 310, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "/Library/Python/2.7/site-packages/django/utils/functional.py", line 35, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "/Library/Python/2.7/site-packages/django/urls/resolvers.py", line 303, in urlconf_module
    return import_module(self.urlconf_name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/jonathanposo/Desktop/Code/my_environments/Webpage2/Webpage/urls.py", line 20, in <module>
    url(r'^', include('apps.personal_page.urls')),
  File "/Library/Python/2.7/site-packages/django/conf/urls/__init__.py", line 50, in include
    urlconf_module = import_module(urlconf_module)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/Users/jonathanposo/Desktop/Code/my_environments/Webpage2/apps/personal_page/urls.py", line 9, in <module>
    url(r'^portfolio$', views.portolfio),
AttributeError: 'module' object has no attribute 'portolfio'
Performing system checks...

System check identified no issues (0 silenced).
July 30, 2019 - 21:12:43
Django version 1.10, using settings 'Webpage.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[30/Jul/2019 21:12:50] "GET / HTTP/1.1" 200 16702
^CJonathans-MacBook-Pro:webpage2 jonathanposo$ ls
Webpage			node_modules
apps			package-lock.json
db.sqlite3		requirements.txt
manage.py
Jonathans-MacBook-Pro:webpage2 jonathanposo$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
August 13, 2019 - 19:15:06
Django version 1.10, using settings 'Webpage.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[13/Aug/2019 19:20:13] "GET / HTTP/1.1" 200 16702
[13/Aug/2019 19:20:13] "GET /static/personal_page/resume.min.css HTTP/1.1" 200 3223
[13/Aug/2019 19:20:13] "GET /static/personal_page/python.png HTTP/1.1" 200 14934
[13/Aug/2019 19:20:13] "GET /static/personal_page/bootstrap-logo.png HTTP/1.1" 200 22154
[13/Aug/2019 19:20:13] "GET /static/personal_page/vendor/jquery-easing/jquery.easing.min.js HTTP/1.1" 200 2532
[13/Aug/2019 19:20:13] "GET /static/personal_page/html.png HTTP/1.1" 200 9955
[13/Aug/2019 19:20:13] "GET /static/personal_page/fire.png HTTP/1.1" 200 11915
[13/Aug/2019 19:20:13] "GET /static/personal_page/resume-icon.png HTTP/1.1" 200 3758
[13/Aug/2019 19:20:13] "GET /static/personal_page/img/me.jpeg HTTP/1.1" 200 270483
[13/Aug/2019 19:20:13] "GET /static/personal_page/vendor/bootstrap/css/bootstrap.min.css HTTP/1.1" 200 155760
[13/Aug/2019 19:20:13] "GET /static/personal_page/swift.png HTTP/1.1" 200 12017
[13/Aug/2019 19:20:13] "GET /static/personal_page/github.png HTTP/1.1" 200 6568
[13/Aug/2019 19:20:13] "GET /static/personal_page/git.png HTTP/1.1" 200 12913
[13/Aug/2019 19:20:13] "GET /static/personal_page/squile.png HTTP/1.1" 200 19770
[13/Aug/2019 19:20:13] "GET /static/personal_page/amazon.png HTTP/1.1" 200 12429
[13/Aug/2019 19:20:13] "GET /static/personal_page/angular.png HTTP/1.1" 200 13080
[13/Aug/2019 19:20:14] "GET /static/personal_page/vendor/fontawesome-free/webfonts/fa-regular-400.woff2 HTTP/1.1" 200 13592
Not Found: /favicon.ico
[13/Aug/2019 19:20:14] "GET /favicon.ico HTTP/1.1" 404 2915
[13/Aug/2019 19:20:18] "GET / HTTP/1.1" 200 16702
Not Found: /accomodations
[13/Aug/2019 19:20:18] "GET /accomodations HTTP/1.1" 404 2921
Not Found: /favicon.ico
[13/Aug/2019 19:20:18] "GET /favicon.ico HTTP/1.1" 404 2915
[13/Aug/2019 19:20:20] "GET /admin HTTP/1.1" 200 5232
Not Found: /favicon.ico
[13/Aug/2019 19:20:20] "GET /favicon.ico HTTP/1.1" 404 2915
[13/Aug/2019 19:20:27] "GET /portfolio HTTP/1.1" 200 3917
[13/Aug/2019 19:20:27] "GET /static/personal_page/img/algoAlarm1.png HTTP/1.1" 200 569343
[13/Aug/2019 19:20:27] "GET /static/personal_page/img/algoAlarm2.png HTTP/1.1" 200 536100
[13/Aug/2019 19:20:27] "GET /static/personal_page/img/algoAlarm3.png HTTP/1.1" 200 1642690
Not Found: /favicon.ico
[13/Aug/2019 19:20:27] "GET /favicon.ico HTTP/1.1" 404 2915
[13/Aug/2019 19:21:06] "GET /portfolio HTTP/1.1" 200 3926
[13/Aug/2019 19:22:04] "GET / HTTP/1.1" 200 16702
[13/Aug/2019 19:22:30] "GET / HTTP/1.1" 200 16717
[13/Aug/2019 19:23:13] "GET / HTTP/1.1" 200 16742
[13/Aug/2019 19:23:20] "GET / HTTP/1.1" 200 16742
[13/Aug/2019 19:23:29] "GET / HTTP/1.1" 200 16744
[13/Aug/2019 19:24:19] "GET / HTTP/1.1" 200 16747
[13/Aug/2019 19:24:27] "GET / HTTP/1.1" 200 16747
[13/Aug/2019 19:24:33] "GET / HTTP/1.1" 200 16741
[13/Aug/2019 19:24:38] "GET / HTTP/1.1" 200 16743
[13/Aug/2019 19:25:12] "GET / HTTP/1.1" 200 17711
[13/Aug/2019 19:25:37] "GET / HTTP/1.1" 200 17744
Not Found: /nathanandlaura.com
[13/Aug/2019 19:25:38] "GET /nathanandlaura.com HTTP/1.1" 404 2936
Not Found: /favicon.ico
[13/Aug/2019 19:25:38] "GET /favicon.ico HTTP/1.1" 404 2915
Not Found: /nathanandlaura.com
[13/Aug/2019 19:25:59] "GET /nathanandlaura.com HTTP/1.1" 404 2936
[13/Aug/2019 19:26:15] "GET / HTTP/1.1" 200 17784
[13/Aug/2019 19:27:03] "GET / HTTP/1.1" 200 17798
[13/Aug/2019 19:27:13] "GET /static/personal_page/vendor/bootstrap/js/bootstrap.bundle.min.js.map HTTP/1.1" 200 311949
[13/Aug/2019 19:27:13] "GET /static/personal_page/vendor/bootstrap/css/bootstrap.min.css.map HTTP/1.1" 200 625953
[13/Aug/2019 19:27:31] "GET / HTTP/1.1" 200 17800
[13/Aug/2019 19:27:54] "GET / HTTP/1.1" 200 17631
[13/Aug/2019 19:29:36] "GET / HTTP/1.1" 200 17664
[13/Aug/2019 19:30:23] "GET / HTTP/1.1" 200 17671
[13/Aug/2019 19:30:32] "GET / HTTP/1.1" 200 17664
[13/Aug/2019 19:30:54] "GET / HTTP/1.1" 200 17575
[13/Aug/2019 19:31:29] "GET / HTTP/1.1" 200 17658
[13/Aug/2019 19:31:48] "GET / HTTP/1.1" 200 17672
[13/Aug/2019 19:32:59] "GET / HTTP/1.1" 200 17467
[13/Aug/2019 19:33:11] "GET / HTTP/1.1" 200 17467
[13/Aug/2019 19:33:49] "GET /static/personal_page/resume/Jonathan%20Poso%20-%20Resume.pdf HTTP/1.1" 200 58694
Not Found: /favicon.ico
[13/Aug/2019 19:33:49] "GET /favicon.ico HTTP/1.1" 404 2915
[13/Aug/2019 19:34:33] "GET / HTTP/1.1" 200 17467
[13/Aug/2019 19:37:59] "GET /barry HTTP/1.1" 200 4083
[13/Aug/2019 19:37:59] "GET /static/personal_page/img/berries1.png HTTP/1.1" 200 597947
[13/Aug/2019 19:37:59] "GET /static/personal_page/img/berries2.png HTTP/1.1" 200 1014252
[13/Aug/2019 19:37:59] "GET /static/personal_page/img/berries3.png HTTP/1.1" 200 1066130
Not Found: /favicon.ico
[13/Aug/2019 19:37:59] "GET /favicon.ico HTTP/1.1" 404 2915
[13/Aug/2019 19:38:02] "GET / HTTP/1.1" 200 17467
Not Found: /favicon.ico
[13/Aug/2019 19:38:02] "GET /favicon.ico HTTP/1.1" 404 2915
[13/Aug/2019 19:38:21] "GET / HTTP/1.1" 200 17467
[13/Aug/2019 19:38:22] "GET /portfolio HTTP/1.1" 200 3936
[13/Aug/2019 19:38:42] "GET /portfolio HTTP/1.1" 200 3936
[13/Aug/2019 19:42:17] "GET /portfolio HTTP/1.1" 200 3997
[13/Aug/2019 19:42:17] "GET /static/personal_page/img/nandl.webarchive HTTP/1.1" 200 1140083
[13/Aug/2019 19:44:45] "GET /portfolio HTTP/1.1" 200 3990
[13/Aug/2019 19:44:45] "GET /static/personal_page/img/nandl.png HTTP/1.1" 404 1694
[13/Aug/2019 19:44:46] "GET /portfolio HTTP/1.1" 200 3990
[13/Aug/2019 19:44:46] "GET /static/personal_page/img/nandl.png HTTP/1.1" 404 1694
[13/Aug/2019 19:45:12] "GET /portfolio HTTP/1.1" 200 3986
[13/Aug/2019 19:45:12] "GET /static/personal_page/nandl.png HTTP/1.1" 404 1682
[13/Aug/2019 19:45:54] "GET /portfolio HTTP/1.1" 200 3990
[13/Aug/2019 19:45:54] "GET /static/personal_page/img/nandl.png HTTP/1.1" 200 2578034
[13/Aug/2019 19:46:08] "GET /portfolio HTTP/1.1" 200 4013
[13/Aug/2019 19:46:40] "GET /portfolio HTTP/1.1" 200 6757
[13/Aug/2019 19:46:40] "GET /static/personal_page/img/nandl.png HTTP/1.1" 304 0
[13/Aug/2019 19:46:54] "GET /portfolio HTTP/1.1" 200 6756
[13/Aug/2019 19:47:21] "GET /portfolio HTTP/1.1" 200 6775
[13/Aug/2019 19:47:21] "GET /static/personal_page/img/nandl.png HTTP/1.1" 304 0
[13/Aug/2019 19:47:30] "GET /portfolio HTTP/1.1" 200 5726
[13/Aug/2019 19:47:43] "GET /portfolio HTTP/1.1" 200 5156
[13/Aug/2019 19:47:52] "GET /portfolio HTTP/1.1" 200 5156
[13/Aug/2019 19:47:53] "GET /portfolio HTTP/1.1" 200 5156
[13/Aug/2019 19:48:00] "GET /portfolio HTTP/1.1" 200 5154
[13/Aug/2019 19:48:12] "GET /portfolio HTTP/1.1" 200 5158
[13/Aug/2019 19:48:12] "GET /static/personal_page/img/nandl.png HTTP/1.1" 304 0
[13/Aug/2019 19:48:25] "GET /portfolio HTTP/1.1" 200 5149
[13/Aug/2019 19:48:29] "GET /portfolio HTTP/1.1" 200 5036
[13/Aug/2019 19:48:40] "GET /portfolio HTTP/1.1" 200 4927
[13/Aug/2019 19:48:47] "GET /portfolio HTTP/1.1" 200 4915
[13/Aug/2019 19:48:56] "GET /portfolio HTTP/1.1" 200 4917
[13/Aug/2019 19:49:04] "GET /portfolio HTTP/1.1" 200 4919
[13/Aug/2019 19:49:04] "GET /static/personal_page/img/nandl.png HTTP/1.1" 304 0
[13/Aug/2019 19:49:12] "GET /portfolio HTTP/1.1" 200 4919
[13/Aug/2019 19:49:32] "GET /portfolio HTTP/1.1" 200 4919
[13/Aug/2019 19:50:24] "GET /portfolio HTTP/1.1" 200 4934
[13/Aug/2019 19:50:24] "GET /static/personal_page/img/nandl.png HTTP/1.1" 304 0
[13/Aug/2019 19:50:24] "GET /static/personal_page/img/algoAlarm1.png HTTP/1.1" 200 569343
[13/Aug/2019 19:50:24] "GET /static/personal_page/img/smartlist-1.png HTTP/1.1" 200 3235933
[13/Aug/2019 19:50:32] "GET /portfolio HTTP/1.1" 200 4934
[13/Aug/2019 19:50:32] "GET /static/personal_page/img/smartlist-2.png HTTP/1.1" 200 2886280
[13/Aug/2019 19:50:52] "GET /portfolio HTTP/1.1" 200 5024
[13/Aug/2019 19:51:04] "GET / HTTP/1.1" 200 17467
[13/Aug/2019 19:52:48] "GET /portfolio HTTP/1.1" 200 5112
[13/Aug/2019 19:52:48] "GET /static/personal_page/img/strata.png HTTP/1.1" 200 597512
[13/Aug/2019 19:52:48] "GET /static/personal_page/img/nandl.png HTTP/1.1" 304 0
Performing system checks...

System check identified no issues (0 silenced).
August 13, 2019 - 19:53:43
Django version 1.10, using settings 'Webpage.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[13/Aug/2019 19:54:21] "GET / HTTP/1.1" 200 17467
[13/Aug/2019 19:54:22] "GET /portfolio HTTP/1.1" 200 5112
[13/Aug/2019 19:54:22] "GET /static/personal_page/img/strata.png HTTP/1.1" 304 0
[13/Aug/2019 19:54:22] "GET /static/personal_page/img/nandl.png HTTP/1.1" 304 0
[13/Aug/2019 19:55:17] "GET /portfolio HTTP/1.1" 200 5184
[13/Aug/2019 19:55:17] "GET /static/personal_page/img/strata.png HTTP/1.1" 304 0
[13/Aug/2019 19:55:17] "GET /portfolio HTTP/1.1" 200 5184
[13/Aug/2019 19:55:38] "GET /portfolio HTTP/1.1" 200 5193
[13/Aug/2019 19:55:38] "GET /static/personal_page/img/strata.png HTTP/1.1" 304 0
[13/Aug/2019 19:55:46] "GET /portfolio HTTP/1.1" 200 5166
[13/Aug/2019 19:55:46] "GET /static/personal_page/img/nandl.png HTTP/1.1" 304 0
[13/Aug/2019 19:56:32] "GET /portfolio HTTP/1.1" 200 5166
[13/Aug/2019 19:56:32] "GET /static/personal_page/img/strata.png HTTP/1.1" 304 0
[13/Aug/2019 19:57:16] "GET /portfolio HTTP/1.1" 200 5166
[13/Aug/2019 19:57:16] "GET /static/personal_page/img/strata.png HTTP/1.1" 304 0
[13/Aug/2019 19:57:45] "GET /portfolio HTTP/1.1" 200 5166
[13/Aug/2019 19:57:45] "GET /static/personal_page/img/nandl.png HTTP/1.1" 304 0
[13/Aug/2019 19:57:47] "GET /portfolio HTTP/1.1" 200 5166
[13/Aug/2019 19:57:55] "GET /portfolio HTTP/1.1" 200 5166
[13/Aug/2019 19:57:55] "GET /static/personal_page/img/strata.png HTTP/1.1" 304 0
[13/Aug/2019 19:57:58] "GET / HTTP/1.1" 200 17467
[13/Aug/2019 19:59:01] "GET /portfolio HTTP/1.1" 200 5166
[13/Aug/2019 19:59:01] "GET /static/personal_page/img/strata.png HTTP/1.1" 304 0
[13/Aug/2019 19:59:04] "GET / HTTP/1.1" 200 17468
[13/Aug/2019 19:59:53] "GET / HTTP/1.1" 200 17503
[13/Aug/2019 20:01:28] "GET / HTTP/1.1" 200 17659
[13/Aug/2019 20:02:28] "GET / HTTP/1.1" 200 17716
[13/Aug/2019 20:03:00] "GET / HTTP/1.1" 200 17887
[13/Aug/2019 20:04:33] "GET / HTTP/1.1" 200 18037
[13/Aug/2019 20:07:04] "GET / HTTP/1.1" 200 18235
[13/Aug/2019 20:09:36] "GET /algo HTTP/1.1" 200 3930
Not Found: /favicon.ico
[13/Aug/2019 20:09:36] "GET /favicon.ico HTTP/1.1" 404 2915
[13/Aug/2019 20:09:37] "GET / HTTP/1.1" 200 18524
[13/Aug/2019 20:17:13] "GET / HTTP/1.1" 200 18626
[13/Aug/2019 20:18:07] "GET / HTTP/1.1" 200 18651
[13/Aug/2019 20:19:38] "GET / HTTP/1.1" 200 19440
[13/Aug/2019 20:19:59] "GET / HTTP/1.1" 200 19328
[13/Aug/2019 20:22:11] "GET / HTTP/1.1" 200 19215
[13/Aug/2019 20:23:01] "GET / HTTP/1.1" 200 19219
[13/Aug/2019 20:23:59] "GET / HTTP/1.1" 200 19317
[13/Aug/2019 20:24:57] "GET / HTTP/1.1" 200 19390
[13/Aug/2019 20:26:24] "GET / HTTP/1.1" 200 19448
[13/Aug/2019 20:26:37] "GET / HTTP/1.1" 200 19481
[13/Aug/2019 20:32:12] "GET / HTTP/1.1" 200 19894
[13/Aug/2019 20:36:42] "GET / HTTP/1.1" 200 19894
Performing system checks...

System check identified no issues (0 silenced).
August 13, 2019 - 20:36:52
Django version 1.10, using settings 'Webpage.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...

System check identified no issues (0 silenced).
August 13, 2019 - 20:37:00
Django version 1.10, using settings 'Webpage.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[13/Aug/2019 20:37:01] "GET / HTTP/1.1" 200 19894
[13/Aug/2019 20:37:27] "GET / HTTP/1.1" 200 19894
[13/Aug/2019 20:37:30] "GET / HTTP/1.1" 200 19894
[13/Aug/2019 20:37:30] "GET /static/personal_page/github.png HTTP/1.1" 200 6568
[13/Aug/2019 20:37:30] "GET /static/personal_page/vendor/jquery-easing/jquery.easing.min.js HTTP/1.1" 200 2532
[13/Aug/2019 20:37:30] "GET /static/personal_page/amazon.png HTTP/1.1" 200 12429
[13/Aug/2019 20:37:30] "GET /static/personal_page/fire.png HTTP/1.1" 200 11915
[13/Aug/2019 20:37:30] "GET /static/personal_page/resume.min.css HTTP/1.1" 200 3223
[13/Aug/2019 20:37:30] "GET /static/personal_page/angular.png HTTP/1.1" 200 13080
[13/Aug/2019 20:37:30] "GET /static/personal_page/img/me.jpeg HTTP/1.1" 200 270483
[13/Aug/2019 20:37:31] "GET / HTTP/1.1" 200 19894
[13/Aug/2019 20:37:31] "GET / HTTP/1.1" 200 19894
Not Found: /accomodations
[13/Aug/2019 20:37:32] "GET /accomodations HTTP/1.1" 404 2454
Not Found: /admin
[13/Aug/2019 20:37:32] "GET /admin HTTP/1.1" 404 2430
Not Found: /admin
[13/Aug/2019 20:37:52] "GET /admin HTTP/1.1" 404 2430
^CJonathans-MacBook-Pro:webpage2 jonathanposo$ ls
Webpage			node_modules
apps			package-lock.json
db.sqlite3		requirements.txt
manage.py
Jonathans-MacBook-Pro:webpage2 jonathanposo$ cd ../
Jonathans-MacBook-Pro:my_environments jonathanposo$ ls
Books		Smartlist	env		wedding
Cards		Webpage		main
Ninjas		Webpage2	py3Env
SandwichApp	djangoPy3Env	venv
Jonathans-MacBook-Pro:my_environments jonathanposo$ cd webpage 2
Jonathans-MacBook-Pro:webpage jonathanposo$ ls
Webpage		apps		db.sqlite3	manage.py
Jonathans-MacBook-Pro:webpage jonathanposo$ cd ../
Jonathans-MacBook-Pro:my_environments jonathanposo$ ls
Books		Smartlist	env		wedding
Cards		Webpage		main
Ninjas		Webpage2	py3Env
SandwichApp	djangoPy3Env	venv
Jonathans-MacBook-Pro:my_environments jonathanposo$ cd webpage2
Jonathans-MacBook-Pro:webpage2 jonathanposo$ ls
Webpage			node_modules
apps			package-lock.json
db.sqlite3		requirements.txt
manage.py
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git add *
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git commit -m "updated 8-13"
[code2 09177c3] updated 8-13
 609 files changed, 72767 insertions(+), 13 deletions(-)
 create mode 100644 apps/personal_page/static/personal_page/img/nandl.png
 create mode 100644 apps/personal_page/static/personal_page/img/strata.png
 create mode 100644 apps/personal_page/static/personal_page/resume/.DS_Store
 rewrite apps/personal_page/static/personal_page/resume/Jonathan Poso - Resume.pdf (81%)
 create mode 120000 node_modules/.bin/detect-libc
 create mode 120000 node_modules/.bin/mkdirp
 create mode 120000 node_modules/.bin/needle
 create mode 120000 node_modules/.bin/node-pre-gyp
 create mode 120000 node_modules/.bin/nopt
 create mode 120000 node_modules/.bin/rc
 create mode 120000 node_modules/.bin/rimraf
 create mode 120000 node_modules/.bin/semver
 create mode 100644 node_modules/abbrev/LICENSE
 create mode 100644 node_modules/abbrev/README.md
 create mode 100644 node_modules/abbrev/abbrev.js
 create mode 100644 node_modules/abbrev/package.json
 create mode 100644 node_modules/ansi-regex/index.js
 create mode 100644 node_modules/ansi-regex/license
 create mode 100644 node_modules/ansi-regex/package.json
 create mode 100644 node_modules/ansi-regex/readme.md
 create mode 100644 node_modules/aproba/LICENSE
 create mode 100644 node_modules/aproba/README.md
 create mode 100644 node_modules/aproba/index.js
 create mode 100644 node_modules/aproba/package.json
 create mode 100644 node_modules/are-we-there-yet/CHANGES.md
 create mode 100644 node_modules/are-we-there-yet/LICENSE
 create mode 100644 node_modules/are-we-there-yet/README.md
 create mode 100644 node_modules/are-we-there-yet/index.js
 create mode 100644 node_modules/are-we-there-yet/package.json
 create mode 100644 node_modules/are-we-there-yet/tracker-base.js
 create mode 100644 node_modules/are-we-there-yet/tracker-group.js
 create mode 100644 node_modules/are-we-there-yet/tracker-stream.js
 create mode 100644 node_modules/are-we-there-yet/tracker.js
 create mode 100644 node_modules/balanced-match/.npmignore
 create mode 100644 node_modules/balanced-match/LICENSE.md
 create mode 100644 node_modules/balanced-match/README.md
 create mode 100644 node_modules/balanced-match/index.js
 create mode 100644 node_modules/balanced-match/package.json
 create mode 100644 node_modules/bcrypt/.editorconfig
 create mode 100644 node_modules/bcrypt/.travis.yml
 create mode 100644 node_modules/bcrypt/CHANGELOG.md
 create mode 100644 node_modules/bcrypt/ISSUE_TEMPLATE.md
 create mode 100644 node_modules/bcrypt/LICENSE
 create mode 100644 node_modules/bcrypt/Makefile
 create mode 100644 node_modules/bcrypt/README.md
 create mode 100644 node_modules/bcrypt/appveyor.yml
 create mode 100644 node_modules/bcrypt/bcrypt.js
 create mode 100644 node_modules/bcrypt/binding.gyp
 create mode 100644 node_modules/bcrypt/examples/async_compare.js
 create mode 100644 node_modules/bcrypt/examples/forever_gen_salt.js
 create mode 100755 node_modules/bcrypt/lib/binding/bcrypt_lib.node
 create mode 100644 node_modules/bcrypt/package.json
 create mode 100644 node_modules/bcrypt/promises.js
 create mode 100644 node_modules/bcrypt/src/bcrypt.cc
 create mode 100644 node_modules/bcrypt/src/bcrypt_node.cc
 create mode 100644 node_modules/bcrypt/src/blowfish.cc
 create mode 100644 node_modules/bcrypt/src/node_blf.h
 create mode 100644 node_modules/bcrypt/test/async.js
 create mode 100644 node_modules/bcrypt/test/implementation.js
 create mode 100644 node_modules/bcrypt/test/promise.js
 create mode 100644 node_modules/bcrypt/test/repetitions.js
 create mode 100644 node_modules/bcrypt/test/sync.js
 create mode 100644 node_modules/brace-expansion/LICENSE
 create mode 100644 node_modules/brace-expansion/README.md
 create mode 100644 node_modules/brace-expansion/index.js
 create mode 100644 node_modules/brace-expansion/package.json
 create mode 100644 node_modules/chownr/LICENSE
 create mode 100644 node_modules/chownr/README.md
 create mode 100644 node_modules/chownr/chownr.js
 create mode 100644 node_modules/chownr/package.json
 create mode 100644 node_modules/code-point-at/index.js
 create mode 100644 node_modules/code-point-at/license
 create mode 100644 node_modules/code-point-at/package.json
 create mode 100644 node_modules/code-point-at/readme.md
 create mode 100644 node_modules/concat-map/.travis.yml
 create mode 100644 node_modules/concat-map/LICENSE
 create mode 100644 node_modules/concat-map/README.markdown
 create mode 100644 node_modules/concat-map/example/map.js
 create mode 100644 node_modules/concat-map/index.js
 create mode 100644 node_modules/concat-map/package.json
 create mode 100644 node_modules/concat-map/test/map.js
 create mode 100644 node_modules/console-control-strings/LICENSE
 create mode 100644 node_modules/console-control-strings/README.md
 create mode 100644 node_modules/console-control-strings/README.md~
 create mode 100644 node_modules/console-control-strings/index.js
 create mode 100644 node_modules/console-control-strings/package.json
 create mode 100644 node_modules/core-util-is/LICENSE
 create mode 100644 node_modules/core-util-is/README.md
 create mode 100644 node_modules/core-util-is/float.patch
 create mode 100644 node_modules/core-util-is/lib/util.js
 create mode 100644 node_modules/core-util-is/package.json
 create mode 100644 node_modules/core-util-is/test.js
 create mode 100644 node_modules/debug/CHANGELOG.md
 create mode 100644 node_modules/debug/LICENSE
 create mode 100644 node_modules/debug/README.md
 create mode 100644 node_modules/debug/dist/debug.js
 create mode 100644 node_modules/debug/node.js
 create mode 100644 node_modules/debug/package.json
 create mode 100644 node_modules/debug/src/browser.js
 create mode 100644 node_modules/debug/src/common.js
 create mode 100644 node_modules/debug/src/index.js
 create mode 100644 node_modules/debug/src/node.js
 create mode 100644 node_modules/deep-extend/CHANGELOG.md
 create mode 100644 node_modules/deep-extend/LICENSE
 create mode 100644 node_modules/deep-extend/README.md
 create mode 100644 node_modules/deep-extend/index.js
 create mode 100644 node_modules/deep-extend/lib/deep-extend.js
 create mode 100644 node_modules/deep-extend/package.json
 create mode 100644 node_modules/delegates/.npmignore
 create mode 100644 node_modules/delegates/History.md
 create mode 100644 node_modules/delegates/License
 create mode 100644 node_modules/delegates/Makefile
 create mode 100644 node_modules/delegates/Readme.md
 create mode 100644 node_modules/delegates/index.js
 create mode 100644 node_modules/delegates/package.json
 create mode 100644 node_modules/delegates/test/index.js
 create mode 100644 node_modules/detect-libc/.npmignore
 create mode 100644 node_modules/detect-libc/LICENSE
 create mode 100644 node_modules/detect-libc/README.md
 create mode 100755 node_modules/detect-libc/bin/detect-libc.js
 create mode 100644 node_modules/detect-libc/lib/detect-libc.js
 create mode 100644 node_modules/detect-libc/package.json
 create mode 100644 node_modules/fs-minipass/LICENSE
 create mode 100644 node_modules/fs-minipass/README.md
 create mode 100644 node_modules/fs-minipass/index.js
 create mode 100644 node_modules/fs-minipass/package.json
 create mode 100644 node_modules/fs.realpath/LICENSE
 create mode 100644 node_modules/fs.realpath/README.md
 create mode 100644 node_modules/fs.realpath/index.js
 create mode 100644 node_modules/fs.realpath/old.js
 create mode 100644 node_modules/fs.realpath/package.json
 create mode 100644 node_modules/gauge/CHANGELOG.md
 create mode 100644 node_modules/gauge/LICENSE
 create mode 100644 node_modules/gauge/README.md
 create mode 100644 node_modules/gauge/base-theme.js
 create mode 100644 node_modules/gauge/error.js
 create mode 100644 node_modules/gauge/has-color.js
 create mode 100644 node_modules/gauge/index.js
 create mode 100644 node_modules/gauge/package.json
 create mode 100644 node_modules/gauge/plumbing.js
 create mode 100644 node_modules/gauge/process.js
 create mode 100644 node_modules/gauge/progress-bar.js
 create mode 100644 node_modules/gauge/render-template.js
 create mode 100644 node_modules/gauge/set-immediate.js
 create mode 100644 node_modules/gauge/set-interval.js
 create mode 100644 node_modules/gauge/spin.js
 create mode 100644 node_modules/gauge/template-item.js
 create mode 100644 node_modules/gauge/theme-set.js
 create mode 100644 node_modules/gauge/themes.js
 create mode 100644 node_modules/gauge/wide-truncate.js
 create mode 100644 node_modules/glob/LICENSE
 create mode 100644 node_modules/glob/README.md
 create mode 100644 node_modules/glob/changelog.md
 create mode 100644 node_modules/glob/common.js
 create mode 100644 node_modules/glob/glob.js
 create mode 100644 node_modules/glob/package.json
 create mode 100644 node_modules/glob/sync.js
 create mode 100644 node_modules/has-unicode/LICENSE
 create mode 100644 node_modules/has-unicode/README.md
 create mode 100644 node_modules/has-unicode/index.js
 create mode 100644 node_modules/has-unicode/package.json
 create mode 100644 node_modules/iconv-lite/Changelog.md
 create mode 100644 node_modules/iconv-lite/LICENSE
 create mode 100644 node_modules/iconv-lite/README.md
 create mode 100644 node_modules/iconv-lite/encodings/dbcs-codec.js
 create mode 100644 node_modules/iconv-lite/encodings/dbcs-data.js
 create mode 100644 node_modules/iconv-lite/encodings/index.js
 create mode 100644 node_modules/iconv-lite/encodings/internal.js
 create mode 100644 node_modules/iconv-lite/encodings/sbcs-codec.js
 create mode 100644 node_modules/iconv-lite/encodings/sbcs-data-generated.js
 create mode 100644 node_modules/iconv-lite/encodings/sbcs-data.js
 create mode 100644 node_modules/iconv-lite/encodings/tables/big5-added.json
 create mode 100644 node_modules/iconv-lite/encodings/tables/cp936.json
 create mode 100644 node_modules/iconv-lite/encodings/tables/cp949.json
 create mode 100644 node_modules/iconv-lite/encodings/tables/cp950.json
 create mode 100644 node_modules/iconv-lite/encodings/tables/eucjp.json
 create mode 100644 node_modules/iconv-lite/encodings/tables/gb18030-ranges.json
 create mode 100644 node_modules/iconv-lite/encodings/tables/gbk-added.json
 create mode 100644 node_modules/iconv-lite/encodings/tables/shiftjis.json
 create mode 100644 node_modules/iconv-lite/encodings/utf16.js
 create mode 100644 node_modules/iconv-lite/encodings/utf7.js
 create mode 100644 node_modules/iconv-lite/lib/bom-handling.js
 create mode 100644 node_modules/iconv-lite/lib/extend-node.js
 create mode 100644 node_modules/iconv-lite/lib/index.d.ts
 create mode 100644 node_modules/iconv-lite/lib/index.js
 create mode 100644 node_modules/iconv-lite/lib/streams.js
 create mode 100644 node_modules/iconv-lite/package.json
 create mode 100644 node_modules/ignore-walk/LICENSE
 create mode 100644 node_modules/ignore-walk/README.md
 create mode 100644 node_modules/ignore-walk/index.js
 create mode 100644 node_modules/ignore-walk/package.json
 create mode 100644 node_modules/inflight/LICENSE
 create mode 100644 node_modules/inflight/README.md
 create mode 100644 node_modules/inflight/inflight.js
 create mode 100644 node_modules/inflight/package.json
 create mode 100644 node_modules/inherits/LICENSE
 create mode 100644 node_modules/inherits/README.md
 create mode 100644 node_modules/inherits/inherits.js
 create mode 100644 node_modules/inherits/inherits_browser.js
 create mode 100644 node_modules/inherits/package.json
 create mode 100644 node_modules/ini/LICENSE
 create mode 100644 node_modules/ini/README.md
 create mode 100644 node_modules/ini/ini.js
 create mode 100644 node_modules/ini/package.json
 create mode 100644 node_modules/is-fullwidth-code-point/index.js
 create mode 100644 node_modules/is-fullwidth-code-point/license
 create mode 100644 node_modules/is-fullwidth-code-point/package.json
 create mode 100644 node_modules/is-fullwidth-code-point/readme.md
 create mode 100644 node_modules/isarray/.npmignore
 create mode 100644 node_modules/isarray/.travis.yml
 create mode 100644 node_modules/isarray/Makefile
 create mode 100644 node_modules/isarray/README.md
 create mode 100644 node_modules/isarray/component.json
 create mode 100644 node_modules/isarray/index.js
 create mode 100644 node_modules/isarray/package.json
 create mode 100644 node_modules/isarray/test.js
 create mode 100644 node_modules/minimatch/LICENSE
 create mode 100644 node_modules/minimatch/README.md
 create mode 100644 node_modules/minimatch/minimatch.js
 create mode 100644 node_modules/minimatch/package.json
 create mode 100644 node_modules/minimist/.travis.yml
 create mode 100644 node_modules/minimist/LICENSE
 create mode 100644 node_modules/minimist/example/parse.js
 create mode 100644 node_modules/minimist/index.js
 create mode 100644 node_modules/minimist/package.json
 create mode 100644 node_modules/minimist/readme.markdown
 create mode 100644 node_modules/minimist/test/dash.js
 create mode 100644 node_modules/minimist/test/default_bool.js
 create mode 100644 node_modules/minimist/test/dotted.js
 create mode 100644 node_modules/minimist/test/long.js
 create mode 100644 node_modules/minimist/test/parse.js
 create mode 100644 node_modules/minimist/test/parse_modified.js
 create mode 100644 node_modules/minimist/test/short.js
 create mode 100644 node_modules/minimist/test/whitespace.js
 create mode 100644 node_modules/minipass/LICENSE
 create mode 100644 node_modules/minipass/README.md
 create mode 100644 node_modules/minipass/index.js
 create mode 100644 node_modules/minipass/package.json
 create mode 100644 node_modules/minizlib/LICENSE
 create mode 100644 node_modules/minizlib/README.md
 create mode 100644 node_modules/minizlib/constants.js
 create mode 100644 node_modules/minizlib/index.js
 create mode 100644 node_modules/minizlib/package.json
 create mode 100644 node_modules/mkdirp/.travis.yml
 create mode 100644 node_modules/mkdirp/LICENSE
 create mode 100755 node_modules/mkdirp/bin/cmd.js
 create mode 100644 node_modules/mkdirp/bin/usage.txt
 create mode 100644 node_modules/mkdirp/examples/pow.js
 create mode 100644 node_modules/mkdirp/index.js
 create mode 100644 node_modules/mkdirp/package.json
 create mode 100644 node_modules/mkdirp/readme.markdown
 create mode 100644 node_modules/mkdirp/test/chmod.js
 create mode 100644 node_modules/mkdirp/test/clobber.js
 create mode 100644 node_modules/mkdirp/test/mkdirp.js
 create mode 100644 node_modules/mkdirp/test/opts_fs.js
 create mode 100644 node_modules/mkdirp/test/opts_fs_sync.js
 create mode 100644 node_modules/mkdirp/test/perm.js
 create mode 100644 node_modules/mkdirp/test/perm_sync.js
 create mode 100644 node_modules/mkdirp/test/race.js
 create mode 100644 node_modules/mkdirp/test/rel.js
 create mode 100644 node_modules/mkdirp/test/return.js
 create mode 100644 node_modules/mkdirp/test/return_sync.js
 create mode 100644 node_modules/mkdirp/test/root.js
 create mode 100644 node_modules/mkdirp/test/sync.js
 create mode 100644 node_modules/mkdirp/test/umask.js
 create mode 100644 node_modules/mkdirp/test/umask_sync.js
 create mode 100644 node_modules/ms/index.js
 create mode 100644 node_modules/ms/license.md
 create mode 100644 node_modules/ms/package.json
 create mode 100644 node_modules/ms/readme.md
 create mode 100644 node_modules/nan/CHANGELOG.md
 create mode 100644 node_modules/nan/LICENSE.md
 create mode 100644 node_modules/nan/README.md
 create mode 100644 node_modules/nan/doc/asyncworker.md
 create mode 100644 node_modules/nan/doc/buffers.md
 create mode 100644 node_modules/nan/doc/callback.md
 create mode 100644 node_modules/nan/doc/converters.md
 create mode 100644 node_modules/nan/doc/errors.md
 create mode 100644 node_modules/nan/doc/json.md
 create mode 100644 node_modules/nan/doc/maybe_types.md
 create mode 100644 node_modules/nan/doc/methods.md
 create mode 100644 node_modules/nan/doc/new.md
 create mode 100644 node_modules/nan/doc/node_misc.md
 create mode 100644 node_modules/nan/doc/object_wrappers.md
 create mode 100644 node_modules/nan/doc/persistent.md
 create mode 100644 node_modules/nan/doc/scopes.md
 create mode 100644 node_modules/nan/doc/script.md
 create mode 100644 node_modules/nan/doc/string_bytes.md
 create mode 100644 node_modules/nan/doc/v8_internals.md
 create mode 100644 node_modules/nan/doc/v8_misc.md
 create mode 100644 node_modules/nan/include_dirs.js
 create mode 100644 node_modules/nan/nan.h
 create mode 100644 node_modules/nan/nan_callbacks.h
 create mode 100644 node_modules/nan/nan_callbacks_12_inl.h
 create mode 100644 node_modules/nan/nan_callbacks_pre_12_inl.h
 create mode 100644 node_modules/nan/nan_converters.h
 create mode 100644 node_modules/nan/nan_converters_43_inl.h
 create mode 100644 node_modules/nan/nan_converters_pre_43_inl.h
 create mode 100644 node_modules/nan/nan_define_own_property_helper.h
 create mode 100644 node_modules/nan/nan_implementation_12_inl.h
 create mode 100644 node_modules/nan/nan_implementation_pre_12_inl.h
 create mode 100644 node_modules/nan/nan_json.h
 create mode 100644 node_modules/nan/nan_maybe_43_inl.h
 create mode 100644 node_modules/nan/nan_maybe_pre_43_inl.h
 create mode 100644 node_modules/nan/nan_new.h
 create mode 100644 node_modules/nan/nan_object_wrap.h
 create mode 100644 node_modules/nan/nan_persistent_12_inl.h
 create mode 100644 node_modules/nan/nan_persistent_pre_12_inl.h
 create mode 100644 node_modules/nan/nan_private.h
 create mode 100644 node_modules/nan/nan_string_bytes.h
 create mode 100644 node_modules/nan/nan_typedarray_contents.h
 create mode 100644 node_modules/nan/nan_weak.h
 create mode 100644 node_modules/nan/package.json
 create mode 100755 node_modules/nan/tools/1to2.js
 create mode 100644 node_modules/nan/tools/README.md
 create mode 100644 node_modules/nan/tools/package.json
 create mode 100644 node_modules/needle/README.md
 create mode 100755 node_modules/needle/bin/needle
 create mode 100644 node_modules/needle/examples/deflated-stream.js
 create mode 100644 node_modules/needle/examples/digest-auth.js
 create mode 100644 node_modules/needle/examples/download-to-file.js
 create mode 100644 node_modules/needle/examples/multipart-stream.js
 create mode 100644 node_modules/needle/examples/parsed-stream.js
 create mode 100644 node_modules/needle/examples/parsed-stream2.js
 create mode 100644 node_modules/needle/examples/stream-events.js
 create mode 100644 node_modules/needle/examples/stream-to-file.js
 create mode 100644 node_modules/needle/examples/upload-image.js
 create mode 100644 node_modules/needle/lib/auth.js
 create mode 100644 node_modules/needle/lib/cookies.js
 create mode 100644 node_modules/needle/lib/decoder.js
 create mode 100644 node_modules/needle/lib/multipart.js
 create mode 100644 node_modules/needle/lib/needle.js
 create mode 100644 node_modules/needle/lib/parsers.js
 create mode 100644 node_modules/needle/lib/querystring.js
 create mode 100644 node_modules/needle/license.txt
 create mode 100644 node_modules/needle/package.json
 create mode 100644 node_modules/needle/test/basic_auth_spec.js
 create mode 100644 node_modules/needle/test/compression_spec.js
 create mode 100644 node_modules/needle/test/cookies_spec.js
 create mode 100644 node_modules/needle/test/decoder_spec.js
 create mode 100644 node_modules/needle/test/errors_spec.js
 create mode 100644 node_modules/needle/test/headers_spec.js
 create mode 100644 node_modules/needle/test/helpers.js
 create mode 100644 node_modules/needle/test/long_string_spec.js
 create mode 100644 node_modules/needle/test/output_spec.js
 create mode 100644 node_modules/needle/test/parsing_spec.js
 create mode 100644 node_modules/needle/test/post_data_spec.js
 create mode 100644 node_modules/needle/test/proxy_spec.js
 create mode 100644 node_modules/needle/test/querystring_spec.js
 create mode 100644 node_modules/needle/test/redirect_spec.js
 create mode 100644 node_modules/needle/test/redirect_with_timeout.js
 create mode 100644 node_modules/needle/test/request_stream_spec.js
 create mode 100644 node_modules/needle/test/response_stream_spec.js
 create mode 100644 node_modules/needle/test/socket_pool_spec.js
 create mode 100644 node_modules/needle/test/url_spec.js
 create mode 100644 node_modules/needle/test/utils/formidable.js
 create mode 100644 node_modules/needle/test/utils/proxy.js
 create mode 100644 node_modules/needle/test/utils/test.js
 create mode 100644 node_modules/node-pre-gyp/CHANGELOG.md
 create mode 100644 node_modules/node-pre-gyp/LICENSE
 create mode 100644 node_modules/node-pre-gyp/README.md
 create mode 100644 node_modules/node-pre-gyp/appveyor.yml
 create mode 100755 node_modules/node-pre-gyp/bin/node-pre-gyp
 create mode 100644 node_modules/node-pre-gyp/bin/node-pre-gyp.cmd
 create mode 100644 node_modules/node-pre-gyp/contributing.md
 create mode 100644 node_modules/node-pre-gyp/lib/build.js
 create mode 100644 node_modules/node-pre-gyp/lib/clean.js
 create mode 100644 node_modules/node-pre-gyp/lib/configure.js
 create mode 100644 node_modules/node-pre-gyp/lib/info.js
 create mode 100644 node_modules/node-pre-gyp/lib/install.js
 create mode 100644 node_modules/node-pre-gyp/lib/node-pre-gyp.js
 create mode 100644 node_modules/node-pre-gyp/lib/package.js
 create mode 100644 node_modules/node-pre-gyp/lib/pre-binding.js
 create mode 100644 node_modules/node-pre-gyp/lib/publish.js
 create mode 100644 node_modules/node-pre-gyp/lib/rebuild.js
 create mode 100644 node_modules/node-pre-gyp/lib/reinstall.js
 create mode 100644 node_modules/node-pre-gyp/lib/reveal.js
 create mode 100644 node_modules/node-pre-gyp/lib/testbinary.js
 create mode 100644 node_modules/node-pre-gyp/lib/testpackage.js
 create mode 100644 node_modules/node-pre-gyp/lib/unpublish.js
 create mode 100644 node_modules/node-pre-gyp/lib/util/abi_crosswalk.json
 create mode 100644 node_modules/node-pre-gyp/lib/util/compile.js
 create mode 100644 node_modules/node-pre-gyp/lib/util/handle_gyp_opts.js
 create mode 100644 node_modules/node-pre-gyp/lib/util/napi.js
 create mode 100644 node_modules/node-pre-gyp/lib/util/nw-pre-gyp/index.html
 create mode 100644 node_modules/node-pre-gyp/lib/util/nw-pre-gyp/package.json
 create mode 100644 node_modules/node-pre-gyp/lib/util/s3_setup.js
 create mode 100644 node_modules/node-pre-gyp/lib/util/versioning.js
 create mode 100644 node_modules/node-pre-gyp/package.json
 create mode 100644 node_modules/nopt/.npmignore
 create mode 100644 node_modules/nopt/.travis.yml
 create mode 100644 node_modules/nopt/CHANGELOG.md
 create mode 100644 node_modules/nopt/LICENSE
 create mode 100644 node_modules/nopt/README.md
 create mode 100755 node_modules/nopt/bin/nopt.js
 create mode 100755 node_modules/nopt/examples/my-program.js
 create mode 100644 node_modules/nopt/lib/nopt.js
 create mode 100644 node_modules/nopt/package.json
 create mode 100644 node_modules/nopt/test/basic.js
 create mode 100644 node_modules/npm-bundled/LICENSE
 create mode 100644 node_modules/npm-bundled/README.md
 create mode 100644 node_modules/npm-bundled/index.js
 create mode 100644 node_modules/npm-bundled/package.json
 create mode 100644 node_modules/npm-packlist/LICENSE
 create mode 100644 node_modules/npm-packlist/README.md
 create mode 100644 node_modules/npm-packlist/index.js
 create mode 100644 node_modules/npm-packlist/package.json
 create mode 100644 node_modules/npmlog/CHANGELOG.md
 create mode 100644 node_modules/npmlog/LICENSE
 create mode 100644 node_modules/npmlog/README.md
 create mode 100644 node_modules/npmlog/log.js
 create mode 100644 node_modules/npmlog/package.json
 create mode 100644 node_modules/number-is-nan/index.js
 create mode 100644 node_modules/number-is-nan/license
 create mode 100644 node_modules/number-is-nan/package.json
 create mode 100644 node_modules/number-is-nan/readme.md
 create mode 100644 node_modules/object-assign/index.js
 create mode 100644 node_modules/object-assign/license
 create mode 100644 node_modules/object-assign/package.json
 create mode 100644 node_modules/object-assign/readme.md
 create mode 100644 node_modules/once/LICENSE
 create mode 100644 node_modules/once/README.md
 create mode 100644 node_modules/once/once.js
 create mode 100644 node_modules/once/package.json
 create mode 100644 node_modules/os-homedir/index.js
 create mode 100644 node_modules/os-homedir/license
 create mode 100644 node_modules/os-homedir/package.json
 create mode 100644 node_modules/os-homedir/readme.md
 create mode 100644 node_modules/os-tmpdir/index.js
 create mode 100644 node_modules/os-tmpdir/license
 create mode 100644 node_modules/os-tmpdir/package.json
 create mode 100644 node_modules/os-tmpdir/readme.md
 create mode 100644 node_modules/osenv/LICENSE
 create mode 100644 node_modules/osenv/README.md
 create mode 100644 node_modules/osenv/osenv.js
 create mode 100644 node_modules/osenv/package.json
 create mode 100644 node_modules/path-is-absolute/index.js
 create mode 100644 node_modules/path-is-absolute/license
 create mode 100644 node_modules/path-is-absolute/package.json
 create mode 100644 node_modules/path-is-absolute/readme.md
 create mode 100644 node_modules/process-nextick-args/index.js
 create mode 100644 node_modules/process-nextick-args/license.md
 create mode 100644 node_modules/process-nextick-args/package.json
 create mode 100644 node_modules/process-nextick-args/readme.md
 create mode 100644 node_modules/rc/LICENSE.APACHE2
 create mode 100644 node_modules/rc/LICENSE.BSD
 create mode 100644 node_modules/rc/LICENSE.MIT
 create mode 100644 node_modules/rc/README.md
 create mode 100644 node_modules/rc/browser.js
 create mode 100755 node_modules/rc/cli.js
 create mode 100755 node_modules/rc/index.js
 create mode 100644 node_modules/rc/lib/utils.js
 create mode 100644 node_modules/rc/node_modules/minimist/.travis.yml
 create mode 100644 node_modules/rc/node_modules/minimist/LICENSE
 create mode 100644 node_modules/rc/node_modules/minimist/example/parse.js
 create mode 100644 node_modules/rc/node_modules/minimist/index.js
 create mode 100644 node_modules/rc/node_modules/minimist/package.json
 create mode 100644 node_modules/rc/node_modules/minimist/readme.markdown
 create mode 100644 node_modules/rc/node_modules/minimist/test/all_bool.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/bool.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/dash.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/default_bool.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/dotted.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/kv_short.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/long.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/num.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/parse.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/parse_modified.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/short.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/stop_early.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/unknown.js
 create mode 100644 node_modules/rc/node_modules/minimist/test/whitespace.js
 create mode 100644 node_modules/rc/package.json
 create mode 100644 node_modules/rc/test/ini.js
 create mode 100644 node_modules/rc/test/nested-env-vars.js
 create mode 100644 node_modules/rc/test/test.js
 create mode 100644 node_modules/readable-stream/.travis.yml
 create mode 100644 node_modules/readable-stream/CONTRIBUTING.md
 create mode 100644 node_modules/readable-stream/GOVERNANCE.md
 create mode 100644 node_modules/readable-stream/LICENSE
 create mode 100644 node_modules/readable-stream/README.md
 create mode 100644 node_modules/readable-stream/doc/wg-meetings/2015-01-30.md
 create mode 100644 node_modules/readable-stream/duplex-browser.js
 create mode 100644 node_modules/readable-stream/duplex.js
 create mode 100644 node_modules/readable-stream/lib/_stream_duplex.js
 create mode 100644 node_modules/readable-stream/lib/_stream_passthrough.js
 create mode 100644 node_modules/readable-stream/lib/_stream_readable.js
 create mode 100644 node_modules/readable-stream/lib/_stream_transform.js
 create mode 100644 node_modules/readable-stream/lib/_stream_writable.js
 create mode 100644 node_modules/readable-stream/lib/internal/streams/BufferList.js
 create mode 100644 node_modules/readable-stream/lib/internal/streams/destroy.js
 create mode 100644 node_modules/readable-stream/lib/internal/streams/stream-browser.js
 create mode 100644 node_modules/readable-stream/lib/internal/streams/stream.js
 create mode 100644 node_modules/readable-stream/package.json
 create mode 100644 node_modules/readable-stream/passthrough.js
 create mode 100644 node_modules/readable-stream/readable-browser.js
 create mode 100644 node_modules/readable-stream/readable.js
 create mode 100644 node_modules/readable-stream/transform.js
 create mode 100644 node_modules/readable-stream/writable-browser.js
 create mode 100644 node_modules/readable-stream/writable.js
 create mode 100644 node_modules/rimraf/LICENSE
 create mode 100644 node_modules/rimraf/README.md
 create mode 100755 node_modules/rimraf/bin.js
 create mode 100644 node_modules/rimraf/package.json
 create mode 100644 node_modules/rimraf/rimraf.js
 create mode 100644 node_modules/safe-buffer/LICENSE
 create mode 100644 node_modules/safe-buffer/README.md
 create mode 100644 node_modules/safe-buffer/index.d.ts
 create mode 100644 node_modules/safe-buffer/index.js
 create mode 100644 node_modules/safe-buffer/package.json
 create mode 100644 node_modules/safer-buffer/LICENSE
 create mode 100644 node_modules/safer-buffer/Porting-Buffer.md
 create mode 100644 node_modules/safer-buffer/Readme.md
 create mode 100644 node_modules/safer-buffer/dangerous.js
 create mode 100644 node_modules/safer-buffer/package.json
 create mode 100644 node_modules/safer-buffer/safer.js
 create mode 100644 node_modules/safer-buffer/tests.js
 create mode 100644 node_modules/sax/LICENSE
 create mode 100644 node_modules/sax/README.md
 create mode 100644 node_modules/sax/lib/sax.js
 create mode 100644 node_modules/sax/package.json
 create mode 100644 node_modules/semver/CHANGELOG.md
 create mode 100644 node_modules/semver/LICENSE
 create mode 100644 node_modules/semver/README.md
 create mode 100755 node_modules/semver/bin/semver
 create mode 100644 node_modules/semver/package.json
 create mode 100644 node_modules/semver/range.bnf
 create mode 100644 node_modules/semver/semver.js
 create mode 100644 node_modules/set-blocking/CHANGELOG.md
 create mode 100644 node_modules/set-blocking/LICENSE.txt
 create mode 100644 node_modules/set-blocking/README.md
 create mode 100644 node_modules/set-blocking/index.js
 create mode 100644 node_modules/set-blocking/package.json
 create mode 100644 node_modules/signal-exit/CHANGELOG.md
 create mode 100644 node_modules/signal-exit/LICENSE.txt
 create mode 100644 node_modules/signal-exit/README.md
 create mode 100644 node_modules/signal-exit/index.js
 create mode 100644 node_modules/signal-exit/package.json
 create mode 100644 node_modules/signal-exit/signals.js
 create mode 100644 node_modules/string-width/index.js
 create mode 100644 node_modules/string-width/license
 create mode 100644 node_modules/string-width/package.json
 create mode 100644 node_modules/string-width/readme.md
 create mode 100644 node_modules/string_decoder/.travis.yml
 create mode 100644 node_modules/string_decoder/LICENSE
 create mode 100644 node_modules/string_decoder/README.md
 create mode 100644 node_modules/string_decoder/lib/string_decoder.js
 create mode 100644 node_modules/string_decoder/package.json
 create mode 100644 node_modules/strip-ansi/index.js
 create mode 100644 node_modules/strip-ansi/license
 create mode 100644 node_modules/strip-ansi/package.json
 create mode 100644 node_modules/strip-ansi/readme.md
 create mode 100644 node_modules/strip-json-comments/index.js
 create mode 100644 node_modules/strip-json-comments/license
 create mode 100644 node_modules/strip-json-comments/package.json
 create mode 100644 node_modules/strip-json-comments/readme.md
 create mode 100644 node_modules/tar/LICENSE
 create mode 100644 node_modules/tar/README.md
 create mode 100644 node_modules/tar/index.js
 create mode 100644 node_modules/tar/lib/.mkdir.js.swp
 create mode 100644 node_modules/tar/lib/buffer.js
 create mode 100644 node_modules/tar/lib/create.js
 create mode 100644 node_modules/tar/lib/extract.js
 create mode 100644 node_modules/tar/lib/header.js
 create mode 100644 node_modules/tar/lib/high-level-opt.js
 create mode 100644 node_modules/tar/lib/large-numbers.js
 create mode 100644 node_modules/tar/lib/list.js
 create mode 100644 node_modules/tar/lib/mkdir.js
 create mode 100644 node_modules/tar/lib/mode-fix.js
 create mode 100644 node_modules/tar/lib/pack.js
 create mode 100644 node_modules/tar/lib/parse.js
 create mode 100644 node_modules/tar/lib/pax.js
 create mode 100644 node_modules/tar/lib/read-entry.js
 create mode 100644 node_modules/tar/lib/replace.js
 create mode 100644 node_modules/tar/lib/types.js
 create mode 100644 node_modules/tar/lib/unpack.js
 create mode 100644 node_modules/tar/lib/update.js
 create mode 100644 node_modules/tar/lib/warn-mixin.js
 create mode 100644 node_modules/tar/lib/winchars.js
 create mode 100644 node_modules/tar/lib/write-entry.js
 create mode 100644 node_modules/tar/package.json
 create mode 100644 node_modules/util-deprecate/History.md
 create mode 100644 node_modules/util-deprecate/LICENSE
 create mode 100644 node_modules/util-deprecate/README.md
 create mode 100644 node_modules/util-deprecate/browser.js
 create mode 100644 node_modules/util-deprecate/node.js
 create mode 100644 node_modules/util-deprecate/package.json
 create mode 100644 node_modules/wide-align/LICENSE
 create mode 100644 node_modules/wide-align/README.md
 create mode 100644 node_modules/wide-align/align.js
 create mode 100644 node_modules/wide-align/package.json
 create mode 100644 node_modules/wrappy/LICENSE
 create mode 100644 node_modules/wrappy/README.md
 create mode 100644 node_modules/wrappy/package.json
 create mode 100644 node_modules/wrappy/wrappy.js
 create mode 100644 node_modules/yallist/LICENSE
 create mode 100644 node_modules/yallist/README.md
 create mode 100644 node_modules/yallist/iterator.js
 create mode 100644 node_modules/yallist/package.json
 create mode 100644 node_modules/yallist/yallist.js
 create mode 100644 package-lock.json
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git push origin master
To https://github.com/Stormlight-Coding/my-webpage.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/Stormlight-Coding/my-webpage.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> code2

Jonathans-MacBook-Pro:webpage2 jonathanposo$ git pull https://github.com/Stormlight-Coding/my-webpage.git
From https://github.com/Stormlight-Coding/my-webpage
 * branch            HEAD       -> FETCH_HEAD
Merge made by the 'recursive' strategy.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git remote add origin https://github.com/Stormlight-Coding/my-webpage.git
fatal: remote origin already exists.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git push origin master
To https://github.com/Stormlight-Coding/my-webpage.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/Stormlight-Coding/my-webpage.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git clone https://github.com/Stormlight-Coding/my-webpage.git
Cloning into 'my-webpage'...
remote: Enumerating objects: 1754, done.
remote: Counting objects: 100% (1754/1754), done.
remote: Compressing objects: 100% (1667/1667), done.
remote: Total 1754 (delta 100), reused 1717 (delta 82), pack-reused
Receiving objects: 100% (1754/1754), 18.33 MiB | 2.58 MiB/s, done.
Resolving deltas: 100% (100/100), done.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git add *
warning: adding embedded git repository: my-webpage
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint:
hint: 	git submodule add <url> my-webpage
hint:
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint:
hint: 	git rm --cached my-webpage
hint:
hint: See "git help submodule" for more information.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git commit -m "test"
[code2 e7ede7b] test
 1 file changed, 1 insertion(+)
 create mode 160000 my-webpage
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git push origin master
To https://github.com/Stormlight-Coding/my-webpage.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/Stormlight-Coding/my-webpage.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ ls
Webpage			db.sqlite3		node_modules		requirements.txt
apps			manage.py		package-lock.json
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git log
commit e7ede7ba7833d0e901ae67dafdef53b56e64fe72 (HEAD -> code2)
Author: Stormlight-Coding <jonposo.music@gmail.com>
Date:   Tue Aug 13 13:44:27 2019 -0700

    test

commit 7a5c7613ad0ad81ae1cc1d0dc77f315a5a18e16b
Merge: 09177c3 5a9e84e
Author: Stormlight-Coding <jonposo.music@gmail.com>
Date:   Tue Aug 13 13:42:00 2019 -0700

    updated 8-13

commit 09177c36cab992ab3c2fb30d4aba7b3917440a6e
Author: Stormlight-Coding <jonposo.music@gmail.com>
Date:   Tue Aug 13 13:41:19 2019 -0700

    updated 8-13

commit 5a9e84e181d3d59fe18573c9e1d031bde764696e (origin/master)
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 15:34:15 2019 -0700

    Add files via upload

commit ff2ef4af5e80a86f440997663621994d68f9ece6
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 15:33:22 2019 -0700

    Delete Jonathan Poso - Resume.pdf

commit e7af1ea3eb14cc715f938bdea4948ab4569890f2
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 13:52:06 2019 -0700

    Add files via upload

commit 468d0d506a98b47ba218456f93cf1d732c01f902
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 13:33:41 2019 -0700

    Add files via upload

commit 0e64c57594a18dd01e245f4bc1235aa5949c1d24
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 13:33:19 2019 -0700

    Delete home.html

commit 1f1e3afc2a2a9547f2a323671bd3c86941fa8ec4
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 13:33:01 2019 -0700

    Add files via upload

commit aa193ee23cfffc382c3d09a80d1518c9051a3a8b (origin/updated-images, origin/code2, updated-images, master)
Author: Stormlight-Coding <jonposo.music@gmail.com>
Date:   Tue Apr 2 13:43:25 2019 -0700

    updated-req
Jonathans-MacBook-Pro:webpage2 jonathanposo$ ls
Webpage			db.sqlite3		node_modules		requirements.txt
apps			manage.py		package-lock.json
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git add *
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git commit -m "update"
[code2 aafe12b] update
 2 files changed, 0 insertions(+), 0 deletions(-)
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git log
commit aafe12bb38d6a32b4cfd4b3248632af85abc1f4c (HEAD -> code2)
Author: Stormlight-Coding <jonposo.music@gmail.com>
Date:   Tue Aug 13 13:50:44 2019 -0700

    update

commit e7ede7ba7833d0e901ae67dafdef53b56e64fe72
Author: Stormlight-Coding <jonposo.music@gmail.com>
Date:   Tue Aug 13 13:44:27 2019 -0700

    test

commit 7a5c7613ad0ad81ae1cc1d0dc77f315a5a18e16b
Merge: 09177c3 5a9e84e
Author: Stormlight-Coding <jonposo.music@gmail.com>
Date:   Tue Aug 13 13:42:00 2019 -0700

    updated 8-13

commit 09177c36cab992ab3c2fb30d4aba7b3917440a6e
Author: Stormlight-Coding <jonposo.music@gmail.com>
Date:   Tue Aug 13 13:41:19 2019 -0700

    updated 8-13

commit 5a9e84e181d3d59fe18573c9e1d031bde764696e (origin/master)
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 15:34:15 2019 -0700

    Add files via upload

commit ff2ef4af5e80a86f440997663621994d68f9ece6
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 15:33:22 2019 -0700

    Delete Jonathan Poso - Resume.pdf

commit e7af1ea3eb14cc715f938bdea4948ab4569890f2
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 13:52:06 2019 -0700

    Add files via upload

commit 468d0d506a98b47ba218456f93cf1d732c01f902
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 13:33:41 2019 -0700

    Add files via upload

commit 0e64c57594a18dd01e245f4bc1235aa5949c1d24
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 13:33:19 2019 -0700

    Delete home.html

commit 1f1e3afc2a2a9547f2a323671bd3c86941fa8ec4
Author: Stormlight-Coding <48965215+Stormlight-Coding@users.noreply.github.com>
Date:   Wed Apr 3 13:33:01 2019 -0700

    Add files via upload

commit aa193ee23cfffc382c3d09a80d1518c9051a3a8b (origin/updated-images, origin/code2, updated-images, master)
Author: Stormlight-Coding <jonposo.music@gmail.com>
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git push origin master
To https://github.com/Stormlight-Coding/my-webpage.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/Stormlight-Coding/my-webpage.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> code2

Jonathans-MacBook-Pro:webpage2 jonathanposo$ git pull https://github.com/Stormlight-Coding/my-webpage.git
From https://github.com/Stormlight-Coding/my-webpage
 * branch            HEAD       -> FETCH_HEAD
Already up to date.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git push origin master
To https://github.com/Stormlight-Coding/my-webpage.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/Stormlight-Coding/my-webpage.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git pull https://github.com/Stormlight-Coding/my-webpage.git
From https://github.com/Stormlight-Coding/my-webpage
 * branch            HEAD       -> FETCH_HEAD
Already up to date.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git add *
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git commit -m "test4"
On branch code2
Changes not staged for commit:
	modified:   .DS_Store
	deleted:    my-webpage

no changes added to commit
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git push origin master
To https://github.com/Stormlight-Coding/my-webpage.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/Stormlight-Coding/my-webpage.git'
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. Check out this branch and integrate the remote changes
hint: (e.g. 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git remote add origin https://github.com/Stormlight-Coding/my-webpage.git
fatal: remote origin already exists.
Jonathans-MacBook-Pro:webpage2 jonathanposo$ git branch -a
* code2
  master
  updated-images
  remotes/origin/code2
  remotes/origin/master
  remotes/origin/updated-images
Jonathans-MacBook-Pro:webpage2 jonathanposo$ ls
Webpage			db.sqlite3		node_modules		requirements.txt
apps			manage.py		package-lock.json
Jonathans-MacBook-Pro:webpage2 jonathanposo$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
August 13, 2019 - 21:01:12
Django version 1.10, using settings 'Webpage.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[13/Aug/2019 21:01:16] "GET / HTTP/1.1" 200 19899
[13/Aug/2019 21:01:18] "GET /static/personal_page/resume/Jonathan%20Poso%20-%20Resume%202019.pdf HTTP/1.1" 200 58634
Not Found: /favicon.ico
[13/Aug/2019 21:01:18] "GET /favicon.ico HTTP/1.1" 404 2448
^CJonathans-MacBook-Pro:webpage2 jonathanposo$ ls
Webpage			db.sqlite3		node_modules		requirements.txt
apps			manage.py		package-lock.json
Jonathans-MacBook-Pro:webpage2 jonathanposo$ cd ../
Jonathans-MacBook-Pro:my_environments jonathanposo$ cd ../../
Jonathans-MacBook-Pro:desktop jonathanposo$ ls
18yuer9k13rdnjpg.jpg
2D-Art-Ivan-Tao-Samurais-Soul-992x1483.jpg
AskBran.Net.webarchive
Book A Brainstorm.docx
Code
Coldplay "Clocks" Sheet Music (Easy Piano) in G Major (transposable) - Download & Print - SKU: MN004.webarchive
Coldplay a sky full of stars @ Amsterdam Arena 24-06-2016.mp4
Cole.pages
Date.docx
Glass Clown.m4a
IMG_7001 2.jpeg
Idea thing.scriv
Images
Job Stuff
Jonathan Poso - Resume 2019.pdf
LB-Home.png
LB-Steak-Modern-American-1.png
MUSIC
P R O L O G U E copy.docx
Rowyn was lost and he knew he would be in trouble again.docx
Screen Shot 2019-02-16 at 10.20.35 AM.png
Screen Shot 2019-02-16 at 10.20.41 AM.png
Screen Shot 2019-03-14 at 3.34.23 PM.png
Screen Shot 2019-03-15 at 3.08.10 PM.png
Screen Shot 2019-03-15 at 3.09.56 PM.png
Screen Shot 2019-03-15 at 3.11.59 PM.png
Screen Shot 2019-03-15 at 3.14.50 PM.png
Screen Shot 2019-05-09 at 12.04.51 PM.png
Screen Shot 2019-05-14 at 2.47.46 PM.png
Screen Shot 2019-05-19 at 10.19.59 PM.png
Screen Shot 2019-05-19 at 10.21.15 PM.png
Screen Shot 2019-05-29 at 6.47.54 PM.png
Screen Shot 2019-05-31 at 2.48.51 PM.png
Screen Shot 2019-05-31 at 2.50.54 PM.png
Screen Shot 2019-06-24 at 3.17.01 PM.png
Spotify-icon.jpg
Tales of the Llore.docx
The_Order.scriv
Untitled 3.mov
Untitled 4.mov
Untitled 6.mov
Untitled.scriv
Yuja Wang - Variations on the Turkish March (Odeonsplatz).mp4
baratheon.jpg
books.sql
cards
cheat-sheet-8-01.numbers
crest.jpg
dinb.mov
july-budget.numbers
my life stuff.docx
patrik-rosander-starwars-redesign-illustration.jpg
red-bone.mov
redbone-cover.mov
ref_letter.pages
somethin.mov
star-wars-wallpapers_291130703.jpg
stark.jpg
starwarsart1.jpg
test.jpg
test2.jpg
test3.jpg
test4.jpg
test5.jpg
test6.jpg
test7.jpg
thoughts and things.pages
webpage-logo.png
wedding-banner.png
wedding-invites.xls.numbers
wedding-invites.xls.xlsx
wiki.py
wiki.pyc
wolf_cub.scriv
Jonathans-MacBook-Pro:desktop jonathanposo$ cd music
Jonathans-MacBook-Pro:music jonathanposo$ l;s
-bash: l: command not found
-bash: s: command not found
Jonathans-MacBook-Pro:music jonathanposo$ ls
Focusrite_Drum_Pack			PK
Icon?					Podcasts
LYRICS					STRATA
Merry-Christmas-Songbook copy 2.pdf	Things to learn
Jonathans-MacBook-Pro:music jonathanposo$ cd pk
Jonathans-MacBook-Pro:pk jonathanposo$ ls
django_pem.pem	web-pem-1.pem
Jonathans-MacBook-Pro:pk jonathanposo$ chmod 400 web-pem-1.pem
Jonathans-MacBook-Pro:pk jonathanposo$ ssh -i "web-pem-1.pem" ubuntu@ec2-3-17-172-255.us-east-2.compute.amazonaws.com
Welcome to Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-1075-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

58 packages can be updated.
0 updates are security updates.


*** System restart required ***
Last login: Tue Jul 30 20:42:06 2019 from 50.255.1.45
ubuntu@ip-172-31-16-179:~$ sudo apt-get update
Hit:1 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial InRelease
Get:2 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial-updates InRelease [109 kB]
Get:3 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial-backports InRelease [107 kB]
Get:4 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial-updates/main Sources [339 kB]
Get:5 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial-updates/universe Sources [260 kB]
Get:6 http://security.ubuntu.com/ubuntu xenial-security InRelease [109 kB]
Get:7 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial-updates/multiverse Sources [8,764 B]
Get:8 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial-updates/main amd64 Packages [1,009 kB]
Get:9 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial-updates/main Translation-en [396 kB]
Get:10 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial-updates/universe amd64 Packages [760 kB]
Get:11 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial-updates/universe Translation-en [318 kB]
Get:12 http://us-east-2.ec2.archive.ubuntu.com/ubuntu xenial-updates/multiverse amd64 Packages [16.7 kB]
Get:13 http://security.ubuntu.com/ubuntu xenial-security/main Sources [152 kB]
Get:14 http://security.ubuntu.com/ubuntu xenial-security/multiverse Sources [3,416 B]
Get:15 http://security.ubuntu.com/ubuntu xenial-security/main amd64 Packages [710 kB]
Get:16 http://security.ubuntu.com/ubuntu xenial-security/universe amd64 Packages [452 kB]
Get:17 http://security.ubuntu.com/ubuntu xenial-security/multiverse amd64 Packages [5,600 B]
Fetched 4,756 kB in 1s (3,232 kB/s)
Reading package lists... Done
ubuntu@ip-172-31-16-179:~$ ls
my-webpage  venv
ubuntu@ip-172-31-16-179:~$ cd my-webpage
ubuntu@ip-172-31-16-179:~/my-webpage$ ls
apps        manage.py         settings.py  venv     Webpage.sock
db.sqlite3  requirements.txt  static       Webpage
ubuntu@ip-172-31-16-179:~/my-webpage$ cd apps
ubuntu@ip-172-31-16-179:~/my-webpage/apps$ ls
__init__.py  personal_page  __pycache__
ubuntu@ip-172-31-16-179:~/my-webpage/apps$ cd personal_page
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page$ ls
admin.py     __init__.py  models.py          __pycache__  templates  views.py
apps.py      LICENSE      package.json       README.md    tests.py
gulpfile.js  migrations   package-lock.json  static       urls.py
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page$ cd templates
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/templates$ ls
personal_page
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/templates$ cd personal_project
-bash: cd: personal_project: No such file or directory
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/templates$ cd personal_pagels
-bash: cd: personal_pagels: No such file or directory
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/templates$ ls
personal_page
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/templates$ cd personal_page
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/templates/personal_page$ ls
algo.html  barry.html  home.html  smartlist.html
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/templates/personal_page$ sudo vim home.html
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/templates/personal_page$ ls
algo.html  barry.html  home.html  smartlist.html
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/templates/personal_page$ cd ../../
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page$ ls
admin.py     __init__.py  models.py          __pycache__  templates  views.py
apps.py      LICENSE      package.json       README.md    tests.py
gulpfile.js  migrations   package-lock.json  static       urls.py
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page$ cd static
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static$ ls
personal_page
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static$ cd personal_page
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page$ ls
amazon.png          github.png           json.png             resume           swift.png
angular.png         git.png              materialize.png      resume.css       typescript.png
bootstrap-logo.png  html.png             mongoDB.png          resume-icon.png  vendor
css.png             img                  mySQL.png            resume.min.css
django.png          iOS.png              node.png             ruby.png
fire.png            JavaScript-logo.png  postgresql-logo.png  scss
flask.png           js                   python.png           squile.png
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page$ cd resume
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page/resume$ ls
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page/resume$ cd ../
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page$ ls
amazon.png          github.png           json.png             resume           swift.png
angular.png         git.png              materialize.png      resume.css       typescript.png
bootstrap-logo.png  html.png             mongoDB.png          resume-icon.png  vendor
css.png             img                  mySQL.png            resume.min.css
django.png          iOS.png              node.png             ruby.png
fire.png            JavaScript-logo.png  postgresql-logo.png  scss
flask.png           js                   python.png           squile.png
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page$ cd resume
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page/resume$ ls
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page/resume$ ls
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page/resume$ scp -i "web-pem-1.pem" Jonathan Poso - Resume 2019.pdf ubuntu@ec2-3-17-172-255.us-east-2.compute.amazonaws.com:Jonathan Poso - Resume 2019.pdf
2019.pdf: No such file or directory
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page/resume$ ls
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page/resume$ ^C
ubuntu@ip-172-31-16-179:~/my-webpage/apps/personal_page/static/personal_page/resume$ exit
logout
Connection to ec2-3-17-172-255.us-east-2.compute.amazonaws.com closed.
Jonathans-MacBook-Pro:pk jonathanposo$ chmod 400 web-pem-1.pem
Jonathans-MacBook-Pro:pk jonathanposo$ ssh -i "web-pem-1.pem" ubuntu@ec2-3-17-172-255.us-east-2.compute.amazonaws.com
Welcome to Ubuntu 16.04.5 LTS (GNU/Linux 4.4.0-1075-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

66 packages can be updated.
0 updates are security updates.

New release '18.04.2 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Tue Aug 13 21:30:02 2019 from 50.255.1.45
ubuntu@ip-172-31-16-179:~$ do-release-upgrade
Checking for a new Ubuntu release
Please install all available updates for your release before upgrading.
ubuntu@ip-172-31-16-179:~$ ls
my-webpage  venv
ubuntu@ip-172-31-16-179:~$ cd my_webpage
-bash: cd: my_webpage: No such file or directory
ubuntu@ip-172-31-16-179:~$ cd my-webpage
ubuntu@ip-172-31-16-179:~/my-webpage$ ls
apps        manage.py         settings.py  venv     Webpage.sock
db.sqlite3  requirements.txt  static       Webpage
ubuntu@ip-172-31-16-179:~/my-webpage$ cd webpage
-bash: cd: webpage: No such file or directory
ubuntu@ip-172-31-16-179:~/my-webpage$ ls
apps        manage.py         settings.py  venv     Webpage.sock
db.sqlite3  requirements.txt  static       Webpage
ubuntu@ip-172-31-16-179:~/my-webpage$ cd Webpage
ubuntu@ip-172-31-16-179:~/my-webpage/Webpage$ ls
__init__.py  __pycache__  settings.py  urls.py  wsgi.py
ubuntu@ip-172-31-16-179:~/my-webpage/Webpage$ sudo vim settings.py

"""
Django settings for Webpage project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^$z4ch5*en9=3ftlr8b25$!d3o&zqa&&c7y26ed$-(d+9t@on='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['3.17.172.255', 'www.jonposo.com', 'jonposo.com', 'jonathanposo.com', 'www.jonathanposo.com']


# Application definition

INSTALLED_APPS = [
    'apps.personal_page',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Webpage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
-- INSERT --                                                                 1,1           Top
