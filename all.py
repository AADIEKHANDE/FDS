/*Write a Python program to store marks scored in subject “Fundamental of
Data Structure” by N students in the class. Write functions to compute
following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency
*/
def average(marks, n):
avg = 0
sum = 0
for i in marks:
if i!=-1:
sum = sum+i
else:
n=n-1
if n!=0:
avg = sum/n
print("Average Score ",avg)
def absent(marks):
ab = 0
for i in marks:
if i == -1:
ab = ab+1
print("No of absent Students : ",ab)
def max_min(marks):
max = 0
min = marks[0]
for i in marks:
if i!=-1:
if max<i:
max = i
if max>i:
min = i
print("Highest Score : ",max)
print("Lowest Score : ",min)
def highest_freq(marks):
temp = []
for i in range(50):
temp.append(0)
for i in marks:
temp[i] = temp[i]+1
max = 0
min = 0
for i in range(50):
if max < temp[i]:max = temp[i]
marks = i
print("Highest Frequency : ",marks)
def main():
marks = []
size = int(input("Enter No of Students : "))
for i in range(size):
marks.append(int(input("Enter Marks : ")))
average(marks,size)
absent(marks)
max_min(marks)
highest_freq(marks)
main()

/*Write a Python program to compute following computation on matrix:
a)Addition of two matrices
b) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix
*/

def read(r,c,mat) :
for i in range(r):
a=[]
for j in range (c):
num=int(input("enter a number"))
a.append(num)
mat.append(a)
def display(r,c,mat,str):
print(str)
for i in range(r):
for j in range (c):
print(mat[i][j],end=" ")
print()
def put_zeros(r,c,mat):
a = []
for i in range(r):
a=[]
for j in range(c):
a.append(0)
mat.append(a)
def addition(mat1,mat2,r1,c1,r2,c2,res):
if((r1 == r2) and (c1 == c2)):
put_zeros(r1,c1,res)
for i in range(r1):
for j in range (c1):
res[i][j]=mat1[i][j]+mat2[i][j]
display(r1,c1,res,"Addition")
else:
print("Matrix Addition not possible")
def subtract(mat1,mat2,r1,c1,r2,c2,res):
if((r1 == r2) and (c1 == c2)):
put_zeros(r1,c1,res)
for i in range(r1):
for j in range (c1):
res[i][j]=mat1[i][j]-mat2[i][j]
display(r1,c1,res,"Subtraction")
else:
print("Matrix Subtraction not possible")def multiply(mat1,mat2,r1,c1,r2,c2,res):
if (r2==c1):
put_zeros(r1,c2,res)
for i in range(r1):
for j in range(c2):
for k in range(r2):
res[i][j] += mat1[i][k] * mat2[k][j]
display(r1,c2,res,"Multiplication")
else:
print("Matrix Multiplication not possible")
def transpose(mat,r,c,res):
put_zeros(c,r,res)
for i in range(0,c):
for j in range(0,r):
res[i][j]=mat[j][i]
def main():
r1=int(input("Enter row for 1st matrix : "))
c1=int(input("Enter col for 1st matrix : "))
r2=int(input("Enter row for 2st matrix : "))
c2=int(input("Enter col for 2st matrix : "))
mat1=[]
mat2=[]
add = []
sub = []
multi = []
tran1 = []
tran2 = []
read(r1,c1,mat1)
display(r1,c1,mat1,"Matrix 1")
read(r2,c2,mat2)
display(r2,c2,mat2,"Matrix 2")
addition(mat1,mat2,r1,c1,r2,c2,add)
subtract(mat1,mat2,r1,c1,r2,c2,sub)
multiply(mat1,mat2,r1,c1,r2,c2,multi)
transpose(mat1,r1,c1,tran1)
transpose(mat2,r2,c2,tran2)
display(c1,r1,tran1,"Transpose of Matrix 1")
display(c2,r2,tran2,"Transpose of Matrix 2")
main()

/*Write a Python program to store first year percentage of students in array.
Write function for sorting array of floating point numbers in ascending order using
a)Selection Sort
b) Bubble sort and display top five scores.*/

def bubble_sort(score,n):
for i in range(n-1):
for j in range(n-1):
if score[j] > score[j+1]:
temp=score[j]
score[j]=score[j+1]
score[j+1]=temp
j=j+1
i=i+1
def selection_sort(score,n):
temp = 0
for i in range(n):
for j in range(i,n-1):
if score[i]>score[j+1]:
temp = score[i]
score[i] = score[j+1]
score[j+1] = temp
def display(score):
print("\nSorted Score")
for i in score:
print(i,end=" ")
def top_5(score,n):
print("\nTop 5 Scores")
for i in range(5):
print(score[(n-1)-i],end=" ")
def main():
score = []
n = int(input("Enter number of students : "))
for i in range(n):
score.append(float(input("Enter score : ")))
print("\n1.Selection Sort")
print("2.Bubble Sort")
c = int(input("Enter Your Choice : "))
if(c == 1):
selection_sort(score,n)
else:
bubble_sort(score,n)
display(score)
top_5(score,n)
main()

/*Write a Python program to store first year percentage of students in
array. Write function for sorting array of floating point numbers in ascending
order using quick sort and display top five scores.*/

def quicksort(a,p,q):
if p<q:
i = partition(a,p,q)
quicksort(a,p,i-1)
quicksort(a,i+1,q)
def partition(a,p,q):
x=a[p]
i=p
for j in range(i+1,q+1):
if a[j]<x :
i=i+1
a[i] , a[j] = a[j] , a[i]
a[p],a[i]=a[i],a[p]
return i
def top_5(score,n):
print("\nTop 5 Scores")
for i in range(5):
print(score[(n-1)-i],end=" ")
def display(score,text):
print(text)
for i in score:
print(i,end = " ")
print()
def main():
score = []
n = int(input("Enter number of students : "))
for i in range(n):
score.append(float(input("Enter score : ")))
display(score,"Marks of Students")
quicksort(score,0,n-1)
display(score,"After Sorting Score")
top_5(score,n)
main()

/*Write a program to search elements in an array using
a)Linear Search
b)Binary Search*/

#include<iostream>
using namespace std;
void linear(int arr[],int n,int key)
{
int flag = 0;
for(int i=0;i<n;i++)
{
if(arr[i] == key)
{
cout<<"\nElement is Found at Index : "<<i;
return;
}
}
cout<<"\nElement Not Found!!";
}
void binary(int arr[],int n,int key)
{
int st = 0,end,mid;
end = n - 1;
while (st <= end)
{
mid = ( st + end ) / 2;
if (arr[mid] == key)
{
cout<<"\nElement is Found at Index : " << (mid + 1);
return;
}
else if ( key > arr[mid])
{
st = mid + 1;
}
else if ( key < arr[mid])
{
end = mid - 1;
}
}
cout << "\nNumber Not Found!!";
}
int main()
{
int n,key;
cout<<"Enter no of Elements : ";cin>>n;
int arr[n];
for(int i=0;i<n;i++)
{
cout<<"Enter Element "<<i<<" : ";
cin>>arr[i];
}
cout<<"Enter Key to Search : ";
cin>>key;
int choice;
cout<<"\n1.Linear Search";
cout<<"\n2.Binary Search";
cout<<"\nEnter your Choice : ";
cin>>choice;
switch(choice)
{
case 1:
linear(arr,n,key);
break;
case 2:
binary(arr,n,key);
break;
default:
cout<<"\nWrong Choice";
break;
}
}


/*Department of Computer Engineering has student's club named 'Pinnacle
Club'. Students of second, third and final year of department can be granted
membership on request. Similarly one may cancel the membership of club.
First node is reserved for president of club and last node is reserved for secretary of club. Write C++
program to maintain club members information using singly linked list. Store student PRN and
Name. Write functions to:
a) Add and delete the members as well as president or even secretary.
b) Compute total number of members of club
c) Display members
d) Two linked lists exists for two divisions. Concatenate two lists.*/


#include<bits/stdc++.h>
using namespace std;
class sll
{
struct node{
int rollno;
string prn;
string name;
node *next;
}* start;
node *temp,*curr;
public:
sll()
{
start = NULL;
}
void create()
{
int choice=1;
do{
temp = new node;
cout<<"\nEnter Name : ";
cin>>temp->name;
cout<<"\nEnter Roll No : ";
cin>>temp->rollno;
cout<<"\nEnter Prn : ";
cin>>temp->prn;
temp->next = NULL;
if(start==NULL)
{
start = temp;
curr = temp;
}
else
{curr->next = temp;
curr = temp;
}
cout<<"\nDo you want to continue? (0/1) : ";
cin>>choice;
}while(choice!=0);
}
void display()
{
cout<<"\nDisplay The List\n";
node * ptr;
ptr = start;
do{
cout<<"Name : "<<ptr->name<<"\n";
cout<<"PRN : "<<ptr->prn<<"\n";
cout<<"Roll No : "<<ptr->rollno<<"\n\n";
ptr = ptr->next;
}while(ptr != NULL);
cout<<"\n\n";
}
void add_president()
{
node * ptr;
ptr = new node;
cout<<"\nEnter President Name : ";
cin>>ptr->name;
cout<<"\nEnter Roll No : ";
cin>>ptr->rollno;
cout<<"\nEnter Prn : ";
cin>>ptr->prn;
ptr->next = start;
start = ptr;
}
void add_secretary()
{
node * ptr, *last;
last = start;
do{
last = last->next;
}while(last->next != NULL);
ptr = new node;
cout<<"\nEnter Secretary Name : ";
cin>>ptr->name;
cout<<"\nEnter Roll No : ";
cin>>ptr->rollno;
cout<<"\nEnter Prn : ";
cin>>ptr->prn;ptr->next = NULL;
last->next = ptr;
}
void add_member()
{
int choice = 1;
do{
node *ptr, *last;
last = start;
do{
last = last->next;
}while(last->next->next != NULL);
ptr = new node;
cout<<"\nEnter Member Name : ";
cin>>ptr->name;
cout<<"\nEnter Roll No : ";
cin>>ptr->rollno;
cout<<"\nEnter Prn : ";
cin>>ptr->prn;
ptr->next = last->next;
last->next = ptr;
cout<<"Do you want to add more? (0/1) : ";
cin>>choice;
}while(choice != 0);
}
int getCount()
{
node *t;
int count=0;
t=start;
if(start==NULL)
{
cout<<"\nList is empty.";
return 0;
}
while(t!=NULL)
{
count++;
t=t->next;
}
cout<<"\nTotal "<<count<<" Members in the Club";
}
void del_member()
{
int flag=0;string no;
node *t,*prev;
if(start==NULL)
cout<<"\nClub is empty!!";
else
{
cout<<"\nEnter PRN of member to be deleted : ";
cin>>no;
t=start->next;
while(t->next!=NULL)
{
if(t->prn == no){
flag=1;
break;
}
prev=t;
t=t->next;
}
if(flag==1)
{
prev->next=t->next;
t->next=NULL;
delete t;
cout<<"\nMember with prn no "<<no<<" is deleted";
}
else
cout<<"\nMember not found in List";
}
}
void del_president()
{
node *t;
if(start==NULL)
cout<<"\nClub is Empty";
else
{
t=start;
start=start->next;
t->next=NULL;
delete t;
cout<<"\nPresident deleted";
}
}
void del_secretary()
{
node *t,*prev;
t=start;
if(start==NULL)
cout<<"\nClub is Empty";
else{
while(t->next!=NULL)
{
prev=t;
t=t->next;
}
prev->next=NULL;
delete t;
cout<<"\nSecretary Deleted";
}
}
void merge(sll &q1)
{
node *t,*p;
t=q1.start;
if(t==NULL)
{
cout<<"\nList 2 is empty";
return;
}
p=start; //first list
while(p->next!=NULL)
{
p=p->next;
}
p->next=t;
q1.start=NULL; //second list is set to null
cout<<"\nAfter concatenationlist";
display();
}
};
int main()
{
sll a;
int choice;
while(choice!=0)
{
cout<<"1.Create List \n";
cout<<"2.Add Member\n";
cout<<"3.Add President\n";
cout<<"4.Add Secretary\n";
cout<<"5.Delete Member\n";
cout<<"6.Delete President\n";
cout<<"7.Delete Secretary\n";
cout<<"8.Display\n";
cout<<"0.Exit\n\n";
cout<<"Enter your choice : ";
cin>>choice;switch(choice)
{
case 1:
a.create();
break;
case 2:
a.add_member();
break;
case 3:
a.add_president();
break;
case 4:
a.add_secretary();
break;
case 5:
a.del_member();
break;
case 6:
a.del_president();
break;
case 7:
a.del_secretary();
break;
case 8:
a.display();
break;
}
}
}


/*In any language program mostly syntax error occurs due to unbalancing delimiter such as (),
{},[]. Write C++ program using stack to check whether given expression is well parenthesized or
not.*/


#include<iostream>
#define MAX 50
using namespace std;
class stack
{
int arr[MAX];
int ptr;
public:
stack()
{
ptr = -1;
}
int top()
{
return arr[ptr];
}
void push(int ele)
{
if(ptr==MAX-1)
cout<<"Stack is Full";
else
{
ptr++;
arr[ptr] = ele;
}
}
void pop()
{
if(ptr==-1)
cout<<"Stack is Empty";
else
ptr--;
}
int empty()
{
if(ptr==-1)
return true;
else
return false;
}
};
bool isBalanced(string para)
{stack a;
for (int i = 0; i < para.length(); i++) {
if (a.empty()) {
a.push(para[i]);
}
else if ((a.top() == '(' && para[i] == ')')|| (a.top() == '{' && para[i] == '}')|| (a.top() == '[' &&
para[i] == ']')) {
a.pop();
}
else {
a.push(para[i]);
}
}
if (a.empty()) {
return true;
}
return false;
}
int main()
{
string para = "{()}[]";
cout<<"Enter Parenthesis Expression : ";
cin>>para;
if (isBalanced(para))
cout << "Balanced";
else
cout << "Not Balanced";
return 0;
}


/*A double-ended queue(deque) is a linear list in which additions and deletions may be made at
either end. Obtain a data representation mapping a deque into a one-dimensional array. Write C++
program to simulate deque with functions to add and delete elements from either end of the
deque.*/


#include<iostream>
using namespace std;
class deque
{
struct node
{
int data;
node *next;
}*front,*rear;
public:
deque()
{
front = NULL;
rear = NULL;
}
void insert_front()
{
int choice = 1;
do
{
node *temp;
temp = new node;
cout<<"enter data : ";
cin>>temp->data;
temp->next = front;
front = temp;
if(rear == NULL)
rear = temp;
cout<<"Do you want to continue (0/1) : ";
cin>>choice;
}
while(choice != 0);
}
void insert_rear()
{
int choice = 1;
do{
node *temp;
temp = new node;
cout<<"Enter Data : ";
cin>>temp->data;
if(rear == NULL)
{
temp->next = NULL;
rear = temp;
}
else
{
temp->next = NULL;
rear->next = temp;
rear = temp;
}if(front==NULL)
front = temp;
cout<<"Do you want to continue? (0/1) : ";
cin>>choice;
}while(choice!=0);
}
void del_front()
{
if(front == NULL)
cout<<"Deque is empty";
else
{
node *temp;
temp = front;
front = front->next;
delete temp;
cout<<"\nElement Deleted Successfully\n";
}
}
void del_rear()
{
if(rear == NULL)
cout<<"Deque is empty";
else
{
node *temp,*r;
temp = front;
do{
temp = temp->next;
}while(temp->next != rear);
temp->next = NULL;
r = rear;
rear = temp;
delete r;
cout<<"\nElement Deleted Successfully\n";
}
}
void display()
{
node *temp;
temp = front;
do
{
cout<<temp->data<<" ";
temp = temp->next;
}while(temp != NULL);
cout<<"\n";
}
};
int main()
{deque a;
int c=1;
while(c!=0)
{
cout<<"\n1.Add element at front";
cout<<"\n2.Add element at rear";
cout<<"\n3.Delete front";
cout<<"\n4.Delete rear";
cout<<"\n5.Display";
cout<<"\n0.Exit";
cout<<"\n\nEnter your choice : ";
cin>>c;
switch(c)
{
case 1:
a.insert_front();
break;
case 2:
a.insert_rear();
break;
case 3:
a.del_front();
break;
case 4:
a.del_rear();
break;
case 5:
a.display();
break;
}
}
}

"""
Group A - Assignment 1
In second year computer engineering class, group A students play
cricket,
group B students play badminton and group C students play football.
Write a python program using functions to compute following: -
a)
List of students who play both cricket and badminton
b)
List of students who play either cricket or badminton but not both
c)
Number of students who play neither cricket nor badminton
d)
Number of students who play cricket and football but not badminton.
(Note- While realizing the group, duplicate entries should be avoided, Do
not use SET built-in functions)
"""


def accept_set(A,Str):
n = int(input("Enter the total no. of student who play %s : "%Str))
for i in range(n) :
x = input("Enter the name of student %d who play %s : "%((i+1),Str))
A.append(x)
print("Set accepted successfully");
def display_set(A,Str):
n = len(A)
if(n == 0) :
print("\nGroup of Students who play %s =
else :
print("\nGroup of Students who play %s =
for i in range(n-1) :
print("%s,"%A[i],end=' ')
print("%s }"%A[n-1]);
def search_set(A,X) :
n = len(A)
for i in range(n):
if(A[i] == X) :
return (1)
return (0)
def find_intersection_set(A,B,C):
for i in range(len(A)):
flag = search_set(B,A[i]);
if(flag == 1) :
C.append(A[i])
def find_difference_set(A,B,C):
for i in range(len(A)):
flag = search_set(B,A[i]);
if(flag == 0) :
C.append(A[i])
def find_union_set(A,B,C):
for i in range(len(A)):
C.append(A[i])
for i in range(len(B)):
flag = search_set(A,B[i]);
if(flag == 0) :
C.append(B[i])
def Main()
Group_A
Group_B
Group_C
:
= []
= []
= []
{ }"%Str)
{"%Str,end=' ')while True :
print ("\t1 : Accept the Information")
print ("\t2 : List of students who play both cricket and badminton")
print ("\t3 : List of students who play either cricket or badminton
but not both")
print ("\t4 : Number of students who play neither cricket nor
badminton")
print ("\t5 : Number of students who play cricket and football but
not badminton")
print ("\t6 : Exit")
ch = int(input("Enter your choice : "))
Group_R = []
if (ch == 6):
print ("End of Program")
break
elif (ch==1):
accept_set(Group_A,"Cricket")
accept_set(Group_B,"Badminton")
accept_set(Group_C,"Football")
display_set(Group_A,"Cricket")
display_set(Group_B,"Badminton")
display_set(Group_C,"Football")
elif (ch==2):
display_set(Group_A,"Cricket")
display_set(Group_B,"Badminton")
find_intersection_set(Group_A,Group_B,Group_R)
display_set(Group_R," both Cricket and Badminton")
elif (ch==3):
display_set(Group_A,"Cricket")
display_set(Group_B,"Badminton")
R1 = []
find_union_set(Group_A,Group_B,R1)
R2 = []
find_intersection_set(Group_A,Group_B,R2)
find_difference_set(R1,R2,Group_R)
display_set(Group_R," either cricket or badminton but not both")
elif (ch==4):
display_set(Group_A,"Cricket")
display_set(Group_B,"Badminton")
display_set(Group_C,"Football")
R1 = []
find_union_set(Group_A,Group_B,R1)
find_difference_set(Group_C,R1,Group_R)
display_set(Group_R," neither cricket nor badminton")
print("Number of students who play neither cricket nor badminton =
%s"%len(Group_R))
elif (ch==5):
display_set(Group_A,"Cricket")
display_set(Group_C,"Football")
display_set(Group_B,"Badminton")
R1 = []
find_intersection_set(Group_A,Group_C,R1)
find_difference_set(R1,Group_B,Group_R)
display_set(Group_R,"cricket and football but not badminton")
print("Number of students who play cricket and football but not
badminton = %s"%len(Group_R))
else :
print ("Wrong choice entered !! Try again")
Main()
quit()
      
"""
Write a python program that determines the location of a saddle point of
matrix
if one exists. An m x n matrix is said to have a saddle point if some entry
a[i][j] is the smallest value in row i and the largest value in j.
"""
      
      
def accept_matrix(M) :
print("\nEnter the order of the Matrix (row,col) : ")
r = int(input("\trow = "))
c = int(input("\tcol = "))
print("Enter the elements of the Matrix : \n")
for i in range(r) :
A = []
for j in range (c) :
A.append(int(input()))
M.append(A)
print("\nMatrix accepted successfully\n")
def display_matrix(M,r,c):
print("Matrix (%d,%d) : "%(r,c))
for i in range(r) :
print("\t\t",end=' ')
for j in range(c):
print("%3d"%M[i][j],end=' ')
print("")
def check_for__saddlepoint(M,r,c) :
count = 0;
for i in range(r) :
#Find the minimum element of row i
min_row = M[i][0]
ci = 0
for j in range(1,c) :
if (min_row > M[i][j]) :
min_row = M[i][j];
ci = j
#Check if the min_row is also the maximum element of column or not
flag = 1
for ri in range(r) :
if (min_row < M[ri][ci]):
flag = 0
break
if (flag == 1) :
count += 1
print("%d value is minimum in row(%d) and maximum in column(%d)"%
(min_row,i+1,ci+1))
if (count == 0) :
print("No Saddle Point Exist for the given Matrix")
else :
print("%d Saddle Point Found in the given Matrix"%count)
def main():
while True :
print("\t\t\t1: Accept Matrix");
print("\t\t\t2: Display Matrix");
print("\t\t\t3: Find the Saddle Point");print("\t\t\t4: Exit");
ch = int(input("Enter your choice : "))
if (ch == 4):
print ("End of Program")
break
elif (ch==1):
Mat = []
print("Input the Matrix ")
accept_matrix(Mat)
r = len(Mat)
c = len(Mat[0])
elif (ch==2):
display_matrix(Mat,r,c)
elif (ch==3):
display_matrix(Mat,r,c)
check_for__saddlepoint(Mat,r,c)
else :
print ("Wrong choice entered !! Try again")
main()
quit()
      

"""
Group B - Assignment 15
Write a python program to store second year percentage of students in array.
Write function for sorting array of floating point numbers in ascending order
using
a) Insertion sort
b) Shell Sort and display top five scores
"""
      
def accept_array(A):
n = int(input("Enter the total no. of student : "))
for i in range(n):
x = float(input("Enter the Second year percentage of student %d : "%
(i+1)))
A.append(x)
print("Array accepted successfully\n\n");
def display_array(A):
n = len(A)
if(n == 0) :
print("\nNo records in the database")
else :
print("Array of SE Marks : ",end=' ')
for i in range(n) :
print("%.2f "%A[i],end=' ')
print("\n");
def Insertion_sort(A) :
n = len(A)
for i in range(1,n) :
element = A[i]
j = i-1
while( j >= 0) :
if (A[j] <= element) :
break
else :
A[j+1] = A[j]
j = j - 1
A[j+1] = element
def shell_sort(A,n):
gap = n // 2
while gap > 0:
for i in range(gap,n):
temp = A[i]
j = i
while j >= gap and A[j - gap] > temp:
A[j] = A[j - gap]
j =j-gap
A[j] = temp
gap= gap// 2def main() :
A = []
while True :
print ("\t1 : Accept & Display the SE Marks")
print ("\t2 : Insertion Sort Ascending order")
print ("\t3 : Shell sort Ascending order and display top five scores")
print ("\t4 : Exit")
ch = int(input("Enter your choice : "))
if (ch == 4):
print ("End of Program")
quit()
elif (ch==1):
A = []
accept_array(A)
display_array(A)
elif (ch==2):
print("Marks before sorting")
display_array(A)
Insertion_sort(A)
print("Marks after sorting")
display_array(A)
elif (ch==3):
print("Marks before sorting")
display_array(A)
n=len(A)
shell_sort(A,n)
print("Marks after sorting")
display_array(A)
n =len(A)
if(n >= 5) :
print("Top Five Scores : ")
for i in range(n-1,n-6,-1) :
print("\t%.2f"%A[i])
else :
print("Top Scorers : ")
for i in range(n-1,-1,-1) :
print("\t%.2f"%A[i])
else :
print ("Wrong choice entered !! Try again")
main()//Program to Calculate 1's, 2's complement and addition of binary numbers using DLL
#include<iostream>
using namespace std;
class binary;
class node
{
node *prev;
bool n;
node *next;
public:
node()
{
prev=next=NULL;
}
node(bool b)
{
n=b;
prev=next=NULL;
}
friend class binary;
};
class binary
{
node *start;
public:
binary()
{
start=NULL;
}
void generateBinary(int no);
void displayBinary();
void onesComplement();
void twoscomplement();
binary operator +(binary n1);
bool addBitAtBegin(bool val)
{
node *nodee=new node(val);
if(start==NULL)
{
start=nodee;
}
else
{
nodee->next=start;
start->prev=nodee;
start=nodee;
}
return true;
}};
void binary::generateBinary(int no)
{
bool rem;
node *p;
rem=no%2;
start=new node(rem);
no=no/2;
while(no!=0)
{
rem=no%2;
no=no/2;
p=new node(rem);
p->next=start;
start->prev=p;
start=p;
}
}
void binary::displayBinary()
{
node *t;
t=start;
while(t!=NULL)
{
cout<<t->n;
t=t->next;
}
}
void binary::onesComplement()
{
node *t;
t=start;
while(t!=NULL)
{
if(t->n==0)
t->n=1;
else
t->n=0;
t=t->next;
}
}
binary binary::operator +(binary n1)
{
binary sum;
node *a=start;
node *b=n1.start;
//
bit *s=sum.start;bool carry=false;
while(a->next!=NULL)
a=a->next;
while(b->next!=NULL)
b=b->next;
while(a!=NULL && b!=NULL)
{
sum.addBitAtBegin((a->n)^(b->n)^carry);
carry=((a->n&& b->n) || (a->n&& carry) || (b->n && carry));
a=a->prev;
b=b->prev;
}
while(a!=NULL)
{
sum.addBitAtBegin(a->n^carry);
a=a->prev;
}
while(b!=NULL)
{
sum.addBitAtBegin(b->n^carry);
b=b->prev;
}
sum.addBitAtBegin(carry);
return sum;
}
void binary::twoscomplement()
{
onesComplement();
bool carry=1;
node *t;
t=start;
while(t->next!=NULL)
{
t=t->next;
}
while(t!=NULL)
{
if(t->n==1 && carry==1)
{
t->n=0;
carry=1;
}
else
if(t->n==0 && carry==1)
{
t->n=1;carry=0;
}
else
if(carry==0)
break;
t=t->prev;
}
displayBinary();
}
int main()
{
int num,num1;
binary n1,n3,n2;
int choice=1;
do
{
cout<<"\n\n=========Binary Number Operations========\n";
cout<<"1. Generate binary\n2.One's Complement\n3.Two's Complement\n4.
Addition\n0.Exit\nEnter your choice: ";
cin>>choice;
switch(choice)
{
case 1: cout<<"\nENter Number in decimal form: ";
cin>>num;
n1.generateBinary(num);
cout<<"\nBinary Representation: ";
n1.displayBinary();
break;
case 2:cout<<"\nENter Number in decimal form: ";
cin>>num;
n1.generateBinary(num);
cout<<"\nBinary Representation: ";
n1.displayBinary();
cout<<"\nOnes Complement: ";
n1.onesComplement();
n1.displayBinary();
break;
case 3:cout<<"\nENter Number in decimal form: ";
cin>>num;
n1.generateBinary(num);
cout<<"\nBinary Representation: ";
n1.displayBinary();
cout<<"\nTwos complement; ";
n1.twoscomplement();
break;
case 4: cout<<"\nENter Two Decimal Numbers: ";
cin>>num>>num1;
n1.generateBinary(num);n2.generateBinary(num1);
n1.displayBinary();
cout<<" + ";
n2.displayBinary();
cout<<"= ";
n3=n1+n2;//n3=n1.operator+(n2);
n3.displayBinary();
}
}while(choice!=0);
return 0;
}
      
/**
A palindrome is a string of character that is the same forward and backward. Typically
, punctuation, capitalization, and spaces are ignored. For example,
||Poor Dan is in a droop|| is a palindrome, as can be seen by examining the
characters ||poor danisina droop|| and observing that they are the same forward
and backward. One way to check for a palindrome is to reverse the characters in the
string and then compare with them the original-in a palindrome, the sequence will
be identical. Write C++ program with functions-
1).
to check whether given string is palindrome or not that uses a stack to
determine whether a string is a palindrome.
2).
to remove spaces and punctuation in string, convert all the Characters to
lowercase, and then call above Palindrome checking function to check for a
palindrome
3).
to print string in reverse order using stack;
**/
       
       
#include<iostream>
#include<stdlib.h>
#define SIZE 80
using namespace std;
class mystack
{
private :
char ST[SIZE];
int top;
public :
mystack();
void push(char X);
char pop();
int isEmpty();
int isFull();
};
mystack :: mystack()
{
top = -1;
}
int mystack :: isEmpty()
{
if(top == -1)
return 1;
else
return 0;
}
int mystack :: isFull()
{
if(top == SIZE-1)
return 1;else
return 0;
}
void mystack :: push(char X)
{
if(!isFull())
{
top++;
ST[top] = X;
}
else
cout<<"\nStack Overflow !! Error!!";
}
char mystack :: pop()
{
char X = '\0';
X = ST[top];
top--;
return X;
}
void convert_string(char Str[],char Str1[])
{
int i,j = 0;
for(i=0;Str[i] != '\0';i++)
{
if(Str[i] >= 'a' && Str[i] <= 'z')
Str1[j++] = Str[i];
if(Str[i] >= 'A' && Str[i] <= 'Z')
Str1[j++] = Str[i] + 32;
}
Str1[j] = '\0';
}
int main()
{
int ch,flag,i;
char Str[80],Str1[80];
mystack S;
system("clear");
do
{
cout<<"\n\t\t\t1 : Check for Palindrome";
cout<<"\n\t\t\t2 : Find Reverse";
cout<<"\n\t\t\t3 : Exit";
cout<<"\n\nEnter ur choice : ";
cin>>ch;
switch(ch)
{case 1 : cout<<"\nEnter the string to be checked for palindrome : ";
cin.ignore();
cin.getline(Str,80);
cout<<"\nEntered String is "<<Str;
convert_string(Str,Str1);
cout<<"\nconverted String is : "<<Str1;
for(i = 0; Str1[i] != '\0';i++)
S.push(Str1[i]);
i = 0; flag = 1;
while(!S.isEmpty())
{
if(Str1[i++] != S.pop())
{
flag = 0;
break;
}
}
if(flag == 1)
cout<<"\nGiven string is a palindrome\n";
else
cout<<"\nGiven String is not a palindrome\n";
break;
case 2 : cout<<"\nEnter the string to be reversed : ";
cin.ignore();
cin.getline(Str,80);
cout<<"\nString entered is "<<Str;
for(i = 0; Str[i] != '\0';i++)
S.push(Str[i]);
cout<<"\nReverse String = ";
while(!S.isEmpty())
{
cout<<S.pop();
}
break;
case 3 : cout<<"\nEnd of Program\n";
break;
default: cout<<"\nInvalid choice !! Try again\n\n";
}
}while(ch != 3);
return 0;
}

       
/*Implement C++ program for expression conversion as infix to postfix and its evaluation using
stack based on given conditions:
1.Operands and operator, both must be single character.
2.Input Postfix expression must be in a desired format.
3.Only '+', '-', '*' and '/ ' operators are expected
*/
       
       
#include<iostream>
#include<stack>
#include<math.h>
using namespace std;
// defines the Boolean function for operator, operand, equalOrhigher precedence and the string
conversion function.
bool IsOperator(char);
bool IsOperand(char);
bool eqlOrhigher(char, char);
string convert(string);
int calculate_Postfix(string post_exp)
{
stack <int> stack1;
int len = post_exp.length();
// loop to iterate through the expression
for (int i = 0; i < len; i++)
{
// if the character is an operand we push it in the stack
// we have considered single digits only here
if ( post_exp[i] >= '0' && post_exp[i] <= '9')
{
stack1.push( post_exp[i] - '0');
}
// if the character is an operator we enter else block
else
{
// we pop the top two elements from the stack and save them in two integers
int a = stack1.top();
stack1.pop();
int b = stack1.top();
stack1.pop();
//performing the operation on the operands
switch (post_exp[i])
{
case '+': // addition
stack1.push(b + a);
break;
case '-': // subtraction
stack1.push(b - a);
break;
case '*': // multiplication
stack1.push(b * a);
break;
case '/': // divisionstack1.push(b / a);
break;
case '^': // exponent
stack1.push(pow(b,a));
break;
}
}
}
//returning the calculated result
return stack1.top();
}
int main()
{
string infix_expression, postfix_expression;
int ch;
do
{
cout << " Enter an infix expression: ";
cin >> infix_expression;
postfix_expression = convert(infix_expression);
cout << "\n Your Infix expression is: " << infix_expression;
cout << "\n Postfix expression is: " << postfix_expression;
//string postfix_expression = "59+33^4*6/-";
cout<<"\n The answer after calculating the postfix expression is : ";
cout<<calculate_Postfix(postfix_expression);
cout << "\n \t Do you want to enter infix expression (1/ 0)?";
cin >> ch;
//cin.ignore();
} while(ch == 1);
return 0;
}
// define the IsOperator() function to validate whether any symbol is operator.
/* If the symbol is operator, it returns true, otherwise false. */
bool IsOperator(char c)
{
if(c == '+' || c == '-' || c == '*' || c == '/' || c == '^' )
return true;
return false;
}
// IsOperand() function is used to validate whether the character is operand.
bool IsOperand(char c)
{
if( c >= 'A' && c <= 'Z') /* Define the character in between A to Z. If not, it returns False.*/
return true;
if (c >= 'a' && c <= 'z') // Define the character in between a to z. If not, it returns False. */
return true;
if(c >= '0' && c <= '9') // Define the character in between 0 to 9. If not, it returns False. */
return true;return false;
}
// here, precedence() function is used to define the precedence to the operator.
int precedence(char op)
{
if(op == '+' || op == '-')
/* it defines the lowest precedence */
return 1;
if (op == '*' || op == '/')
return 2;
if(op == '^') /* exponent operator has the highest precedence */
return 3;
return 0;
}
/* The eqlOrhigher() function is used to check the higher or equal precedence of the two operators
in infix expression. */
bool eqlOrhigher (char top_stack, char incoming)
{
int p1 = precedence(top_stack);
int p2 = precedence(incoming);
if (p1 == p2)
{
if (incoming == '^' )
return false;
return true;
}
return (p1>p2 ? true : false);
}
       
       
/* string convert() function is used to convert the infix expression to the postfix expression of the
Stack */
       
       
string convert(string infix)
{
stack <char> S;
string postfix ="";
char ch;
S.push( '(' );
infix += ')';
for(int i = 0; i<infix.length(); i++)
{
ch = infix[i];
if(ch == ' ')
continue;
else if(ch == '(')
S.push(ch);
else if(IsOperand(ch))
postfix += ch;
else if(IsOperator(ch))
{
while(!S.empty() && eqlOrhigher(S.top(), ch)){
postfix += S.top();
S.pop();
}
S.push(ch);
}
else if(ch == ')')
{
while(!S.empty() && S.top() != '(')
{
postfix += S.top();
S.pop();
}
S.pop();
}
}
return postfix;
}

       
/*
Queues are frequently used in computer programming, and a typical example is the creation of a job
queue by an operating system.
If the operating system does not use priorities, then the jobs are processed in the order they enter the
system.
Write C++ program for simulating job queue. Write functions to add job and delete job from queue.
*/
       
#include <iostream>
using namespace std;
#define size 5
class spq
{
int f,r,job,djob;
//data members
int simpq[size],prioq[size];
public:
spq() //Default constructor
{
f=r=-1; //init front and rear to -1.
job=djob=0;
prioq[-1]=0;
}
//To check Q is full or not
int isQfull()
{
if(r==size-1)
return 1;
else
return 0;
}
//To check Q is empty or not
int isQempty()
{
if((f==-1)||(f>r))
return 1;
else
return 0;
}
void simpqadd(); //member functions.
void showsimpleQ();
void delsimpleQ();
void prioqadd();
void delprioQ();
void showprioQ();
};
//To insert the job inside the simple queue.
void spq::simpqadd()
{
cout<<"\nEnter the Job: ";
cin>>job;
if(isQfull())cout<<"\nSorry !! Queue is full....\n";
else
{
if(f==-1)
{
f=r=0;
simpq[r]=job;
}
else
{
r=r+1;
simpq[r]=job;
}
}
}
//To delete job from the simple queue.
void spq::delsimpleQ()
{
if(isQempty())
cout<<"\nSorry Q is empty...\n";
else
{
djob=simpq[f];
f=f+1;
cout<<"\nDeleted job is: "<<djob;
}
}
//To show all the jobs from SimpleQueue.
void spq::showsimpleQ()
{
cout<<"\nThe simple Queue job are as follows....\n";
int temp;
for(temp=f;temp<=r;temp++)
{
cout<<"\t"<<simpq[temp];
}
}
//To delete job from the simple queue.
void spq::delprioQ()
{
if(isQempty())
cout<<"\nSorry Q is empty...\n";
else
{
djob=prioq[f];
f=f+1;
cout<<"\nDeleted job is: "<<djob;
}}
//To show all the jobs from PrioQueue.
void spq::showprioQ()
{
cout<<"\nThe priority Queue job are as follows....\n";
int temp;
for(temp=f;temp<=r;temp++)
{
cout<<"\t"<<prioq[temp];
}
}
//To add the jobs as per the priority.
void spq::prioqadd()
{
int t=0;
cout<<"\nEnter the job: ";
cin>>job;
if(isQfull())
cout<<"\nSorry!! Priority Queue is full...\n";
else
{
if(f==-1)
{
f=r=0; //initially when q is empty insert first job.
prioq[r]=job;
}
else if(job<prioq[r]) //Check the priority(Ascending) of incoming job if it is high
{
t=r;
while(job<prioq[t])//do until priority is high
{
prioq[t+1]=prioq[t]; //then shift all the jobs towards right
t=t-1; //decrement index to check another job.
}
t=t+1; //increment index
prioq[t]=job; //store job at its appropriate location.
r=r+1; //increment rear index by one
}
else
{
r=r+1; // as per the priority store in Q.
prioq[r]=job;
}
}
}
int main()
{
spq s1,s2; //object creation. s1 for simple Q and s2 for priority Q
int ch;do
{
cout<< "\n\t!!!Operating System Job Queue!!!" << endl; // prints the msg.
cout<<"\n1.SimpleQ Add_Job\n2.SimpleQ Del_Job\n3.Show SimpleQ\n4.PrioQ Add_Job\
n5.PrioQ Del_Job\n6.Show PrioQ";
cout<<"\nEnter Your Choice:";
cin>>ch;
switch(ch)
{
case 1:s1.simpqadd();break;//calling adding element in simple Q without priority.
case 2:s1.delsimpleQ();break;
case 3:s1.showsimpleQ();break;
case 4:s2.prioqadd();break;//calling adding element in priority Q with priority.
case 5:s2.delprioQ();break;
case 6:s2.showprioQ();break;
}
}while(ch!=7);
return 0;
}
