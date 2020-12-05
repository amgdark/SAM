from django.test import TestCase
from django.urls import reverse
from inventario.models import Partidas, Productos, Stock


class TestViews(TestCase):
    
    def test_url_salida_inventario(self):
        response = self.client.get('/inventario_salida/')
        self.assertEqual(response.status_code,200)

    def test_html_salida_inventario(self):
        response = self.client.get('/inventario_salida/')
        self.assertTemplateUsed(response, 'salida_productos_form.html')

    def test_url_inventario_lista(self):
        response = self.client.get('/inventario_lista/')
        self.assertEqual(response.status_code,200)

    def test_html_inventario_lista(self):
        response = self.client.get('/inventario_lista/')
        self.assertTemplateUsed(response, 'lista_inventario.html')

    def test_url_añadir_a_inventario_lista(self):
        response = self.client.get('/añadir_inventario/')
        self.assertEqual(response.status_code,200)
    
    def test_html_añadir_a_inventario(self):
        response = self.client.get('/añadir_inventario/')
        self.assertTemplateUsed(response, 'stock_form.html')
    

    def test_envio_de_añadir_producto_al_inventario(self):
        
        self.agrega_a_inventario()   
        response = self.client.get('/inventario_lista/')
        self.assertEquals('ABC123', response.context['object_list'][0].no_factura)


    def test_limpia_pisos_esta_en_el_template(self):
        self.agrega_a_inventario()
        response = self.client.get('/inventario_lista/')
        self.assertContains(response,'limpia pisos')

    def test_limpia_pisos_esta_en_el_template_en_un_td(self):
        self.agrega_a_inventario()
        response = self.client.get('/inventario_lista/')
        self.assertInHTML('<td>limpia pisos</td>', response.rendered_content)

    def test_numero_factura_esta_en_el_template(self):
        self.agrega_a_inventario()
        response = self.client.get('/inventario_lista/')
        self.assertContains(response,'ABC123')

    def test_numero_factura_esta_en_un_td_en_el_template(self):
        self.agrega_a_inventario()
        response = self.client.get('/inventario_lista/')
        self.assertInHTML('<td>ABC123</td>', response.rendered_content)

    def agrega_partida(self):
        partidaC = Partidas.objects.create(
            numero_partida = 1024,
            nombre_partida = 'Limpieza' ,
            descripcion = 'Para hacer Aseo',
        )

        return partidaC

    def agregar_producto(self):
        productoC = Productos.objects.create(
            nombre = 'limpia pisos',
            marca = 'fabuloso',
            precio = 14,
            giro = 'pa limpiar',
            unidad = '1 pieza',
            presentacion = 'unica',
            partida = self.agrega_partida(),
        )
        return productoC
    
    def agrega_a_inventario(self):
        inventario_add = Stock.objects.create(
            no_factura = 'ABC123',
            fecha = '2020-01-10',
            producto = self.agregar_producto(),
            cantidad = 12
        )



