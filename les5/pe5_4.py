bestandje = open("/Users/mikefraanje/Desktop/HU/Programming/hardlopers.txt", "w")


hardloper = input('wat is de naam van de hardloper')
tijd = "Tue, 26. sep., 2017 14:32"

bestandje.write(tijd + "" + hardloper + "\n")
bestandje.close()

