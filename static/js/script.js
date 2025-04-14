document.addEventListener("DOMContentLoaded", function () {
  const chatMessages = document.getElementById("chat-messages");
  const userInput = document.getElementById("user-input");
  const sendButton = document.getElementById("send-button");

  /**
   * @param {string} message
   * @param {bool} isUser
   */
  function addMessage(message, isUser) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    messageDiv.classList.add(isUser ? "user" : "bot");

    const messageContent = document.createElement("div");
    messageContent.classList.add("message-content");
    messageContent.textContent = message;

    messageDiv.appendChild(messageContent);
    chatMessages.appendChild(messageDiv);

    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

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

  /**
   * @param {string} message
   * */
  async function sendMessage(message) {
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

      chatMessages.removeChild(typingIndicator);

      addMessage(data.response, false);
    } catch (error) {
      console.error("Erro ao enviar mensagem:", error);
      chatMessages.removeChild(typingIndicator);
      addMessage(
        "Desculpe, ocorreu um erro na comunicação. Tente novamente mais tarde.",
        false,
      );
    }
  }

  sendButton.addEventListener("click", function () {
    const message = userInput.value.trim();
    if (message) {
      addMessage(message, true);
      userInput.value = "";
      sendMessage(message);
    }
  });

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

  const suggestions = [
    "Minha internet está lenta",
    "Esqueci minha senha",
    "Problemas com impressora",
    "Computador travando",
    "Não consigo acessar meu email",
  ];

  setTimeout(() => {
    addMessage(
      "Aqui estão alguns problemas comuns que posso ajudar a resolver:",
      false,
    );

    const suggestionsDiv = document.createElement("div");
    suggestionsDiv.classList.add("message", "bot");

    const suggestionsContent = document.createElement("div");
    suggestionsContent.classList.add("message-content", "suggestions");

    suggestions.forEach((suggestion) => {
      const btn = document.createElement("button");
      btn.classList.add("suggestion-btn");
      btn.textContent = suggestion;
      btn.addEventListener("click", () => {
        addMessage(suggestion, true);
        sendMessage(suggestion);
      });
      suggestionsContent.appendChild(btn);
    });

    suggestionsDiv.appendChild(suggestionsContent);
    chatMessages.appendChild(suggestionsDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }, 1000);

  userInput.focus();
});
