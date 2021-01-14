st = "     python is very fun     "

print(st)
print("{}{}{}".format('*', st.strip(), '*'))
print("{}{}{}".format('*', st.rstrip(), '*'))
print("{}{}{}".format('*', st.lstrip(), '*'))

st2 = '--p--y--t--h--o--n'
print(st2.strip('-'))
print(st2.rstrip('-'))
print(st2.lstrip('-'))

st3 = '2020/09/09'
print(st3.replace('/','.'))
print(st3.replace('2020','2014'))
print(st3.replace(st[0:4],'2014'))
