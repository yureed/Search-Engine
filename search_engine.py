from re import search
from bs4 import BeautifulSoup
import timeit
import os
from Trie import Trie
from LinkedList import CircularList
from BST import BST
from HashTable import HashTable
from AVL import AVL
import operator

class SearchEngine:
    def __init__(self,directory,mode):
        self.directory = directory
        self.mode = mode
        self.filelist = []
        fileCount = 0
        if self.mode == 1:
            totalTime = 0
            tempLinked = CircularList() 
            for filename in os.listdir("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia"):
                with open(os.path.join("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia", filename), encoding = 'utf-8') as f:
                    soup = BeautifulSoup(f,features="html.parser")
                    text = soup.get_text()
                    text=list(text.split())
                    for i in text:
                        starttime = timeit.default_timer()
                        tempLinked.add(i)
                        time = timeit.default_timer() - starttime
                        totalTime += time
                    fileCount += 1
                    print(fileCount)
            print(f"Files loaded successfully. {fileCount} URLs loaded from the folder in {time} seconds")
            '''
            count = 1
            starttime = timeit.default_timer()  
            tempLinked = OrderedList()    
            for i in self.filelist:
                print(count)
                for j in i:
                    starttime = timeit.default_timer()
                    tempLinked.add(j)
                    time = timeit.default_timer() - starttime
                count += 1
            '''
            
        if self.mode == 2:
            for filename in os.listdir("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia"):
                with open(os.path.join("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia", filename), encoding = 'utf-8') as f:
                    soup = BeautifulSoup(f,features="html.parser")
                    soup.extract() 
                    text = soup.get_text()
                    text=list(text.split())
                    self.filelist.append(text)
                    fileCount +=1 
             
            tempBST = BST()     
            for i in self.filelist:
                for j in i:
                    starttime = timeit.default_timer() 
                    tempBST.insertR(j)
                    time = timeit.default_timer() - starttime
            print(f"Files loaded successfully. {fileCount} URLs loaded from the folder in {time} seconds")
        if self.mode == 3:
            for filename in os.listdir("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia"):
                with open(os.path.join("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia", filename), encoding = 'utf-8') as f:
                    soup = BeautifulSoup(f,features="html.parser")
                    soup.extract() 
                    text = soup.get_text()
                    text=list(text.split())
                    self.filelist.append(text)
                    fileCount +=1 
            tempAVL = AVL()     
            for i in self.filelist:
                for j in i:
                    starttime = timeit.default_timer() 
                    tempAVL.insertR(j)
                    time = timeit.default_timer() - starttime
            print(f"Files loaded successfully. {fileCount} URLs loaded from the folder in {time} seconds")

        if self.mode == 4:
            for filename in os.listdir("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia"):
                with open(os.path.join("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia", filename), encoding = 'utf-8') as f:
                    soup = BeautifulSoup(f,features="html.parser")
                    soup.extract() 
                    text = soup.get_text()
                    text=list(text.split())
                    self.filelist.append(text)
                    fileCount +=1 
              
            tempHash = HashTable()
            HashCount = 0     
            for i in self.filelist:
                for j in i:
                    starttime = timeit.default_timer()
                    tempHash.put(HashCount,j)
                    HashCount += 1
                    time = timeit.default_timer() - starttime
            print(f"Files loaded successfully. {fileCount} URLs loaded from the folder in {time} seconds")
        
        if self.mode == 5:
            for filename in os.listdir("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia"):
                with open(os.path.join("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia", filename), encoding = 'utf-8') as f:
                    soup = BeautifulSoup(f,features="html.parser")
                    soup.extract() 
                    text = soup.get_text()
                    text=list(text.split())
                    self.filelist.append(text)
                    fileCount +=1  
            tempTrie = Trie()     
            for i in self.filelist:
                for j in i:
                    starttime = timeit.default_timer()
                    tempTrie.insert(j)
                    time = timeit.default_timer() - starttime
            print(f"Files loaded successfully. {fileCount} URLs loaded from the folder in {time} seconds")

    
    def use_class(self):
        pass

    
    def search(self,term):
        if self.mode == 1:
            rankedList = self.selectLinked(term)
            return rankedList
        elif self.mode == 2:
            rankedList = self.selectBST(term)
            return rankedList
        elif self.mode == 3:
            rankedList = self.selectAVL(term)
            return rankedList
        elif self.mode == 4:
            rankedList= self.selectHash(term)
            return rankedList
        elif self.mode == 5:
            rankedList =self.selectTrie(term)
            return rankedList

    def selectLinked(self,term):
        self.filelist = []
        fileList = []
        for filename in os.listdir("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia"):
            with open(os.path.join("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikiepedia", filename), encoding = 'utf-8') as f:
                soup = BeautifulSoup(f,features="html.parser")
                soup.extract() 
                text = soup.get_text()
                text=list(text.split())
                self.filelist.append(text)
                fileList.append(filename)
        tempList = []
        tempDict = {}
        countFile = 0
        totalTime = 0
        totalSearch = 0
        tempClass = CircularList()
        for i in self.filelist:
            for j in i:
                tempClass.add(j) 
            starttime = timeit.default_timer()  
            temp = tempClass.search(term)
            time = timeit.default_timer() - starttime
            totalTime += time
            totalSearch = temp + totalSearch
            tempDict[fileList[countFile]] = temp
            countFile += 1
        print(f"{totalSearch} result(s) found in {totalTime} seconds")

        if totalSearch != 0:
            sortedDict = dict( sorted(tempDict.items(), key=operator.itemgetter(1),reverse=True))
        
            for key in sortedDict:
                tempList.append(key)
        else:
            tempList = None

        return tempList

    def selectBST(self,term):
        self.filelist = []
        fileList = []
        for filename in os.listdir("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia"):
            with open(os.path.join("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia", filename), encoding = 'utf-8') as f:
                soup = BeautifulSoup(f,features="html.parser")
                soup.extract() 
                text = soup.get_text()
                text=list(text.split())
                self.filelist.append(text)
                fileList.append(filename)
        tempList = []
        tempDict = {}
        countFile = 0
        totalTime = 0
        totalSearch = 0
        tempClass = BST()
        for i in self.filelist:
            for j in i:
                tempClass.insertR(j)
            starttime = timeit.default_timer() 
            temp = tempClass.inOrder(term)
            time = timeit.default_timer() - starttime
            totalTime += time
            totalSearch = temp + totalSearch
            tempDict[fileList[countFile]] = temp
            countFile += 1
        print(f"{totalSearch} result(s) found in {totalTime} seconds")

        if totalSearch != 0:
            sortedDict = dict( sorted(tempDict.items(), key=operator.itemgetter(1),reverse=True))
        
            for key in sortedDict:
                tempList.append(key)
        else:
            tempList = None
        return tempList
    
    def selectAVL(self,term):
        self.filelist = []
        fileList = []
        for filename in os.listdir("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia"):
            with open(os.path.join("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia", filename), encoding = 'utf-8') as f:
                soup = BeautifulSoup(f,features="html.parser")
                soup.extract() 
                text = soup.get_text()
                text=list(text.split())
                self.filelist.append(text)
                fileList.append(filename)
        tempList = []
        tempDict = {}
        countFile = 0
        totalTime = 0
        totalSearch = 0
        tempClass = BST()
        for i in self.filelist:
            for j in i:
                tempClass.insertR(j)
            starttime = timeit.default_timer()  
            temp = tempClass.search(term)
            time = timeit.default_timer() - starttime
            totalTime += time
            totalSearch = temp + totalSearch
            tempDict[fileList[countFile]] = temp
            countFile += 1
        print(f"{totalSearch} result(s) found in {totalTime} seconds")
        
        if totalSearch != 0:
            sortedDict = dict( sorted(tempDict.items(), key=operator.itemgetter(1),reverse=True))
        
            for key in sortedDict:
                tempList.append(key)
            print(tempList)
        else:
            tempList = None
        return tempList
    
    def selectHash(self,term):
        self.filelist = []
        fileList = []
        for filename in os.listdir("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia"):
            with open(os.path.join("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia", filename), encoding = 'utf-8') as f:
                soup = BeautifulSoup(f,features="html.parser")
                soup.extract() 
                text = soup.get_text()
                text=list(text.split())
                self.filelist.append(text)
                fileList.append(filename)
        tempList = []
        tempDict = {}
        countFile = 0
        totalTime = 0
        totalSearch = 0
        tempClass = BST()
        for i in self.filelist:
            for j in i:
                tempClass.insertR(j)
            starttime = timeit.default_timer()  
            temp = tempClass.search(term)
            time = timeit.default_timer() - starttime
            totalTime += time
            totalSearch = temp + totalSearch
            tempDict[fileList[countFile]] = temp
            countFile += 1
        print(f"{totalSearch} result(s) found in {totalTime} seconds")

        if totalSearch != 0:
            sortedDict = dict( sorted(tempDict.items(), key=operator.itemgetter(1),reverse=True))
        
            for key in sortedDict:
                tempList.append(key)
            print(tempList)
        else:
            tempList = None
        return tempList
    
    def selectTrie(self,term):
        self.filelist = []
        fileList = []
        for filename in os.listdir("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia"):
            with open(os.path.join("H://Yureed//UNIVERSITY//4thsemester//DSA//assignment2//wikipedia", filename), encoding = 'utf-8') as f:
                soup = BeautifulSoup(f,features="html.parser")
                soup.extract() 
                text = soup.get_text()
                text=list(text.split())
                self.filelist.append(text)
                fileList.append(filename)
        tempList = []
        tempDict = {}
        countFile = 0
        totalTime = 0
        totalSearch = 0
        tempClass = BST()
        for i in self.filelist:
            for j in i:
                tempClass.insertR(j)
            starttime = timeit.default_timer()  
            temp = tempClass.search(term)
            time = timeit.default_timer() - starttime
            totalTime += time
            totalSearch = temp + totalSearch
            tempDict[fileList[countFile]] = temp
            countFile += 1
        print(f"{totalSearch} result(s) found in {totalTime} seconds")

        if totalSearch != 0:
            sortedDict = dict( sorted(tempDict.items(), key=operator.itemgetter(1),reverse=True))
        
            for key in sortedDict:
                tempList.append(key)
            print(tempList)
        else:
            tempList = None
        return tempList
    
s = SearchEngine(1,1)