# ThueProject

This is a project I did for school in 2021, it is an interpreter, and a IDE for Thue language programming.  
  
Thue is a non-deterministic string replacement language.
A programm in Thue is composed of a string of text and a set of rules wich will be applied to it.
The order of the rules is arbitrary and can't be predicted, neither can be the part of the string that will be modified.  
  
Thue has a simple syntax to define rules:  
  
lhs ::= rhs  
with lhs being the string that will be detected and replaced by rhs  
there exists operators for input and output streams  
  
a:::  
will open up a dialog to ask for an input for each 'a' comprised inside the text  
a::=~b  
will display 'b' in the output field for each 'a' in the text.  
  
Rules are saved in a .thue file, that can be opened and edited by the program,  
Several examples of ruleset are available in /examples  
  
To execute a program, simply click the Execute button after having loaded a set of rules and an input text.
