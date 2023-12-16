#1.	Prompt the user for a number which will represent the number of items in a list. Then use a for loop to add that many integers to the list. For example, if the use enters 3, the for loop should get 3 integers from the user and load them into the list. Then display the list.  

def dl1 (list1):
  x = int(input("How many items in your list? "))
  for x in range(0,x,1):
    s = int(input("Enter an integer: "))
    list1.append(s)
  return list1
def displaylist(list1):
  for item in list1:
      print(item)

#main
list1 = []   # define an empty list
list1 =  dl1(list1)  
#displaylist(list1)
print(" ")
print("Original list: ")
print(list1)
print(" ")

#2.	Insert the score of 99 at position 1 within the list. Display the updated list.
list1.insert(0,99)
print("New list once 99 is inserted at position 1: ")
print(list1)
print(" ")

#3.	Replace the value of 99 with the value 100. Display the updated list.
list1[0] = 100
print("New list once 99 is replaced with 100: ")
print(list1)
print(" ")

#4.	Create a second list with the values 500, 600, 700, 800, 900. Display this list. Extend the first list with this second list. Display the first list. 
list2 = ["500", "600", "700", "800", "900"]
print("Second list: ")
print(list2)
print(" ")

#4. Cont.
list1.extend(list2)
print("List one extended with list two: ")
print(list1)
print(" ")

#5.	Remove the value 800 from the first list. Display the first list. 
list1.remove("800")
print("List 1 with '800' removed: ")
print(list1)
print(" ")

#6.	Remove the third item from the first list. Display the first list. 
list1.remove(2)
print("List 1 with 3rd item removed: ")
print(list1)
print(" ")

#7.	Create a list of grades: grades =["A", "B", "C", "A", "A", "C"]
list3 = ["A", "B", "C", "A", "A", "C"]

#8.	Display a count of the number of A grades. 
print("Number of A grades in the list: ", list3.count("A"))
print(" ")

#9.	Display the index (position) of the first B grade. 
print("Index of the first B grade: ", list3.index("B"))
print(" ")

#10.	Look for grade of F in the grades list. Display a message that F is not in the list. (Do not let the code generate an error). 
def seqsearch(list3, grade):
  l = len(list3)
  sindex = -1
  for i in range(0, l, 1):
    if list3[i] == grade:
      sindex = i

  return sindex

Prompt = input("Do you want to search for a grade?")
while Prompt == "Yes" or Prompt == "yes" or Prompt == "YES" or Prompt == "Y" or Prompt == "y":
  grade = input("Enter the grade to search for: ")
  i = seqsearch(list3, grade)
  if i == -1:
    print(grade, "was not found")
  else:
    print(grade, "was found in the list.")
  Prompt = input("Do you want to search for another grade?")

#11.	Clear (but do not delete) the second list of integers. Display the list. )
list2.clear()
print(" ")
print("List two after being cleared: ")
print(list2)
print(" ")

#P12.	Delete the second list. Try to display it. (should get an error because the list no longer exists.  
#REMOVE THE HASHTAGS BEFORE LINES 99-102 TO SEE THE CODE RUN. THIS MUST BE WRITTEN AS A COMMENT IN ORDER TO RUN THE REST OF THE CODE.
#del list2
#print("List two after being deleted: ")
#print(list2)
#print(" ")

#13.	Create a list of players in this order (“Rizzo”, “Davis”, “Baez”, “Happ”, “Bryan”)
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

#14.	Sort the list of players. Display the sorted list. 
players.sort()
print("List of players sorted: ")
print(players)
print(" ")

#15.	Make a copy of the list of players called players2. Display players2.
players2 = players.copy()
print("Copy of list of players: ")
print(players2)
print(" ")

#16.	Reverse the order of players2. Display players, then display players2. 
players.reverse()
print("Original list of players: ")
print(players)
print(" ")
print("reversed, sorted, copy of list of players: ")
print(players2)
