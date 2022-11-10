/*
Subject code: CSEB2213/CSEB214/CSNB244 Programming II/
                Programming II with C++
Section:01B
Student Name: Mus'ab Salihin Bin Mustaffa
Student ID no: SW01081837
Question no: 
*/

#include <iostream>

using namespace std;

//create class Rectangle
class Rectangle {
    
//initialize private data members
double length, width;

//initialize public data members
public:
    //set data from main to private data members
    void setdata(double l,double w)
    {
        length = l;
        width = w;
    }
    //calculate perimeter
    double perimeter()
    {
        return length+length+width+width;
    }
    //calculate area
    double area()
    {
        return length*width;
    }
    //show data in main
    void showdata()
    {
        cout<<"length: "<<length<<endl;
        cout<<"width: "<<width<<endl;
        cout<<"Perimeter: "<<perimeter()<<endl;
        cout<<"Area: "<<area()<<endl;
    }
};

int main(void)
{
    //initialize object
    Rectangle rect;
    //initialize length and width to get from user in main
    double l, w;
    //get input from user
    cout<<"Length: ";
    cin>>l;
    cout<<"Width: ";
    cin>>w;
    
    //set input to object's variables
    rect.setdata(l,w);
    
    //show data length,width,perimeter,area in main
    rect.showdata();

    return 0;
}