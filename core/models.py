from django.template.defaultfilters import slugify
import os
from model_utils.models import TimeStampedModel
from django.contrib.auth import get_user_model

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

#USUARIOS
class User(AbstractUser):
    REGION = [
        ('Región de Arica y Parinacota', 'Arica y Parinacota'),('Región de Tarapacá', 'Tarapacá'),
        ('Región de Antofagasta', 'Antofagasta'),
        ('Región de Atacama', 'Atacama'),
        ('Región de Coquimbo', 'Coquimbo'),
        ('Región de Valparaíso', 'Valparaíso'),
        ('Región Metropolitana de Santiago', 'Metropolitana de Santiago'),
        ('Región del Libertador General Bernardo OHiggins', 'OHiggins'),
        ('Región del Maule', 'Maule'),
        ('Región de Ñuble', 'Ñuble'),
        ('Región del Biobío', 'Biobío'),
        ('Región de La Araucanía', 'La Araucanía'),
        ('Región de Los Ríos', 'Los Ríos'),
        ('Región de Los Lagos', 'Los Lagos'),
        ('Región de Aysén del General Carlos Ibáñez del Campo', 'Aysén del General Carlos Ibáñez del Campo'),
        ('Región de Magallanes y de la Antártica Chilena', 'Magallanes y de la Antártica Chilena')
    ] 
    COMUNA = [
        ('Algarrobo', 'Algarrobo'), ('Alhué', 'Alhué'), ('Alto Biobío', 'Alto Biobío'), ('Alto del Carmen', 'Alto del Carmen'), ('Alto Hospicio', 'Alto Hospicio'),
        ('Ancud', 'Ancud'), ('Andacollo', 'Andacollo'), ('Angol', 'Angol'), ('Antártica', 'Antártica'), ('Antofagasta', 'Antofagasta'),
        ('Arauco', 'Arauco'), ('Arica', 'Arica'), ('Buin', 'Buin'), ('Bulnes', 'Bulnes'), ('Cabildo', 'Cabildo'), ('Cabo de Hornos (Ex Navarino)', 'Cabo de Hornos (Ex Navarino)'),
        ('Cabrero', 'Cabrero'), ('Calama', 'Calama'), ('Calbuco', 'Calbuco'), ('Caldera', 'Caldera'), ('Calera', 'Calera'),
        ('Calera de Tango', 'Calera de Tango'), ('Calle Larga', 'Calle Larga'), ('Camarones', 'Camarones'), ('Camiña', 'Camiña'), ('Canete', 'Cañete'),
        ('Carahue', 'Carahue'), ('Cartagena', 'Cartagena'), ('Casablanca', 'Casablanca'), ('Castro', 'Castro'), ('Catemu', 'Catemu'),
        ('Cauquenes', 'Cauquenes'), ('Cerrillos', 'Cerrillos'), ('Cerro Navia', 'Cerro Navia'), ('Chaitén', 'Chaitén'), ('Chanco', 'Chanco'),
        ('Chañaral', 'Chañaral'), ('Chépica', 'Chépica'), ('Chiguayante', 'Chiguayante'), ('Chile Chico', 'Chile Chico'), ('Chillán', 'Chillán'),
        ('Chillán Viejo', 'Chillán Viejo'), ('Chimbarongo', 'Chimbarongo'), ('Cholchol', 'Cholchol'), ('Chonchi', 'Chonchi'), ('Cisnes', 'Cisnes'),
        ('Cobquecura', 'Cobquecura'), ('Cochamó', 'Cochamó'), ('Cochrane', 'Cochrane'), ('Codegua', 'Codegua'), ('Coelemu', 'Coelemu'),
        ('Coihaique', 'Coihaique'), ('Coihueco', 'Coihueco'), ('Coinco', 'Coinco'), ('Colbún', 'Colbún'), ('Colchane', 'Colchane'),
        ('Colina', 'Colina'), ('Collipulli', 'Collipulli'), ('Coltauco', 'Coltauco'), ('Combarbalá', 'Combarbalá'), ('Concepción', 'Concepción'),
        ('Conchalí', 'Conchalí'), ('Constitución', 'Constitución'), ('Contulmo', 'Contulmo'), ('Copiapó', 'Copiapó'), ('Coquimbo', 'Coquimbo'),
        ('Coronel', 'Coronel'), ('Corral', 'Corral'), ('Cunco', 'Cunco'), ('Curacautín', 'Curacautín'), ('Curacaví', 'Curacaví'),
        ('Curaco de Vélez', 'Curaco de Vélez'), ('Curanilahue', 'Curanilahue'), ('Curarrehue', 'Curarrehue'), ('Curepto', 'Curepto'), ('Curicó', 'Curicó'),
        ('Dalcahue', 'Dalcahue'), ('Diego de Almagro', 'Diego de Almagro'), ('Doñihue', 'Doñihue'), ('El Bosque', 'El Bosque'), ('El Carmen', 'El Carmen'),
        ('El Monte', 'El Monte'), ('El Quisco', 'El Quisco'), ('El Tabo', 'El Tabo'), ('Empedrado', 'Empedrado'), ('Ercilla', 'Ercilla'),
        ('Estación Central', 'Estación Central'), ('Florida', 'Florida'), ('Freire', 'Freire'), ('Freirina', 'Freirina'), ('Fresia', 'Fresia'),
        ('Frutillar', 'Frutillar'), ('Futaleufú', 'Futaleufú'), ('Futrono', 'Futrono'), ('Galvarino', 'Galvarino'), ('General Lagos', 'General Lagos'),
        ('Gorbea', 'Gorbea'), ('Graneros', 'Graneros'), ('Guaitecas', 'Guaitecas'), ('Hijuelas', 'Hijuelas'), ('Hualaihué', 'Hualaihué'),
        ('Hualañé', 'Hualañé'), ('Hualpén', 'Hualpén'), ('Hualqui', 'Hualqui'), ('Huara', 'Huara'), ('Huasco', 'Huasco'),
        ('Huechuraba', 'Huechuraba'), ('Illapel', 'Illapel'), ('Independencia', 'Independencia'), ('Iquique', 'Iquique'), ('Isla de Maipo', 'Isla de Maipo'),
        ('Isla de Pascua', 'Isla de Pascua'), ('Juan Fernández', 'Juan Fernández'), ('La Calera', 'La Calera'), ('La Cisterna', 'La Cisterna'),
        ('La Cruz', 'La Cruz'), ('La Estrella', 'La Estrella'), ('La Florida', 'La Florida'), ('La Granja', 'La Granja'), ('La Higuera', 'La Higuera'),
        ('La Ligua', 'La Ligua'), ('La Pintana', 'La Pintana'), ('La Reina', 'La Reina'), ('La Serena', 'La Serena'), ('La Unión', 'La Unión'),
        ('Lago Ranco', 'Lago Ranco'), ('Lago Verde', 'Lago Verde'), ('Laguna Blanca', 'Laguna Blanca'), ('Laja', 'Laja'), ('Lampa', 'Lampa'),
        ('Lanco', 'Lanco'), ('Las Cabras', 'Las Cabras'), ('Las Condes', 'Las Condes'), ('Lautaro', 'Lautaro'), ('Lebu', 'Lebu'),
        ('Licantén', 'Licantén'), ('Limache', 'Limache'), ('Linares', 'Linares'), ('Litueche', 'Litueche'), ('Llanquihue', 'Llanquihue'),
        ('Lo Barnechea', 'Lo Barnechea'), ('Lo Espejo', 'Lo Espejo'), ('Lo Prado', 'Lo Prado'), ('Lolol', 'Lolol'), ('Loncoche', 'Loncoche'),
        ('Longaví', 'Longaví'), ('Lonquimay', 'Lonquimay'), ('Los Alamos', 'Los Álamos'), ('Los Andes', 'Los Andes'), ('Los Ángeles', 'Los Ángeles'),
        ('Los Lagos', 'Los Lagos'), ('Los Muermos', 'Los Muermos'), ('Los Sauces', 'Los Sauces'), ('Los Vilos', 'Los Vilos'), ('Lota', 'Lota'),
        ('Lumaco', 'Lumaco'), ('Machalí', 'Machalí'), ('Macul', 'Macul'), ('Máfil', 'Máfil'), ('Maipú', 'Maipú'), ('Malloa', 'Malloa'),
        ('Marchihue', 'Marchihue'), ('María Elena', 'María Elena'), ('María Pinto', 'María Pinto'), ('Mariquina', 'Mariquina'), ('Maule', 'Maule'),
        ('Maullín', 'Maullín'), ('Mejillones', 'Mejillones'), ('Melipeuco', 'Melipeuco'), ('Melipilla', 'Melipilla'), ('Molina', 'Molina'),
        ('Monte Patria', 'Monte Patria'), ('Mostazal', 'Mostazal'), ('Mulchén', 'Mulchén'), ('Nacimiento', 'Nacimiento'), ('Nancagua', 'Nancagua'),
        ('Natales', 'Natales'), ('Navidad', 'Navidad'), ('Negrete', 'Negrete'), ('Ninhue', 'Ninhue'), ('Ñiquén', 'Ñiquén'),
        ('Nogales', 'Nogales'), ('Nueva Imperial', 'Nueva Imperial'), ('Ñuñoa', 'Ñuñoa'), ('Olivar', 'Olivar'), ('Ollagüe', 'Ollagüe'),
        ('Olmue', 'Olmué'), ('Osorno', 'Osorno'), ('Ovalle', 'Ovalle'), ('Padre Hurtado', 'Padre Hurtado'), ('Padre Las Casas', 'Padre Las Casas'),
        ('Paihuano', 'Paihuano'), ('Paillaco', 'Paillaco'), ('Paine', 'Paine'), ('Palena', 'Palena'), ('Palmilla', 'Palmilla'),
        ('Panguipulli', 'Panguipulli'), ('Panquehue', 'Panquehue'), ('Papudo', 'Papudo'), ('Paredones', 'Paredones'), ('Parral', 'Parral'),
        ('Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'), ('Pelarco', 'Pelarco'), ('Pelluhue', 'Pelluhue'), ('Pemuco', 'Pemuco'), ('Pencahue', 'Pencahue'),
        ('Penco', 'Penco'), ('Peñaflor', 'Peñaflor'), ('Peñalolén', 'Peñalolén'), ('Peralillo', 'Peralillo'), ('Perquenco', 'Perquenco'),
        ('Petorca', 'Petorca'), ('Peumo', 'Peumo'), ('Pica', 'Pica'), ('Pichidegua', 'Pichidegua'), ('Pichilemu', 'Pichilemu'),
        ('Pinto', 'Pinto'), ('Pirque', 'Pirque'), ('Pitrufquén', 'Pitrufquén'), ('Placilla', 'Placilla'), ('Portezuelo', 'Portezuelo'),
        ('Porvenir', 'Porvenir'), ('Pozo Almonte', 'Pozo Almonte'), ('Primavera', 'Primavera'), ('Providencia', 'Providencia'), ('Puchuncaví', 'Puchuncaví'),
        ('Pucón', 'Pucón'), ('Pudahuel', 'Pudahuel'), ('Puente Alto', 'Puente Alto'), ('Puerto Montt', 'Puerto Montt'), ('Puerto Octay', 'Puerto Octay'),
        ('Puerto Varas', 'Puerto Varas'), ('Pumanque', 'Pumanque'), ('Punitaqui', 'Punitaqui'), ('Punta Arenas', 'Punta Arenas'), ('Puqueldón', 'Puqueldón'),
        ('Purén', 'Purén'), ('Purranque', 'Purranque'), ('Putaendo', 'Putaendo'), ('Putre', 'Putre'), ('Puyehue', 'Puyehue'),
        ('Queilen', 'Queilen'), ('Quellón', 'Quellón'), ('Quemchi', 'Quemchi'), ('Quilaco', 'Quilaco'), ('Quilicura', 'Quilicura'),
        ('Quilleco', 'Quilleco'), ('Quillón', 'Quillón'), ('Quillota', 'Quillota'), ('Quilpué', 'Quilpué'), ('Quinchao', 'Quinchao'),
        ('Quinta de Tilcoco', 'Quinta de Tilcoco'), ('Quinta Normal', 'Quinta Normal'), ('Quintero', 'Quintero'), ('Quirihue', 'Quirihue'), ('Rancagua', 'Rancagua'),
        ('Ránquil', 'Ránquil'), ('Rauco', 'Rauco'), ('Recoleta', 'Recoleta'), ('Renaico', 'Renaico'), ('Renca', 'Renca'),
        ('Rengo', 'Rengo'), ('Requínoa', 'Requínoa'), ('Retiro', 'Retiro'), ('Rinconada', 'Rinconada'), ('Rio Bueno', 'Río Bueno'),
        ('Río Claro', 'Río Claro'), ('Río Hurtado', 'Río Hurtado'), ('Río Ibáñez', 'Río Ibáñez'), ('Río Negro', 'Río Negro'), ('Río Verde', 'Río Verde'),
        ('Romeral', 'Romeral'), ('Saavedra', 'Saavedra'), ('Sagrada Familia', 'Sagrada Familia'), ('Salamanca', 'Salamanca'), ('San Antonio', 'San Antonio'),
        ('San Bernardo', 'San Bernardo'), ('San Carlos', 'San Carlos'), ('San Clemente', 'San Clemente'), ('San Esteban', 'San Esteban'), ('San Fabián', 'San Fabián'),
        ('San Felipe', 'San Felipe'), ('San Fernando', 'San Fernando'), ('San Gregorio', 'San Gregorio'), ('San Ignacio', 'San Ignacio'), ('San Javier', 'San Javier'),
        ('San Joaquín', 'San Joaquín'), ('San José de Maipo', 'San José de Maipo'), ('San Juan de la Costa', 'San Juan de la Costa'), ('San Miguel', 'San Miguel'),
        ('San Nicolás', 'San Nicolás'), ('San Pablo', 'San Pablo'), ('San Pedro', 'San Pedro'), ('San Pedro de Atacama', 'San Pedro de Atacama'), ('San Pedro de la Paz', 'San Pedro de la Paz'),
        ('San Rafael', 'San Rafael'), ('San Ramón', 'San Ramón'), ('San Rosendo', 'San Rosendo'), ('San Vicente', 'San Vicente'), ('Santa Bárbara', 'Santa Bárbara'),
        ('Santa Cruz', 'Santa Cruz'), ('Santa Juana', 'Santa Juana'), ('Santa María', 'Santa María'), ('Santiago', 'Santiago'), ('Santo Domingo', 'Santo Domingo'),
        ('Sierra Gorda', 'Sierra Gorda'), ('Talagante', 'Talagante'), ('Talca', 'Talca'), ('Talcahuano', 'Talcahuano'), ('Taltal', 'Taltal'),
        ('Temuco', 'Temuco'), ('Teno', 'Teno'), ('Teodoro Schmidt', 'Teodoro Schmidt'), ('Tierra Amarilla', 'Tierra Amarilla'), ('Tiltil', 'Tiltil'),
        ('Timaukel', 'Timaukel'), ('Tirúa', 'Tirúa'), ('Tocopilla', 'Tocopilla'), ('Toltén', 'Toltén'), ('Tomé', 'Tomé'),
        ('Torres del Paine', 'Torres del Paine'), ('Tortel', 'Tortel'), ('Traiguén', 'Traiguén'), ('Trehuaco', 'Trehuaco'), ('Tucapel', 'Tucapel'),
        ('Valdivia', 'Valdivia'), ('Vallenar', 'Vallenar'), ('Valparaíso', 'Valparaíso'), ('Vichuquén', 'Vichuquén'), ('Victoria', 'Victoria'),
        ('Vicuña', 'Vicuña'), ('Vilcún', 'Vilcún'), ('Villa Alegre', 'Villa Alegre'), ('Villa Alemana', 'Villa Alemana'), ('Villarrica', 'Villarrica'),
        ('Viña del Mar', 'Viña del Mar'), ('Vitacura', 'Vitacura'), ('Yerbas Buenas', 'Yerbas Buenas'), ('Yumbel', 'Yumbel'),
        ('Yungay', 'Yungay'), ('Zapallar', 'Zapallar')
    ]

    picture = models.ImageField(default = 'users/profile_default.png', upload_to='media/users/')
    direccion = models.CharField(max_length=60, null=True, blank =True)
    region = models.CharField(max_length=200, choices=REGION, default=REGION[0][0])
    comuna = models.CharField(max_length=200, choices=COMUNA, default=COMUNA[0][0])
    telefono = models.BigIntegerField(null=True)
    fecha_nac = models.DateField(null=True)
    tipo_user = models.CharField(max_length=60, null=True, blank =True)

#PRODUCTO

class Producto(models.Model):

    PLATAFORMA = [
                    ('', '----'),
                    ('PlayStation 5', 'PlayStation 5'),
                    ('Xbox Series X', 'Xbox Series X'),
                    ('Xbox 360', 'Xbox 360'),
                    ('Nintendo Switch', 'Nintendo Switch'),
                    ('PC Gaming', 'PC Gaming'),
                    ('PlayStation 4', 'PlayStation 4'),
                    ('Xbox One', 'Xbox One'),
                    ('Nintendo 3DS', 'Nintendo 3DS'),
                    ('Sega Genesis Mini', 'Sega Genesis Mini'),
                    ('Super Nintendo Entertainment System (SNES) Classic Edition', 'Super Nintendo Entertainment System (SNES) Classic Edition'),
                    ('Nintendo Entertainment System (NES) Classic Edition', 'Nintendo Entertainment System (NES) Classic Edition')
        ]

    CATEGORIA = [
                    ('', '----'),
                    ('Acción', 'Acción'),
                    ('Aventura', 'Aventura'),
                    ('Estrategia', 'Estrategia'),
                    ('RPG', 'RPG'),
                    ('Deportes', 'Deportes'),
                    ('Música', 'Música'),
                    ('Carreras', 'Carreras'),
                    ('Puzzle', 'Puzzle'),
                    ('Plataformas', 'Plataformas'),
                    ('Shooter', 'Shooter'),
                    ('Simulación', 'Simulación')
        ]

    TIPO_PRODUCTO = [
                        ('', '----'),
                        ('Juego Físico','Juego Físico'),
                        ('Accesorio','Accesorio'),
                        ('Código Digital','Código Digital'),    
                    ] 
 
    id_producto = models.CharField(max_length = 255, unique = True, null = True, blank= True)
    nombre = models.CharField(max_length = 255, unique = True, null = True)
    descripcion = models.CharField(max_length = 255, unique = True, null = False)
    categoria = models.CharField(max_length=200, choices=CATEGORIA, default=CATEGORIA[0][0])
    plataforma = models.CharField(max_length=200, choices=PLATAFORMA, default=PLATAFORMA[0][0])
    tipo_producto = models.CharField(max_length=200, choices=TIPO_PRODUCTO, default=TIPO_PRODUCTO[0][0])
    picture = models.ImageField(upload_to = 'media/productos/', null = True, blank = True)
    costo = models.IntegerField(null = False)
    cantidad = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'producto'
            verbose_name_plural = 'productos'
            order_with_respect_to = 'tipo_producto'

    def __str__(self):
        return self.id_producto


class Codigo(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='codigos', default=1)
    codigo = models.CharField(max_length = 255, unique = True, null = True, blank= True)

    class Meta:
            verbose_name = 'codigo'
            verbose_name_plural = 'codigos'
            order_with_respect_to = 'codigo'

    def __str__(self):
        return self.codigo

class Compra(models.Model):

    PLATAFORMA = [
                    ('', '----'),
                    ('PlayStation 5', 'PlayStation 5'),
                    ('Xbox Series X', 'Xbox Series X'),
                    ('Xbox 360', 'Xbox 360'),
                    ('Nintendo Switch', 'Nintendo Switch'),
                    ('PC Gaming', 'PC Gaming'),
                    ('PlayStation 4', 'PlayStation 4'),
                    ('Xbox One', 'Xbox One'),
                    ('Nintendo 3DS', 'Nintendo 3DS'),
                    ('Sega Genesis Mini', 'Sega Genesis Mini'),
                    ('Super Nintendo Entertainment System (SNES) Classic Edition', 'Super Nintendo Entertainment System (SNES) Classic Edition'),
                    ('Nintendo Entertainment System (NES) Classic Edition', 'Nintendo Entertainment System (NES) Classic Edition')
        ]

    TIPO_PRODUCTO = [
                        ('', '----'),
                        ('Juego Físico','Juego Físico'),
                        ('Accesorio','Accesorio'),
                        ('Código Digital','Código Digital'),
                    ] 
    
    ESTADO_ORDEN = [
                        ('', '----'),
                        ('Bloqueada','Bloqueada'),
                        ('Aceptada','Aceptada'),
                        ('Pendiente','Pendiente'),
                    ] 
    
    id_orden = models.CharField(max_length = 255, unique = True, null = True, blank= True)
    sku = models.CharField(max_length = 255, unique = True, null = True)
    nombre = models.CharField(max_length = 255, unique = True, null = True)
    proveedor = models.CharField(max_length = 255, unique = True, null = True)
    plataforma = models.CharField(max_length=200, choices=PLATAFORMA, default=PLATAFORMA[0][0])
    tipo_producto = models.CharField(max_length=200, choices=TIPO_PRODUCTO, default=TIPO_PRODUCTO[0][0])
    costo = models.IntegerField(null = False)
    cantidad = models.IntegerField(null = False)
    estado_orden = models.CharField(max_length=200, choices=ESTADO_ORDEN, default=ESTADO_ORDEN[0][0])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'compra'
            verbose_name_plural = 'compras'
            order_with_respect_to = 'id_orden'
 

#ÓRDENES

class Order(TimeStampedModel):
    REGION = [
                ('Región de Arica y Parinacota', 'Arica y Parinacota'),('Región de Tarapacá', 'Tarapacá'),
                ('Región de Antofagasta', 'Antofagasta'),
                ('Región de Atacama', 'Atacama'),
                ('Región de Coquimbo', 'Coquimbo'),
                ('Región de Valparaíso', 'Valparaíso'),
                ('Región Metropolitana de Santiago', 'Metropolitana de Santiago'),
                ('Región del Libertador General Bernardo OHiggins', 'OHiggins'),
                ('Región del Maule', 'Maule'),
                ('Región de Ñuble', 'Ñuble'),
                ('Región del Biobío', 'Biobío'),
                ('Región de La Araucanía', 'La Araucanía'),
                ('Región de Los Ríos', 'Los Ríos'),
                ('Región de Los Lagos', 'Los Lagos'),
                ('Región de Aysén del General Carlos Ibáñez del Campo', 'Aysén del General Carlos Ibáñez del Campo'),
                ('Región de Magallanes y de la Antártica Chilena', 'Magallanes y de la Antártica Chilena')
            ] 
    COMUNA = [
                ('Algarrobo', 'Algarrobo'), ('Alhué', 'Alhué'), ('Alto Biobío', 'Alto Biobío'), ('Alto del Carmen', 'Alto del Carmen'), ('Alto Hospicio', 'Alto Hospicio'),
                ('Ancud', 'Ancud'), ('Andacollo', 'Andacollo'), ('Angol', 'Angol'), ('Antártica', 'Antártica'), ('Antofagasta', 'Antofagasta'),
                ('Arauco', 'Arauco'), ('Arica', 'Arica'), ('Buin', 'Buin'), ('Bulnes', 'Bulnes'), ('Cabildo', 'Cabildo'), ('Cabo de Hornos (Ex Navarino)', 'Cabo de Hornos (Ex Navarino)'),
                ('Cabrero', 'Cabrero'), ('Calama', 'Calama'), ('Calbuco', 'Calbuco'), ('Caldera', 'Caldera'), ('Calera', 'Calera'),
                ('Calera de Tango', 'Calera de Tango'), ('Calle Larga', 'Calle Larga'), ('Camarones', 'Camarones'), ('Camiña', 'Camiña'), ('Canete', 'Cañete'),
                ('Carahue', 'Carahue'), ('Cartagena', 'Cartagena'), ('Casablanca', 'Casablanca'), ('Castro', 'Castro'), ('Catemu', 'Catemu'),
                ('Cauquenes', 'Cauquenes'), ('Cerrillos', 'Cerrillos'), ('Cerro Navia', 'Cerro Navia'), ('Chaitén', 'Chaitén'), ('Chanco', 'Chanco'),
                ('Chañaral', 'Chañaral'), ('Chépica', 'Chépica'), ('Chiguayante', 'Chiguayante'), ('Chile Chico', 'Chile Chico'), ('Chillán', 'Chillán'),
                ('Chillán Viejo', 'Chillán Viejo'), ('Chimbarongo', 'Chimbarongo'), ('Cholchol', 'Cholchol'), ('Chonchi', 'Chonchi'), ('Cisnes', 'Cisnes'),
                ('Cobquecura', 'Cobquecura'), ('Cochamó', 'Cochamó'), ('Cochrane', 'Cochrane'), ('Codegua', 'Codegua'), ('Coelemu', 'Coelemu'),
                ('Coihaique', 'Coihaique'), ('Coihueco', 'Coihueco'), ('Coinco', 'Coinco'), ('Colbún', 'Colbún'), ('Colchane', 'Colchane'),
                ('Colina', 'Colina'), ('Collipulli', 'Collipulli'), ('Coltauco', 'Coltauco'), ('Combarbalá', 'Combarbalá'), ('Concepción', 'Concepción'),
                ('Conchalí', 'Conchalí'), ('Constitución', 'Constitución'), ('Contulmo', 'Contulmo'), ('Copiapó', 'Copiapó'), ('Coquimbo', 'Coquimbo'),
                ('Coronel', 'Coronel'), ('Corral', 'Corral'), ('Cunco', 'Cunco'), ('Curacautín', 'Curacautín'), ('Curacaví', 'Curacaví'),
                ('Curaco de Vélez', 'Curaco de Vélez'), ('Curanilahue', 'Curanilahue'), ('Curarrehue', 'Curarrehue'), ('Curepto', 'Curepto'), ('Curicó', 'Curicó'),
                ('Dalcahue', 'Dalcahue'), ('Diego de Almagro', 'Diego de Almagro'), ('Doñihue', 'Doñihue'), ('El Bosque', 'El Bosque'), ('El Carmen', 'El Carmen'),
                ('El Monte', 'El Monte'), ('El Quisco', 'El Quisco'), ('El Tabo', 'El Tabo'), ('Empedrado', 'Empedrado'), ('Ercilla', 'Ercilla'),
                ('Estación Central', 'Estación Central'), ('Florida', 'Florida'), ('Freire', 'Freire'), ('Freirina', 'Freirina'), ('Fresia', 'Fresia'),
                ('Frutillar', 'Frutillar'), ('Futaleufú', 'Futaleufú'), ('Futrono', 'Futrono'), ('Galvarino', 'Galvarino'), ('General Lagos', 'General Lagos'),
                ('Gorbea', 'Gorbea'), ('Graneros', 'Graneros'), ('Guaitecas', 'Guaitecas'), ('Hijuelas', 'Hijuelas'), ('Hualaihué', 'Hualaihué'),
                ('Hualañé', 'Hualañé'), ('Hualpén', 'Hualpén'), ('Hualqui', 'Hualqui'), ('Huara', 'Huara'), ('Huasco', 'Huasco'),
                ('Huechuraba', 'Huechuraba'), ('Illapel', 'Illapel'), ('Independencia', 'Independencia'), ('Iquique', 'Iquique'), ('Isla de Maipo', 'Isla de Maipo'),
                ('Isla de Pascua', 'Isla de Pascua'), ('Juan Fernández', 'Juan Fernández'), ('La Calera', 'La Calera'), ('La Cisterna', 'La Cisterna'),
                ('La Cruz', 'La Cruz'), ('La Estrella', 'La Estrella'), ('La Florida', 'La Florida'), ('La Granja', 'La Granja'), ('La Higuera', 'La Higuera'),
                ('La Ligua', 'La Ligua'), ('La Pintana', 'La Pintana'), ('La Reina', 'La Reina'), ('La Serena', 'La Serena'), ('La Unión', 'La Unión'),
                ('Lago Ranco', 'Lago Ranco'), ('Lago Verde', 'Lago Verde'), ('Laguna Blanca', 'Laguna Blanca'), ('Laja', 'Laja'), ('Lampa', 'Lampa'),
                ('Lanco', 'Lanco'), ('Las Cabras', 'Las Cabras'), ('Las Condes', 'Las Condes'), ('Lautaro', 'Lautaro'), ('Lebu', 'Lebu'),
                ('Licantén', 'Licantén'), ('Limache', 'Limache'), ('Linares', 'Linares'), ('Litueche', 'Litueche'), ('Llanquihue', 'Llanquihue'),
                ('Lo Barnechea', 'Lo Barnechea'), ('Lo Espejo', 'Lo Espejo'), ('Lo Prado', 'Lo Prado'), ('Lolol', 'Lolol'), ('Loncoche', 'Loncoche'),
                ('Longaví', 'Longaví'), ('Lonquimay', 'Lonquimay'), ('Los Alamos', 'Los Álamos'), ('Los Andes', 'Los Andes'), ('Los Ángeles', 'Los Ángeles'),
                ('Los Lagos', 'Los Lagos'), ('Los Muermos', 'Los Muermos'), ('Los Sauces', 'Los Sauces'), ('Los Vilos', 'Los Vilos'), ('Lota', 'Lota'),
                ('Lumaco', 'Lumaco'), ('Machalí', 'Machalí'), ('Macul', 'Macul'), ('Máfil', 'Máfil'), ('Maipú', 'Maipú'), ('Malloa', 'Malloa'),
                ('Marchihue', 'Marchihue'), ('María Elena', 'María Elena'), ('María Pinto', 'María Pinto'), ('Mariquina', 'Mariquina'), ('Maule', 'Maule'),
                ('Maullín', 'Maullín'), ('Mejillones', 'Mejillones'), ('Melipeuco', 'Melipeuco'), ('Melipilla', 'Melipilla'), ('Molina', 'Molina'),
                ('Monte Patria', 'Monte Patria'), ('Mostazal', 'Mostazal'), ('Mulchén', 'Mulchén'), ('Nacimiento', 'Nacimiento'), ('Nancagua', 'Nancagua'),
                ('Natales', 'Natales'), ('Navidad', 'Navidad'), ('Negrete', 'Negrete'), ('Ninhue', 'Ninhue'), ('Ñiquén', 'Ñiquén'),
                ('Nogales', 'Nogales'), ('Nueva Imperial', 'Nueva Imperial'), ('Ñuñoa', 'Ñuñoa'), ('Olivar', 'Olivar'), ('Ollagüe', 'Ollagüe'),
                ('Olmue', 'Olmué'), ('Osorno', 'Osorno'), ('Ovalle', 'Ovalle'), ('Padre Hurtado', 'Padre Hurtado'), ('Padre Las Casas', 'Padre Las Casas'),
                ('Paihuano', 'Paihuano'), ('Paillaco', 'Paillaco'), ('Paine', 'Paine'), ('Palena', 'Palena'), ('Palmilla', 'Palmilla'),
                ('Panguipulli', 'Panguipulli'), ('Panquehue', 'Panquehue'), ('Papudo', 'Papudo'), ('Paredones', 'Paredones'), ('Parral', 'Parral'),
                ('Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'), ('Pelarco', 'Pelarco'), ('Pelluhue', 'Pelluhue'), ('Pemuco', 'Pemuco'), ('Pencahue', 'Pencahue'),
                ('Penco', 'Penco'), ('Peñaflor', 'Peñaflor'), ('Peñalolén', 'Peñalolén'), ('Peralillo', 'Peralillo'), ('Perquenco', 'Perquenco'),
                ('Petorca', 'Petorca'), ('Peumo', 'Peumo'), ('Pica', 'Pica'), ('Pichidegua', 'Pichidegua'), ('Pichilemu', 'Pichilemu'),
                ('Pinto', 'Pinto'), ('Pirque', 'Pirque'), ('Pitrufquén', 'Pitrufquén'), ('Placilla', 'Placilla'), ('Portezuelo', 'Portezuelo'),
                ('Porvenir', 'Porvenir'), ('Pozo Almonte', 'Pozo Almonte'), ('Primavera', 'Primavera'), ('Providencia', 'Providencia'), ('Puchuncaví', 'Puchuncaví'),
                ('Pucón', 'Pucón'), ('Pudahuel', 'Pudahuel'), ('Puente Alto', 'Puente Alto'), ('Puerto Montt', 'Puerto Montt'), ('Puerto Octay', 'Puerto Octay'),
                ('Puerto Varas', 'Puerto Varas'), ('Pumanque', 'Pumanque'), ('Punitaqui', 'Punitaqui'), ('Punta Arenas', 'Punta Arenas'), ('Puqueldón', 'Puqueldón'),
                ('Purén', 'Purén'), ('Purranque', 'Purranque'), ('Putaendo', 'Putaendo'), ('Putre', 'Putre'), ('Puyehue', 'Puyehue'),
                ('Queilen', 'Queilen'), ('Quellón', 'Quellón'), ('Quemchi', 'Quemchi'), ('Quilaco', 'Quilaco'), ('Quilicura', 'Quilicura'),
                ('Quilleco', 'Quilleco'), ('Quillón', 'Quillón'), ('Quillota', 'Quillota'), ('Quilpué', 'Quilpué'), ('Quinchao', 'Quinchao'),
                ('Quinta de Tilcoco', 'Quinta de Tilcoco'), ('Quinta Normal', 'Quinta Normal'), ('Quintero', 'Quintero'), ('Quirihue', 'Quirihue'), ('Rancagua', 'Rancagua'),
                ('Ránquil', 'Ránquil'), ('Rauco', 'Rauco'), ('Recoleta', 'Recoleta'), ('Renaico', 'Renaico'), ('Renca', 'Renca'),
                ('Rengo', 'Rengo'), ('Requínoa', 'Requínoa'), ('Retiro', 'Retiro'), ('Rinconada', 'Rinconada'), ('Rio Bueno', 'Río Bueno'),
                ('Río Claro', 'Río Claro'), ('Río Hurtado', 'Río Hurtado'), ('Río Ibáñez', 'Río Ibáñez'), ('Río Negro', 'Río Negro'), ('Río Verde', 'Río Verde'),
                ('Romeral', 'Romeral'), ('Saavedra', 'Saavedra'), ('Sagrada Familia', 'Sagrada Familia'), ('Salamanca', 'Salamanca'), ('San Antonio', 'San Antonio'),
                ('San Bernardo', 'San Bernardo'), ('San Carlos', 'San Carlos'), ('San Clemente', 'San Clemente'), ('San Esteban', 'San Esteban'), ('San Fabián', 'San Fabián'),
                ('San Felipe', 'San Felipe'), ('San Fernando', 'San Fernando'), ('San Gregorio', 'San Gregorio'), ('San Ignacio', 'San Ignacio'), ('San Javier', 'San Javier'),
                ('San Joaquín', 'San Joaquín'), ('San José de Maipo', 'San José de Maipo'), ('San Juan de la Costa', 'San Juan de la Costa'), ('San Miguel', 'San Miguel'),
                ('San Nicolás', 'San Nicolás'), ('San Pablo', 'San Pablo'), ('San Pedro', 'San Pedro'), ('San Pedro de Atacama', 'San Pedro de Atacama'), ('San Pedro de la Paz', 'San Pedro de la Paz'),
                ('San Rafael', 'San Rafael'), ('San Ramón', 'San Ramón'), ('San Rosendo', 'San Rosendo'), ('San Vicente', 'San Vicente'), ('Santa Bárbara', 'Santa Bárbara'),
                ('Santa Cruz', 'Santa Cruz'), ('Santa Juana', 'Santa Juana'), ('Santa María', 'Santa María'), ('Santiago', 'Santiago'), ('Santo Domingo', 'Santo Domingo'),
                ('Sierra Gorda', 'Sierra Gorda'), ('Talagante', 'Talagante'), ('Talca', 'Talca'), ('Talcahuano', 'Talcahuano'), ('Taltal', 'Taltal'),
                ('Temuco', 'Temuco'), ('Teno', 'Teno'), ('Teodoro Schmidt', 'Teodoro Schmidt'), ('Tierra Amarilla', 'Tierra Amarilla'), ('Tiltil', 'Tiltil'),
                ('Timaukel', 'Timaukel'), ('Tirúa', 'Tirúa'), ('Tocopilla', 'Tocopilla'), ('Toltén', 'Toltén'), ('Tomé', 'Tomé'),
                ('Torres del Paine', 'Torres del Paine'), ('Tortel', 'Tortel'), ('Traiguén', 'Traiguén'), ('Trehuaco', 'Trehuaco'), ('Tucapel', 'Tucapel'),
                ('Valdivia', 'Valdivia'), ('Vallenar', 'Vallenar'), ('Valparaíso', 'Valparaíso'), ('Vichuquén', 'Vichuquén'), ('Victoria', 'Victoria'),
                ('Vicuña', 'Vicuña'), ('Vilcún', 'Vilcún'), ('Villa Alegre', 'Villa Alegre'), ('Villa Alemana', 'Villa Alemana'), ('Villarrica', 'Villarrica'),
                ('Viña del Mar', 'Viña del Mar'), ('Vitacura', 'Vitacura'), ('Yerbas Buenas', 'Yerbas Buenas'), ('Yumbel', 'Yumbel'),
                ('Yungay', 'Yungay'), ('Zapallar', 'Zapallar')
            ]
    ESTADO_VENTA = [
                    ('En Preparación', 'En Preparación'),
                    ('En Ruta', 'En Ruta'),
                    ('Entregado', 'Entregado'),
    ]
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    direccion = models.CharField("Dirección", max_length=250, null = True)
    telefono = models.CharField("Teléfono", max_length=250, null = True)
    descripcion = models.CharField("Descripción", max_length=250, blank=True)
    region = models.CharField("Región", max_length=200, choices=REGION, default=REGION[0][0])
    comuna = models.CharField("Comuna", max_length=200, choices=COMUNA, default=COMUNA[0][0])
    estado_venta = models.CharField("Estado Órden", max_length=200, choices=ESTADO_VENTA, default=ESTADO_VENTA[0][0])
    is_pagado = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created", )
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"

    def __str__(self):
        return 'Compra {}'.format(self.id)

    def get_precio_total(self):
        total_costo = sum(item.get_precio_total() for item in self.items.all())
        return total_costo

    def get_description(self):
        descriptions = []
        for item in self.items.all():
            if item.producto.tipo_producto == "Código Digital" and item.codigo:
                description = ''
            else:
                description = '{} x {}'.format(item.cantidad, item.producto.nombre)
                if description.startswith(', '):
                    description = description[2:]
            if description:
                descriptions.append(description)
        
        return ", ".join(descriptions)







class Item(models.Model):
    orden = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name="order_items", on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(settings.CART_ITEM_MAX_CANTIDAD),])
    codigo = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return str(self.id)

    def get_precio_total(self):
        return self.costo * self.cantidad



class Orden(TimeStampedModel):
    
    REGION = [
                ('Región de Arica y Parinacota', 'Arica y Parinacota'),('Región de Tarapacá', 'Tarapacá'),
                ('Región de Antofagasta', 'Antofagasta'),
                ('Región de Atacama', 'Atacama'),
                ('Región de Coquimbo', 'Coquimbo'),
                ('Región de Valparaíso', 'Valparaíso'),
                ('Región Metropolitana de Santiago', 'Metropolitana de Santiago'),
                ('Región del Libertador General Bernardo OHiggins', 'OHiggins'),
                ('Región del Maule', 'Maule'),
                ('Región de Ñuble', 'Ñuble'),
                ('Región del Biobío', 'Biobío'),
                ('Región de La Araucanía', 'La Araucanía'),
                ('Región de Los Ríos', 'Los Ríos'),
                ('Región de Los Lagos', 'Los Lagos'),
                ('Región de Aysén del General Carlos Ibáñez del Campo', 'Aysén del General Carlos Ibáñez del Campo'),
                ('Región de Magallanes y de la Antártica Chilena', 'Magallanes y de la Antártica Chilena')
            ] 
    COMUNA = [
                ('Algarrobo', 'Algarrobo'), ('Alhué', 'Alhué'), ('Alto Biobío', 'Alto Biobío'), ('Alto del Carmen', 'Alto del Carmen'), ('Alto Hospicio', 'Alto Hospicio'),
                ('Ancud', 'Ancud'), ('Andacollo', 'Andacollo'), ('Angol', 'Angol'), ('Antártica', 'Antártica'), ('Antofagasta', 'Antofagasta'),
                ('Arauco', 'Arauco'), ('Arica', 'Arica'), ('Buin', 'Buin'), ('Bulnes', 'Bulnes'), ('Cabildo', 'Cabildo'), ('Cabo de Hornos (Ex Navarino)', 'Cabo de Hornos (Ex Navarino)'),
                ('Cabrero', 'Cabrero'), ('Calama', 'Calama'), ('Calbuco', 'Calbuco'), ('Caldera', 'Caldera'), ('Calera', 'Calera'),
                ('Calera de Tango', 'Calera de Tango'), ('Calle Larga', 'Calle Larga'), ('Camarones', 'Camarones'), ('Camiña', 'Camiña'), ('Canete', 'Cañete'),
                ('Carahue', 'Carahue'), ('Cartagena', 'Cartagena'), ('Casablanca', 'Casablanca'), ('Castro', 'Castro'), ('Catemu', 'Catemu'),
                ('Cauquenes', 'Cauquenes'), ('Cerrillos', 'Cerrillos'), ('Cerro Navia', 'Cerro Navia'), ('Chaitén', 'Chaitén'), ('Chanco', 'Chanco'),
                ('Chañaral', 'Chañaral'), ('Chépica', 'Chépica'), ('Chiguayante', 'Chiguayante'), ('Chile Chico', 'Chile Chico'), ('Chillán', 'Chillán'),
                ('Chillán Viejo', 'Chillán Viejo'), ('Chimbarongo', 'Chimbarongo'), ('Cholchol', 'Cholchol'), ('Chonchi', 'Chonchi'), ('Cisnes', 'Cisnes'),
                ('Cobquecura', 'Cobquecura'), ('Cochamó', 'Cochamó'), ('Cochrane', 'Cochrane'), ('Codegua', 'Codegua'), ('Coelemu', 'Coelemu'),
                ('Coihaique', 'Coihaique'), ('Coihueco', 'Coihueco'), ('Coinco', 'Coinco'), ('Colbún', 'Colbún'), ('Colchane', 'Colchane'),
                ('Colina', 'Colina'), ('Collipulli', 'Collipulli'), ('Coltauco', 'Coltauco'), ('Combarbalá', 'Combarbalá'), ('Concepción', 'Concepción'),
                ('Conchalí', 'Conchalí'), ('Constitución', 'Constitución'), ('Contulmo', 'Contulmo'), ('Copiapó', 'Copiapó'), ('Coquimbo', 'Coquimbo'),
                ('Coronel', 'Coronel'), ('Corral', 'Corral'), ('Cunco', 'Cunco'), ('Curacautín', 'Curacautín'), ('Curacaví', 'Curacaví'),
                ('Curaco de Vélez', 'Curaco de Vélez'), ('Curanilahue', 'Curanilahue'), ('Curarrehue', 'Curarrehue'), ('Curepto', 'Curepto'), ('Curicó', 'Curicó'),
                ('Dalcahue', 'Dalcahue'), ('Diego de Almagro', 'Diego de Almagro'), ('Doñihue', 'Doñihue'), ('El Bosque', 'El Bosque'), ('El Carmen', 'El Carmen'),
                ('El Monte', 'El Monte'), ('El Quisco', 'El Quisco'), ('El Tabo', 'El Tabo'), ('Empedrado', 'Empedrado'), ('Ercilla', 'Ercilla'),
                ('Estación Central', 'Estación Central'), ('Florida', 'Florida'), ('Freire', 'Freire'), ('Freirina', 'Freirina'), ('Fresia', 'Fresia'),
                ('Frutillar', 'Frutillar'), ('Futaleufú', 'Futaleufú'), ('Futrono', 'Futrono'), ('Galvarino', 'Galvarino'), ('General Lagos', 'General Lagos'),
                ('Gorbea', 'Gorbea'), ('Graneros', 'Graneros'), ('Guaitecas', 'Guaitecas'), ('Hijuelas', 'Hijuelas'), ('Hualaihué', 'Hualaihué'),
                ('Hualañé', 'Hualañé'), ('Hualpén', 'Hualpén'), ('Hualqui', 'Hualqui'), ('Huara', 'Huara'), ('Huasco', 'Huasco'),
                ('Huechuraba', 'Huechuraba'), ('Illapel', 'Illapel'), ('Independencia', 'Independencia'), ('Iquique', 'Iquique'), ('Isla de Maipo', 'Isla de Maipo'),
                ('Isla de Pascua', 'Isla de Pascua'), ('Juan Fernández', 'Juan Fernández'), ('La Calera', 'La Calera'), ('La Cisterna', 'La Cisterna'),
                ('La Cruz', 'La Cruz'), ('La Estrella', 'La Estrella'), ('La Florida', 'La Florida'), ('La Granja', 'La Granja'), ('La Higuera', 'La Higuera'),
                ('La Ligua', 'La Ligua'), ('La Pintana', 'La Pintana'), ('La Reina', 'La Reina'), ('La Serena', 'La Serena'), ('La Unión', 'La Unión'),
                ('Lago Ranco', 'Lago Ranco'), ('Lago Verde', 'Lago Verde'), ('Laguna Blanca', 'Laguna Blanca'), ('Laja', 'Laja'), ('Lampa', 'Lampa'),
                ('Lanco', 'Lanco'), ('Las Cabras', 'Las Cabras'), ('Las Condes', 'Las Condes'), ('Lautaro', 'Lautaro'), ('Lebu', 'Lebu'),
                ('Licantén', 'Licantén'), ('Limache', 'Limache'), ('Linares', 'Linares'), ('Litueche', 'Litueche'), ('Llanquihue', 'Llanquihue'),
                ('Lo Barnechea', 'Lo Barnechea'), ('Lo Espejo', 'Lo Espejo'), ('Lo Prado', 'Lo Prado'), ('Lolol', 'Lolol'), ('Loncoche', 'Loncoche'),
                ('Longaví', 'Longaví'), ('Lonquimay', 'Lonquimay'), ('Los Alamos', 'Los Álamos'), ('Los Andes', 'Los Andes'), ('Los Ángeles', 'Los Ángeles'),
                ('Los Lagos', 'Los Lagos'), ('Los Muermos', 'Los Muermos'), ('Los Sauces', 'Los Sauces'), ('Los Vilos', 'Los Vilos'), ('Lota', 'Lota'),
                ('Lumaco', 'Lumaco'), ('Machalí', 'Machalí'), ('Macul', 'Macul'), ('Máfil', 'Máfil'), ('Maipú', 'Maipú'), ('Malloa', 'Malloa'),
                ('Marchihue', 'Marchihue'), ('María Elena', 'María Elena'), ('María Pinto', 'María Pinto'), ('Mariquina', 'Mariquina'), ('Maule', 'Maule'),
                ('Maullín', 'Maullín'), ('Mejillones', 'Mejillones'), ('Melipeuco', 'Melipeuco'), ('Melipilla', 'Melipilla'), ('Molina', 'Molina'),
                ('Monte Patria', 'Monte Patria'), ('Mostazal', 'Mostazal'), ('Mulchén', 'Mulchén'), ('Nacimiento', 'Nacimiento'), ('Nancagua', 'Nancagua'),
                ('Natales', 'Natales'), ('Navidad', 'Navidad'), ('Negrete', 'Negrete'), ('Ninhue', 'Ninhue'), ('Ñiquén', 'Ñiquén'),
                ('Nogales', 'Nogales'), ('Nueva Imperial', 'Nueva Imperial'), ('Ñuñoa', 'Ñuñoa'), ('Olivar', 'Olivar'), ('Ollagüe', 'Ollagüe'),
                ('Olmue', 'Olmué'), ('Osorno', 'Osorno'), ('Ovalle', 'Ovalle'), ('Padre Hurtado', 'Padre Hurtado'), ('Padre Las Casas', 'Padre Las Casas'),
                ('Paihuano', 'Paihuano'), ('Paillaco', 'Paillaco'), ('Paine', 'Paine'), ('Palena', 'Palena'), ('Palmilla', 'Palmilla'),
                ('Panguipulli', 'Panguipulli'), ('Panquehue', 'Panquehue'), ('Papudo', 'Papudo'), ('Paredones', 'Paredones'), ('Parral', 'Parral'),
                ('Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'), ('Pelarco', 'Pelarco'), ('Pelluhue', 'Pelluhue'), ('Pemuco', 'Pemuco'), ('Pencahue', 'Pencahue'),
                ('Penco', 'Penco'), ('Peñaflor', 'Peñaflor'), ('Peñalolén', 'Peñalolén'), ('Peralillo', 'Peralillo'), ('Perquenco', 'Perquenco'),
                ('Petorca', 'Petorca'), ('Peumo', 'Peumo'), ('Pica', 'Pica'), ('Pichidegua', 'Pichidegua'), ('Pichilemu', 'Pichilemu'),
                ('Pinto', 'Pinto'), ('Pirque', 'Pirque'), ('Pitrufquén', 'Pitrufquén'), ('Placilla', 'Placilla'), ('Portezuelo', 'Portezuelo'),
                ('Porvenir', 'Porvenir'), ('Pozo Almonte', 'Pozo Almonte'), ('Primavera', 'Primavera'), ('Providencia', 'Providencia'), ('Puchuncaví', 'Puchuncaví'),
                ('Pucón', 'Pucón'), ('Pudahuel', 'Pudahuel'), ('Puente Alto', 'Puente Alto'), ('Puerto Montt', 'Puerto Montt'), ('Puerto Octay', 'Puerto Octay'),
                ('Puerto Varas', 'Puerto Varas'), ('Pumanque', 'Pumanque'), ('Punitaqui', 'Punitaqui'), ('Punta Arenas', 'Punta Arenas'), ('Puqueldón', 'Puqueldón'),
                ('Purén', 'Purén'), ('Purranque', 'Purranque'), ('Putaendo', 'Putaendo'), ('Putre', 'Putre'), ('Puyehue', 'Puyehue'),
                ('Queilen', 'Queilen'), ('Quellón', 'Quellón'), ('Quemchi', 'Quemchi'), ('Quilaco', 'Quilaco'), ('Quilicura', 'Quilicura'),
                ('Quilleco', 'Quilleco'), ('Quillón', 'Quillón'), ('Quillota', 'Quillota'), ('Quilpué', 'Quilpué'), ('Quinchao', 'Quinchao'),
                ('Quinta de Tilcoco', 'Quinta de Tilcoco'), ('Quinta Normal', 'Quinta Normal'), ('Quintero', 'Quintero'), ('Quirihue', 'Quirihue'), ('Rancagua', 'Rancagua'),
                ('Ránquil', 'Ránquil'), ('Rauco', 'Rauco'), ('Recoleta', 'Recoleta'), ('Renaico', 'Renaico'), ('Renca', 'Renca'),
                ('Rengo', 'Rengo'), ('Requínoa', 'Requínoa'), ('Retiro', 'Retiro'), ('Rinconada', 'Rinconada'), ('Rio Bueno', 'Río Bueno'),
                ('Río Claro', 'Río Claro'), ('Río Hurtado', 'Río Hurtado'), ('Río Ibáñez', 'Río Ibáñez'), ('Río Negro', 'Río Negro'), ('Río Verde', 'Río Verde'),
                ('Romeral', 'Romeral'), ('Saavedra', 'Saavedra'), ('Sagrada Familia', 'Sagrada Familia'), ('Salamanca', 'Salamanca'), ('San Antonio', 'San Antonio'),
                ('San Bernardo', 'San Bernardo'), ('San Carlos', 'San Carlos'), ('San Clemente', 'San Clemente'), ('San Esteban', 'San Esteban'), ('San Fabián', 'San Fabián'),
                ('San Felipe', 'San Felipe'), ('San Fernando', 'San Fernando'), ('San Gregorio', 'San Gregorio'), ('San Ignacio', 'San Ignacio'), ('San Javier', 'San Javier'),
                ('San Joaquín', 'San Joaquín'), ('San José de Maipo', 'San José de Maipo'), ('San Juan de la Costa', 'San Juan de la Costa'), ('San Miguel', 'San Miguel'),
                ('San Nicolás', 'San Nicolás'), ('San Pablo', 'San Pablo'), ('San Pedro', 'San Pedro'), ('San Pedro de Atacama', 'San Pedro de Atacama'), ('San Pedro de la Paz', 'San Pedro de la Paz'),
                ('San Rafael', 'San Rafael'), ('San Ramón', 'San Ramón'), ('San Rosendo', 'San Rosendo'), ('San Vicente', 'San Vicente'), ('Santa Bárbara', 'Santa Bárbara'),
                ('Santa Cruz', 'Santa Cruz'), ('Santa Juana', 'Santa Juana'), ('Santa María', 'Santa María'), ('Santiago', 'Santiago'), ('Santo Domingo', 'Santo Domingo'),
                ('Sierra Gorda', 'Sierra Gorda'), ('Talagante', 'Talagante'), ('Talca', 'Talca'), ('Talcahuano', 'Talcahuano'), ('Taltal', 'Taltal'),
                ('Temuco', 'Temuco'), ('Teno', 'Teno'), ('Teodoro Schmidt', 'Teodoro Schmidt'), ('Tierra Amarilla', 'Tierra Amarilla'), ('Tiltil', 'Tiltil'),
                ('Timaukel', 'Timaukel'), ('Tirúa', 'Tirúa'), ('Tocopilla', 'Tocopilla'), ('Toltén', 'Toltén'), ('Tomé', 'Tomé'),
                ('Torres del Paine', 'Torres del Paine'), ('Tortel', 'Tortel'), ('Traiguén', 'Traiguén'), ('Trehuaco', 'Trehuaco'), ('Tucapel', 'Tucapel'),
                ('Valdivia', 'Valdivia'), ('Vallenar', 'Vallenar'), ('Valparaíso', 'Valparaíso'), ('Vichuquén', 'Vichuquén'), ('Victoria', 'Victoria'),
                ('Vicuña', 'Vicuña'), ('Vilcún', 'Vilcún'), ('Villa Alegre', 'Villa Alegre'), ('Villa Alemana', 'Villa Alemana'), ('Villarrica', 'Villarrica'),
                ('Viña del Mar', 'Viña del Mar'), ('Vitacura', 'Vitacura'), ('Yerbas Buenas', 'Yerbas Buenas'), ('Yumbel', 'Yumbel'),
                ('Yungay', 'Yungay'), ('Zapallar', 'Zapallar')
            ]

    ESTADO_ORDEN = [
                    ('Pendiente', 'Pendiente'),
                    ('Bloqueada', 'Bloqueada'),
                    ('Aceptada', 'Aceptada'),
                    ('Finalizada', 'Finalizada'),
                    
    ]

    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField("Nombre de Empresa", max_length=250, null = True)
    email = models.EmailField()
    direccion = models.CharField("Dirección", max_length=250, null = True)
    telefono = models.CharField("Teléfono", max_length=250, null = True)
    descripcion = models.CharField("Comentarios", max_length=250, blank=True)
    region = models.CharField("Región", max_length=200, choices=REGION, default=REGION[0][0])
    comuna = models.CharField("Comuna", max_length=200, choices=COMUNA, default=COMUNA[0][0])
    estado_orden = models.CharField("Estado Órden", max_length=200, choices=ESTADO_ORDEN, default=ESTADO_ORDEN[0][0])
    is_pagado = models.BooleanField(default=False)
    nfactura = models.CharField(max_length=250, null = True)


    class Meta:
        ordering = ("-created", )
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return 'O/C Nº  {}'.format(self.id)

    def get_precio_total(self):
        total_costo = sum(itemprovider.get_precio_total() for itemprovider in self.itemproviders.all())
        return total_costo

    def get_description(self):
        return ", ".join(['{} x {}'.format(itemprovider.cantidad, itemprovider.producto.nombre) for itemprovider in self.itemproviders.all()])


class ItemProvider(models.Model):
    orden = models.ForeignKey(Orden, related_name="itemproviders", on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name="order_items_oc", on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(settings.PROVIDER_ITEM_MAX_CANTIDAD),])

    def __str__(self):
        return str(self.id)

    def get_precio_total(self):
        return self.costo * self.cantidad