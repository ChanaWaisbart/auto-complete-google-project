# **AUTO COMPLETE**
## Google Project
### By Chana Waisbart

<br/>

### **What is auto-complete program?**
In order to improve the user experience of the Google search engine, the development team decided to allow the completion of sentences from articles, documentation and information files on various technological topics.

### **About this program**
This project, implements an algorithm that load the 2021-archive txt files, and then run a cmd which lets you to enter word, hit enter, than get five sentences with best adjustment to the entered value as follows.
 ![](demo.gif)

### **Cope with mistakes at the entered word**

If no 5 options are found continue to the value entered,
A search for the same sentence will be performed with a single change.
Change can be - replacement, addition or omission of a single character 

### **Usage**
```
py AutoComplete.py 
```
Then will appear the message-
Loading the files and preparing the system ...
This step may take a few minutes, after which you can start entering the search term.

As long as you didn't enter '#' char , you continue the last sentence search. 
As you enter '#', you can begin new sentence.
The program is smart and ignore multiple spaces and special chars at the word.






