#!/usr/bin/env python
# encoding: utf-8

try:
    print "I am sure no exception is going to occur."
except Exception:
    print "exception"
else:

    # Those codes only work at try has no exception
    # But those eccept will not catch
    print 'This would only run if no exception occurs. And an error here '
finally:
    print "This would be printed in every case. "
    # output: I am sure no exception is going to occur!
    # This would only run if no exception occurs.
    # This would be printed in every case.
