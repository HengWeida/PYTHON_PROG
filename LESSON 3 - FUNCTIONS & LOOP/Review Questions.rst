{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "46ca109c-9121-445f-a747-2265def38999",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "def cube(num):\n",
    "    return num ** 3\n",
    "print(cube(2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6e8cfbe0-568b-4ae3-9c97-6fd91bed8bcd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Alice !\n"
     ]
    }
   ],
   "source": [
    "def greet(name):\n",
    "    return (\"Hello \" + name + \" !\")\n",
    "print(greet(\"Alice\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2d2f4d0f-cd41-4eea-b9c7-d0b759876492",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a temperature in degrees F:  72\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "72.0 degrees f = 22.22 degrees C\n"
     ]
    }
   ],
   "source": [
    "farenheit = float(input(\"Enter a temperature in degrees F: \"))\n",
    "\n",
    "def convert_far_to_cel(farenheit):\n",
    "    return (farenheit - 32) * 5 / 9\n",
    "    \n",
    "celsius = convert_far_to_cel(farenheit)\n",
    "print(f\"{farenheit} degrees f = {celsius:.2f} degrees C\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8101d03c-364b-4f9d-beb4-5fbe35eb3df7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a temperature in degrees C:  37\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "37.00 degrees C = 98.60 degrees F\n"
     ]
    }
   ],
   "source": [
    "celsius = float(input(\"Enter a temperature in degrees C: \"))\n",
    "def convert_cel_to_far(celsius):\n",
    "    return (celsius * 9 / 5) + 32\n",
    "farenheit = convert_cel_to_far(celsius)\n",
    "print(f\"{celsius:.2f} degrees C = {farenheit:.2f} degrees F\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0a7ae80e-fd66-4f5d-9344-d1b6c12e62e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for n in range(2,11):\n",
    "    print(n)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d08908a6-9678-430e-96af-122ce1bd0b73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "n = 2\n",
    "while n < 11:\n",
    "    print(n)\n",
    "    n = n + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "50c11c7b-5f1c-4cb6-a0e5-71c6bb17ec8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a number to start doubling:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "8\n",
      "16\n"
     ]
    }
   ],
   "source": [
    "def doubles(num):\n",
    "    return num * 2\n",
    "\n",
    "number = int(input(\"Enter a number to start doubling: \"))\n",
    "\n",
    "for _ in range(3):\n",
    "    number = doubles(number)\n",
    "    print(number)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b64e819f-2a31-4283-9044-fe2bba905cf6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
