/*
* Author: Drew Montooth
* Instructor: Alejandro Rosales
*/
#include <iostream>
using namespace std;


int main() {
	/*
	Ask for user name, dispaly hello _name_
	ask for x and y and then add them together 
	then display that saying ur answer is _answer_
	*/
	string name;
	cout << "What is your name: ";
	cin >> name;
	cout << "Hello: " << name << "\n";
	int x, y;
	cout << "Enter a number: ";
	cin >> x;
	cout << "Enter a second number: ";
	cin >> y;
	int sum = x + y;
	int sub = x - y;
	int mult = x * y;
	int div = x / y;
	int mod = x % y;
	cout << "Added numbers: " << sum << "\n";
	cout << "Subtracted: " << sub << "\n";
	cout << "Multiplied: " << mult << "\n";
	cout << "Divided: " << div << "\n";
	cout << "Modulus: " << mod << "\n";
	return 0;
}
