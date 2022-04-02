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
	'4:50': ['https://meet.google.com/xup-kije-drj'],
}
Monday_red = {
	'3:10': ['https://meet.google.com/oua-wmat-duq'],
	'4:50': ['https://meet.google.com/xup-kije-drj'],
}
Wednesday = {
	#1 в зуме
	'3:10': ['https://meet.google.com/iwg-hndb-qwg'],
	'4:50': ['https://meet.google.com/zth-nanc-zrb'],
	'6:50': ['https://meet.google.com/zth-nanc-zrb'],
}
Thursday_blue = {
	'3:10': ['https://meet.google.com/jmj-njvg-ugs'],
	'4:50': ['https://meet.google.com/vde-utdm-fks'],
	'6:20': ['https://meet.google.com/jmj-njvg-ugs'], #перерыв
	'6:50': ['https://meet.google.com/jmj-njvg-ugs'],
}
Thursday_red = {
	'3:10': ['https://meet.google.com/vde-utdm-fks'],
	'4:50': ['https://meet.google.com/vde-utdm-fks'],
	'6:20': ['https://meet.google.com/vde-utdm-fks'], #перерыв
	'6:50': ['https://meet.google.com/vde-utdm-fks'],
}
Friday = {#n
	'3:10': ['https://meet.google.com/vde-utdm-fks'],
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