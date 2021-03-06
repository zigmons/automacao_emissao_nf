from login import *

notas_emitir = pd.read_excel(r'C:\Users\rafae\OneDrive\PhytonAulas\AulasHashtag - windows\Automacao Web(Web-Scraping)\exercicio_automatizaremissaonf\NotasEmitir.xlsx')
print(notas_emitir)

razao_social = driver.find_element(By.NAME, 'nome')
endereco = driver.find_element(By.NAME, 'endereco')
bairro = driver.find_element(By.NAME, 'bairro')
municipio = driver.find_element(By.NAME, 'municipio')
cep = driver.find_element(By.NAME, 'cep')
uf = driver.find_element(By.NAME, 'uf')
cnpj = driver.find_element(By.NAME, 'cnpj')
inscricao = driver.find_element(By.NAME, 'inscricao')
descricao = driver.find_element(By.NAME, 'descricao')
qnt = driver.find_element(By.NAME, 'quantidade')
valor_unitario = driver.find_element(By.NAME, 'valor_unitario')
total = driver.find_element(By.NAME, 'total')

driver.implicitly_wait(10)

for linha in notas_emitir.index:
    razao_social.send_keys(notas_emitir.loc[linha,'Cliente'])
    driver.implicitly_wait(10)
    endereco.send_keys(notas_emitir.loc[linha,'Endereço'])
    driver.implicitly_wait(10)
    bairro.send_keys(notas_emitir.loc[linha,'Bairro'])
    municipio.send_keys(notas_emitir.loc[linha,'Municipio'])
    cep.send_keys(str(notas_emitir.loc[linha,'CEP']))
    uf.send_keys(notas_emitir.loc[linha,'UF'])
    cnpj.send_keys(str(notas_emitir.loc[linha,'CPF/CNPJ']))
    inscricao.send_keys(str(notas_emitir.loc[linha,'Inscricao Estadual']))
    descricao.send_keys(notas_emitir.loc[linha, 'Descrição'])
    qnt.send_keys(str(notas_emitir.loc[linha,'Quantidade']))
    valor_unitario.send_keys(str(notas_emitir.loc[linha,'Valor Unitario']))
    total.send_keys(str(notas_emitir.loc[linha,'Valor Total']))
    driver.find_element(By.CLASS_NAME,'registerbtn').click()
    driver.refresh()
    razao_social = driver.find_element(By.NAME, 'nome')
    endereco = driver.find_element(By.NAME, 'endereco')
    bairro = driver.find_element(By.NAME, 'bairro')
    municipio = driver.find_element(By.NAME, 'municipio')
    cep = driver.find_element(By.NAME, 'cep')
    uf = driver.find_element(By.NAME, 'uf')
    cnpj = driver.find_element(By.NAME, 'cnpj')
    inscricao = driver.find_element(By.NAME, 'inscricao')
    descricao = driver.find_element(By.NAME, 'descricao')
    qnt = driver.find_element(By.NAME, 'quantidade')
    valor_unitario = driver.find_element(By.NAME, 'valor_unitario')
    total = driver.find_element(By.NAME, 'total')
