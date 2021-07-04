# challenge3
Instrunctions to Install

1. Install Python  -> https://realpython.com/installing-python/
2. Git clone repo on local system && cd challenge3
3. Install required packages -> pip install -r requirements.txt
4. Run script -> python3 task3.py
    - Input Object Path
    - Input Key Value


Sample Input/output

sidharthaggarwal:~/study/python/challenge3$ python3 task3.py
Enter Object Path: {"a":{"b":{"c":"d"}}}
Enter key value in format x/y/z: a/b
{'c': 'd'}

sidharthaggarwal:~/study/python/challenge3$ python3 task3.py
Enter Object Path: {"a":{"b":{"c":"d"}}}
Enter key value in format x/y/z: a/b/d
path is not correct

sidharthaggarwal:~/study/python/challenge3$ python3 task3.py
Enter Object Path: {"a":{"b":{"c":"d"}}}
Enter key value in format x/y/z: a
{'b': {'c': 'd'}}

sidharthaggarwal:~/study/python/challenge3$ python3 task3.py
Enter Object Path: {“a”:{“b”:{“c”:”d”}}}
Object path is not correct
