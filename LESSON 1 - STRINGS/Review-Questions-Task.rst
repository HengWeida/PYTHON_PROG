.. code:: ipython3

    #Create a string and print its length using the len() function.
    var1 = "Happy"
    print(len(var1))


.. parsed-literal::

    5
    

.. code:: ipython3

    #Create two strings, concatenate them, and print the resulting string.\
    var1 = "Happy"
    var2 = "Birthday"
    print(var1 + var2)


.. parsed-literal::

    HappyBirthday
    

.. code:: ipython3

    '''Create two strings and use concatenation to add a space inbetween
    them. Then print the result.'''
    var1 = "Happy"
    var2 = "Birthday"
    print(var1 + " " + var2)


.. parsed-literal::

    Happy Birthday
    

.. code:: ipython3

    '''Print the string "fox" by using slice notation on the string "The quick
    brown fox jumped over the lazy dog. #1234567890!" to specify the
    correct range of characters.'''
    var3 = ("The quickbrown fox jumped over the lazy dog. #1234567890!")
    print(var3[15:19])
    


.. parsed-literal::

    fox 
    

.. code:: ipython3

    '''Write a script that converts the following strings to lowercase:"Animals","Badger","Honey Bee","Honeybadger". 
    Print each lowercase string on a separate line.'''
    animalsVar1 = "Animals"
    animalsVar2 = "Badger"
    animalsVar3 = "Honey Bee"
    animalsVar4 = "Honeybadger"
    
    print(animalsVar1.lower())
    print(animalsVar2.lower())
    print(animalsVar3.lower())
    print(animalsVar4.lower())
    
    


.. parsed-literal::

    animals
    badger
    honey bee
    honeybadger
    

.. code:: ipython3

    #Repeat Exercise 1, but convert each string to uppercase instead of lowercase.
    animalsVar1 = "Animals"
    animalsVar2 = "Badger"
    animalsVar3 = "Honey Bee"
    animalsVar4 = "Honeybadger"
    
    print(animalsVar1.upper())
    print(animalsVar2.upper())
    print(animalsVar3.upper())
    print(animalsVar4.upper())
    


.. parsed-literal::

    ANIMALS
    BADGER
    HONEY BEE
    HONEYBADGER
    

.. code:: ipython3

    #Write a script that removes whitespace from the following strings:
    string1 = " Filet Mignon"
    string2 = "Brisket "
    
    print(string1.lstrip())
    print(string2.rstrip())
    


.. parsed-literal::

    Filet Mignon
    Brisket
    

.. code:: ipython3

    #Write a script that prints out the result of .startswith("be") on each ofthe following strings:
    string1 = "Becomes"
    string2 = "becomes"
    
    print(string1.startswith("be"))
    print(string2.startswith("be"))
    


.. parsed-literal::

    False
    True
    

.. code:: ipython3

    #Using the same strings from Exercise 4, write a script that uses string methods to alter each string so that .startswith("be") returns True for all of them.
    string1 = "Becomes"
    string2 = "becomes"
    
    print(string1.lower().startswith("be"))
    print(string2.startswith("be"))


.. parsed-literal::

    True
    True
    

.. code:: ipython3

    #Write a script that takes input from the user and displays that input back.
    ai1 = ("What is you're favorite movie? ")
    user = input(ai1)
    print("You said: " + user)


.. parsed-literal::

    What is you're favorite movie?  kingkong
    

.. parsed-literal::

    You said: kingkong
    

.. code:: ipython3

    #Write a script that takes input from the user and displays the input in lowercase.
    ai1 = ("What is you're favorite movie? ")
    user = input(ai1)
    print("You said: " + user.lower())


.. parsed-literal::

    What is you're favorite movie?  SJFBDF
    

.. parsed-literal::

    You said: sjfbdf
    

.. code:: ipython3

    #Write a script that takes input from the user and displays the number of characters inputted.
    ai3 = ("What perfume do you use?")
    user3 = input(ai3)
    print(len(user3))


.. parsed-literal::

    What perfume do you use? kqjwe
    

.. parsed-literal::

    5
    

.. code:: ipython3

    #Write a script named first_letter.py that first prompts the user for input by using the string "Tell me your name:" The script should then determine the first letter of the user’s input, convert that letter to upper-case, and display it back
    ai4 = ("Tell me your name: ")
    user4 = input(ai4)
    first_letter = user4[0].upper()
    print("The first letter of your name is: " + first_letter)


.. parsed-literal::

    Tell me your name:  Neri
    

.. parsed-literal::

    The first letter of your name is: N
    

.. code:: ipython3

    #Create a string containing an integer, then convert that string into an actual integer object using int(). Test that your new object is a number by multiplying it by another number and displaying the result.
    num = '10'
    num1 = int(num)
    print(num1 * 2)


.. parsed-literal::

    20
    

.. code:: ipython3

    #Repeat the previous exercise, but use a floating-point number and float().
    flt = '1.5'
    num2 = float(flt)
    print(num2 * 2)


.. parsed-literal::

    3.0
    

.. code:: ipython3

    #Create a string object and an integer object, then display them side by side with a single print statement by using the str() function.
    num = '6'
    num1 = 9
    print(num + str(num1))


.. parsed-literal::

    69
    

.. code:: ipython3

    #Write a script that gets two numbers from the user using the input() function twice, multiplies the numbers together, and displays the result.
    ai = ("Give me two numbers and I will multiply them! \n")
    num1 = input(ai)
    num2 = input()
    print("The answer is: ", int(num1) * int(num2))


.. parsed-literal::

    Give me two numbers and I will multiply them! 
     5
     5
    

.. parsed-literal::

    The answer is:  25
    

.. code:: ipython3

    #In one line of code, display the result of trying to .find() the substring "a" in the string "AAA".
    print("AAA".find('a'))


.. parsed-literal::

    -1
    

.. code:: ipython3

    #Replace every occurrence of the character "s" with "y” in the string "Somebody said something to Samantha."
    var = "Somebody said something to Samantha."
    var2 = var.replace("S", "Y").replace("s", "y")
    print(var2)


.. parsed-literal::

    Yomebody yaid yomething to Yamantha.
    

.. code:: ipython3

    #Write and test a script that accepts user input using the input() function and displays the result of trying to .find() a particular letter in that input
    user = input("Give me a word: ")
    print(user.find("a"))


.. parsed-literal::

    Give me a word:  back
    

.. parsed-literal::

    1
    

.. code:: ipython3

    '''Write a script called translate.py that asks the user for some input
    with the following prompt: Enter some text:. Then use the .replace()
    method to convert the text entered by the user into “leetspeak” by making the following changes to lower-case letters:
    • The letter a becomes 4
    • The letter b becomes 8
    • The letter e becomes 3
    • The letter l becomes 1
    • The letter o becomes 0
    • The letter s becomes 5
    • The letter t becomes 7
    Your program should then display the resulting string as output.
    Below is a sample run of the program:
    Enter some text: I like to eat eggs and spam.
    I 1ik3 70 347 3gg5 4nd 5p4m'''
    
    translate = input("Give me some text: ")
    translate1 = translate.replace("a", "4").replace("b", "8").replace("e", "3").replace("l", "1").replace("o", "0").replace("s", "5").replace("t", "7")
    print(translate1)
    


.. parsed-literal::

    Give me some text:  i want to eat some eggs
    

.. parsed-literal::

    i w4n7 70 347 50m3 3gg5
    

