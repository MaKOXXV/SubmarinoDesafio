@given(u'um item adicionado no Carrinho')
def step_impl(context):
    context.sh_car.add_item()
    
@when(u'removo este item')
def step_impl(context):
    context.sh_car.remove_item()

@then(u'uma solicitação será enviada')
def step_impl(context):
    context.driver.implicitly_wait(7)
    context.sh_car.reflesh()
    assert (context.sh_car.text_h2() == 'Seu carrinho está vazio')
