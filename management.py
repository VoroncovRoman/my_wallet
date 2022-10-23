"""
Содержит набор функций по работе с базой данных со стороны приложения
"""

import sqlite3


def parse_date(date: str) -> str:
	if '/' in date:
		date = date.split('/')
	elif '-' in date:
		date = date.split('-')
	elif '.' in date:
		date = date.split('.')


	# === Если указаны год, месяц и день
	if len(date) == 3:
		date = str(date[2]) + str()

	print(date)



def push_history_data(data: list[str, int]) -> None:
	"""Заносит получаемые значения а БД"""
	conn = sqlite3.connect('wallet.db')
	cur = conn.cursor()
	try:
		cur.execute("INSERT INTO history VALUES (?,?,?,?,?,?,?)", (data))
		conn.commit()
		print('Данные успешно добавлены в БД')
	except:
		message = """ОШИБКА, функция "add_operation_dialog":\nПри добавлени записи в БД, что-то пошло не так"""
		print(message)
	conn.close()



def get_last_balance(wallet_name: str) -> int:
	"""Возвращает значение баланса последней записи"""
	conn = sqlite3.connect('wallet.db')
	cur = conn.cursor()
	try:
		req = """
		SELECT balance FROM history
		WHERE rowid = (
			SELECT MAX(rowid) FROM history
			WHERE wallet_name = '{0}'
		)
		""".format(wallet_name)
		
		cur.execute(req)
		conn.commit()
	except:
		message = """ОШИБКА, функция "get_last_balance":\nПри чтении БД что-то пошло не так"""
		print(message)

	balance = cur.fetchone()[0]
	conn.close()
	
	return balance


def add_history_data_dialog() -> None:
	"""Реализует получение данных от пользователя и их проверку"""
	print('Внесение новой информации в таблицу history'+ '\n'+'='*80)

	date = input('Введите дату операции в формате ГГГГ-ММ-ДД -> ')
	parse_date(date)


	# wallet_name = input(' '*17+'Введите название кошелька -> ')
	# op_type = input(' '*22+'Введите тип операции -> ')
	# value = input(' '*26+'Введите значение -> ')
	# comment = input(' '*23+'Введите комментарий\n -> ')
	# category_name = input(' '*25+'Введите категорию -> ')

	# balance = get_last_balance(wallet_name)
	# if op_type == 'income':
	# 	balance += int(value)
	# elif op_type == 'spend':
	# 	balance -= int(value)

	# print('-'*80)
	# push_history_data([date, wallet_name, op_type, value, str(balance), comment, category_name])
	# print(f'Текущий баланс кошелька "{wallet_name}" = {balance}')

	
	"""
	TODO

	* Проверку и парсинг вводимой даты
	
	* если пользователь не указал год, то подставляется текущий год
	* если пользователь не указал месяц, то подставлется текущий месяц
	* если пользователь не указал дату, то вставляется текущая дата
	* если пользователь указал дату, которая позже послденей введенной 
	в БД, то появляется предупреждение

	* Исправить введение баланса: сделать ввод с торицательными числами

	* Ввод типа операции сделать автоматическим

	* Проверку всех вводимых значений с базой данных: название кошелька, 
	категории

	* Добавить свой класс ошибки

	* operation_type не долже участвовать во внесении данных. Пользователю 
	будет удобоней вносить расходы в виде отрицатеьлных значений. А мы в 
	зависимости от значения будет указывать тип операции.

	Тип операции я считаю важным параметром, поскольку мы учитываем перевод из 
	одного кошелька в другой
	
	* и другие доработки

	"""

	
if __name__ == '__main__':
	add_history_data_dialog()