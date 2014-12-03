#-*- coding: utf-8-*-
import sys
import time
import email
import smtplib

print "*****   PAISES Y CAPITALES   *****"
encabezado={"PAISES  ":"CAPITALES ",}
paises={}
lista_capitales=[]
#**************** funcion ingreso pais/capital ******************************************
#****************************************************************************************
#***************************** CLACES ***************************************************
class pais_capital(object):
	def __init__(self):
		pass
#***************************************************************************************
#***************************************************************************************
	def paises_capitales(self):
		eleccion=True
		while eleccion==True:
			opcion=raw_input("Desea ingresar el nombre del pais/capital YES/NO?: ")
			try:
				if opcion.isalpha()==True:
					if opcion.lower()=="yes":
						eleccion_pais=True
						while eleccion_pais==True:
							pais=raw_input("ingrese el pais   : ")
							try:
								texto=pais
								for x in texto:
									if x.isalpha()==True or x==" ":
										eleccion_pais=False
									else:
										print "no se aceptan datos numericos"
							except:
								eleccion_pais=True
						eleccion_capital=True
						while eleccion_capital==True:
							capital=raw_input("Ingrese la capital: ")
							try:
								texto=capital
								for x in texto:
									if x.isalpha()==True or x==" ":
										eleccion_capital=False
									else:
										print "No se aceptan datos numericos"
							except:
								eleccion_capital=True
							paises[pais]=capital
						
																 								
					elif opcion.lower()=="no":
						break
					else:
						print "dato no reconocido"
				else:
					print "no se aceptan datos numericos"
			except:
				eleccion=True
		return 0

#************************* fin ingreso pais/capital ************************************
#***************************************************************************************

#*************************** MENU ******************************************************
#****************************************************************************************************************************

op_menu=True
while op_menu==True:
	print "         *** MENU ***"
	print "1) Agregar paises/capital  : "
	print "2) PAISES                  :"
	print "3) CAPITALES               :"
	print "4) TODO                    :"
	print "5) TODO ORDENADO CAPITAL   :"
	print "6) TODO MAIL               :"
	opcion_menu=raw_input("Que opcion desea realizar? : ")
	try:
		if opcion_menu.isalpha()==False:
#***********************************************************************************			
#******************** menu ingreso paises/capital **********************************			
			if opcion_menu.lower()=="1":
				ejemplo=pais_capital()
				ejemplo.paises_capitales()
				validar=True
				while validar==True:
					volver=raw_input("Desea volver al menu YES/NO?: ")
					print ""
					try:
						if volver.isalpha()==True:
							if volver.lower()=="yes":
								validar=False
							elif volver.lower()=="no":
								op_menu=False
								break
						else:
							print "dato no valido"
					except:
						print "no se aceptan datos numericos"					
#**********************************************************************************
#******************** menu ver lista paises ***************************************
			elif opcion_menu.lower()=="2":
				print "*** LISTA DE PAISES ***"
				#***** aqui tenes que poner el codigo para la lsta de paises
				
				for item in paises:
					print (item)


				#***********************************************************
				validar=True
				while validar==True:
					print ""
					volver=raw_input("Desea volver al menu YES/NO?: ")
					print ""
					try:
						if volver.isalpha()==True:
							if volver.lower()=="yes":
								validar=False
							elif volver.lower()=="no":
								op_menu=False
								break
						else:
							print "dato no valido"
					except:
						print "no se aceptan datos numericos"			
#**********************************************************************************
#******************** menu ver lista capitales ************************************
			elif opcion_menu.lower()=="3":
				print "*** LISTA DE CAPITALES ***"
				#***** aqui tenes que poner el codigo para la lsta de capitales
				for x in paises:
					print paises[x]

				#***********************************************************
				validar=True
				while validar==True:
					print""
					volver=raw_input("Desea volver al menu YES/NO?: ")
					print ""
					try:
						if volver.isalpha()==True:
							if volver.lower()=="yes":
								validar=False
							elif volver.lower()=="no":
								op_menu=False
								break
						else:
							print "dato no valido"
					except:
						print "no se aceptan datos numericos"							
#**********************************************************************************
#******************** lista paises/capital ****************************************
			elif opcion_menu.lower()=="4":
				print "*** LISTA PAISES/CAPITALES ***"
				print ""
				for clave in encabezado:
					print clave,":",encabezado[clave] 
				for clave in paises:
					print clave,":",paises[clave] 
				validar=True
				while validar==True:
					print ""
					volver=raw_input("Desea volver al menu YES/NO?: ")
					print ""
					try:
						if volver.isalpha()==True:
							if volver.lower()=="yes":
								validar=False
							elif volver.lower()=="no":
								op_menu=False
								break
						else:
							print "dato no valido"
					except:
						print "no se aceptan datos numericos"		
#***************************** TODO ORDENADO **************************************
#**********************************************************************************
			elif opcion_menu.lower()=="5":
				print "*** LISTA PAISES/CAPITALES ORDENADO ***"
				print "PAISES"
				for item in paises:
					print (item)
				print ""
#************************** ORDENAR CAPITALES *************************************
				print "CAPITALES ORDENADO"

				for x in paises:
					lista_capitales.append(x)
				print lista_capitales.sort()
				print " ".join(lista_capitales)
#********************************** validacion volver menu **************************
				validar=True
				while validar==True:
					print ""
					volver=raw_input("Desea volver al menu YES/NO?: ")
					print ""
					try:
						if volver.isalpha()==True:
							if volver.lower()=="yes":
								validar=False
							elif volver.lower()=="no":
								op_menu=False
								break
						else:
							print "dato no valido"
					except:
						print "no se aceptan datos numericos"


#**********************************************************************************						
#********************************* CORREO *****************************************
			elif opcion_menu.lower()=="6":
				print "*** ENVIAR CORREO ***"
				mensaje=""
				for x in paises:
					mensaje=mensaje+("%s \n")%(x)
				mensajecapitales=""
				for x in paises:
					mensajecapitales=mensajecapitales+("%s \n")%(paises[x])
				
				msg = email.message_from_string("Lista de paises:\n   %s \nlista de capitales:\n   %s"%(mensaje,mensajecapitales))

				
				direccion_correo=raw_input("Ingrese la direccion de correo electronico: ")
				msg['From'] = direccion_correo
				msg['To'] = "jalejandrotamayo@hotmail.com"
				msg['Subject'] = "Cognits"
				s = smtplib.SMTP("smtp.live.com",587)
				s.ehlo()
				s.starttls() 
				s.ehlo()
				s.login('jalejandrotamayo@hotmail.com', 'peluso')

				s.sendmail(direccion_correo, direccion_correo, msg.as_string())
				s.quit()
				print "Su mensaje ha sido enviado a la direccion %s"%(direccion_correo)
#****************************** FIN CORREO ***************************************
#**********************************************************************************

			else:
				print "no a ingreado una opcion valida"
		
		else:
			print "no se aceptan datos alphabeticos"
	except:
		op_menu=True
print "ADIOS"
time.sleep(4)
