# Basic Calculator Program

A simple Python calculator program that performs basic arithmetic operations on two numbers. This project demonstrates fundamental programming concepts including variables, data types, user input, and error handling.

## 🚀 Features

### Basic Calculator
- ✅ Addition (+)
- ✅ Subtraction (-)
- ✅ Multiplication (*)
- ✅ Division (/)
- ✅ Division by zero protection
- ✅ Input validation
- ✅ Clean formatted output

### Enhanced Calculator
- ✅ All basic operations
- ✅ Modulus (%)
- ✅ Exponentiation (**)
- ✅ Multiple calculations in one session
- ✅ Enhanced error handling
- ✅ User-friendly interface

## 📋 Requirements

- Python 3.6 or higher
- No external libraries required

## 🔧 Installation

1. Clone this repository:
```bash
git clone https://github.com/CPeculiar/Basic_Calculator_Python_PLP_Assignment.git
```

2. Navigate to the project directory:
```bash
cd basic-calculator
```

3. Run the program:
```bash
python calculator.py
```

## 💻 Usage

### Basic Calculator Example
```
Enter the first number: 10
Enter the second number: 5
Enter the operation (+, -, *, /): +

10.0 + 5.0 = 15.0
```

### Enhanced Calculator Example
```
Enter the first number: 2
Enter the second number: 3
Enter the operation (+, -, *, /, %, **): **

2.0 ** 3.0 = 8.0

Do you want to perform another calculation? (y/n): n
```

## 🎯 Learning Objectives

This project demonstrates the following Python programming concepts:

- **Variables**: Storing and manipulating data
- **Data Types**: Working with integers, floats, and strings
- **User Input**: Getting input from users using `input()`
- **Conditional Statements**: Using `if/elif/else` for decision making
- **Exception Handling**: Managing errors with `try/except` blocks
- **String Formatting**: Using f-strings for clean output
- **Functions**: Organizing code into reusable functions
- **Loops**: Implementing repetitive operations
- **Dictionaries**: Storing key-value pairs for operations

## 📁 Project Structure

```
basic-calculator/
│
├── calculator.py          # Main calculator program
├── README.md             # Project documentation
```

## 🔍 Code Highlights

### Error Handling
```python
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter valid numbers!")
```

### Division by Zero Protection
```python
if operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed!")
```

### Clean Output Formatting
```python
print(f"{num1} + {num2} = {num1 + num2}")
```

## 🐛 Known Issues

- None at this time

## 🚀 Future Enhancements

- [ ] Add support for more advanced operations (square root, trigonometric functions)
- [ ] Implement calculation history
- [ ] Add a graphical user interface (GUI)
- [ ] Support for complex numbers
- [ ] Memory functions (store/recall)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Your Name**
- GitHub: [@cpeculiar](https://github.com/cpeculiar)
- Email: pecudamicable@gmail.com

## 🙏 Acknowledgments

- Thanks to the Python community for excellent documentation
- Inspired by the need to practice fundamental programming concepts

---

⭐ **If you found this project helpful, please give it a star!** ⭐