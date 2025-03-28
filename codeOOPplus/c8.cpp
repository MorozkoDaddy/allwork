#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <locale>

// Определение структуры для хранения информации о химическом элементе
struct ChemicalElement {
	int atomicNumber;
	std::string name;
	double atomicMass;
	std::string symbol;
};

int main() {
	// Установка локали для поддержки русских символов
	std::setlocale(LC_ALL, "");
	
	const int MAX_ELEMENTS = 118; // Максимальное количество элементов в таблице Менделеева
	ChemicalElement elements[MAX_ELEMENTS];
	int numElements = 0;
	
	// Открытие файла для чтения
	std::ifstream infile("elemetns.txt");
	if (!infile) {
		std::cerr << "Не удалось открыть файл." << std::endl;
		return 1;
	}
	
	// Чтение данных из файла построчно
	std::string line;
	while (std::getline(infile, line)) {
		std::istringstream iss(line);
		if (!(iss >> elements[numElements].atomicNumber >>
			elements[numElements].name >>
			elements[numElements].atomicMass >>
			elements[numElements].symbol)) {
			std::cerr << "Ошибка чтения строки: " << line << std::endl;
			continue;
		}
		
		// Вывод промежуточных данных для отладки
		std::cout << "Прочитано: " << elements[numElements].atomicNumber << " "
		<< elements[numElements].name << " "
		<< elements[numElements].atomicMass << " "
		<< elements[numElements].symbol << std::endl;
		
		++numElements;
	}
	
	infile.close(); // Закрытие файла
	
	// Проверка, что файл не пуст
	if (numElements == 0) {
		std::cerr << "Файл пуст или не содержит данных." << std::endl;
		return 1;
	}
	
	// Вывод общего количества элементов
	std::cout << "Всего элементов: " << numElements << std::endl;
	
	// Вывод всех прочитанных данных
	for (int i = 0; i < numElements; ++i) {
		std::cout << "Элемент №" << elements[i].atomicNumber << ": "
		<< elements[i].name << ", символ: " << elements[i].symbol
		<< ", атомная масса: " << elements[i].atomicMass << std::endl;
	}
	
	return 0;
}
