from typing import List
import nltk
import random
import string
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")  # Tokenizer
nltk.download("wordnet")  # English lemmatizer
nltk.download("omw-1.4")  # Portuguese lemmatizer


class ChatBot:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.responses = self._load_responses()
        self.greetings = [
            "olá",
            "oi",
            "e aí",
            "bom dia",
            "boa tarde",
            "boa noite",
        ]
        self.farewell = ["tchau", "até logo", "adeus", "até mais", "até breve"]

    def _load_responses(self):
        return {
            "internet": [
                "Problemas com internet podem ser resolvidos reiniciando seu roteador. Você já tentou desligar e ligar novamente?",
            ],
            "senha": [
                "Para redefinir sua senha, acesse a página de 'esqueci minha senha' no site de login.",
            ],
            "lento": [
                "Computador lento pode ser sinal de pouco espaço no disco ou memória insuficiente. Tente fechar programas não utilizados.",
            ],
            "impressora": [
                "Problemas com impressora geralmente são resolvidos reiniciando o dispositivo. Você já tentou desligar e ligar novamente?",
            ],
            "email": [
                "Não está recebendo emails? Verifique sua pasta de spam ou lixo eletrônico.",
            ],
            "software": [
                "Para reinstalar um software, primeiro desinstale a versão atual através do Painel de Controle/Configurações.",
            ],
            "hardware": [
                "Problemas de hardware geralmente requerem uma inspeção física. Verifique se todos os cabos estão conectados corretamente.",
            ],
            "wifi": [
                "Para melhorar o sinal WiFi, posicione o roteador em um local central, longe de paredes grossas e aparelhos eletrônicos.",
            ],
            "virus": [
                "Para remover vírus, execute um antivírus completo no sistema. Mantenha seu antivírus sempre atualizado.",
            ],
            "ajuda": [
                "Estou aqui para ajudar com problemas técnicos. Qual dificuldade você está enfrentando?",
            ],
            "default": [
                "Não tenho certeza se entendi completamente seu problema. Pode fornecer mais detalhes?",
                "Para melhor ajudá-lo, preciso de informações mais específicas sobre o problema que está enfrentando.",
                "Hmm, isso é algo que posso precisar encaminhar para um especialista. Pode explicar melhor a situação?",
            ],
        }

    def _parse_text(self, text: str) -> str:
        text = text.lower()
        text = "".join([char for char in text if char not in string.punctuation])
        return text

    def _tokenizer(self, text: str) -> List[str]:
        return nltk.word_tokenize(text, language="portuguese")

    def _lematizer(self, words: List[str]) -> List[str]:
        return [self.lemmatizer.lemmatize(word) for word in words]

    def _find_keyword(self, words: List[str]) -> str:
        keyword = set(words)
        for key in self.responses.keys():
            if key in keyword:
                return key

        related_words = {
            "internet": [
                "conexão",
                "rede",
                "wifi",
                "fibra",
                "banda",
                "larga",
                "net",
                "navegar",
                "navegador",
            ],
            "wifi": ["wireless", "sem", "fio", "sinal", "rede", "roteador", "modem"],
            "lento": [
                "devagar",
                "travando",
                "travar",
                "performance",
                "desempenho",
                "carregando",
                "demorado",
            ],
            "impressora": [
                "imprimir",
                "scanner",
                "digitalizar",
                "tinta",
                "cartucho",
                "papel",
                "imprimir",
            ],
            "email": [
                "correio",
                "eletrônico",
                "gmail",
                "outlook",
                "hotmail",
                "mensagem",
                "caixa",
                "entrada",
            ],
            "senha": [
                "login",
                "acesso",
                "conta",
                "entrar",
                "cadastro",
                "usuário",
                "password",
            ],
            "software": [
                "programa",
                "aplicativo",
                "app",
                "sistema",
                "windows",
                "mac",
                "instalar",
                "desinstalar",
            ],
            "hardware": [
                "equipamento",
                "dispositivo",
                "físico",
                "peça",
                "componente",
                "placa",
                "processador",
            ],
            "virus": [
                "malware",
                "trojan",
                "spyware",
                "infectado",
                "antivírus",
                "segurança",
                "proteção",
            ],
        }

        for categoria, terms in related_words.items():
            for word in words:
                if word in terms:
                    return categoria

        return "default"

    def answer(self, text: str) -> str:
        if not text:
            return "Por favor, digite algo."

        parsed_text = self._parse_text(text)
        words = self._tokenizer(parsed_text)
        words = self._lematizer(words)

        for word in words:
            if word in self.greetings:
                return f"{random.choice(self.greetings).capitalize()}! Como posso ajudar hoje?"
            if word in self.farewell:
                return f"{random.choice(self.farewell).capitalize()}! Foi um prazer conversar com você."

        keyword = self._find_keyword(words)
        return random.choice(self.responses[keyword])
