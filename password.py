password = 'a123456'
i = 0
while i < 3:
	user = input('請輸入密碼: ')
	i = i + 1
	if password == user:
		print('你猜對惹')
		break
	else:
		if i < 3:
			print('你猜錯惹 你還剩下', 3 - i, '次機會')

			
if i == 3:
	print('你沒救惹88')