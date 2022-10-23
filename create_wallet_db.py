"""
Создает базу данных для учета трат и расходов

Здесь попробуем создать несколько связанных таблиц с внешними 
ключами

22.10.2022
"""

import sqlite3
import pandas as pd


def create_table_wallet() -> None:
	"""Таблица, хранящая все имеющиеся кошельки"""
	req = """
	CREATE TABLE IF NOT EXISTS wallet(
		name TEXT PRIMARY KEY,
		comment TEXT
	)
	"""
	cur.execute(req)
	conn.commit()


def create_table_category() -> None:
	"""Содержит категории доходов и расходов"""
	req = """
	CREATE TABLE IF NOT EXISTS category(
		name TEXT PRIMARY KEY,
		comment TEXT
	)
	"""
	cur.execute(req)
	conn.commit()


def create_table_operation_type() -> None:
	"""Содержит тип операции: доход, расход, перевод"""
	req = """
	CREATE TABLE IF NOT EXISTS operation_type(
		type TEXT PRIMARY KEY
	)
	"""
	cur.execute(req)
	conn.commit()


def create_table_history() -> None:
	"""Таблица с тратами и доходами"""
	req = """
	CREATE TABLE IF NOT EXISTS history(
		data DATE,
		wallet_name TEXT,
		operation_type TEXT,
		value INT,
		balance INT,
		сomment TEXT,
		category_name TEXT,
		
		FOREIGN KEY (wallet_name) REFERENCES wallet (name)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
		FOREIGN KEY (category_name) REFERENCES category (name)
		ON DELETE CASCADE
		ON UPDATE CASCADE
		FOREIGN KEY (operation_type) REFERENCES operation_type (type)
		ON DELETE CASCADE
		ON UPDATE CASCADE
 	)
	"""
	cur.execute(req)
	conn.commit()


def view_data() -> None:
	"""Вывод содержимого таблиц"""

	# Снмаем ограничения с количества отображаемых столбцов
	pd.set_option('max_columns', None) 

	data = pd.read_sql_query("SELECT * FROM wallet", conn)
	print('\n'+'='*6 + ' [wallet] ' + '='*56)
	print(data)
	data = pd.read_sql_query("SELECT * FROM category", conn)
	print('\n'+'='*6 + ' [category] ' + '='*54)
	print(data)
	data = pd.read_sql_query("SELECT * FROM operation_type", conn)
	print('\n'+'='*6 + ' [operation_type] ' + '='*52)
	print(data)
	data = pd.read_sql_query("SELECT * FROM history", conn)
	print('\n'+'='*6 + ' [history] ' + '='*55)
	print(data)


def add_column() -> None:
	"""Добавим колонки в таблицы"""
	req = """
	ALTER TABLE category
	ADD COLUMN comment TEXT
	"""
	cur.execute(req)
	conn.commit()


def update_oper_type() -> None:
	# В SQlite по умолчанию идет отключение поддержики внешнего ключа.
	# Каждый раз, когда происходит открыте БД, то параметр ниже будет иметь 
	# значение OFF. Поэтому будем его перезаписывать, обращаясь к параметру 
	# PRAGMA (прим. 2)
	req0 = """PRAGMA foreign_keys = ON"""
	cur.execute(req0)

	req1 = """
	UPDATE operation_type
	SET type = 'spend'
	WHERE type = 'spend111'
	"""
	cur.execute(req1)
	conn.commit()

if __name__ == '__main__':
	conn = sqlite3.connect('wallet.db')
	cur = conn.cursor()
	
	create_table_wallet()
	create_table_category()
	create_table_history()
	create_table_operation_type()

	# update_oper_type()

	view_data()


	conn.close()


"""
Примечание 1. 
База может ругаться, есть столбец называется 
transaction, так как это зарезервированное слово. Могут быть и другие

Примечание 2.
Ссылка SteckOverFlow: 
https://stackoverflow.com/questions/13641250/sqlite-delete-cascade-not-working
"""
