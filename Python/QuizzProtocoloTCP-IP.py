import random
from os import system as esac
from time import sleep

gabarito = ['A', 'B', 'A', 'D', 'D', 'B', 'D', 'B', 'C', 'C', 'C', 'C', 'D', 'A', 'D', 'C', 'C', 'A', 'A', 'A', 'C', 'C',
        'D', 'A', 'B', 'A', 'A', 'C','A', 'D', 'D', 'B', 'A', 'B', 'B', 'D', 'B', 'D', 'D', 'A', 'D', 'C', 'A', 'D', 
        'C', 'B', 'D', 'D', 'C', 'C','C']




pontos = [ 100, 20, 20, 50, 50, 20, 20, 50, 50, 100, 100, 75, 75, 50, 50, 100, 100, 20, 20, 50, 50, 20, 50, 20, 100, 50,
          50, 50, 50, 20, 100, 50, 20, 75, 20,
          50, 20, 100, 50, 20, 50, 100, 100, 100, 50, 100, 20, 20, 50, 50, 20]


pos = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,
41,42,43,44,45,46,47,48,49,50]
 #Cria um vetor com 50 posições com valores nulos para armazenar os valores que serão sorteados
vetsort = list() #Vetor para armazenar os valores sorteados
aux = list() #Irá armazenar todos os valores do vetor (VETSORT) que são os numeros sorteados
perguntasfeitas = list() #PEguntas já sorteadas
ran = 0
acertos = 0
erros = 0
cont = 1

print(len(gabarito))
print(len(pontos))
print(len(pos))


perguntas = [
    """X""",

    """As camadas do modelo OSI são, respectivamente:
    A) Física, Enlace, Rede, Transporte, Sessão, Apresentação e Aplicação
    B) Física, Enlace, Rede, Sessão, Transporte, Apresentação e Aplicação
    C) Física, Enlace, Rede, Transporte, Sessão, Aplicação e Apresentação
    D) Física,  Transporte, Sessão, Apresentação, Aplicação, Enlace e Rede
    """,

        """- Qunatas camadas possui o modelo TCP/IP     
        
        A) 3030 CAMADAS.
        B) 4 CAMADAS.
        C) 9 CAMADAS.
        D) Não possui camadas""",

        """- O protocolo DNS(DOMAIN NAME SYSTEM) é resposável por: 
        
        A) localizar e traduzir para números IP os endereços dos sites que digitamos nos navegadores.
        B) Dominar o mundo
        C) Deletar o endereço IP e MAC para obter maior desempenho.
        D) Estabelecer uma conexão com o Oráculo.""",

        """- Qual dos protocolos abaixo pertence à camada INTERNET do Modelo TCP/IP?
        
        A) IP
        B) HTTP
        C) FTP
        D) DNS""",

        """- Switch´s, roteadores e hubs pertencem a que camada?:
        
        A) Interna
        B) Rede
        C) externa
        D) Física
        """,

        """ - HTTP, SMTP, POP, PPP, SSH e FTP são exemplos de protocolos da camada de aplicação.
        
        A) Errado
        B) Certo
        """,

        """- Na camada Física, podem-se utilizar elementos de interconexão 
        como HUB, SWITCH E BRIGDE.
        
        A) Errado
        B) Certo""",

        """- No que diz respeito à arquitetura OSI, 
        detectar e corrigir erros é função da seguinte camada:
        
        A) Rede
        B) Física
        C) Enlace
        D) Sessão""",

        """- Em que ano foi criado o modelo OSI:
        A) 1900
        B) 1979
        C) 1894
        D) 1984""",

        """- Qual a finalidade da criação do modelo osi:
        A) Pare remover os protocolos da rede.
        B) Para realizar a formatação de dados.
        C) Para padronizar a criação de protocolos.
        D) Para rotear os pacotes através de uma rede.""",

        """- Qaul é a função da camada de transporte:
        A) Determinar uma arquitetura de protocolos para redes.
        B) Padronizar a criação de protocolos.
        C) Defini os meios e métodos para a entrega de dados ponta-a-ponta.
        D) Executar taredas solicitadas pela rede.""",

        """- O protocolo TCP pertence a a qual camada?:
        
        A) Rede 
        B) Física
        C) Transporte
        D) Enlace""",

        """- Abaixo estão algumas alternativas, somente UMA dela corresponde
        às CARACTERÍSTICAS do TCP, indentifique-a:
        
        A) Controle de fluxo, sequenciação e transferência de dados.
        B) Remontação de dados, serviço orientado à rede, gestão de pacotes.
        C) Envio de dados, transmissçao de dados, liberação de pacotes.
        D) Transporte de mensagens, capacidade de rotear, detecção de erros.""",

        """- Sobre as 7 camadas do modelo OSI é correto afirmar que:
        
        A) Elas dividem a comunicação em partes menores, facilitando a compreesã
            e o gerenciamento de incidentes/problemas.
        
        B) São responsáveis pelas especificações mecânicas elétricas, funcionais
            e os procedimentos.
        
        C) Permitem e habilitam as tecnologias mais antigas e as novas a se 
            conectarem à internet.
        
        D) Possibilitam a recuperãção automática da falha de qualquer dispositivo
            na rede.""",

        """- O que são protocolos:
        
        A) São mediadas cabíveis para a resoulução de problemas do cotidiano.
        B) São parâmetros para serem aplicados na culinária.
        C) São vestimentas típica do sul do brasil.
        D) São regras de comunicação usadas para conectar dois ou mais computadores.""",

        """- O que sgnificia RFC?
        
        A) Routing File Protocol
        B) Relay File Path
        C) Routing foward Path
        D) Request File Name""",

        """- Abaixo estão alguns protocolos, identificque os que pertecem ao modelo
        TCP/IP:
        
        A) TTC, KLK, THG e DFC.
        B) WSW, QAS, SXC, VFG e TGH.
        C) FTP, HTTP, SMTP e UDP.
        D) MMN, MMA, RMI, MIB.""",

        """-Qual a função do protocolo FTP:
        
        A) Permitir a transferência de arquivos entre dois computadores
        através de login e senha,
        B) É utilizado para o transporte de e-mail.
        C) É um método de designar endereços IPs
        D) É utilizados entre roteadores de diferentes sistemas.""",

        """- Quem criou o modelo OSI:
        
        A) A ISO (International Organization for Standardization)
        B) O OPI (Operation Party International.)
        C) A IMA ( International Murcle Arm.)
        D) o IPP ( International Party Purple.)""",
        """O TCP transacional é uma extensão do TCP que manipula interações
        cliente/servidor com um número reduzido de pacotes.
        A) Correto
        B) Errado""",

        """- Qual a função da camada de aplicação?
        
        A) Tem por objetivo padronizar todas as comunicações de rede. 
        B) Funções especializadas no nível de aplicação.
        C) Interpretar a informação contida na comunicação e executar a tarefa solicitada.
        D) Possuir a capacidade de decidir qual a melhor rota a seguir dentro da malha de rede. """,

        """- Qual a função da camada de sessão?
        
        A) identificar o tipo de requisição que está sendo realizada.
        B) funções especializadas no nível de aplicação.
        C) negociação e estabelecimento de conexão com outro nó.  
        D) não possuir as características de controle. """,

        """- Qual a função da camada de rede?
        
        A) define uma arquitetura de protocolos para redes
        B) produzir seus equipamentos de maneira a se comunicarem
        C) interpretar a informação contida na comunicação e executar a tarefa solicitada
        D) roteamento de pacotes por através de uma ou várias redes""",

        """-  Qual a função da camada de enlace?
        
        A) detecção e correção de erros introduzidos pelo meio de transmissão 
        B) garantir que a aplicação que iniciou a conversação encontrará no seu destino a aplicação desejada
        C) permite a transmissão mais rápida da informação
        D)  fornece comunicações de ponta a ponta""",

        """- Qual a função da camada de física?
        A) para padronizar a criação de protocolos
        B) transmissão dos bits através do meio de transmissão 
        C) permite que equipamentos de diferentes tecnologias, fabricantes e finalidades possam se entender
        D) roteamento de pacotes por através de uma ou várias redes""",

        """- Qual a função da camada de apresentação?
        A) formatação de dados e conversão de caracteres e códigos  
        B)  padronizar a criação de protocolos
        C) permitir a troca de um grande volume de informações
        D) observar como se relacionam as 4 camadas""",

        """- Os modelos de arquitetura OSI/ISO e TCP/IP possuem, 
        respectivamente, sete e quatro camadas. Na camada de rede, 
        o modelo OSI/ISO é compatível com a comunicação sem conexão e com a 
        comunicação orientada a conexões. No modelo TCP/IP, só há um modo de 
        operação na camada de rede (sem conexão), mas, na camada de transporte,
        o modelo TCP/IP aceita ambos os modos, oferecendo aos usuários a possibilidade 
        de escolha.
        
        A)  Verdadeiro
        B)  Falso""",

        """- No que diz respeito à arquitetura OSI, detectar e corrigir erros é função da seguinte camada:
        
        A) Rede
        B) Física.
        C) Enlace.
        D) Sessão.
        E) Aplicação.""",
        """- Quais os protocolos utilizados, respectivamente, para envio e recebimento de  e-mail?
        
        A) SMTP/POP.
        B) POP/SNMP.
        C) SNMP/POP.
        D) SMTP/SNMP.""",

        """- Considerando o modelo OSI, um exemplo de protocolo da camada de Aplicação é o:
        
        A) OSPF
        B) IPsec
        C) ARP
        D) FTP
        E) ICMP""",

        """ - No endereçamento existe alguns protocolos, dentre eles o mais atual é:
        
        A) IPV4
        B) IPv10
        C) IPv5
        D) IPv6 """,

        """ Dentre as camadas, qual delas possui um canal específico ou porta?
        
        A) Rede
        B) Transporte 
        C) Prototipação
        D) Endereçamento""",

        """ - O formato Datagrama UDP é dividido em duas partes quais são elas?
        
        A) cabeçalho e rodapé
        B) rodapé e informação
        C) cabeçalho e dados 
        D) dados e rodapé""",

        """ - O protocolo UDP é interessante por não necessitar de:
        
        A) controle 
        B) conexão
        C) senha
        D) dados""",

        """- A sigla do protocolo TCP significa:
        
        A) Treinamento de controle de protocolo.
        B) Protocolo de Controle de Transmissão. 
        C) Protocolo de Transmissão controlada.
        D)Centro de Tratamento de Protocolos.""",

        """- Com o TCP é garantido que:
        
        A) não tem conexão.
        B) o cabeçalho é pequeno.
        C) não foi entregue.
        D) foi entregue.""",

        """ O que não faz parte da camada de aplicação é:
        
        A) híbrido de cliente-servidor.
        B) controle de rede. 
        C) peer-to-peer.
        D) cliente-servidor""",

        """ - A camada de aplicação possui muitas características, qual delas abaixo não faz parte?
        
        A) Não possui perca de dados.
        B) Temporização.
        C) Segurança.
        D) vazão.""",

        """ - O TELNET é um protocolo que não transmite:
        A) Dados 
        B) Mensagem
        C) Segurança
        D) Arquivos descriptografado""",

        """ - A porta utilizada pelo protocolo SSH é:
        A) 55
        B) 896
        C) 22 
        D) 37""",

        """- A chave de autenticação utilizada pelo SSH é:
        
        A) estrangeira
        B) particular
        C) pública
        D) privada""",

        """- O limite de portas na camada de transporte vai até:
        
        A) 1024
        B) 1023
        C) 255
        D) 1000""",

        """ - O protocolo que verifica o cabeçalho é:
        
        A) UTP
        B) IP
        C) UDP
        D) TCP""",

        """- Entre os diversos protocolos que formam o Protocolo TCP/IP, aquele que é orientado 
        à conexão e fornece um serviço confiável de transferência de dados fim-a-fim é:
        
        A) ARP 
        B) IP
        C) RARP
        D) TCP
        E) UDP""",

        """ O modelo TCP/IP possui uma pilha de protocolos que atua na camada de transporte das redes de computadores. 
        Nessa camada, a comunicação entre processos finais, por meio de uma conexão virtual, utilizada): 
        
        A) o endereçamento com classes.
        B) o endereço socket.
        C) o paradigma peer-to-peer.
        D) o protocolo confiável UDP (User Datagram Protocol).
        E) os protocolos RARP, BOOT e DHCP.""",

        """- A porta TCP/IP padrão para o protocolo de comunicação news é a:
        
        A) 80.
        B) 119.
        C) 443.
        D) 1 024.
        E) 8 088.""",

        """- Entre os vários  protocolos TCP/IP, a camada responsável pelo envio de 
        pacotes individuais de um nó origem a um nó destino é a camada: 
        A) de enlace.
        B) de aplicação.
        C) de rede.
        D) de transporte.
        E) física""",

        """ - um protocolo de roteamento em redes TCP/IP que continua sendo muito utilizado é: 
        
        A) IPPR.
        B) DVMP.
        C) STP.
        D) RTCP.
        E) RIP.""",

        """- O modelo TCP/IP se divide em camadas. Assinale a opção que apresenta todas as camadas pertencentes a esse modelo : 
        
        A) transporte e rede 
        B) aplicação, transporte e rede 
        C) apresentação, aplicação, transporte e rede 
        D) apresentação e rede 
        E) aplicação, transporte, inter-rede e rede.""",

        """- As conexões TCP são do tipo:
        
        A) Full-duplex e multidifusão.
        B) Duplex e multidifusão.
        C) Full-duplex e ponto a ponto.
        D) Duplex e difusão.
        E) Simplex e ponto a ponto.""",

        """- Assinale a alternativa que indica o protocolo responsável por atribuir IPs dinamicamente.
        
        A) TCP.
        B) HTTP.
        C) DNS.
        D) GET IP.
        E) DHCP."""]


# SORTEIA OS VALORES PARA AS PERGUNTA E ARMAZENA NO VETOR (VETSORT)
while len(vetsort) != 51:
    num = random.choice(pos)
    vetsort.append(num)
    aux = vetsort
    for ele in aux:
        repete = vetsort.count(ele)
        while repete != 1:
            vetsort.remove(ele)
            repete -= 1


# Exibi a pergunta
def exibi_caixaperg():
    print(f"""
                   |-------------------------------------------------------|
                   |      PERGUNTA N°{cont},  VALE:{pontos[perguntasort]}                           |   
                   |-------------------------------------------------------|

    {perguntas[perguntasort]}             
               """)




# exibi o resultado
def resultado():
    print('Colhendo resultados...')
    sleep(2)
    esac('clear')
    print(f"""       |-----------------------------------------------------| 
                  |               R E S U L T A D O                     |
                  |-----------------------------------------------------|
                  |                                                     |
                  |    {nome}, Sua PONTUAÇÃO  foi de:`{totpont}            |       
                  |                                                     |
                  |           ACERTOS: {acertos}                           |
                  |           ERROS:  {erros}                               |
                  |=====================================================|                          
    """)
    final = int(input('Digite 0 para sair ou 1 para voltar ao menu.'))
    if final == 1:
        menu()
    else:
        exit()


####################################################################################


def primeirafase():
    global perguntasort, erros, acertos, totpont, cont
    cont = 1
    totpont = 0
    nome = str(input('Informe seu nome:'))
    esac('clear')
    print(f"OK {nome}, O quizz irá começar em 3 segundos...")
    sleep(1)
    
    for i in range(3, 0, -1):
        print(i)
        sleep(1)
    esac('clear')

    for i in range(1, 26):
        perguntasort = vetsort[i]
        exibi_caixaperg()
        perguntasfeitas.append(perguntasort)  # ARMAZENA AS PEGUNTAS JÁ FEITA EM UM VETOR
        resp = str(input("Digite uma das alternativas acima:")).upper()
        if resp == gabarito[perguntasort]:
            print("Você acertou!!")
            acertos += 1
            totpont += pontos[perguntasort]
        else:
            print("Você errou!")
            print(f"Resposta correta: {gabarito[perguntasort]}")
            erros += 1
        cont += 1
        esac('clear')

def segundafase():
    #Evita o encerramento do programa se o usuário introduzir uma resposta incorreta.
    continua = ''
    while (continua != 'S') and (continua != 'N'):
        continua = str(input('Deseja ir para a próxima fase? (S/N)')).upper()


    if continua == 'S':
        print('O quizz irá continuar em 3 segundos...')
        for i in range(3, 0, -1):
            print(i)

        esac('clear')
        for i in range(26,51):
            perguntasort = vetsort[i]
            exibi_caixaperg()
            resp = str(input("Digite uma das alternativas acima:").upper())
            if resp == gabarito[perguntasort]:
                sleep(1)
                print("Você acertou!!")
                acertos += 1
                totpont += pontos[perguntasort]
                sleep(1)
            else:
                print("Você errou!")
                print(f"Resposta correta: {gabarito[perguntasort]}")
                erros += 1
                sleep(1)
            cont += 1
            esac('clear')
    else:
        resultado()             

    resultado()


print("""
    ======================================================================
    |                                                                    |
    |               B E M  V I N D O  AO  Q U I Z Z!!                    |
    |--------------------------------------------------------------------|
    |              ASSUNTO:   MODELO OSI-TCP/IP                          |
    |--------------------------------------------------------------------|
    |                                                                    |
    |                        OPÇÕES                                      |
    |                                                                    |
    |                 1 - PARA INICIAR O QUIZZ                           |
    |                                                                    |
    |                 0 - PARA SAIR                                      |
    ----------------------------------------------------------------------
    """)
opcao = int(input("Digite uma das OPÇÕES acima:"))
esac('clear')

if opcao == 1:
    primeirafase()
    continua = ''
    while (continua != 'S') and (continua != 'N'):
        continua = str(input('Deseja ir para a próxima fase? (S/N)')).upper()

    segundafase()

else:
    exit()

