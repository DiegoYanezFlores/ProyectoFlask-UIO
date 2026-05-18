#database/models.py
from . import db

class Usuario(db.Model):
    # Representamos a bibliotecarios o administradores del sistema, No a los usuarios que piden prestamos
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    contrasena = db.Column(db.String(50), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    activo = db.Column(db.Boolean, nullable=False, default=True)
    
    #Relaciones con otras tablas
    libros_registrado = db.relationship('Libro', backref='bibliotecario', lazy=True)
    prestamos_tramitados = db.relationship('Prestamo', backref='bibliotecario', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'rol': self.rol
        }

class Cliente(db.Model):
    #Aqui van a estar los socios o los que piden prestados libros
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    cedula = db.Column(db.String(20), unique=True, nullable=False)
    fecha_registro = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    #Relaciones con otras tablas
    prestamos = db.relationship('Prestamo', backref='cliente', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cedula': self.cedula,
            'miembro_desde': self.fecha_registro,
            'email': self.email,
            'telefono': self.telefono
        }

class Libro(db.Model):
    # Tabla que contiene los libros de la biblioteca
    __tablename__ = 'libros'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    autor = db.Column(db.String(50), nullable=False)
    editorial = db.Column(db.String(50), nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.String(50), unique=True, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

    def to_dict(self):

        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'editorial': self.editorial,
            'anio': self.anio,
            'isbn': self.isbn,
            'stock': self.stock
        }   
    
    def to_dict_relacional(self):
        """Diccionario anidado que inyecta los objetos relacionados cargados en memoria."""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'editorial': self.editorial,
            'anio': self.anio,
            'isbn': self.isbn,
            'stock': self.stock,
            'categoria': {
                'id': self.categoria.id,
                'nombre': self.categoria.nombre
            } if self.categoria else None,
            'registrado_por': {
                'id': self.bibliotecario.id,
                'nombre': self.bibliotecario.nombre,
                'rol': self.bibliotecario.rol
            } if self.bibliotecario else None
        }

    #Relaciones con otras tablas
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    prestamos = db.relationship('Prestamo', backref='libro', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'editorial': self.editorial,
            'anio': self.anio,
            'isbn': self.isbn,
            'stock': self.stock
        }   

class Categoria(db.Model):
    #Tabla que contiene las categorias de los libros
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)

    #Relaciones con otras tablas    
    libros = db.relationship('Libro', backref='categoria', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
        }

class Prestamo(db.Model):
    __tablename__ = 'prestamos'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha_prestamo = db.Column(db.Date, nullable=False)
    fecha_devolucion = db.Column(db.Date, nullable=False)
    fecha_entrega = db.Column(db.Date, nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    multa = db.Column(db.Float, nullable=False, default=0.0)
    
    #Relaciones con otras tablas
    libro_id = db.Column(db.Integer, db.ForeignKey('libros.id'), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'fecha_prestamo': self.fecha_prestamo,
            'fecha_devolucion': self.fecha_devolucion,
            'fecha_entrega': self.fecha_entrega,
            'estado': self.estado,
            'multa': self.multa,
            'libro_id': self.libro_id,
            'cliente_id': self.cliente_id,
            'usuario_id': self.usuario_id
        }   