"""
1002655776: contrasena123   // sysadmin
1002655777: 123456          // administrativo
1002655778: nuevacontrasena // Vendedor
1002655778: 234567          // Vendedor
"""
"""
1002655776: 123456          // SysAdmin
1002655777: 234567          // Administrativo 1
1002655778: 345678          // Administrativo 2
1002655779: 456789          // Administrativo 3
1002655779: 567890          // Vendedor 1
1002655779: 678901          // Vendedor 2
1002655779: 789012          // Vendedor 3
"""
users = (
(1002655777, 234567, 1, 1,'Juano Guevara'),
(1002655778, 345678, 1, 2,'Juana Guevara'),
(1002655779, 456789, 1, 3,'Juanes Guevara'),
(1002655780, 567890, 0, 1,'Juanito Guevara'),
(1002655781, 678901, 0, 2,'Juanita Guevara'),
(1002655782, 789012, 0, 3,'Juano No Guevara'))

from hashlib import sha256

h = sha256()
for user in users:
    h.update(str(user[1]).encode())
    consigna = f"INSERT INTO USUARIOS VALUES( {user[0]}, '{h.hexdigest()}', {user[2]}, {user[3]}, '{user[4]}' );"
    print(consigna)
