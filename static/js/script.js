document.addEventListener("DOMContentLoaded", function () {
  const chatMessages = document.getElementById("chat-messages");
  const userInput = document.getElementById("user-input");
  const sendButton = document.getElementById("send-button");

  // Função para adicionar mensagem ao chat
  function addMessage(message, isUser) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    messageDiv.classList.add(isUser ? "user" : "bot");

    const messageContent = document.createElement("div");
    messageContent.classList.add("message-content");
    messageContent.textContent = message;

    messageDiv.appendChild(messageContent);
    chatMessages.appendChild(messageDiv);

    // Rolar para a mensagem mais recente
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Função para simular digitação (efeito de aguardando resposta)
  function showTypingIndicator() {
    const typingDiv = document.createElement("div");
    typingDiv.classList.add("message", "bot", "typing-indicator");

    const typingContent = document.createElement("div");
    typingContent.classList.add("message-content");
    typingContent.textContent = "Digitando...";

    typingDiv.appendChild(typingContent);
    chatMessages.appendChild(typingDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    return typingDiv;
  }

  // Função para enviar mensagem do usuário para o backend
  async function sendMessage(message) {
    // Mostrar indicador de digitação
    const typingIndicator = showTypingIndicator();

    try {
      const response = await fetch("/api/message", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: message }),
      });

      const data = await response.json();

      // Remover indicador de digitação
      chatMessages.removeChild(typingIndicator);

      // Adicionar resposta do bot ao chat
      addMessage(data.response, false);
    } catch (error) {
      console.error("Erro ao enviar mensagem:", error);
      // Remover indicador de digitação
      chatMessages.removeChild(typingIndicator);
      addMessage(
        "Desculpe, ocorreu um erro na comunicação. Tente novamente mais tarde.",
        false,
      );
    }
  }

  // Event listener para o botão de enviar
  sendButton.addEventListener("click", function () {
    const message = userInput.value.trim();
    if (message) {
      addMessage(message, true);
      userInput.value = "";
      sendMessage(message);
    }
  });

  // Event listener para tecla Enter
  userInput.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
      const message = userInput.value.trim();
      if (message) {
        addMessage(message, true);
        userInput.value = "";
        sendMessage(message);
      }
    }
  });

  // Sugestões de perguntas comuns
  const sugestoes = [
    "Minha internet está lenta",
    "Esqueci minha senha",
    "Problemas com impressora",
    "Computador travando",
    "Não consigo acessar meu email",
  ];

  // Adicionar sugestões iniciais após um curto delay
  setTimeout(() => {
    addMessage(
      "Aqui estão alguns problemas comuns que posso ajudar a resolver:",
      false,
    );

    const sugestoesDiv = document.createElement("div");
    sugestoesDiv.classList.add("message", "bot");

    const sugestoesContent = document.createElement("div");
    sugestoesContent.classList.add("message-content", "sugestoes");

    sugestoes.forEach((sugestao) => {
      const btn = document.createElement("button");
      btn.classList.add("sugestao-btn");
      btn.textContent = sugestao;
      btn.addEventListener("click", () => {
        addMessage(sugestao, true);
        sendMessage(sugestao);
      });
      sugestoesContent.appendChild(btn);
    });

    sugestoesDiv.appendChild(sugestoesContent);
    chatMessages.appendChild(sugestoesDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }, 1000);

  // Foco inicial no campo de input
  userInput.focus();
});
