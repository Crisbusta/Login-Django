# Login-Django
Este es un sistema de creación de usuarios, está desarrollado en Django 3.0 + docker + postgresql. 

# Funcionalidad
Este es un proyecto de Django el cual nos facilita la creación de usuarios mediante los modelos User que provee Django, además de eso extendemos el modelo User proveido por Django
y le agregamos atributos personalizados. 

La aplicación auth_login es la que se encarga de todo el proceso de autenticación de usuarios, la aplicación de accounts fue creada solo con el fin de poder extender el modelo User (con el cual trabajamos en la aplicación auth_login)
