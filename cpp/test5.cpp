#include <iostream>
int main(){
		int val1[10];
		int i;
		int sum=0;
		double avg;
		for(i=0;i<10;i++){
				std::cin >>val1[i]	;
		}
		for(i=0;i<10;i++){
				sum +=val1[i];
		}
		avg = (double) sum / 10;
		std::cout << "total value " << sum <<"\n";
		std::cout << "total average " << avg<<"\n";
}

