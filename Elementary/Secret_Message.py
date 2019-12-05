'''
Дан кусок текста. Соберите все заглавные буквы в одно слово в том порядке как они встречаются в куске текста.

Например: текст = "How are you? Eh, ok. Low or Lower? Ohhh.", если мы соберем все заглавные буквы, то получим сообщение "HELLO".
Hello
'''




def find_message(text: str) -> str:
	count = ''
	for x in text:
		if x.isupper():
			count += x
	return count

if __name__ == '__main__':
	print('Example:')
	print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
	
	#These "asserts" using only for self-checking and not necessary for auto-testing
	assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
	assert find_message("hello world!") == "", "Nothing"
	assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
