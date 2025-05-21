# Day-11-to-15
BlackJack Project, Coffee Machine, Hangman, etc. 

## Notes
It took me a whole month to be able to do Day 11 to 15. I've been re-doing the projects that I've had trouble on, and to be completely honest, I still have a hard time grasping on where it is I am struggling. I've read somewhere online, where in a normal college beginner python class the projects I've been doing are usually reserved for midterms or finals; here I am trying to complete these projects,a different one, once a day. 

I've redone these projects so much to the point where I can actually remember the solution, so now I'm seeking other projects I can possibly do at my skill level. 

## what i've learned 
###Scope 
- Local Scope: Variables (or functions) declared inside functions have local scope (also called function scope). They are only seen by other code within the same block of code.
  ``` javascript
  def my_function():
    my_local_var = 2 #within the function
  ```
- Global Scope: Variables or functions declared at the top level (unindented) of a code file have global scope. It is accessible anywhere in the code file.
  ``` javascript
  my_global_var = 3 #outside the function
  def my_function():
    # This works no problems
    print(my_global_var)
  ```
  - can modify the global scope, although it is not recommened since code can get really long, and modifying the global scope can lead to errors.
    ``` javascript
    a = 1
    def my_function():
      global a
      a += 1
      print(a)
    ```
    - if you want to modify the global scope, you can use input and return function for better syntax instead
    ``` javascript
    enemies = 1 
    def increase_enemies(ENEMY):
      return enemy + 1
    enemies = increase_enemies(enemy) ##all just to modify the global variable
    ```
    - global constants are usually formatted as ALL_CAPS! e.g. PI = 3.14 
- No Block Scope! This means that variables created nested in other blocks of code e.g. for loops, if statements, while loops etc. don't get local scope. They are given function scope if they are within a function or global scope if they are not.
  ``` javascript
  # Accessible anywhere
  my_global_var = 1

  def my_function():
      # Only accessible within my_function()
      my_local_var = 2
    
  for _ in range(10):
      # Accessible anywhere
      my_block_var = 3
  ```
### Tackling a Problem 
- Describe the problem
- reproduce the bug
- play computer (think or act like the computer)
- fix the error
- use print (printing result of the function can show you what's going on in the console)
- use a debugger (I really like to use thonny as it has an easy interface) 




