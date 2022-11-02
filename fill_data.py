"""
Чтобы не нагружать логикой остальный фалы, все запросы на наполнение базы 
тестовыми данными вынес сюда
"""

import sqlite3

def insert_data_into_wallet() -> None:
	req = """
	INSERT INTO wallet
	VALUES
		('ВТБ', 'None'),
		('Сбер', 'None'),
		('Наличные', 'None')
	"""
	cur.execute(req)
	conn.commit()


def insert_data_into_category() -> None:
	req = """
	INSERT INTO category
	VALUES
		('Без категории', 'None')
	"""
	cur.execute(req)
	conn.commit()


def inser_data_into_operation_type() -> None:
	req = """
	INSERT INTO operation_type
	VALUES
		('income'),
		('spend'),
		('transfer')
	"""
	cur.execute(req)
	conn.commit()


def insert_data_into_history() -> None:
	req0 = """PRAGMA foreign_keys = ON"""
	cur.execute(req0)

	req = """
	INSERT INTO history
	VALUES
		('2022-10-22', 'ВТБ', 'income','100', '200', 'Зарплата', 'Без категории'),
		('2022-10-22', 'ВТБ', 'spend','50', '150', 'Автобус', 'Без категории'),
		('2022-10-22', 'ВТБ', 'income','40', '190', 'Зарплата', 'Без категории'),
		('2022-10-22', 'Сбер', 'income','500', '600', 'Зарплата', 'Без категории'),
		('2022-10-22', 'ВТБ', 'spend', '90', '100', 'Обед', 'Без категории')
	"""
	cur.execute(req)
	conn.commit()


if __name__ == '__main__':
	conn = sqlite3.connect('wallet.db')
	cur = conn.cursor()

	# Уже была ситуация, что случилась ошибка при выполнении SQL запроса, но
	# соединение с базой не закрылось. Поэтому воспользуемся try
	try:
		insert_data_into_wallet()
		insert_data_into_category()
		inser_data_into_operation_type()
		insert_data_into_history()
	except:
		print('ОШИБКА: что-то пошло не так, но соединение было закрыто')

	conn.close()