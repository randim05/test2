real_password = '123'


def wrong_password(password):
    return (password == "" or (not password and real_password)) or password != real_password

# password == "" --> False
#
# not password --> False
#
# real_password -- > True
#
# (True and True)(a and b) --> b --> real_password!!!!!!
#
# False or True(False or real_password) --> real_password
#
# password != real_password True if ne sovpali
# password != real_password False if SOVPALI
# need False
#
# real_password or False --> real_password


def solve():
    # Write your code here
    print(wrong_password(False))


# passwd = '321'
# # passwd = '123'
# # passwd = ''
# solve(passwd)
# print(False == '')