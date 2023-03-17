#include <iostream>
#include "string.h"
#include "function.cpp"
#include "order.h"

using namespace std;

int main(void)
{
    FruitList list;
    Receipt cashier;
    order *cust_order = new order[list.totalFruit];

    list.assign_fruit(cust_order);
    list.printMenu();
    cashier.getOrder(cust_order);
    cashier.printReceipt(cust_order,list.totalFruit);

    delete[] cust_order;
    
    int sen = 0;
    while(sen<=0)
    {
        cin>>sen;
    }

    return 0;
}


