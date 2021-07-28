#include <iostream> 
#include <algorithm> 

int main()
{
	int const length = 5;
	int array[length] = { 300, 510, 100000, 0, 40 };


	for (int startIndex = 0; startIndex < length - 1; ++startIndex)
	{


		int smallestIndex = startIndex;


		for (int currentIndex = startIndex + 1; currentIndex < length; ++currentIndex)
		{

			if (array[currentIndex] < array[smallestIndex])

				smallestIndex = currentIndex;
		}

		std::swap(array[startIndex], array[smallestIndex]);
	}

	for (int index = 0; index < length; ++index)
		std::cout << array[index] << ' ';

	return 0;
}