# 🃏 Blackjack Game

> A command-line Blackjack game built in Python — from easy single player to intermediate multiplayer!

---

## 📖 Description

This is a fully playable command-line Blackjack game built in Python 3. The project was developed in stages — starting from a simple single player game and gradually adding features like multiplayer support, input validation, and dealer logic.

---

## ✨ Features

- 🃏 Full Blackjack gameplay with standard rules
- 🎉 Blackjack detection (21 with first 2 cards)
- 🔄 Ace handling — automatically switches between 11 and 1
- 🏦 Dealer draws until score reaches 17 or more
- 👥 Multiplayer support (1-4 players)
- ✅ Input validation for all user inputs
- 🎨 ASCII art logo display
- 🔁 Play again option after each round

---

## 📁 Project Structure

```
blackjack/
│
├── main.py              # Game entry point and restart loop
├── blackjack.py         # Core game logic and functions
├── blackjack_list.py    # Deck card values dictionary
└── art.py               # ASCII art logo
```

---

## 🚀 How to Install and Run

1. **Clone the repository:**
```bash
git clone https://github.com/Faith-75/blackjack.git
cd blackjack
```

2. **Make sure Python 3 is installed:**
```bash
python --version
```

3. **Run the game:**
```bash
python main.py
```

No external libraries needed — only Python's built-in `random` and `string` modules are used!

---

## 🎮 How to Play

1. Run the game and choose the number of players (1-4)
2. Each player is dealt 2 cards
3. The dealer shows only one card
4. Each player chooses to **hit** (draw a card) or **stand** (keep current hand)
5. Try to get as close to **21** as possible without going over
6. Going over 21 is a **bust** — automatic loss!
7. After all players finish, the dealer reveals their hand and draws until reaching 17
8. Scores are compared and winners are announced!

---

## 🃏 Card Values

| Card | Value |
|------|-------|
| 2 - 10 | Face value |
| Jack, Queen, King | 10 |
| Ace | 11 or 1 |

---

## 💡 Key Concepts Learned

- Functions and separation of concerns
- Lists and list of lists for multiplayer hands
- While loops and for loops
- Input validation with try/except
- Modular code structure with multiple files
- Dictionary usage for card values
- Recursive Ace handling with while loop

---

## 🐛 Interesting Bugs Fixed Along the Way

- **Global variable leaks** — functions were accidentally using global variables instead of parameters
- **Ace conversion** — needed a while loop not an if statement to handle multiple Aces
- **Dealer logic** — compare function was inside the dealer while loop causing premature game ending
- **Blackjack detection** — returning 0 as a special signal for Blackjack instead of 21

---

## 🔜 What's Next — Difficult Level

- 💰 Betting system with player balance
- 🂠 Real 52 card deck that depletes
- ✂️ Split — split identical cards into 2 hands
- 2️⃣ Double down — double bet for exactly one more card

---

## 👤 Author

**Faith-75**
- GitHub: [@Faith-75](https://github.com/Faith-75)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ and Python 3*
