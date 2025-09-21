Tuples, Lists, and Dictionaries
===============================

Review Questions 1
==================

.. code:: ipython3

    CARDINAL_NUMBERS = ("FIRST", "SECOND", "THIRD")

.. code:: ipython3

    CARDINAL_NUMBERS = ("FIRST", "SECOND", "THIRD")
    print(CARDINAL_NUMBERS[1])


.. parsed-literal::

    SECOND
    

.. code:: ipython3

    POSITION1, POSITION2, POSITION3 = CARDINAL_NUMBERS
    print(POSITION1)
    print(POSITION2)
    print(POSITION3)


.. parsed-literal::

    FIRST
    SECOND
    THIRD
    

.. code:: ipython3

    MY_NAME = tuple("Neri, Sergio")

.. code:: ipython3

    MY_NAME = tuple("Neri, Sergio")
    print("X" in MY_NAME)


.. parsed-literal::

    False
    

.. code:: ipython3

    MY_NAME = tuple("Neri, Sergio")
    print(MY_NAME[1:])


.. parsed-literal::

    ('e', 'r', 'i', ',', ' ', 'S', 'e', 'r', 'g', 'i', 'o')
    

Review Question 2
=================

.. code:: ipython3

    FOOD = ["RICE", "BEANS"]

.. code:: ipython3

    FOOD = ["RICE", "BEANS"]
    FOOD.append("BROCCOLI")

.. code:: ipython3

    FOOD = ["RICE", "BEANS"]
    FOOD.append("BROCCOLI")
    FOOD.extend(["BREAD", "PIZZA"])

.. code:: ipython3

    FOOD = ["RICE", "BEANS"]
    FOOD.append("BROCCOLI")
    FOOD.extend(["BREAD", "PIZZA"])
    print(FOOD[:2])


.. parsed-literal::

    ['RICE', 'BEANS']
    

.. code:: ipython3

    FOOD = ["RICE", "BEANS"]
    FOOD.append("BROCCOLI")
    FOOD.extend(["BREAD", "PIZZA"])
    print(FOOD[-1])


.. parsed-literal::

    PIZZA
    

.. code:: ipython3

    BREAKFAST = "EGGS, FRUIT, ORANGE JUICE".split(", ")

.. code:: ipython3

    BREAKFAST = "EGGS, FRUIT, ORANGE JUICE".split(", ")
    print(len(BREAKFAST))


.. parsed-literal::

    3
    

.. code:: ipython3

    BREAKFAST = "EGGS, FRUIT, ORANGE JUICE".split(", ")
    LENGTHS = [len(item) for item in BREAKFAST]
    print(LENGTHS)


.. parsed-literal::

    [4, 5, 12]
    

Review Questions 3
==================

.. code:: ipython3

    DATA = ((1, 2), (3, 4))

.. code:: ipython3

    row = 1
    for t in DATA:
        print(f"Row {row} sum: {sum(t)}")
        row += 1


.. parsed-literal::

    Row 1 sum: 3
    Row 2 sum: 7
    

.. code:: ipython3

    NUMBERS = [5, 2, 9, 1, 3]

.. code:: ipython3

    NUMBERS = [5, 2, 9, 1, 3]
    COPY_NUMBERS = NUMBERS[:]

.. code:: ipython3

    NUMBERS = [5, 2, 9, 1, 3]
    COPY_NUMBERS = NUMBERS[:]
    NUMBERS.sort()
    
    print("Original copy: ", COPY_NUMBERS)
    print("Sorted numbers:", NUMBERS)


.. parsed-literal::

    Original copy:  [5, 2, 9, 1, 3]
    Sorted numbers: [1, 2, 3, 5, 9]
    

Challenge: List of Lists
========================

.. code:: ipython3

    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]
    
    for uni in universities:
        print(f"{uni[0]} - Students: {uni[1]}, Tuition: {uni[2]}")
    


.. parsed-literal::

    California Institute of Technology - Students: 2175, Tuition: 37704
    Harvard - Students: 19627, Tuition: 39849
    Massachusetts Institute of Technology - Students: 10566, Tuition: 40732
    Princeton - Students: 7802, Tuition: 37000
    Rice - Students: 5879, Tuition: 35551
    Stanford - Students: 19535, Tuition: 40569
    Yale - Students: 11701, Tuition: 40500
    

Challenge: Wax Poetic
=====================

.. code:: ipython3

    NOUNS = ["FOSSIL", "HORSE", "AARDVARK", "JUDGE", "CHEF", "MANGO", "EXTROVERT", "GORILLA"]
    
    VERBS = ["KICKS", "JINGLES", "BOUNCES", "SLURPS", "MEOWS", "EXPLODES", "CURDLES"]
    
    ADJECTIVES = ["FURRY", "BALDING", "INCREDULOUS", "FRAGRANT", "EXUBERANT", "GLISTENING"]
    
    PREPOSITIONS = ["AGAINST", "AFTER", "INTO", "BENEATH", "UPON", "FOR", "IN", "LIKE", "OVER", "WITHIN"]
    
    ADVERBS = ["CURIOUSLY", "FURIOUSLY", "SENSUOUSLY", "EXTRAVAGANTLY", "TANTALIZINGLY"]

Review Questions 4
==================

.. code:: ipython3

    CAPTAINS = {}

.. code:: ipython3

    CAPTAINS = {}
    CAPTAINS['Enterprise'] = 'Picard'
    CAPTAINS['Voyager'] = 'Janeway'
    CAPTAINS['Defiant'] = 'Sisko'

.. code:: ipython3

    CAPTAINS = {}
    CAPTAINS['Enterprise'] = 'Picard'
    CAPTAINS['Voyager'] = 'Janeway'
    CAPTAINS['Defiant'] = 'Sisko'
    
    if 'Enterprise' not in CAPTAINS:
        CAPTAINS['Enterprise'] = 'UNKNOWN'
    if 'Discovery' not in CAPTAINS:
        CAPTAINS['Discovery'] = 'UNKNOWN'

.. code:: ipython3

    CAPTAINS = {}
    CAPTAINS['Enterprise'] = 'Picard'
    CAPTAINS['Voyager'] = 'Janeway'
    CAPTAINS['Defiant'] = 'Sisko'
    
    if 'Enterprise' not in CAPTAINS:
        CAPTAINS['Enterprise'] = 'UNKNOWN'
    if 'Discovery' not in CAPTAINS:
        CAPTAINS['Discovery'] = 'UNKNOWN'
        
    for ship in CAPTAINS:
        print(f"The {ship} is captained by {CAPTAINS[ship]}.")


.. parsed-literal::

    The Enterprise is captained by Picard.
    The Voyager is captained by Janeway.
    The Defiant is captained by Sisko.
    The Discovery is captained by UNKNOWN.
    

.. code:: ipython3

    CAPTAINS = {}
    CAPTAINS['Enterprise'] = 'Picard'
    CAPTAINS['Voyager'] = 'Janeway'
    CAPTAINS['Defiant'] = 'Sisko'
    
    if 'Enterprise' not in CAPTAINS:
        CAPTAINS['Enterprise'] = 'UNKNOWN'
    if 'Discovery' not in CAPTAINS:
        CAPTAINS['Discovery'] = 'UNKNOWN'
    
    del CAPTAINS['Discovery']
    
    for ship in CAPTAINS:
        print(f"The {ship} is captained by {CAPTAINS[ship]}.")


.. parsed-literal::

    The Enterprise is captained by Picard.
    The Voyager is captained by Janeway.
    The Defiant is captained by Sisko.
    

.. code:: ipython3

    CAPTAINS2 = dict(
        Enterprise="Picard",
        Voyager="Janeway",
        Defiant="Sisko"
    )
    
    print("\nDictionary:")
    for ship in CAPTAINS2:
        print(f"The {ship} is captained by {CAPTAINS2[ship]}.")


.. parsed-literal::

    
    Dictionary:
    The Enterprise is captained by Picard.
    The Voyager is captained by Janeway.
    The Defiant is captained by Sisko.
    

CHALLENGE: CAPITAL CITY LOOP
============================

.. code:: ipython3

    capitals_dict = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta'
    }
    
    for state, capital in capitals_dict.items():
        print(f"The capital of {state} is {capital}.")


.. parsed-literal::

    The capital of Alabama is Montgomery.
    The capital of Alaska is Juneau.
    The capital of Arizona is Phoenix.
    The capital of Arkansas is Little Rock.
    The capital of California is Sacramento.
    The capital of Colorado is Denver.
    The capital of Connecticut is Hartford.
    The capital of Delaware is Dover.
    The capital of Florida is Tallahassee.
    The capital of Georgia is Atlanta.
    

