#include <iostream>

int main()
{

	std::string s = "1115"; // ( 111 -> 5 ) => 55

	while (s.find("111") != -1)
	{
		int pozition = s.find("111");
		s.replace(pozition, 3, "5"); // позиция, 3 - количество, на "5" замена
	}

	std::cout << s;

	return 0;
}