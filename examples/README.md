Increment and Decrement require a binary number followed and preceded by underscores    
For example, Increment will change _0110_ into _0111_  
You can simulate any logic gate with Thue, AND,OR,XOR,and NOT will do those operations on a bit-by-bit case from the input text  
For example, AND will change 01101 into 0 and 111 into 1  
  
It is actually possible to simulate any logical operation by simply writing the truth table of the system as a set of rules  
  
Romain will take a binary number stored on 8 or less bits and transcript it into roman numerals.  
Note that the non-deterministic nature of Thue doesn't allow for exact roman numerals and we instead get a system similar to it,
where 4 is written IIII and 9 is written VIIII instead of IV and IX  
  
Adding a way to force the selection of rules to be made in a certain order is necessary to obtain a true roman number transcription, 
but doing so would make us lose the non-deterministic part of Thue.  
When putting multiple numbers as an input, Romain will sum them up and display the result as the additions of the number, as long as their sum is contained in 8 bits.  
