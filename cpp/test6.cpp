#include <iostream>
int main(){
		int *p,val1=100;
		p = &val1;
		std::cout << "value of val1 " << val1 << "\n";
		std::cout << "value of *p " << *p << "\n";
		val1=160;
		std::cout << "value of val1 " << val1 << "\n";
		std::cout << "value of *p " << *p << "\n";
		*p=200;
		std::cout << "value of val1 " << val1 << "\n";
		std::cout << "value of *p " << *p << "\n";
}

