#Расписание
#1 пара - 1:30
#2 пара - 3:10
#3 пара - 4:50
#перерыв - 6:20
#4 пара - 6:50


#Минуты писать не 05 а 5 -> 12:05(x) 12:5(v)
Monday_blue = {
	'1:30': ['https://meet.google.com/oua-wmat-duq'],
	'3:10': ['https://meet.google.com/oua-wmat-duq'],
	#3 пара вроде как в zoom
}
Monday_red = {
	'3:10': ['https://meet.google.com/oua-wmat-duq'],
	#3 пара вроде как в zoom
}
Wednesday = {
	#1 в зуме
	'3:10': ['https://meet.google.com/iwg-hndb-qwg'],
	'4:50': ['https://meet.google.com/zth-nanc-zrb'],
	'6:50': ['https://meet.google.com/iwg-hndb-qwg'],#Ссылка вроде как и на 3 паре!!!!!!!!!!!!!!!
}
Thursday_blue = {#n
	
}
Thursday_red = {
	'3:10': ['https://meet.google.com/vde-utdm-fks'],
	'4:50': ['https://meet.google.com/vde-utdm-fks'],
	'6:50': ['https://meet.google.com/vde-utdm-fks'],
}
Friday = {#n
	#2 пара подгаева
	'4:50': ['https://meet.google.com/iwg-hndb-qwg'],
	'6:20': ['https://meet.google.com/iwg-hndb-qwg'], #перерыв
	'6:50': ['https://meet.google.com/iwg-hndb-qwg']
}


week_day = {
	'11': Monday_blue,
	'10': Monday_red,
	'31': Wednesday,  
	'30': Wednesday,
	'41': Thursday_blue,
	'40': Thursday_red,
	'51': Friday,
	'50': Friday,
}