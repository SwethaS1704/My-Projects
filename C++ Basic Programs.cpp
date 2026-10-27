//data types
#include<iostream>
#include<iomanip>
#include<string>
using namespace std;
int main()
{
    int age=17;
    float cgpa=9.54e3;
    float pi=3.14151617181910283648742848;
    double p=3.14151617181910283648742848;
    bool isf=false;
    char a=66;
    string gr="Hi welcome";
    cout<<"My age is "<<age<<endl;
    cout<<"My CGPA is "<<cgpa<<endl;
    cout<<fixed<<setprecision(14);
    cout<<"Float is "<<pi<<endl;
    cout<<"Double is "<<p<<endl;
    cout<<isf<<endl;
    cout<<a<<endl;
    cout<<gr<<endl;
    return 0;
}


//dynamic memory allocation
#include<iostream>
using namespace std;
int main()
{
    int age=17;
    cout<<age<<endl;
    int *p;
    p=new int;
    *p=45;
    cout<<*p<<endl;
    cout<<p<<endl;
    cout<<new int<<endl;
    return 0;
}


//function overloading
#include<iostream>
using namespace std;
int sum(int a,int b)
{
    return a+b;
}
double sum(double a,int b)
{
    return a-b;
}
int sum(int a,int b,int c)
{
    return a+b+c;
}
double sum(double a,double b)
{
    return a+b;
}
double sum(int a,double b)
{
    return a+b;
}
int main()
{
    cout<<sum(2,3)<<endl;
    cout<<sum(2,3,4)<<endl;
    cout<<sum(2.5,3.5)<<endl;
    cout<<sum(2,3.5)<<endl;
    return 0;
}



//recursion
#include<iostream>
using namespace std;
int fibo(int n)
{
    if(n==0)
    {
        return 0;
    } 
    if(n==1)
    {
        return 1;
    }
    return fibo(n-1)+fibo(n-2);
}
int main()
{
    int a;
    cout<<"Enter number of terms:"<<endl;
    cin>>a;
    for(int i=0;i<a;i++)
    {
        cout<<fibo(i)<<endl;
    }
    return 0;
}



//marks calculation
#include <iostream>
using namespace std;
int main() 
{
    int n;
    cout << "Enter number of students: ";
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        int marks[5];
        int total = 0;
        float average;

        cout << "--- Student " << i << " ---"<<endl;
        int j = 0;
        while (j < 5)
        {
            cout << "Enter marks for Subject " << j + 1 << " (0-100): ";
            cin >> marks[j];
            if (marks[j] < 0 || marks[j] > 100) 
            {
                cout << "Invalid marks! Please enter between 0 and 100"<<endl;
                continue;
            }
            total += marks[j];
            j++;
        }
        average = total / 5.0;
        cout << "Total Marks = " << total<<endl;
        cout << "Average = " << average<<endl;

        if (average >= 90) 
        {
            cout << "Grade = A+"<<endl;
        }
        else if (average >= 80) 
        {
            cout << "Grade = A"<<endl;
        }
        else if (average >= 70) 
        {
            cout << "Grade = B"<<endl;
        }
        else if (average >= 60) 
        {
            cout << "Grade = C"<<endl;
        }
        else if (average >= 50) 
        {
            cout << "Grade = D"<<endl;
        }
        else 
        {
            cout << "Grade = F"<<endl;
        }

        bool passed = true;
        for (int k = 0; k < 5; k++) {
            if (marks[k] < 35) {
                passed = false;
                break;  // stop checking if one subject is failed
            }
        }

        if (passed) {
            cout << "Result = PASS"<<endl;
        }
        else {
            cout << "Result = FAIL"<<endl;
        }

    }
    cout << "\nProgram completed successfully!\n";
    return 0;
}



//access specifier
#include<iostream>
using namespace std;
class Student{
    private:
        int rollno;
    protected:
        string name;
    public:
        float marks;
    void setdata(int r,string n,float m){
        rollno=r;
        name=n;
        marks=m;
    }
    void display(){
        cout<<"Roll no:"<<rollno<<endl;
        cout<<"Name:"<<name<<endl;
        cout<<"Marks:"<<marks<<endl;
    }
};
int main(){
    Student s;
    s.setdata(101,"abc",90);
    s.display();
    return 0;
}



//constructor and destructor
#include<iostream>
using namespace std;
class Student{
    public:
        int rollno;
        string name;
    Student(int r,string n){            //constructor
        rollno=r;
        name=n;
        cout<<"Student object created using constructor"<<endl;
    }
    void display(){
        cout<<"Rollno:"<<rollno<<endl;
        cout<<"Name:"<<name<<endl;
    }
    ~Student(){
        cout<<"Student object destroyed using destructor"<<endl;
    }
};
int main(){
    Student s1(101,"ABC");
    s1.display();
    return 0;
}



//constructor overloading
#include<iostream>
using namespace std;
class Student{
    public:
    Student(){
        cout<<"Default constructor called:"<<endl;
    }
    Student(string name){
        cout<<"Constructor with name:"<<name<<endl;
    }
    Student(string name,int age){
        cout<<"COnstructor with name and age:"<<name<<","<<age<<endl;
    }
};
int main(){
    Student s1;
    Student s2("ABC");
    Student s3("ABC",20);
    return 0;
}



//pointers and references
#include<iostream>
using namespace std;
void swapref(int &a,int &b)
{
    int t=a;;
    a=b;
    b=t;
}
void swapptr(int *a,int *b)
{
    int t=*a;
    *a=*b;
    *b=t;
}
int main()
{
    int x,y;
    cout<<"Enter 2 numbers:"<<endl;
    cin>>x>>y;
    int &r=x;//reference
    int *p=&y;//pointer
    cout<<"reference variable &r= "<<r<<" ,pointer variable *p="<<*p<<endl;
    swapref(x,y);
    cout<<"swapref: value of x is "<<x<<" and y is "<<y<<endl;
    swapptr(&x,&y);
    swapptr<"swapptr: value of x is "<<x<<" and y is "<<y<<endl;
    return 0;
}
