# String Calculator


### Simple add method
 - The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0) for example “” or “1” or “1,2”
 - Start with the simplest test case of an empty string and move to 1 and two numbers

### Allow the add method to handle an any amount of numbers
- example: `"1,2,3,4,5"` should return 15

### Allow the add method to handle new lines between numbers (instead of commas).
- example:  `“1\n2,3”` should return 6
- the following input is NOT ok:  `“1,\n”`

### Support different delimiters
- format: “//[delimiter]\n[numbers…]”
- example: `“//;\n1;2”` should return 3

### Calling Add with a negative number
- throw an exception “negatives not allowed”
- show all of negative addends in the exception message

### Numbers bigger than 1000 should be ignored
- example: `"1000,2"` should return 2

### Delimiters can be of any length
- format:  `“//[delimiter]\n”`
- example: `“//[***]\n1***2***3”`should return 6

### Allow multiple delimiters
- format:  `“//[delim1][delim2]\n”`
- example: `“//[*][%]\n1*2%3”` should return 6.
- make sure you can also handle multiple delimiters with length longer than one char
