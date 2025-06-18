import os

'''
TODO modularizar o código,
'''

# DADOS MOCKADOS
clientes = [
    {'nome': 'João da Silva', 'cpf': '1', 'email': 'joao.silva@email.com'},
    {'nome': 'Maria Oliveira', 'cpf': '2', 'email': 'maria.oliveira@email.com'},
    {'nome': 'Carlos Pereira', 'cpf': '3', 'email': 'carlos.pereira@email.com'},
    {'nome': 'Ana Santos', 'cpf': '4', 'email': 'ana.santos@gmail.com'},
    {'nome': 'Pedro Costa', 'cpf': '5', 'email': 'pedro.costa@hotmail.com'},
    {'nome': 'Lucia Ferreira', 'cpf': '6', 'email': 'lucia.ferreira@yahoo.com'},
    {'nome': 'Roberto Almeida', 'cpf': '7', 'email': 'roberto.almeida@outlook.com'},
    {'nome': 'Fernanda Lima', 'cpf': '8', 'email': 'fernanda.lima@email.com'},
    {'nome': 'José Rodrigues', 'cpf': '9', 'email': 'jose.rodrigues@gmail.com'},
    {'nome': 'Carla Mendes', 'cpf': '10', 'email': 'carla.mendes@email.com'},
    {'nome': 'Marcos Souza', 'cpf': '11', 'email': 'marcos.souza@hotmail.com'},
    {'nome': 'Sandra Nunes', 'cpf': '12', 'email': 'sandra.nunes@yahoo.com'},
    {'nome': 'Antonio Barbosa', 'cpf': '13', 'email': 'antonio.barbosa@gmail.com'},
    {'nome': 'Patricia Moreira', 'cpf': '14', 'email': 'patricia.moreira@outlook.com'},
    {'nome': 'Rafael Cardoso', 'cpf': '15', 'email': 'rafael.cardoso@email.com'}
]

veiculos = [
    {'id_auto': '1' , 'marca': 'Fiat', 'modelo': 'Uno', 'ano': '2012', 'valor_compra': 12000.00, 'estado': '1', 'vendido': False},
    {'id_auto': '2' , 'marca': 'Volkswagen', 'modelo': 'Gol', 'ano': '2014', 'valor_compra': 15000.00, 'estado': '2', 'vendido': True},
    {'id_auto': '3' , 'marca': 'Chevrolet', 'modelo': 'Onix', 'ano': '2018', 'valor_compra': 30000.00, 'estado': '1', 'vendido': True},
    {'id_auto': '4' , 'marca': 'Honda', 'modelo': 'Civic', 'ano': '2020', 'valor_compra': 45000.00, 'estado': '1', 'vendido': False},
    {'id_auto': '5' , 'marca': 'Toyota', 'modelo': 'Corolla', 'ano': '2019', 'valor_compra': 42000.00, 'estado': '1', 'vendido': False},
    {'id_auto': '6' , 'marca': 'Ford', 'modelo': 'Ka', 'ano': '2015', 'valor_compra': 18000.00, 'estado': '2', 'vendido': True},
    {'id_auto': '7' , 'marca': 'Hyundai', 'modelo': 'HB20', 'ano': '2017', 'valor_compra': 25000.00, 'estado': '1', 'vendido': False},
    {'id_auto': '8' , 'marca': 'Nissan', 'modelo': 'March', 'ano': '2013', 'valor_compra': 16000.00, 'estado': '2', 'vendido': False},
    {'id_auto': '9' , 'marca': 'Peugeot', 'modelo': '208', 'ano': '2016', 'valor_compra': 22000.00, 'estado': '1', 'vendido': True},
    {'id_auto': '10', 'marca': 'Renault', 'modelo': 'Sandero', 'ano': '2014', 'valor_compra': 17000.00, 'estado': '2', 'vendido': False},
    {'id_auto': '11', 'marca': 'Fiat', 'modelo': 'Palio', 'ano': '2010', 'valor_compra': 10000.00, 'estado': '3', 'vendido': False},
    {'id_auto': '12', 'marca': 'Volkswagen', 'modelo': 'Fox', 'ano': '2011', 'valor_compra': 13000.00, 'estado': '2', 'vendido': False},
    {'id_auto': '13', 'marca': 'Chevrolet', 'modelo': 'Celta', 'ano': '2009', 'valor_compra': 8000.00, 'estado': '3', 'vendido': False},
    {'id_auto': '14', 'marca': 'Honda', 'modelo': 'Fit', 'ano': '2016', 'valor_compra': 28000.00, 'estado': '1', 'vendido': True},
    {'id_auto': '15', 'marca': 'Toyota', 'modelo': 'Etios', 'ano': '2015', 'valor_compra': 21000.00, 'estado': '2', 'vendido': False},
    {'id_auto': '16', 'marca': 'Ford', 'modelo': 'Fiesta', 'ano': '2013', 'valor_compra': 19000.00, 'estado': '2', 'vendido': False},
    {'id_auto': '17', 'marca': 'Hyundai', 'modelo': 'i30', 'ano': '2018', 'valor_compra': 35000.00, 'estado': '1', 'vendido': False},
    {'id_auto': '18', 'marca': 'Nissan', 'modelo': 'Versa', 'ano': '2017', 'valor_compra': 32000.00, 'estado': '1', 'vendido': True},
    {'id_auto': '19', 'marca': 'Peugeot', 'modelo': '2008', 'ano': '2019', 'valor_compra': 38000.00, 'estado': '1', 'vendido': False},
    {'id_auto': '20', 'marca': 'Renault', 'modelo': 'Captur', 'ano': '2020', 'valor_compra': 40000.00, 'estado': '1', 'vendido': False}
]

servicos = [
    {'id_auto': '1' , 'descricao': 'Troca de óleo', 'valor': 150.00, 'data': '10/06/2025'},
    {'id_auto': '1' , 'descricao': 'Alinhamento e balanceamento', 'valor': 200.00, 'data': '12/06/2025'},
    {'id_auto': '1' , 'descricao': 'Troca de pastilhas de freio', 'valor': 280.00, 'data': '15/06/2025'},
    {'id_auto': '3' , 'descricao': 'Revisão geral', 'valor': 500.00, 'data': '14/06/2025'},
    {'id_auto': '3' , 'descricao': 'Troca de pneus', 'valor': 800.00, 'data': '16/06/2025'},
    {'id_auto': '4' , 'descricao': 'Troca de óleo', 'valor': 180.00, 'data': '05/06/2025'},
    {'id_auto': '4' , 'descricao': 'Limpeza de bicos injetores', 'valor': 350.00, 'data': '08/06/2025'},
    {'id_auto': '4' , 'descricao': 'Troca de filtro de ar', 'valor': 120.00, 'data': '10/06/2025'},
    {'id_auto': '5' , 'descricao': 'Revisão dos 10.000 km', 'valor': 450.00, 'data': '02/06/2025'},
    {'id_auto': '5' , 'descricao': 'Troca de correias', 'valor': 300.00, 'data': '04/06/2025'},
    {'id_auto': '7' , 'descricao': 'Troca de óleo', 'valor': 160.00, 'data': '01/06/2025'},
    {'id_auto': '7' , 'descricao': 'Balanceamento', 'valor': 80.00, 'data': '03/06/2025'},
    {'id_auto': '7' , 'descricao': 'Troca de velas', 'valor': 200.00, 'data': '06/06/2025'},
    {'id_auto': '8' , 'descricao': 'Reparo no ar condicionado', 'valor': 400.00, 'data': '07/06/2025'},
    {'id_auto': '8' , 'descricao': 'Troca de bateria', 'valor': 350.00, 'data': '09/06/2025'},
    {'id_auto': '10', 'descricao': 'Troca de óleo', 'valor': 140.00, 'data': '11/06/2025'},
    {'id_auto': '10', 'descricao': 'Reparo na suspensão', 'valor': 600.00, 'data': '13/06/2025'},
    {'id_auto': '11', 'descricao': 'Reparo no motor', 'valor': 1200.00, 'data': '20/05/2025'},
    {'id_auto': '11', 'descricao': 'Troca de embreagem', 'valor': 800.00, 'data': '25/05/2025'},
    {'id_auto': '11', 'descricao': 'Pintura parcial', 'valor': 500.00, 'data': '28/05/2025'},
    {'id_auto': '12', 'descricao': 'Troca de óleo', 'valor': 150.00, 'data': '30/05/2025'},
    {'id_auto': '12', 'descricao': 'Alinhamento', 'valor': 100.00, 'data': '02/06/2025'},
    {'id_auto': '13', 'descricao': 'Reparo na transmissão', 'valor': 900.00, 'data': '15/05/2025'},
    {'id_auto': '13', 'descricao': 'Troca de pneus', 'valor': 600.00, 'data': '18/05/2025'},
    {'id_auto': '13', 'descricao': 'Reparo elétrico', 'valor': 300.00, 'data': '22/05/2025'},
    {'id_auto': '15', 'descricao': 'Revisão preventiva', 'valor': 400.00, 'data': '25/05/2025'},
    {'id_auto': '15', 'descricao': 'Troca de filtros', 'valor': 180.00, 'data': '27/05/2025'},
    {'id_auto': '16', 'descricao': 'Troca de óleo', 'valor': 155.00, 'data': '29/05/2025'},
    {'id_auto': '16', 'descricao': 'Reparo no freio', 'valor': 320.00, 'data': '31/05/2025'},
    {'id_auto': '17', 'descricao': 'Revisão completa', 'valor': 550.00, 'data': '03/06/2025'},
    {'id_auto': '17', 'descricao': 'Troca de amortecedores', 'valor': 700.00, 'data': '05/06/2025'},
    {'id_auto': '19', 'descricao': 'Troca de óleo', 'valor': 170.00, 'data': '07/06/2025'},
    {'id_auto': '19', 'descricao': 'Calibragem de pneus', 'valor': 50.00, 'data': '09/06/2025'},
    {'id_auto': '20', 'descricao': 'Primeira revisão', 'valor': 300.00, 'data': '11/06/2025'},
    {'id_auto': '20', 'descricao': 'Enceramento', 'valor': 150.00, 'data': '13/06/2025'}
]

vendas = [
    {'id_auto': '3' , 'cpf': '1', 'valor_venda': 32000.00, 'data_venda': '15/06/2025'},
    {'id_auto': '2' , 'cpf': '2', 'valor_venda': 18000.00, 'data_venda': '16/06/2025'},
    {'id_auto': '6' , 'cpf': '4', 'valor_venda': 22000.00, 'data_venda': '10/06/2025'},
    {'id_auto': '9' , 'cpf': '5', 'valor_venda': 26000.00, 'data_venda': '12/06/2025'},
    {'id_auto': '14', 'cpf': '7', 'valor_venda': 32000.00, 'data_venda': '08/06/2025'},
    {'id_auto': '18', 'cpf': '8', 'valor_venda': 36000.00, 'data_venda': '05/06/2025'},

]

# ESTRUTURAS
funcionalidades = {
    1 :'Cadastro de Clientes',
    2 :'Cadastro de Veículos',
    3 :'Registro de Serviços no automovel',
    4 :'Venda de Veículos',
    5 :'Relatórios'
}

subfuncionalidades = {
    1 : [{
        1 : 'Cadastrar Cliente',
        2 : 'Editar Cliente',
        3 : 'Excluir Cliente',
          }
          ],
    2 : [{
        1 : 'Cadastrar Veículo',
        2 : 'Editar Veículo',
        3 : 'Excluir Veículo',
          }
          ],
    3 : [{
        1 : 'Registro de Serviços Realizados' 
        }],
    4 : [{
        1 : 'Registrar Venda' 
        }],
    5 : [{
        1 : 'Veículos em estoque',
        2 : 'Histórico de servicos por veículo',
        3 : 'Vendas realizadas',
        4 : 'Listar Clientes'
          }
          ],
}

# FUNÇÕES
def verifica_se_existe_veiculo(id_auto):
    for veiculo in veiculos:
        if veiculo['id_auto'] == id_auto:
            if veiculo['vendido'] == False:
                return True
        
    return False

def estadoveiculo(estado):
    match estado:
        case '1':
            return 'Bom'
        case '2':
            return 'Regular'
        case '3':
            return 'Ruim'
        case _:
            return 'Estado não válido'

def mostra_caminho_percorrido(kwargs):
    print(kwargs)
    pri = funcionalidades[int(acao)]
    seg = subfuncionalidades[int(acao)][0][int(acao_especifica)]
    # seg = seg
    ter = kwargs['funcao']
    limpatela()
    print(f'{pri} > {seg} > {ter}')

def cadastra_cliente(**kwargs):
    if kwargs:
        kwargs['funcao'] = 'Cadastro de Cliente'
        mostra_caminho_percorrido(kwargs)

    nome = input('Digite o nome do cliente: ')
    cpf = input('Digite o CPF do cliente: ex:. 12878995827: ')
    
    if clientes:
        for cliente in clientes:
            if cliente['cpf'] == cpf:
                print(f'CPF já está cadastrado !!!')
                return None

    email = input('Digite o EMAIL do cliente: joao@email.com: ')

    cliente = {
        'nome': nome,
        'cpf': cpf,
        'email': email
    }
    # TODO adicionar verificações de cpf etc

    clientes.append(cliente) 
    return print(f'Cliente {nome.title()} Cadastrado!')

def edita_cliente(**kwargs):
    if kwargs:
        kwargs['funcao'] = 'Editar Cliente'
        mostra_caminho_percorrido(kwargs)

        cpf = input('Digite o CPF do cliente para editar: ')

        for cliente in clientes:
            if cliente['cpf'] == cpf:
                listar_clientes(cliente=cliente)

                nome_temp = cliente['nome']

                campo = input(f'Qual Campo editar para {nome_temp}\nCampos válidos[nome, cpf, email ou "todos"]: ')
                
                if campo.lower() == 'todos':
                    for _ in cliente.keys():
                        novo_nome = input('Digite o nome do cliente: ')
                        novo_cpf = input('Digite o CPF do cliente: ex:. 12878995827: ')
                        novo_email = input('Digite o EMAIL do cliente: joao@email.com: ')

                        cliente['nome'] = novo_nome
                        cliente['cpf'] = novo_cpf
                        cliente['email'] = novo_email

                        print(f'Todos os campos do cliente {novo_nome} foram editados com sucesso!')
                        return None
                    
                if campo.lower() in ['nome', 'cpf', 'email']:
                    cliente[campo.lower()] = input(f'Digite o novo {campo.lower()}: ')
                    print(f'Dados de {campo.lower()} do cliente {nome_temp} editados com sucesso!')
                    return None
                else:
                    print('Digite um campo válido')
            else:
                return 'Nenhum cliente econtrado com o CPF informado...'
    return 'edita_cliente'

def exclui_cliente(**kwargs):
    if kwargs:
        kwargs['funcao'] = 'Excluir Cliente'
        mostra_caminho_percorrido(kwargs)

        cpf = input('Digite o CPF do cliente para deletar: ')

        for cliente in clientes:
            if cliente['cpf'] == cpf:
                del cliente['cpf']
                print('Cliente DELETADO!')
    
    return 'exclui_cliente'

def cadastra_veiculo(**kwargs):
    if kwargs:
        kwargs['funcao'] = 'Cadastrar Veículo'
        mostra_caminho_percorrido(kwargs)

    id_auto = input('Digite um ID para o Veículo: ')

    if veiculos:
        for veiculo in veiculos:
            if veiculo['id_auto'] == id_auto:
                print(f'Veículo já está cadastrado !!!')
                return None

    marca = input('Digite a Marca do Veículo: ')
    modelo = input('Digite o Modelo do Veículo: ')
    ano = input('Digite o Ano do Veículo: ')
    valor_compra = float(input('Digite o valor da compra (Apenas número): R$'))
    estado = input('Digite estado de conservação do Veículo\n1->Bom\n2->Regular\n3->Ruim\n: ')

    veiculo = {
        'id_auto': id_auto,
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'valor_compra': valor_compra,
        'estado': estado,
        'vendido': False
    }

    veiculos.append(veiculo) 
    return print(f'Veículo {modelo.title()}/{ano} Cadastrado!')

def edita_veiculo(**kwargs):
    if kwargs:
        kwargs['funcao'] = 'Editar Veículo'
        mostra_caminho_percorrido(kwargs)
        id_veiculo = input('Digite o ID do veículo para editar: ') # TODO ver se o veículo existe
        
        print('-'*50)
        for veiculo in veiculos:
            if veiculo['id_auto'] == id_veiculo:
                nome_veiculo = relatorio_veiculos_estoque(veiculo=id_veiculo)
                print('-'*50)
                campo = input(f'Qual campo editar para {nome_veiculo}?\nCampos Válidos [marca, modelo, ano, valor_compra, estado ou "todos"]: ')

                if campo.lower() == 'todos':
                    for _ in veiculo.keys():
                        nova_marca = input('Digite a marca do veículo: ')
                        novo_modelo = input('Digite o modelo do veículo: ')
                        novo_ano = input('Digite o ano do veículo: ')
                        novo_val_compra = input('Digite o valor de compra: ') 
                        novo_estado = input('Digite o estado de conservação: ')

                        veiculo['marca'] = nova_marca
                        veiculo['modelo'] = novo_modelo
                        veiculo['ano'] = novo_ano
                        veiculo['valor_compra'] = novo_val_compra
                        veiculo['estado'] = novo_estado
                        nome_veiculo_novo = relatorio_veiculos_estoque(veiculo=id_veiculo)
                        print(f'Todos os campos do veiculo {nome_veiculo}->{nome_veiculo_novo} foram editados com sucesso!')
                        return None
                if campo.lower() in ['marca','modelo', 'ano', 'valor_compra', 'estado']:
                    veiculo[campo.lower()] = input(f'Digite o novo {campo.lower()}: ')
                    print(f'Dados de {campo.lower()} do veículo {nome_veiculo} editados com sucesso!')
                    return None
                else:
                    print('Digite um campo válido')
                    return None
            else:
                print('Nenhum veículo encontrado...')
                return None
            
def exclui_veiculo(**kwargs):
    if kwargs:
        kwargs['funcao'] = 'Excluir'
        mostra_caminho_percorrido(kwargs)

        id_auto = input('Digite o ID do veículo para deletar: ')

        for veiculo in veiculos:
            if veiculo['id_auto'] == id_auto:
                del veiculo['id_auto']
                print('Veículo deletado!')

    return 'exclui_veiculo'

def cadastra_servicos_veiculo(**kwargs):
    if kwargs:
        kwargs['funcao'] = 'Cadastrar Serviço Veículo'
        mostra_caminho_percorrido(kwargs)

        id_auto = input('Digite o ID do veículo para o atribuir o serviço: ')
        # verificar se existe veículo
        if verifica_se_existe_veiculo(id_auto):
            descricao = input('Qual a descrição do serviço do veículo: ')
            valor = float(input('Digite o valor do serviço R$:'))
            data = input('Digite a data em que o serviço foi feito: ex:. dd/mm/yyyy: ')

            servico = {
                'id_auto': id_auto,
                'descricao': descricao,
                'valor': valor,
                'data': data
            }

            servicos.append(servico)
        else:
            print('Ops... Carro não está disponível')
    return 'cadastra_servicos_veiculo'

def seta_veiculo_como_vendido(id_auto):
    for veiculo in veiculos:
        if veiculo['id_auto'] == id_auto:
            veiculo['vendido'] = True
            return True
    return False

def registra_venda_veiculo(**kwargs):
    if kwargs:
        kwargs['funcao'] = 'Registro de Venda'
        mostra_caminho_percorrido(kwargs)

        id_auto = input('Qual é o ID do veículo a ser vendido: ')

        if verifica_se_existe_veiculo(id_auto):
            cpf = input('Qual é o cpf do cliente: ')
            valor_venda = float(input('Qual é o valor da venda?: '))
            data =  input('Qual é a data da venda? dd/mm/yyyy: ')
        
            venda = {
                'id_auto' : id_auto,
                'cpf' : cpf,
                'valor_venda' : valor_venda,
                'data_venda': data,
            }

            vendas.append(venda)
            seta_veiculo_como_vendido(id_auto)
            print('Venda registrada com sucesso!')
        else:
            print(f'Ops... Não encontramos um veículo com esse ID {id_auto} ou ja foi vendido!')

def relatorio_veiculos_estoque(**kwargs):
    if 'veiculo' in kwargs.keys():
        if kwargs['veiculo']:
            for auto in veiculos:
                if auto['id_auto'] == str(kwargs['veiculo']):
                    id_ = auto['id_auto']
                    marca = auto['marca']
                    modelo = auto['modelo']
                    ano = auto['ano']
                    valor_compra = auto['valor_compra']
                    estado = estadoveiculo(auto['estado'])
                    print(f'ID:{id_}\nMarca/modelo: {marca}-{modelo}\nAno: {ano}\nValor Compra R$: {valor_compra}\nEstado: {estado}')
                    return f'{id_}-{marca}-{modelo}-{ano}'
    else:
        if kwargs:
            kwargs['funcao'] = 'Veículos em estoque'
            mostra_caminho_percorrido(kwargs)
        
        print('\nLISTANDO VEÍCULOS EM ESTOQUE')
        for veiculo in veiculos:

            if veiculo['vendido'] == False:
                id_ = veiculo['id_auto']
                marca = veiculo['marca']
                modelo = veiculo['modelo']
                ano = veiculo['ano']
                valor_compra = veiculo['valor_compra']
                estado = estadoveiculo(veiculo['estado'])

                print('-'*50)  
                print(f'ID:{id_}\nMarca/modelo: {marca}-{modelo}\nAno: {ano}\nValor Compra R$: {valor_compra}\nEstado: {estado}')
                print('-'*50)  
            else:
                continue
        input('Digite qualquer tecla para continuar...')
        limpatela()

def relatorio_veiculo_servicos(**kwargs):
    if kwargs:
        kwargs['funcao'] = 'Serviços Veículos'
        mostra_caminho_percorrido(kwargs)

        id_auto = input('Digite o ID do veículo para listar os serviços: ')
        
        relatorio_veiculos_estoque(veiculo=id_auto)
        print('Serviços realizados')
        total = 0
        for servico in servicos:
            if servico['id_auto'] == id_auto:
                descricao = servico['descricao']
                valor = servico['valor']
                data = servico['data']
                total += float(valor)
            
                print('-'*50)
                print(f'Data:{data}\nDescrição: {descricao}\nR${valor}')
                
        print('='*50)
        print(f'TOTAL DE SERVIÇOS R${total}')
        print('='*50)

        _ = input('Digite qualquer tecla para continuar...')

    return 'relatorio_veiculo_servicos'

def relatorio_vendas(**kwargs):
    if kwargs:
        kwargs['funcao'] = 'Relatório de vendas'
        mostra_caminho_percorrido(kwargs)

        for venda in vendas:
            print()
            print('='*100)
            id_auto = venda['id_auto']
            cpf = venda['cpf']
            valor = venda['valor_venda']
            data = venda['data_venda']

            print(f'Data venda: {data}\nCPF cliente: {cpf}\n')
            print('Veiculo vendido:')

            for veiculo in veiculos:
                if veiculo['vendido'] == True:
                    if veiculo['id_auto'] == id_auto:
                        marca = veiculo['marca']
                        modelo = veiculo['modelo']
                        ano = veiculo['ano']
                        valor_compra = veiculo['valor_compra']
                        estado = estadoveiculo(veiculo['estado'])
                        print('. '*50)
                        print(f'Marca/modelo: {marca}-{modelo} | Ano: {ano} | Valor Compra R$: {valor_compra} | Estado: {estado}')
                        print('\nServiços realizados:')
                        total_servicos = 0
                        tem_servico = False
                        for servico in servicos:
                            if servico['id_auto'] == id_auto:
                                descricao = servico['descricao']
                                valor_servico = servico['valor']
                                data_servico = servico['data']
                                print(f'• Valor Serviço R$ {valor_servico} | Data Serviço {data_servico} | Descrição: {descricao}')
                                total_servicos += float(valor_servico)
                                tem_servico = True
                        if tem_servico == False:
                            print('• Nenhum serviço Realizado')
                        # Sumário...
                        print('- '*50)
                        print(f'TOTAL CUSTO: {int(float(total_servicos)+float(valor_compra))}')
                        print(f'VALOR VENDA: {int(valor)}')
                        print('. '*50)
        _ = input('Digite algo para continuar...')

def listar_clientes(**kwargs):
    if 'cliente' in kwargs.keys():

        if clientes:
            nome = kwargs['cliente']['nome']
            cpf = kwargs['cliente']['cpf']
            email = kwargs['cliente']['email']
            
            print('-'*50)
            print(f'Nome: {nome}\nCPF: {cpf}\nE-mail: {email}')
            print('-'*50)   
        return None

    else:
        print('\nLISTANDO CLIENTES')
        for cliente in clientes:
            nome = cliente['nome']
            cpf = cliente['cpf']
            email = cliente['email']
            
            print('-'*50)
            print(f'Nome: {nome}\nCPF: {cpf}\nE-mail: {email}')
            print('-'*50)

        input('Digite qualquer tecla para continuar...')
        limpatela()

def retorna_funcao(acao, acao_especifica):
    try:
        sacao = str(acao)
        sacao_esp = str(acao_especifica)
        chave = f'{sacao}.{sacao_esp}'

        funcao = mapa_funcoes[chave]
        return funcao
    except:
        return None

def limpatela(msg_fixa='ERP para Garagistas'):
    qtd_letras = len(msg_fixa)
    qtd_underlines = 100 - qtd_letras

    os.system('cls')

    if qtd_underlines % 2 == 0:  
        q = qtd_underlines/2
        separador = '_'*int(q)
        
    else:
        q = (qtd_underlines-1)/2
        separador = '_'*int(q)

    print(separador, msg_fixa, separador)   

def verifica_sair(entrada):
    entrada = str(entrada)
    if entrada.lower() == 'sair':
        return True
    return False

def bemvindo():
    limpatela()
    print('_'*100)
    print('Bem vindo ao seu ERP para Garagistas')
    print('Para sair digite "sair"')
    print('_'*100)

def menu_principal():

    print('\nMENU >\nEscolha uma Funcionalidade:\n')
    
    for k, v  in funcionalidades.items():
        print(f'[{k}] -> {v}')
    print('\n')
    acao_selecionada = input('Digite a ação desejada: ')

    limpatela()
    return acao_selecionada

def submenu(acao):
    if acao:
        print(f'SUBMENU > {funcionalidades[int(acao)]}')
        print('\nEscolha uma Funcionalidade:\n')
        acoes_possiveis = subfuncionalidades[int(acao)]

        for k, v in acoes_possiveis[0].items():
            print(f'[{k}] -> {v}')

        lista_idx = acoes_possiveis[0].keys()
        print(f'[{max(lista_idx)+1}] -> Voltar para menu')
        print('='*50)
        acao_selecionada = input('Digite a ação desejada: ')

        # verificando se é voltar a escolha
        # ta aqui porque uso um indice móvel é mutável a cada opção pai escolhida...
        if acao_selecionada == max(lista_idx)+1:
            limpatela()
            return None

        limpatela()
        return acao_selecionada
    
    else:
        raise 'ERRO'

##################
mapa_funcoes = {
     '1.1' : cadastra_cliente,                   # FEITO
     '1.2' : edita_cliente,                      # FEITO
     '1.3' : exclui_cliente,                     # FEITO
     '2.1' : cadastra_veiculo,                   # FEITO
     '2.2' : edita_veiculo,                      # FEITO
     '2.3' : exclui_veiculo,                     # FEITO
     '3.1' : cadastra_servicos_veiculo,          # FEITO
     '4.1' : registra_venda_veiculo,             # FEITO
     '5.1' : relatorio_veiculos_estoque,         # FEITO
     '5.2' : relatorio_veiculo_servicos,         # FEITO
     '5.3' : relatorio_vendas,                   # FEITO
     '5.4' : listar_clientes,                    # FEITO
 }   

# sistema
bemvindo()
while True:
    # try:
    acao = menu_principal()

    if verifica_sair(acao):
        break

    if acao:
        acao_especifica = submenu(acao) 

    if verifica_sair(acao_especifica):
        break

    if acao_especifica:
        funcao = retorna_funcao(acao, acao_especifica)
        limpatela()

        if not funcao is None:
            funcao(acao=acao, acao_especifica=acao_especifica)
        else:
            continue

    if verifica_sair(acao_especifica): # ????? precisa?
        break
