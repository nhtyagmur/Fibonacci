{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "7ec64a09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "10\n",
      "44\n",
      "188\n",
      "798\n",
      "3382\n",
      "14328\n",
      "60696\n",
      "257114\n",
      "1089154\n",
      "4613732\n"
     ]
    }
   ],
   "source": [
    "F1=1\n",
    "F2=1\n",
    "Fn=0\n",
    "Sum=0\n",
    "while Fn<=4000000:\n",
    "    Fn=F1+F2\n",
    "    F1=F2\n",
    "    F2=Fn\n",
    "    if Fn%2==0:\n",
    "        Sum+=Fn\n",
    "        print(Sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e04aaf06",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8c2e991b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c5a21adc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0fa49238",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b20a16d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb1b1ca9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50596920",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
