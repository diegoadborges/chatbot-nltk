from nltk.chat.util import Chat

pares = [
    [
        r"(oi|olá|bom dia|boa tarde|boa noite)",
        [
            "Olá! Bem-vindo ao suporte técnico. Como posso te ajudar hoje?",
            "Oi! Está enfrentando algum problema com seu dispositivo?",
            "Saudações! Pronto para resolver seu problema tecnológico.",
        ],
    ],
    [
        r"(tchau|até mais|valeu|falou)",
        [
            "Se precisar de mais ajuda, é só chamar!",
            "Até logo! Espero que tudo funcione bem por aí.",
            "Valeu! Estaremos por aqui se precisar.",
        ],
    ],
    [
        r".*(internet.*lenta|wifi.*lento|conexão.*lenta).*",
        [
            "Tente reiniciar seu modem e verifique se não há muitos dispositivos conectados.",
            "Você pode testar a velocidade em sites como speedtest.net e verificar se está condizente com seu plano.",
        ],
    ],
    [
        r".*(sem.*internet|caiu.*conexão|não.*conecta).*",
        [
            "Verifique se os cabos estão conectados corretamente e tente reiniciar o roteador.",
            "Às vezes o problema é na operadora. Você pode ligar lá para confirmar se há manutenção na sua região.",
        ],
    ],
    [
        r".*(meu computador.*não liga|pc.*não liga).*",
        [
            "Verifique se o cabo de energia está conectado e se há sinal de energia no estabilizador ou tomada.",
            "Tente segurar o botão de ligar por alguns segundos. Se não funcionar, pode ser um problema de hardware.",
        ],
    ],
    [
        r".*(impressora.*não funciona|não.*imprime|erro.*impressora).*",
        [
            "Verifique se a impressora está ligada, com papel e tinta, e conectada corretamente ao computador.",
            "Você já tentou reinstalar o driver da impressora?",
        ],
    ],
    [
        r".*(esqueci.*senha|como.*trocar.*senha).*",
        [
            "Para redefinir a senha, acesse a opção 'Esqueci minha senha' na tela de login do serviço.",
            "Verifique se o e-mail de recuperação está atualizado e siga os passos enviados.",
        ],
    ],
    [
        r".*(vírus|malware|computador.*lento).*",
        [
            "Recomendo rodar um antivírus confiável. Você pode usar o Windows Defender ou outro da sua preferência.",
            "Evite instalar programas de fontes desconhecidas e mantenha seu sistema atualizado.",
        ],
    ],
    [
        r".*(problema.*áudio|sem.*som).*",
        [
            "Verifique se o volume está ativado e os cabos de áudio estão conectados corretamente.",
            "Abra as configurações de som e veja se o dispositivo de saída está correto.",
        ],
    ],
    [
        r".*(tela.*azul|blue screen|erro.*sistema).*",
        [
            "A tela azul geralmente indica falha de hardware ou driver. Anote o código de erro e busque no site da Microsoft.",
            "Tente inicializar em modo de segurança e verifique se há atualizações pendentes.",
        ],
    ],
    [
        r".*(como.*formatar|resetar.*pc).*",
        [
            "Você pode usar a ferramenta de restauração do sistema no painel de configurações.",
            "Lembre-se de fazer backup dos seus arquivos antes de formatar o computador.",
        ],
    ],
    [
        r".*(não abre|app.*travando|programa.*erro).*",
        [
            "Tente reinstalar o aplicativo. Se o problema persistir, verifique se há atualizações disponíveis.",
            "Limpar o cache ou reiniciar o sistema pode ajudar nesse caso.",
        ],
    ],
    [
        r".*(como.*fazer backup|salvar arquivos).*",
        [
            "Você pode usar serviços de nuvem como Google Drive ou OneDrive, ou copiar para um HD externo.",
            "Organizar seus arquivos por pastas facilita muito na hora do backup!",
        ],
    ],
    [
        r".*(quais.*horários.*suporte|atendimento).*",
        [
            "Nosso suporte está disponível de segunda a sexta, das 8h às 18h.",
            "Pode mandar mensagem a qualquer hora, mas respondemos mais rápido durante o expediente.",
        ],
    ],
    [
        r".*(problema.*e-?mail|email.*erro|não.*recebo.*email|não.*envio.*email).*",
        [
            "Verifique se você está conectado à internet e se as configurações do servidor de e-mail estão corretas.",
            "Cheque a pasta de spam e se há espaço suficiente na sua conta para novos e-mails.",
            "Se estiver usando um cliente de e-mail como Outlook ou Thunderbird, tente remover e adicionar a conta novamente.",
        ],
    ],
]

reflexoes_pt = {
    "eu": "você",
    "me": "te",
    "meu": "seu",
    "minha": "sua",
    "meus": "seus",
    "minhas": "suas",
    "sou": "é",
    "estou": "está",
    "era": "era",
    "fui": "foi",
    "serei": "será",
    "estive": "esteve",
    "estava": "estava",
    "estarei": "estará",
    "você": "eu",
    "vc": "eu",
    "te": "me",
    "seu": "meu",
    "sua": "minha",
    "seus": "meus",
    "suas": "minhas",
    "é": "sou",
    "está": "estou",
    "foi": "fui",
    "será": "serei",
    "esteve": "estive",
    "estava": "estava",
    "estará": "estarei",
    "nós": "vocês",
    "nosso": "seu",
    "nossa": "sua",
    "nossos": "seus",
    "nossas": "suas",
    "vocês": "nós",
    "seus": "nossos",
    "suas": "nossas",
}

chatbot = Chat(pares, reflexoes_pt)


def get_response(user_input):
    resposta = chatbot.respond(user_input)
    if resposta:
        return resposta
    else:
        return (
            "Desculpe, não entendi muito bem. Poderia reformular ou dar mais detalhes?"
        )
