@given(u'a tela inicial do submarino')
def step_impl(context):
    context.home_page.go_home()

@when(u'selecionado o botão mais informações')
def step_impl(context):
    context.home_page.more_info()

@when(u'selecionada a opcao hoteis')
def step_impl(context):
    context.driver.implicitly_wait(4)
    context.home_page.hotels_link()
    

@then(u'aparecerá a página do submarino viagens')
def step_impl(context):
    context.waitting(13)
    assert (context.driver.title == 'Submarino - Os Produtos que você curte estão aqui. Explore!')