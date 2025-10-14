#include <iostream>
int main(){
	int n = 5,total=0;
	int p;
	int i;
	double average;
	std::cout << "hello world \n";
	for(i=0;i<n;i++){
		std::cout << "Enter price of item : " << i + 1 << ": ";
		std::cin >> p;
		total += p;
	}
	std::cout << std::endl << "total price " << total << std::endl;
	average = (double) total / n;
	std::cout << "average price " << average << "\n";
}
