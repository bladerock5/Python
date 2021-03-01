from ldap3 import Server, Connection, SUBTREE

AD_SERVER = '10.2.2.2'
AD_USER = 'Andrey.Naumov@softline.com'
print('Пароль:')
AD_PASSWORD = input()
AD_SEARCH_TREE = 'DC=office,DC=softline,DC=ru'

server = Server(AD_SERVER)
conn = Connection(server, user=AD_USER, password=AD_PASSWORD)
conn.bind()
attr =  ['*'] #['sAMAccountName', 'legacyExchangeDN']
search_filter = '(objectClass=Person)'
#        (objectClass=inetOrgPerson)
#        (!(cn=Tim Howes))
#        (&(objectClass=Person)(|(sn=Jensen)(cn=Babs J*)))
#        (o=univ*of*mich*)
#        (seeAlso=)
conn.search(AD_SEARCH_TREE, search_filter, SUBTREE, attributes=attr)
print(len(conn.entries))

print(conn.entries[0].sAMAccountName)
print(conn.entries[0])
print('=====================================================================')