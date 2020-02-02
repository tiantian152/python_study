class A(object):    # ()中是继承的对象
    pass

a1 = A()
a2 = A()

print(a1)
print(a2)

# <__main__.A object at 0x00000188A2DEA5C8>
# <__main__.A object at 0x00000188A2DEA648>
# at后的是对象所在的地址