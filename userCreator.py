"""
1002655776: contrasena123   // sysadmin
1002655777: 123456          // administrativo
1002655778: nuevacontrasena // Vendedor
1002655778: 234567          // Vendedor
"""
"""
1002655776: 123456          // SysAdmin
"""

from hashlib import sha256

h = sha256()
h.update(b'123456')
consigna = f"INSERT INTO USUARIOS VALUES( 1002655776, '{h.hexdigest()}', 0, 0, 'Juan Esteban Guevara Roncancio' );"
print(consigna)
