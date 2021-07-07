# challenge3
Instrunctions to Install

1. Install Python3  -> https://realpython.com/installing-python/
2. Git clone repo on local system && cd challenge3
3. Install required packages -> pip3 install -r requirements.txt
4. Run script -> python3 task3.py
    - Input Object Path
    - Input Key Value


Sample Input/output

sidharthaggarwal:~/study/python/challenge3$ python3 task3.py <br />
Enter Object Path: {"a":{"b":{"c":"d"}}} <br />
Enter key value in format x/y/z: a/b <br />
{'c': 'd'} 

sidharthaggarwal:~/study/python/challenge3$ python3 task3.py <br />
Enter Object Path: {"a":{"b":{"c":"d"}}} <br />
Enter key value in format x/y/z: a/b/d <br />
path is not correct 

sidharthaggarwal:~/study/python/challenge3$ python3 task3.py <br />
Enter Object Path: {"a":{"b":{"c":"d"}}} <br />
Enter key value in format x/y/z: a <br />
{'b': {'c': 'd'}}

sidharthaggarwal:~/study/python/challenge3$ python3 task3.py <br />
Enter Object Path: {“a”:{“b”:{“c”:”d”}}} <br />
Object path is not correct
