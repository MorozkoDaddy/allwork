#include <iostream>
#include <string>
#include <vector>

int main() {
	// Пример строки с набором слов
	std::string words = "слово1;слово2а;слово3;слово4а:";
	
	// Разделяем строку на слова по символам ";" и ":"
	std::vector<std::string> words_list;
	size_t start = 0;
	size_t end = 0;
	
	while ((end = words.find(';', start)) != std::string::npos) {
		std::string word = words.substr(start, end - start);
		words_list.push_back(word);
		start = end + 1;
	}
	
	// Обрабатываем последнее слово перед двоеточием
	std::string last_word = words.substr(start, words.size() - start - 1);
	words_list.push_back(last_word);
	
	// Подсчитываем количество слов, оканчивающихся на "а"
	int count = 0;
	for (const auto& word : words_list) {
		if (word.back() == 'а' || word.back() == 'А') {
			count++;
		}
	}
	
	// Выводим результат
	std::cout << "Количество слов, оканчивающихся на букву 'а': " << count << std::endl;
	
	return 0;
}
