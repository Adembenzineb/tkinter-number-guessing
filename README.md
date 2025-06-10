# Number Guessing Game

A simple and interactive number guessing game built with Python's Tkinter GUI library. Test your luck and intuition by guessing a randomly generated number within your chosen range!

## 🎮 Game Description

This is a classic number guessing game where the computer generates a random number within a range you specify, and you have to guess it within a limited number of attempts. The game provides helpful feedback after each guess to guide you toward the correct answer.

## 🚀 Features

- **Customizable Range**: Set your own minimum and maximum values for the random number
- **Limited Attempts**: You get 7 chances to guess the correct number
- **Interactive Feedback**: Get hints whether your guess is too high, too low, or correct
- **Input Validation**: Prevents invalid inputs and provides error messages
- **User-Friendly GUI**: Clean and simple interface built with Tkinter
- **Game Statistics**: Shows number of attempts used when you win

## 📋 Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## 🎯 How to Play

1. **Set the Range**: 
   - Enter a minimum number in the "select minimum" field
   - Enter a maximum number in the "select maximum" field

2. **Start the Game**: 
   - Click the "Start" button to generate a random number within your range
   - The game will display "You have 7 guesses"

3. **Make Your Guesses**: 
   - Enter your guess in the "Enter your guess" field
   - Click "Enter" to submit your guess
   - The game will tell you if your guess is:
     - **"Too high!"** - Your guess is greater than the target number
     - **"Too low!"** - Your guess is less than the target number
     - **"Correct!"** - You've found the number!

4. **Win or Lose**: 
   - If you guess correctly, you'll see a success message with your attempt count
   - If you use all 7 attempts without success, the game reveals the correct number

5. **Exit**: Click "Quit" to close the game

## 🔧 Installation & Running

1. Make sure you have Python installed on your system
2. Save the code as `number_guessing_game.py`
3. Run the game using:
   ```bash
   python number_guessing_game.py
   ```

## 💡 Game Strategy Tips

- Start with the middle value of your range to eliminate half the possibilities
- Use binary search strategy: always guess the middle of the remaining range
- Pay attention to the "too high" and "too low" feedback to narrow down your next guess
- Choose a reasonable range - too wide makes it very difficult!

## 🎨 Interface Elements

The game window (450x300 pixels) contains:
- Range selection inputs (minimum and maximum)
- Start button to begin the game
- Guess input field and Enter button
- Feedback display area
- Quit button to exit

## ⚠️ Input Validation

The game includes robust error handling:
- Checks for empty input fields
- Validates that inputs are numeric (decimal numbers only)
- Displays appropriate error messages for invalid inputs
- Prevents game crashes from unexpected user input

## 🔮 Example Gameplay

```
1. Set range: Min = 1, Max = 100
2. Click "Start" → Random number generated (let's say it's 67)
3. Guess: 50 → "Too low!"
4. Guess: 75 → "Too high!"
5. Guess: 62 → "Too low!"
6. Guess: 68 → "Too high!"
7. Guess: 65 → "Too low!"
8. Guess: 67 → "Correct! The number is 67. You guessed it in 6 attempts."
```

## 🛠️ Technical Details

- **Language**: Python 3.x
- **GUI Framework**: Tkinter
- **Random Number Generation**: Python's `random.randint()` function
- **Layout Manager**: Grid layout for organized component placement
- **Event Handling**: Button click events for game interactions

## 📝 Future Enhancements

Potential improvements you could add:
- Difficulty levels (different number of attempts)
- Score tracking across multiple games
- High score leaderboard
- Sound effects
- Better visual design with colors and themes
- Hint system for beginners

## 🐛 Known Limitations

- Only accepts positive integers
- Fixed number of attempts (7)
- Basic visual design
- No game history or statistics persistence

---

Enjoy playing the Number Guessing Game! 🎲