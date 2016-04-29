#!/usr/bin/env python
# encoding: utf-8

@logit()
def myfunc1():
    pass
class email_logit(logit):


    def __init__(self, email='liuwenju@honliv.com', *args, **kwargs):
        sefl.email = email
        super(logit, self).__init__(*args, **kwargs)


    def notify(self):
        pass
