def split_decarator(function):
    def inner():
        func=function()
        string_split=func.split()
        print((string_split))
        return string_split
    return inner
@split_decarator
def hello():
    return 'hello world'
# hello=split_decarator(hello)
hello()


# def division(function):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return function(a,b)
#     return inner
#
# @division
# def div(a,b):
#     return a/b
#
# print(div(2,4))