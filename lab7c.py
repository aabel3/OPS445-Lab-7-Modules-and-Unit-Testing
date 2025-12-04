#!/usr/bin/env python3

def function1():
    global authorName
    authorName = 'Andrew 1'
    print(authorName)

def function2():
    global authorName
    authorName = 'Andrew 2'
    print(authorName)

authorName = 'Andrew'
print(authorName)       # Andrew
function1()             # Andrew 1
print(authorName)       # Andrew 1
function2()             # Andrew 2
authorName = 'Andrew 1'
print(authorName)       # Andrew 1
