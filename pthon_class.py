# class person:
#     pass
#
# p=person()
# print p
####################################
#  class Person:
#     def sayHi(self):
#         print 'Hello, how are you?'
#
#  p = Person().sayHi()
# print p
######################################
class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print 'Hello, my name is', self.name

p = Person ('anand')
p.sayHi()