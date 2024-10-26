import reflex as rx



class Index(rx.Component):
    library="/public/pages/index"
    tag="HomePage"
    
# Define los componentes basados en tu estructura de carpetas de Next.js
class Products(rx.Component):
    library = "/public/pages/admin/productos"
    tag = "AdminProductos"

class Users(rx.Component):
    library = "/public/pages/admin/usuarios"
    tag = "AdminUsuarios"

class LibroDetalles(rx.Component):
    library = "/public/pages/libros/[id]"
    tag = "LibroDetallesPage"

class UsuarioDetalles(rx.Component):
    library = "/public/pages/usuarios/[id]"
    tag = "UsuarioDetallesPage"

class Cart(rx.Component):
    library = "/public/pages/cart"
    tag = "CartPage"

class UsuarioIndex(rx.Component):
    library = "/public/pages/index"
    tag = "UsuarioIndex"

class Login(rx.Component):
    library = "/public/pages/login"
    tag = "LoginPage"

class Register(rx.Component):
    library = "/public/pages/register"
    tag = "RegisterPage"


def Index_component():
    return Index.create()

def Products_component():
    return Products.create()

def Users_component():
    return Users.create()

def LibroDetalles_component():
    return LibroDetalles.create()

def UsuarioDetalles_component():
    return UsuarioDetalles.create()

def Cart_component():
    return Cart.create()

def UsuarioIndex_component():
    return UsuarioIndex.create()

def Login_component():
    return Login.create()

def Register_component():
    return Register.create()

# Define la aplicación y sus rutas
app = rx.App()

app.add_page(Index_component,route="/")                         # Ruta raíz que usa el componente Hello
app.add_page(Products_component, route="/admin/products")  # Ruta para productos
app.add_page(Users_component, route="/admin/users")        # Ruta para usuarios en admin
app.add_page(LibroDetalles_component, route="/libros/[id]")  # Ruta dinámica para detalles del libro
app.add_page(UsuarioDetalles_component, route="/usuarios/[id]")  # Ruta dinámica para detalles del usuario
app.add_page(Cart_component, route="/cart")       # Ruta para el carrito de usuarios
# app.add_page(UsuarioIndex_component,route="/usuarios")    # Ruta principal para usuarios
app.add_page(Login_component, route="/login")     # Ruta para login de usuarios
app.add_page(Register_component, route="/register")  # Ruta para registro de usuarios

# # Inicia la aplicación de Reflex
# app.run()
