{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6ed46d62-4fd1-4ef3-91d8-1f09cdf8065c",
   "metadata": {},
   "outputs": [],
   "source": [
    "class sample():\n",
    "    def subfields():\n",
    "        List=[\"Machine Learning\",\"Neural Networks\",\"vision\",\"Robotics\",\"Speech Processing\",\"Natural Language Processing\"]\n",
    "        print(\"subfields in AI are\")\n",
    "        for name in List:\n",
    "            print(name)\n",
    "    def oddEven():\n",
    "        num=int(input(\"Enter a number\"))\n",
    "        if num%2==0:\n",
    "            print(num,\"is Even number\")\n",
    "        else:\n",
    "            print(\"Number is odd\")\n",
    "    def eligible():\n",
    "        gender=input(\"your gender\")\n",
    "        age=int(input(\"your Age\"))\n",
    "        if gender==\"male\" and age>21:\n",
    "            print(\"eligible for marriage\")\n",
    "        elif gender==\"female\" and age>21:\n",
    "            print(\"eligible for marriage\")\n",
    "        else:\n",
    "            print(\"not eligible for marriage\")\n",
    "    def percentage():\n",
    "        subject1=int(input(\"subject1\"))\n",
    "        subject2=int(input(\"subject2\"))\n",
    "        subject3=int(input(\"subject3\"))\n",
    "        subject4=int(input(\"subject4\"))\n",
    "        subject5=int(input(\"subject5\"))\n",
    "        total=subject1+subject2+subject3+subject4+subject5\n",
    "        print(\"Total:\",total)\n",
    "        per=total/5\n",
    "        print(\"percentage: {:.15f}\".format(per))\n",
    "    def Triangle():\n",
    "        Height=int(input(\"Height:\"))\n",
    "        Breadth=int(input(\"Breadth:\"))\n",
    "        print(\"Area formula:(Height*Breadth)/2\")\n",
    "        Area=(Height*Breadth)/2\n",
    "        print(\"Area of Triangle:\",Area)\n",
    "        Height1=int(input(\"Height1\"))\n",
    "        Height2=int(input(\"Height2\"))\n",
    "        Breadth=int(input(\"Breadth\"))\n",
    "        print(\"Perimeter formula:Height1+Height2+Breadth\")\n",
    "        perimeter=(Height1+Height2+Breadth)\n",
    "        print(\"perimeter of Triangle\",perimeter)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9352a3ab-3e48-4f51-92dd-24f0183a7d30",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
