#!/usr/bin/python3

#----------------------------------
#		if
#----------------------------------
names = ['atom','lz','tom','ww']
#for i in names:
#	if i == 'atom':				#if语句检查是否相等
#		print (i.upper())
#	else:
#		print (i.title())
#----------------------------------
#for i in names:
#	if i != 'atom':
#		print (i.upper())
#----------------------------------
#num = 20
#if (num > 10) and (num < 30):	#用and,or检查多个条件
#	print('True')
#----------------------------------
#name = 'atom'					#用in来查看变量是否在列表中
#if (name in names):
#	print (True)
#----------------------------------
#name = 'atom1'					#用not in检查是否不包含在列表中
#if (name not in names):
#	print ('True')
#----------------------------------

#----------------------------------
	#		字典		＃
#----------------------------------
#用{}来创建字典，字典是一系列‘键－值’
#----------------------------------
alien_0 = {'color':'green','point':5}
#print (alien_0['color'])		
#print (alien_0['point'])
#print (alien_0)
#----------------------------------
#字典是动态结构，可以随时添加键－值对
#alien_0['x_point'] = 20
#alien_0['y_point'] = 30
#alien_0['point'] = 6
#print (alien_0)
#----------------------------------
#创建多行的键值
#languages = {
#        'atom':'c/c++',
#        'lz':'??',
#        'shixi':'python'
#        }
#for name in languages:
#    print('Atom' + 
#    'love' +
#    languages[name].title()
#    )
#----------------------------------
#for中用items()访问字典的键和值
#for key,value in alien_0.items():
#    print("\nkey:"+ key)
#    print("value:"+str(value))
#----------------------------------
#for中用keys来遍历所以键
#for name in alien_0.keys():
#    print(name)
#    print(alien_0[name])
#----------------------------------
#for中用values来遍历所以值
#for value in alien_0.values():
#    print(str(value))
#----------------------------------

