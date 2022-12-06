#ifndef FUNCTION_CPP
#define FUNCTION_CPP
#include <iostream>
#include "string.h"
#include "order.h"

using namespace std;

class FruitList
{
public:
    int totalFruit = 5;

    void printMenu()
    {
        cout << "Welcome to Only Fresh Fruit Shop\n"
             << endl;
        cout << "Today's fresh fruit <Price per kg>" << endl;
        cout << "0- Sunkist Orange RM2" << endl;
        cout << "1- Strawberry RM22" << endl;
        cout << "2- Papaya RM5" << endl;
        cout << "3- Star Fruit RM6" << endl;
        cout << "4- Kiwi RM10" << endl;
    }
    void assign_fruit(order *cust_order)
    {
        // initialize fruit name
        strcpy(cust_order[0].fruit_name, "Sunkist Orange");
        strcpy(cust_order[1].fruit_name, "Strawberry");
        strcpy(cust_order[2].fruit_name, "Papaya");
        strcpy(cust_order[3].fruit_name, "Star Fruit");
        strcpy(cust_order[4].fruit_name, "Kiwi");
        initialize_weight_price(cust_order);
    }

private:
    void initialize_weight_price(order *cust_order)
    {
        // initialize weight and price
        for (int i = 0; i < totalFruit; i++)
        {
            cust_order[i].weight = 0;
            cust_order[i].price = 0;
        }
    }
};

class Receipt
{
public:
    void getOrder(order *cust_order)
    {
        int fruit, price_per_kg, sen = 1;
        while (sen > 0)
        {

            cout << "\nEnter fruit code <-1 to stop>: ";
            cin >> fruit;
            if (fruit == -1 || fruit > 4)
            {
                sen = -1;
                break;
            }
            switch (fruit)
            {
            case 0:
                price_per_kg = 2;
                break;
            case 1:
                price_per_kg = 22;
                break;
            case 2:
                price_per_kg = 5;
                break;
            case 3:
                price_per_kg = 6;
                break;
            case 4:
                price_per_kg = 10;
                break;
            default:
                sen = -1;
            }

            if (cust_order[fruit].weight == 0)
            {
                cout << "Enter weight<kg>: ";
                cin >> cust_order[fruit].weight;
            }
            else
            {
                float add_weight;
                cout << "How many kg you want to add/remove for this fruit: ";
                cin >> add_weight;
                cust_order[fruit].weight += add_weight;
            }
            cust_order[fruit].price = price_per_kg * cust_order[fruit].weight;
        }
    }
    void printReceipt(order *cust_order, int totalFruit)
    {
        float total = 0;

        cout << "\n\n---------------------------------------" << endl;
        cout << "RECEIPT" << endl;
        for (int i = 0; i < totalFruit; i++)
        {
            if (cust_order[i].weight == 0)
                continue;
            cout << cust_order[i].fruit_name << " RM" << cust_order[i].price << endl;
            total += cust_order[i].price;
        }
        cout << "TOTAL = RM" << total << endl;
        cout << "---------------------------------------" << endl;
    }
};
#endif