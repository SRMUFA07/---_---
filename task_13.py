# B6
# A	.html
# Б	www.
# В	/
# Г	ftp
# Д	.ru
# Е	http
# Ж	index
# З	://
# http://www.ftp.ru/index.html
# Ответ: ЕЗБГДВЖА

# B6.1
# a	info
# b	/
# c	.net
# d	.edu
# e	http
# f	exam
# g	://
# hhtp://info.edu/exam.net
# Ответ: egadbfc


# Сеть задана IP-адресом 172.16.168.0 и маской сети 255.255.248.0.
# Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не кратно 5?
# from ipaddress import *

# net = ip_network('172.16.168.0/255.255.248.0', 0)
# result = 0

# for ip in net:
#     ip_bin = f'{ip:b}'
#     if ip_bin.count('1') % 5 != 0:
#         result += 1

# print(result)


