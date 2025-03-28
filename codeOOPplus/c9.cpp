#include <iostream>
#include <fstream>
#include <vector>

int main() {
	const int N = 10;  // Количество чисел для записи в файл
	const std::string FILE_NAME = "numbers.dat";  // Имя файла
	
	// Создание вектора с числами
	std::vector<double> numbers(N);
	for (int i = 0; i < N; ++i) {
		numbers[i] = i + 1.0;  // Генерация чисел от 1.0 до N
	}
	
	// Открытие файла для записи
	std::ofstream output(FILE_NAME, std::ios::binary);
	if (!output) {
		std::cerr << "Ошибка открытия файла для записи." << std::endl;
		return 1;
	}
	
	// Запись чисел в файл
	for (double number : numbers) {
		output.write(reinterpret_cast<const char*>(&number), sizeof(double));
	}
	
	output.close();  // Закрытие файла после записи
	
	// Открытие файла для чтения
	std::ifstream input(FILE_NAME, std::ios::binary);
	if (!input) {
		std::cerr << "Ошибка открытия файла для чтения." << std::endl;
		return 1;
	}
	
	// Чтение первого числа
	double first_number;
	input.read(reinterpret_cast<char*>(&first_number), sizeof(double));
	
	// Переход в конец файла
	input.seekg(-sizeof(double), std::ios::end);
	
	// Чтение последнего числа
	double last_number;
	input.read(reinterpret_cast<char*>(&last_number), sizeof(double));
	
	// Нахождение разности
	double difference = first_number - last_number;
	
	// Вывод результата
	std::cout << "Разность первого и последнего числа: " << difference << std::endl;
	
	input.close();  // Закрытие файла после чтения
	
	return 0;
}
