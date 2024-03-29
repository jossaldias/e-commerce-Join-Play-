from .models import Producto, User, Order , Compra, Orden
from django.conf import settings
from django import forms  
from django.forms import TextInput
from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit, ButtonHolder, HTML
from django.core.exceptions import ValidationError


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
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
        telefono = forms.IntegerField()
        direccion = forms.CharField(max_length=60 )
        region = forms.ChoiceField(choices=REGION)
        comuna = forms.ChoiceField(choices=COMUNA)
        
    
        class Meta:
            model = User
            fields = ['username','first_name','last_name','email','region','comuna','direccion','telefono','password1','password2']

class editarUsuarioForm(forms.ModelForm):
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
        TIPO_USER = [
                      ('Administrador General', 'Administrador General'), 
                      ('Administrador Logístico', 'Administrador Logístico'), 
                      ('Ejecutivo', 'Ejecutivo'), 
                      ('Cliente', 'Cliente'), 
        ]
        region = forms.ChoiceField(choices=REGION)
        comuna = forms.ChoiceField(choices=COMUNA)
        tipo_user = forms.ChoiceField(choices=TIPO_USER)

        class Meta:
                    model = User
                    fields = ['username','first_name','last_name','picture', 'email','region','comuna','direccion', 'telefono', 'fecha_nac','tipo_user',]
                    labels = {
                                'username':'Nombre de Usuario',
                                'first_name':'Primer Nombre',
                                'last_name': 'Apellido', 
                                'picture':'Avatar',
                                'email': 'E-mail',
                                'region': 'Región',
                                'comuna':'Comuna',
                                'direccion':'Dirección',
                                'telefono':'Teléfono',
                                'fecha_nac':'Fecha de Nacimiento',
                                'tipo_user': 'Tipo de Usuario',
                            
                    }
                    widgets = {
                                'username':forms.TextInput(attrs={'type': 'text', 'id': 'username_editar'}),
                                'first_name':forms.TextInput(attrs={'id': 'nombre_editar'}),
                                'last_name':forms.TextInput(attrs={'id': 'apellido_editar'}),
                                'email':forms.TextInput(attrs={'id': 'email_editar'}),
                                'direccion':forms.TextInput(attrs={'id' :'direccion_editar'}),
                                'region': forms.TextInput(attrs={'id': 'region_editar'}),
                                'comuna':forms.TextInput(attrs={'id': 'comuna_editar'}),
                                'telefono':forms.NumberInput(attrs={'id': 'telefono_editar'}),
                                'fecha_nac': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date' }),
                                'tipo_user':forms.TextInput(attrs={'id': 'tipo_user_editar'}),

                                
                    }



class editarPerfilForm(forms.ModelForm):
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
        

        region = forms.ChoiceField(choices=REGION)
        comuna = forms.ChoiceField(choices=COMUNA)


        class Meta:
                    model = User
                    fields = ['username','first_name','last_name','picture', 'email','region','comuna','direccion','telefono', 'fecha_nac']
                    labels = {
                                'username':'Nombre de Usuario',
                                'first_name':'Primer Nombre',
                                'last_name': 'Apellido', 
                                'picture':'Avatar',
                                'email': 'E-mail',
                                'region': 'Región',
                                'comuna':'Comuna',
                                'direccion':'Dirección',
                                'telefono':'Teléfono',
                                'fecha_nac':'Fecha de Nacimiento'
                            
                    }
                    widgets = {
                                'username':forms.TextInput(attrs={'type': 'text', 'id': 'username_editar'}),
                                'first_name':forms.TextInput(attrs={'id': 'nombre_editar'}),
                                'last_name':forms.TextInput(attrs={'id': 'apellido_editar'}),
                                'email':forms.TextInput(attrs={'id': 'email_editar'}),
                                'direccion':forms.TextInput(attrs={'id' :'direccion_editar'}),
                                'region': forms.TextInput(attrs={'id': 'region_editar'}),
                                'comuna':forms.TextInput(attrs={'id': 'comuna_editar'}),
                                'telefono':forms.TextInput(attrs={'id': 'telefono_editar'}),
                                'fecha_nac': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'form-control','placeholder': 'Select a date', 'type': 'date' }),
                                
                    }



class agregarProductoForm(forms.ModelForm):
        
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
        
        id_producto = forms.CharField(widget=forms.HiddenInput(), max_length=255, required=False, label='')
        nombre = forms.CharField(max_length=255, label='Nombre')
        plataforma = forms.ChoiceField(choices=PLATAFORMA, required=False)
        categoria = forms.ChoiceField(choices=CATEGORIA, required=False)
        tipo_producto = forms.ChoiceField(choices=TIPO_PRODUCTO)
        cantidad = forms.IntegerField(widget=forms.HiddenInput(), initial=0, label='')

        def clean_nombre(self):
            nombre = self.cleaned_data['nombre']
            if Producto.objects.filter(nombre=nombre).exists():
                raise ValidationError('El Producto ya existe, revisa el inventario e intenta otra vez')
            return nombre


        class Meta:
                model = Producto
                fields = ['nombre', 'categoria', 'plataforma','tipo_producto','descripcion', 'picture', 'costo'] 
                labels = {
                            'nombre':'Nombre Producto',
                            'categoria': 'Categoría', 
                            'plataforma': 'Plataforma',
                            'tipo_producto': 'Tipo de Producto',
                            'descripcion':'Descripción del Producto',
                            'picture':'Imágen del Producto',
                            'costo':'Costo',
                            
                }



class editarProductoForm(forms.ModelForm):
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

    plataforma = forms.ChoiceField(choices=PLATAFORMA, required=False)
    categoria = forms.ChoiceField(choices=CATEGORIA, required=False)
    tipo_producto = forms.ChoiceField(choices=TIPO_PRODUCTO)


    class Meta:
                model = Producto
                fields = ['id_producto', 'nombre', 'categoria', 'plataforma','tipo_producto','descripcion', 'picture', 'costo', 'cantidad'] 
                labels = {
                            'id_producto':'SKU',
                            'nombre':'Nombre Producto',
                            'categoria': 'Categoría', 
                            'plataforma': 'Plataforma',
                            'tipo_producto': 'Tipo de Producto',
                            'descripcion':'Descripción del Producto',
                            'picture':'Imágen del Producto',
                            'costo':'Costo',
                            'cantidad':'Cantidad',
                }
                widgets = {
                            'id_producto':forms.TextInput(attrs={'type': 'text', 'id': 'producto_editar'}),
                            'nombre':forms.TextInput(attrs={'id': 'nombre_editar'}),
                            'descripcion':forms.TextInput(attrs={'id': 'descripcion_editar'}),
                            'costo':forms.TextInput(attrs={'id': 'costo_editar'}),
                            'cantidad':forms.TextInput(attrs={'id' :'cantidad_editar'}),
                            
                }


class OrdenCompraForm(forms.ModelForm):

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
    
    plataforma = forms.ChoiceField(choices=PLATAFORMA, required=False)
    tipo_producto = forms.ChoiceField(choices=TIPO_PRODUCTO, required=False)
    estado_orden = forms.ChoiceField(choices=ESTADO_ORDEN, required=False)


    class Meta:
                model = Compra
                fields = ['id_orden', 'sku', 'nombre', 'proveedor', 'plataforma','tipo_producto', 'costo', 'cantidad','estado_orden'] 
                labels = {
                            'id_orden':'Nº Órden de Compra',
                            'sku':'SKU',
                            'nombre':'Nombre Producto',
                            'proveedor':'Proveedor',
                            'plataforma': 'Plataforma',
                            'tipo_producto': 'Tipo de Producto',
                            'costo':'Costo',
                            'cantidad':'Cantidad',
                            'estado_orden':'Estado de Órden de Compra'
                }

class editarOrdenForm(forms.ModelForm):

    ESTADO_ORDEN = [
                        ('', '----'),
                        ('Bloqueada','Bloqueada'),
                        ('Aceptada','Aceptada'),
                        ('Pendiente','Pendiente'),
                        ('Finalizada', 'Finalizada'),
                    ] 
    
    estado_orden = forms.ChoiceField(choices=ESTADO_ORDEN, required=False)


    class Meta:
                model = Compra
                fields = ['estado_orden'] 
                labels = {
                          'estado_orden':'Estado de Órden de Compra'
                }
                widgets = {
                         'estado_orden':forms.TextInput(attrs={'id' :'estado_editar'}),
                            
                }

class editarEnvioForm(forms.ModelForm):

    ESTADO_VENTA = [
                    ('En Preparación', 'En Preparación'),
                    ('En Ruta', 'En Ruta'),
                    ('Entregado', 'Entregado'),
    ]
    
    estado_venta = forms.ChoiceField(choices=ESTADO_VENTA, required=False)


    class Meta:
                model = Order
                fields = ['estado_venta'] 
                labels = {
                          'estado_venta':'Estado de Venta'
                }
                widgets = {
                         'estado_venta':forms.TextInput(attrs={'id' :'estado_envio'}),
                            
                }


PRODUCTO_CANTIDAD_CHOICES = [
  (i, str(i)) for i in range(1, settings.CART_ITEM_MAX_CANTIDAD + 1)
]


class CartAddProductoForm(forms.Form):
  cantidad = forms.IntegerField(
    label="Cantidad",
  )
  override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderCreateForm(forms.ModelForm):

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

  region = forms.ChoiceField(choices=REGION)
  comuna = forms.ChoiceField(choices=COMUNA)

  class Meta:
    model = Order
    fields = [
    
      "email",
      "direccion",
      "telefono",
      "descripcion",
      "region",
      "comuna",
    ]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = "post"
    self.helper.form_action = "."
    self.helper.layout = Layout(
      Fieldset(
        Div(
          Field("nombre", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("email", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("region", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
         Div(
          Field("comuna", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("direccion", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("telefono", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("descripcion", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        css_class="border-bottom mb-3",
      ),
      ButtonHolder(
            Submit(
                "submit",
                "Escoger Método de Pago",
                css_class="btn btn-success btn-lg btn-block"
            ),
            HTML('<a href="/clear/" class="btn btn-danger btn-lg btn-block">Cancelar compra</a>'),
            css_class="button-holder")
    )




PRODUCTO_CANTIDAD_CHOICES = [
  (i, str(i)) for i in range(1, settings.PROVIDER_ITEM_MAX_CANTIDAD + 1)
]


class ProviderAddProductoForm(forms.Form):
  cantidad = forms.IntegerField(
    label="Cantidad",
  )
  override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrdenCreateForm(forms.ModelForm):

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

  region = forms.ChoiceField(choices=REGION)
  comuna = forms.ChoiceField(choices=COMUNA)

  class Meta:
    model = Orden
    fields = [
      "nombre",
      "email",
      "direccion",
      "telefono",
      "descripcion",
      "region",
      "comuna",
    ]

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_method = "post"
    self.helper.form_action = '.'
    self.helper.add_input(
      Submit(
        "submit",
        "Enviar por E-mail",
        css_class="btn btn-success btn-lg btn-block",
      )
    )
    self.helper.layout = Layout(
      Fieldset(
        Div(
          Field("nombre", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("nombre", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("email", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("region", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
         Div(
          Field("comuna", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("direccion", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("telefono", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        Div(
          Field("descripcion", css_class="form-control", wrapper_class="col"),
          css_class="row",
        ),
        css_class="border-bottom mb-3",
      )
    )
