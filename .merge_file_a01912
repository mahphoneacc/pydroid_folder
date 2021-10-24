
import os

import pandas as pd

import hashlib


class Df_val_set:
	'Список значений'
	df_file_name =  'names.csv';
	VAL_COL_NAME = 'name';
	IND_COL_NAME = 'ind';
	
	def fix(self):
	    print('fix');
	    for  i, row in self.df.iterrows():
	    	row[self.VAL_COL_NAME] = row[self.VAL_COL_NAME].lower().strip();
	    
	def delete_by_index(self, ind):
	    if ind in self.df.index.values:
	    	self.df = self.df.drop(index=[ind]);
		
	def count(self):
	    return len(self.df.index);
     	
	def print(self):
		print(self.df);
		
	def print_df_name_file(self):
		print(self.DF_FILE_NAME);


class Df_fio(Df_val_set):
	'класс хранящий фио человека'
	DF_FILE_NAME =  'fio.csv';
	column_list = ['surname', 'name','secondname',  'md5'];
	
	def __init__(self, df_file_name = 'filename.csv', ind_col_name = 'ind'):
		self.df_file_name = df_file_name;
		print('--init Df_fio with "', df_file_name, '"');
		#self.df_file_name = 'names.csv';
		if os.path.isfile(df_file_name):
			self.df = pd.read_csv(df_file_name, index_col=ind_col_name);
			#print(self.df);
			print('df_name_file: ', df_file_name);
		else:
			#print('selfindcolname:', self.IND_COL_NAME);
			#print('columnlist: ', self.column_list);
			self.df = pd.DataFrame(columns = self.column_list);
	
	# получить индекс элемента name
	def get_index(self, surname = '', name = '', secondname = ''):
		name = name.lower().strip();
		ind_list = self.df[(self.df['surname'] == surname) & (self.df['secondname'] == secondname) & (self.df['name'] == name)].index.tolist();
		if ind_list ==[]:
			hashmd5 = hashlib.md5((surname + name + secondname).encode()).hexdigest();
			self.df = self.df.append({'surname': surname, 'name': name, 'secondname': secondname, 'md5': hashmd5}, ignore_index=True);
			ind_list = self.df[(self.df['surname'] == surname) & (self.df['secondname'] == secondname) & (self.df['name'] == name)].index.tolist();
		return ind_list[0];
	
	#поиск по неполным данным
	def get_rows_like(self, surname = '', name = '', secondname = ''):
		name = name.lower().strip();
		ind_list = self.df[(self.df['surname'] == surname) & (self.df['secondname'] == secondname) & (self.df['name'] == name)].index.tolist();
		if surname != '':
			ret_df = self.df[(self.df['surname'] == surname)].copy;
		
		
		if ind_list ==[]:
			hashmd5 = hashlib.md5((surname + name + secondname).encode()).hexdigest();
			self.df = self.df.append({'surname': surname, 'name': name, 'secondname': secondname, 'md5': hashmd5}, ignore_index=True);
			ind_list = self.df[(self.df['surname'] == surname) & (self.df['secondname'] == secondname) & (self.df['name'] == name)].index.tolist();
		return ind_list[0];
	
		# appended добавляет имя name и возвращает 1,  если name уже в списке,то возвращает 0
	def appended(self, surname = '', name = '', secondname = ''):
		name = name.lower().strip();
		if self.df[(self.df['surname'] == surname) & (self.df['secondname'] == secondname) & (self.df['name'] == name)].index.tolist() == []:
			hashmd5 = hashlib.md5((surname + name + secondname).encode()).hexdigest();
			self.df = self.df.append({'surname': surname, 'name': name, 'secondname': secondname, 'md5': hashmd5}, ignore_index=True);
			return 1;
		else:
			return 0;
	
	def append(self, surname = '', name = '', secondname = ''):
		print('append');
		self.appended(surname, name, secondname);
	
	def fix(self):
	    print('fix');
	    for  i, row in self.df.iterrows():
	    	row['surname'] = row['surname'].lower().strip();
	    	row['name'] = row['name'].lower().strip();
	    	row['secondname'] = row['secondname'].lower().strip();
	    	
	def delete(self, surname, name, secondname):
	    name = name.lower().strip();
	    surname = surname.lower().strip();
	    secondname = secondname.lower().strip();
	    print('deleting "', surname, '", "', name, '", "', secondname, '"');
	    list_ind=self.df[((self.df['surname'] == surname) & (self.df['secondname'] == secondname) & (self.df['name'] == name))].index.to_list();
	    print('deleting index list: ', list_ind);
	    self.df.drop(list_ind, inplace=True);
     
	def save(self):
		print('df_name_file: ', self.df_file_name);
		self.df.to_csv(self.df_file_name, columns=self.column_list, index_label=self.IND_COL_NAME);


# класс, который будет еще и подсчитывать количество элементов
class Df_val_cnt(Df_val_set):
	'класс со списком элементов и их количеством'
	val_col_name = 'name';
	CNT_COL_NAME = 'cnt';
	
	#инициализация. Добавление столбца cnt,если его нет.
	def __init__(self, df_file_name = 'filename.csv', col_name = 'name', ind_col_name = 'ind'):
		self.df_file_name = df_file_name;
		self.val_col_name = col_name;
		print('--init Df_val_cnt with "', df_file_name, '"');
		#self.df_file_name = 'names.csv';
		if os.path.isfile(df_file_name):
			self.df = pd.read_csv(df_file_name, index_col = ind_col_name);
			#print(self.df);
			print('df_name_file: ', df_file_name);
			# проверю существование колонки cnt. Если нету - создать.
			if not 'cnt' in self.df.columns:
				self.df['cnt'] = None;
				self.df.loc[:, 'cnt'] = 0;
		else:
			self.df = pd.DataFrame(columns = [self.val_col_name, self.CNT_COL_NAME]);
	
	def in_list(self, name):
		name = name.lower().strip();
		list_ind = self.df[self.df[self.val_col_name] == name].index.tolist();
		if list_ind ==[]:
			return 0
		else:
			return len(list_ind);
	
	def inc_cnt(self, name):
		self.df.loc[(self.df[self.val_col_name] == name), self.CNT_COL_NAME] = self.df[self.df[self.val_col_name] == name][self.CNT_COL_NAME].values[0] + 1;
		
	def ins_element(self, name):
		self.df = self.df.append({self.val_col_name: name, self.CNT_COL_NAME: 1}, ignore_index=True);

	# получить индекс элемента name, если нету,то вставить и получить.
	def get_index(self, name):
		name = name.lower().strip();
		if self.in_list(name):
			self.inc_cnt(name);
		else:
			self.ins_element(name);
		return self.df[self.df[self.val_col_name] == name].index.tolist()[0];
		
	#проверить, что элемент уже есть, если нет, то создать
	def appended(self, name):
		name = name.lower().strip();
		if self.in_list(name):
			self.inc_cnt(name);
			return 0;
		else:
			self.ins_element(name);
			return 1;
	
	def append(self, name):
		print('Df_val_cnt append', name);
		self.appended(name);
	
	def save(self):
		print('df_name_file: ', self.df_file_name);
		self.df.to_csv(self.df_file_name, columns=[self.val_col_name, self.CNT_COL_NAME], index_label=self.IND_COL_NAME);
	
	# найти датафрейм походящих
	def find_rows(self, name):
		#print('find_rows', name);
		return self.df[self.df[self.val_col_name] == name].copy();


class Df_link():
	'класс связи'
	
	#инициализация.
	def __init__(self, df_file_name = 'filename.csv', l_code = 'l_code', r_code = 'r_code', l_hash = 'l_hash', r_hash = 'r_hash', ind_col_name = 'ind', lnk_hash = 'lnk_hash'):
		self.df_file_name = df_file_name;
		self.l_code = l_code;
		self.r_code = r_code;
		self.l_hash = l_hash;
		self.r_hash = r_hash;
		self.ind_col_name = ind_col_name;
		self.lnk_hash = lnk_hash;
		
		print('--init Df_link with "', df_file_name, '"');
		#self.df_file_name = 'names.csv';
		if os.path.isfile(df_file_name):
			self.df = pd.read_csv(df_file_name, index_col = ind_col_name);
			#print(self.df);
			# проверю существование колонок. Если нету - создам
			for el in [lnk_hash, l_code, r_code, l_hash, r_hash]:
				if not el in self.df.columns:
					self.df[el] = None;
					self.df.loc[:, el] = 0;
		else:
			self.df = pd.DataFrame(columns = [lnk_hash, l_code, r_code, l_hash, r_hash]);
			
	def in_list_codes(self, l_code, r_name):
		l_code = l_code.lower().strip();
		r_code = r_cide.lower().strip();
		list_ind = self.df[(self.df[self.l_code] == l_code)&(self.df[self.r_code] == r_code)].index.tolist();
		if list_ind ==[]:
			return 0
		else:
			return len(list_ind);
		
	def ins_element(self, l_code, r_code):
		l_hashmd5 = hashlib.md5(l_code.encode()).hexdigest();
		r_hashmd5 = hashlib.md5(r_code.encode()).hexdigest();
		hashmd5 = hashlib.md5((l_code + r_code).encode()).hexdigest();
		self.df = self.df.append({self.l_code: l_code, self.r_code: r_code, self.l_hash: l_hashmd5, self.r_hash: r_hashmd5, self.lnk_hash: hashmd5}, ignore_index=True);
		
	def save(self):
		print('df_name_file: ', self.df_file_name);
		self.df.to_csv(self.df_file_name, columns=[self.l_code, self.r_code, self.l_hash, self.r_hash, self.lnk_hash], index_label=self.ind_col_name);
		
		
		
	#def get_index():
	#def append():
	#def appended():
			
			
			
# проверка Df_val_cnt
#df_email = Df_val_cnt('email.csv');
#df_email.append('brin@gmail.com');
#df_email.append('bezos@gmail.com');
#df_email.append('thanks@gmail.com');
#df_email.append('tliri@gmail.com');
#df_email.appended('bezos@gmail.com');
#df_email.append('bezos@gmail.com');
#df_email.print();
#df_email.delete('bezos@gmail.com');
#df_email.print();


#dfnam = Df_name();
#dfnam=Df_val_cnt('names.csv');
#dfnam.print();
#dfnam.append('Инокентий');
#dfnam.append('петя');
#dfnam.fix();
#dfnam.print();
#dfnam.delete('инакентий');
#dfnam.delete_by_index(2);
#dfnam.print();
#dfnam.print_df_name_file();
#dfnam.print_const();
#dfnam.save();



#dfsur = Df_surname();
#dfsur.print();
#dfsur.get_index('дуков');
#dfsur.append('гуков');
#dfsur.fix();
#dfsur.print();
#dfsur.save();


# проверка Df_fio
#dffio = Df_fio();
#print(dffio.get_index('Famil', '    imya   ', 'otch'));
#dffio.append('Dgeronimov', 'petr', 'albertovich');
#dffio.print();
#print(dffio.get_index('Dgeronimov', 'petr', 'albertovich'));
#dffio.fix();
#dffio.delete('   Famil', '  imya  ', 'otch');
#dffio.print();


#print('--------');





