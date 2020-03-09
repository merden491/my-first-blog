print("Merhaba, Django girls!")

if 5 > 2:
	print("5 buyuktur 2 den")
else:
	print("5 kucuktur 2 den")


name = "Zeynep"
if name == "Ayse":
	print("Selam Ayse")
elif name == "Zeynep":
	print("Selam Zeynep")
else:
	print("Selam yabanci")		
	

volume = 57
if volume < 20:
	print("Cok sessiz")
elif 20 <= volume < 40:
	print("Guzel bir fon muzigi")
elif 40 <= volume < 60:
	print("Harika her notayi duyabiliyorum")
elif 60 <= volume < 80:
	print("Parti baslasin")
elif 80 <= volume <100:
	print("Biraz gurultulu")
else:
	print("Kulaklarim agriyor!")