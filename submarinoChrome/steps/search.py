@given(u'o acesso a página principal')
def step_impl(context):
    context.home_page.go_home()


@when(u'é feita a busca do produto')
def step_impl(context):
    context.home_page.search_product()


@then(u'será acessada a página de pesquisa.')
def step_impl(context):
    assert context.driver.title == 'Motorola X4 com Ofertas Incríveis no Submarino.com'