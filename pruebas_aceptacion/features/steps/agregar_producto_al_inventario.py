from behave import when, then, given
import time

from selenium import webdriver

@given(u'que ingreso al sistema')
def step_impl(context):
    login(context)

@given(u'entro a la sección de inventario')
def step_impl(context):
    
    context.driver.get(context.url+'lista_productos/')
    
    context.driver.find_element_by_id('Inventario').click()


@when(u'presiono el boton de agregar al inventario')
def step_impl(context):
    context.driver.find_element_by_id('boton_añadir_inventario').click()


@then(u'puedo  agregar el producto "Pluma" al inventario con su cantidad de "4", con la fecha "4/12/2020", y el numero de factura "ABC123"')
def step_impl(context):
    
    context.driver.find_element_by_id('id_no_factura').send_keys("ABC123")
    context.driver.find_element_by_id('id_fecha').send_keys("2020-12-4")
    context.driver.find_element_by_id('id_cantidad').send_keys(4)
    context.driver.find_element_by_id('id_producto').click()
    context.driver.find_element_by_id('id_producto').send_keys("p")
    context.driver.find_element_by_id('Agregar').click()

    

    



def login(context):
    context.driver.get(context.url+'login/')

    context.driver.find_element_by_name('username').send_keys('Toto')
    context.driver.find_element_by_name('password').send_keys('123')
    context.driver.find_element_by_tag_name('button').click()
