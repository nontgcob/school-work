const quotes = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Don't waste your time with explanations: people only hear what they want to hear. - Paulo Coelho",
    "You cannot hang out with negative people and expect to live a positive life. - Joel Osteen",
    "The greatest gift you can give someone is your time. Don't waste it on peple who don't value it.",
    "Surround yourself with those who bring out the best in you, not the stress in you.",
    "Life is too short to spend it with people who suck the happiness out of you.",
    "Respect yourself enough to walk away from anything that no longer serves you, grows you, or makes you happy. - Robert Tew",
    "Don't let the behavior of others destroy your inner peace. - Dalai Lama",
    "Stop letting people who do so little for you control so much of your mind, feelings, and emotions. - Will Smith",
  ];
  
  function pickRandomQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    const quoteElement = document.getElementById('quote');
    quoteElement.textContent = quotes[randomIndex];
  }
  
  document.getElementById('new-quote').addEventListener('click', pickRandomQuote);