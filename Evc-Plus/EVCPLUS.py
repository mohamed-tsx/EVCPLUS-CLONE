import datetime #waxaan soo import gareyay library-gan oo naga caawinaya date and time wakhtiga loo baahd
haraaga=54  #qeybtan waxaa u isticmaalay keydinta haraaga waxaan ku haraaga kadibna marku qofku lacagta dirayo looga jaro
lambarkeyga=610000000      #qeybtan waxaan ku keydiyay lambarkeyga waxaana isticmaaleyna markii aan lacag direyno si aan uga feejignano in aan lacag u dirno isla lambarkeenaa
password=int(input("Fadlan geli pin cusub\n")) #qeybtan waxay keydisaa pin-ka cusub
pin=int(input("Fadlan hubi pin-kaga\n")) #qebtan waxey hubisaa pin-ka cusub ee lagu keydiyay variable-ka kore inuu sax yahay iyo i kale
while pin!=password:
	pin=int(input("Pinka aad gelisay waa khalad fadlan hubi mar kale\n")) #haddi aa khalado pin-ka cusub qeybtan waxey soo celineysaa Error ah lagugu dhahaayo pin-ka aad gelisay waa khalad
if pin==password:
	passw=int(input("Fadlan geli pin-kaga\n"))
if passw==password:
	dooro=int(input("1.Itus haraagaga\n2.Kaarka Hadalka\n3.Bixi Biil\n4.U wareeji EvcPlus\n5.Warbixin Kooban\n6.Salaam Bank\n7.Maareynta\n8.Taaj\n9.Pay Pill\n"))
	if dooro==1:
		print(f"Haraagagu Waa ${haraaga}")
#qeybta kaarka halkan ayay ka bilaabaneysaa
	elif dooro==2:
		kaarka=int(input("1.Ku Shub Airtime\n2.Ugu shubo Airtime\n3.MIFI Packages\n4.Ku shubo Internet\n5.Ugu shub qof kale(MMT)\n"))
		if kaarka==1:
			ku=int(input("Fadlan geli lacagta aa ku shubaneysid\n"))
			dir=int(input(f"Ma hubtaa inaa ugu shubatid ${ku} Undefined\n1.Haa\n2.Maya\n"))
			if dir==1:
				haray=int(haraaga)-int(ku)
				if int(haraaga)>=int(ku):
					print(f"Waxaad ${ku} u dirtay undefined haraagagu waa ${haray}")
				else:
					print("haraaga xisaabtada kuguma filna")
			elif dir==2:
				print("Howshaan laguma guuleysan Macsalaamo")
			else:
				print("Macsalaamo")
		elif kaarka==2:
			udir=int(input("Fadlan geli numberka aad lacagta ugu shubeysid\n"))
			
			lacagta=int(input("Fadlan geli lacagta aad ugu shubeysid\n"))
			haray=int(haraaga)-int(lacagta)
			udiro=int(input(f"Ma hubtaa in aad {udir} Ugu shubtid ${lacagta}\n1.Haa\n2.Maya\n"))
			if udiro==1:
				if int(haraaga)>=int(lacagta):
					print(f"Waxaad ${lacagta} Ugu Shubtay {udir} Haraagagu waa ${haray}")
				else:
					print("Haraaga Xisaabtada kugama filna")
					
			elif udiro==2:
				print("Howshaan Laguma Guuleysan Macsalaamo")
			else:
				print("Macsalaamo")
		elif kaarka==3:
			mif=int(input("1.Ku Shubo Data-da MIFI\n"))
			if mif==1:
				mifi=int(input("--Internet Bundle Packages--\n1.Maalinle(Daily)\n2.Isbuucle(Daily)\n3.Bille(Monthly)\n"))
				if mifi==1:
					maalin=int(input("1: $1=2GB\n2: $2=5GB\n"))
					if maalin==1:
						mifi_num=int(input("Fadlan Geli Mifi User\n"))
						dir=int(input(f"Ma hubtaa inaad ${maalin} ugu shubtid {mifi_num}\n1.Haa\n2.Maya\n"))
						if dir==1:
							haray=int(haraaga)-int(maalin)
							print(f"Waxaad ${maalin} ugu shubtay {mifi_num} haraagagu waa ${haray}")
						elif dir==2:
								print("Howshaan laguma guuleysan mahadsanid")
						else:
					
									print("Macslaamo")
					if maalin==2:
						mifi_num=int(input("Fadlan Geli Mifi User\n"))
						dir=int(input(f"Ma hubtaa inaad ${maalin} ugu shubtid {mifi_num}\n1.Haa\n2.Maya\n"))
						if dir==1:
							haray=int(haraaga)-int(maalin)
							print(f"Waxaad ${maalin} ugu shubtay {mifi_num} haraagagu waa ${haray}")
						elif dir==2:
								print("Howshaan laguma guuleysan mahadsanid")
						else:
									print("Macslaamo")
				if mifi==2:
					isbuuc=int(input("1: $5=10GB\n2: $10=25GB\n"))
					if isbuuc==1:
						isbuuc=5
						isbuuc_qiimo="$5 oo u dhiganta 10GB"
						mifi_num=int(input("Fadlan Geli Mifi User\n"))
						dir=int(input(f"Ma hubtaa inaad {isbuuc_qiimo} ugu shubtid {mifi_num}\n1.Haa\n2.Maya\n"))
						if dir==1:
							haray=int(haraaga)-int(isbuuc)
							print(f"Waxaad {isbuuc_qiimo} ugu shubtay {mifi_num} haraagagu waa ${haray}")
						elif dir==2:
								print("Howshaan laguma guuleysan mahadsanid")
						else:
									print("Macslaamo")
					if isbuuc==2:
						isbuuc=10
						isbuuc_qiimo="$10 oo u dhiganta 25GB"
						mifi_num=int(input("Fadlan Geli Mifi User\n"))
						dir=int(input(f"Ma hubtaa inaad {isbuuc_qiimo} ugu shubtid {mifi_num}\n1.Haa\n2.Maya\n"))
						if dir==1:
							haray=int(haraaga)-int(isbuuc)
							print(f"Waxaad {isbuuc_qiimo} ugu shubtay {mifi_num} haraagagu waa ${haray}")
						elif dir==2:
								print("Howshaan laguma guuleysan mahadsanid")
						else:
									print("Macslaamo")
				if mifi==3:
					bil=int(input("1: $20=40GB\n2: $40=85GB\n3: $60=150GB\n"))
					if bil==1:
						bil=20
						bil_qiimo="$20 oo u dhiganta 40GB"
						mifi_num=int(input("Fadlan Geli Mifi User\n"))
						dir=int(input(f"Ma hubtaa inaad ${bil_qiimo} ugu shubtid {mifi_num}\n1.Haa\n2.Maya\n"))
						if dir==1:
							haray=int(haraaga)-int(bil)
							print(f"Waxaad ${bil_qiimo} ugu shubtay {mifi_num} haraagagu waa ${haray}")
						elif dir==2:
								print("Howshaan laguma guuleysan mahadsanid")
						else:
									print("Macslaamo")
					if bil==2:
						bil=40
						bil_qiimo="$40 oo u dhiganta 85GB"
						mifi_num=int(input("Fadlan Geli Mifi User\n"))
						dir=int(input(f"Ma hubtaa inaad {bil_qiimo} ugu shubtid {mifi_num}\n1.Haa\n2.Maya\n"))
						if dir==1:
							haray=int(haraaga)-int(bil)
							print(f"Waxaad ${bil_qiimo} ugu shubtay {mifi_num} haraagagu waa ${haray}")
						elif dir==2:
								print("Howshaan laguma guuleysan mahadsanid")
						else:
									print("Macslaamo")
					if bil==3:
						bil=60
						bil_qiimo="$60 oo u dhiganta 150GB"
						mifi_num=int(input("Fadlan Geli Mifi User\n"))
						dir=int(input(f"Ma hubtaa inaad {bil_qiimo} ugu shubtid {mifi_num}\n1.Haa\n2.Maya\n"))
						if dir==1:
								haray=int(haraaga)-int(bil)
								print(f"Waxaad {bil_qiimo} ugu shubtay {mifi_num} haraagagu waa ${haray}")
						else:
									print("Haraaga xisaabtada kuguma filna")
					elif dir==2:
						print("Howshaan laguma guuleysan mahadsanid")
					else:
						print("Macslaamo")
		elif kaarka==4:
			inte=int(input("Fadlan dooro habka aad ugu shubaneysid\n1.Maalinle(Daily)\n2.Isbuucle(Weekly)\n3.Bille(Monthly)\n4.Time Passed Package\n5.DATA\n" ))
			if inte==1:
				maalin=int(input("Fadlan geli lacagta aad ku shubaneysid\n"))
				
				dir=int(input(f"Ma hubtaa ina ku shubatid ${maalin}\n1.Haa\n2.Maya"))
				if dir==1:
					if int(haraaga)>=int(maalin):
						haray=int(haraaga)-int(maalin)
						print(f"waxaad ${maalin} ugu shubtay undefined haraagagu waa ${haray}")
					else:
						print("Haraaga xisaabtadu kuguma filna")
				elif dir==2:
					print("Howshaan laguma guuleysan Macsalaamo")
					
				else:
					print("Macsalaamo")
			elif inte==2:
				isbuuc=int(input("Fadlan geli lacagta aad ku shubaneysid\n"))
				dir=int(input(f"Ma hubtaa ina ku shubatid ${isbuuc}\n1.Haa\n2.Maya"))
				if dir==1:
					if int(haraaga)>=int(isbuuc):
						haray=int(haraaga)-int(isbuuc)
						print(f"waxaad ${haray} ugu shubtay undefined")
					else:
						print("Haraaga xisaabtadu kuguma filna")
				elif dir==2:
					print("Howshaan laguma guuleysan Macsalaamo")
					
				else:
					print("Macsalaamo")
			elif inte==3:
				bil=int(input("Fadlan geli lacagta aad ku shubaneysid\n"))
				dir=int(input(f"Ma hubtaa ina ku shubatid ${bil}\n1.Haa\n2.Maya\n"))
				if dir==1:
					if int(haraaga)>=int(bil):
						haray=int(haraaga)-int(bil)
						print(f"waxaad ${bil} ugu shubtay undefined Haraagagu waa ${haray}")
					else:
						print("Haraaga xisaabtadu kuguma filna")
				elif dir==2:
					print("Howshaan laguma guuleysan Macsalaamo")
					
				else:
					print("Macsalaamo")
			elif inte==4:
				tim=int(input("Fadlan geli lacagta aad ku shubaneysid\n"))
				dir=int(input(f"Ma hubtaa ina ku shubatid ${tim}\n1.Haa\n2.Maya\n"))
				if dir==1:
					if int(haraaga)>=int(tim):
						haray=int(haraaga)-int(tim)
						print(f"waxaad ${tim} ugu shubtay undefined haraagagu waa ${haray}")
					else:
						print("Haraaga xisaabtadu kuguma filna")
				elif dir==2:
					print("Howshaan laguma guuleysan Macsalaamo")
					
				else:
					print("Macsalaamo")
			if inte==5:
				data=int(input("Fadlan geli lacagta aad ku shubaneysid\n"))
				dir=int(input(f"Ma hubtaa ina ku shubatid ${data}\n1.Haa\n2.Maya\n"))
				if dir==1:
					if int(haraaga)>=int(data):
						haray=int(haraaga)-int(data)
						print(f"waxaad ${data} ugu shubtay undefined haraagagu waa ${haray}")
					else:
						print("haraaga xisaabtadu kuguma filna")
				elif dir==2:
					print("Howshaan laguma guuleysan Macsalaamo")
					
				else:
					print("Macsalaamo")
			else:
				print("Macsalaamo")
		elif kaarka==5:
			mmt=int(input("Fadlan geli mobile-ka\n"))
			mmtl=int(input("Fadlan Geli Lacagta\n"))
			dir=int(input(f"Ma hubtaa inad {mmt} ugu shubtid ${mmtl}\n1.Haa\n2.Maya\n"))
			if dir==1:
				if int(haraaga)>=int(mmtl):
					haray=int(haraaga)-int(mmtl)
					print(f"Waxaad {mmtl} ugu shubtay {mmt} haraagagu waa ${haray}")
				else:
					print("Haraaga xisaabtadu kuguma filna")
#qeybta kaarka halkan ayay ku dhamaaneysaa

#inta waxaa ka bilaanaa qeybta bixinta biilka
	elif dooro==3:
		biil=int(input("1.Post Paid\n2.Ku iibso\n"))
		if biil==1:
			post=int(input("1.Ogow Biilka\n2.Bixi Biilka\n3.Ku Bixi Biil"))
			if post==1:
				#qeybtan error baa ka jira i.a waan ka shaqeysiin doonaa
				print("Error baa jira dib ayaan ka xalin i.a")
			elif post==2:
				bixi=int(input("Fadlan geli lacagta biilka aad bixineyso\n"))
				bixi_l=int(input(f"Ma hubtaa inaad bexiso ${bixi} biil\n1.Haa\n2.Haa\n"))
				if bixi_l==1:
					if int(haraaga)>=int(bixi):
						haray=int(haraaga)-int(bixi)
						print(f"Waxaad bixisay ${bixi} haraagagu waa ${haray}")
					else:
						print("haraaga xisaabtadu kuguma filna")
				elif bixi_l==2:
					print("Macsalaamo!")
				else:
					print("Macsalaamo")
			elif post==3:
				ku_bixi=int(input("Fadlan geli numberka aad lacagta u direysid\n"))
				lacag=int(input("Fadlan geli lacagta aad u direysid\n"))
				hubin=int(input("Ma hubtaa inaad ${lacag} u dirtid {ku_bixi}\n1.Haa\n2.Maya\n"))
				if hubin==1:
					if int(haraaga)>=int(lacag):
						haray=int(haraaga)-int(lacag)
						print("Waxaad bixisay ${lacag} biil haraagagu waa ${haray}")
					else:
						print("Haraaga xisaabtadu kuguma filna")
				elif hubin==2:
					print("Macsalaamo!")
				else:
					print("Macsalaamo")
			else:
				print("Fadlan dooro number sax ah")
		elif biil==2:
			aqoonsiga=int(input("Fadlan geli aqoonsiga ganagsiga\n"))
			lacag=int(input("Fadlan geli lacagta\n"))
			hubin=int(input(f"Ma hubtaa ${lacag} wax ugu iibsato ganacsadaha aqoonsigisu yahay {aqoonsiga}\n1.Haa\n2.Maya\n"))
			if hubin==1:
				if int(haraaga)>=int(lacag):
					haray=int(haraaga)-int(lacag)
					print(f"Waxaad ${lacag} wax uga iibsato ganacsadaha aqoonsigiisu yahay {aqoonsiga} haraagagu waa${haray}")
				else:
					print("Haraaga xisaabtadu kuguma filna")
			elif hubin==2:
				print("Macsalaamo!")
			else:
				print("Macsalaamo")
		else:
			print("Fadlan dooro number sax ah")
#inta waxaa ku eg qebyta biilka
#inta waxaa ka bilaabanaya qeybta wareejinta
	elif dooro==4:
	   	num=int(input("Fadlan geli numberka aad lacagta aa direyso\n"))
	   	lacagta=int(input("Fadlan geli lacagta aa u direyso\n"))
	   	hubin=int(input(f"Ma hubtaa ina u ${lacagta} wareejisid {num}\n1.Haa\n2.Maya\n"))
	   	if hubin==1:
	   			if int(haraaga)>=int(lacagta):
	   				haray=int(haraaga)-int(lacagta)
	   				if num==lambarkeyga:
	   					print("Loo diraha iyo diraha isku mid ma noqon karaan fadlan ku celi markale")
	   				else:
	   					print(f"Waxaad ${lacagta} u wareejisay {num} haraagagu waa ${haray}")
	   			else:
	   				print("Haraaga xisaabtadu kuguma filna")
	   	elif hubin==2:
	   		print("Macsalaamo!")
	   	else:
	   		print("Macsalaamo")
	elif dooro==5:
		war=int(input("1.Last Action\n2.Wareejintii u dambeysay\n3.Iibsashadii U dambeysay\n4.Last 3 actions\n5.Email my last activity\n"))
		if war==1:
			maanta=datetime.datetime.today()
			print("10$ Ayaad ka heshay 252619880131, Taariikh:", maanta.strftime("%Y-%m-%d %H:%m"))
		elif war==2:
			state=int(input("Statementiga:\n1.u dirtay\n2.Ka heshay"))
			if state==1:
				lambar=int(input("Fadlan geli number-ka\n"))
				print("Your mini statement has been sent as SMS to your registered mobile no")
			elif state==2:
				lambar = int(input("Fadlan geli number-ka\n"))
				print("Your mini statement has been sent as SMS to your registered mobile no")
			else:
				print("Fadlan dooro number sax ah")
		elif war==3:
			iibso=int(input("Fadlan geli aqoonsiga ganacsiga"))
			ganacsade_name="WAAYA ARAG"
			ganacsade=223424166
			if iibso==ganacsade:
				maanta = datetime.datetime.today()
				print(f"10$ Ayaad uga iibsatay ganacsade {ganacsade_name} {iibso}, Taariikh:", maanta.strftime("%Y-%m-%d %H:%m"))
			else:
				print("Operation succeeded\nNO Transactions to display!")
		elif war==4:
			print("Yor mini statement has been sent as SMS to your registered mobile no")
		elif war==5:
			emayl=str(input("Fadlan geli email-kaga\n"))
			tarikh_hore=input("Fadlan geli taariikhda hore,\n(MAALIN/BISHA/SANADKA e.g 01/04/2017)\n")
			tarikh_danbe=input("Fadlan geli taariikhda danbe,\n(MAALIN/BISHA/SANADKA e.g 30/04/2017)\n")
			print(f"your request is been processed and the activity will be emailed to {emayl}")
		else:
			print("Fadlan dooro number sax ah")
	elif dooro==6:
		salam=int(input("1.ka wareeji EVCPLUS\n"))
		if salam==1:
			xisaabta=int(input("Fadlan dooro xisaabta Bangiga\n1.Daarusalam Bank\n2.Salaam Somali Bank\n3,Bank Beeraha\n4.Salaam Sch\n"))
			if xisaabta==1:
				darusam=int(input("Fadlan Accountiga\n"))
				maclumad=input("Fadlan geli macluumaad\n")
				lacag=int(input("Fadlan geli lacagta aa dhiganeyso\n"))
				if haraaga > lacag:
					haray = int(haraaga - lacag)
					print(f"Waxaad {lacag}$ dhigatay koontada {darusam} darusalam somali bank haraagagu waa {haray}")
				else:
					print("Haraaga xisaabtada kuguma filna")
			elif xisaabta==2:
				salam=int(input("Fadlan Accountiga\n"))
				maclumad=input("Fadlan geli macluumaad\n")
				lacag=int(input("Fadlan geli lacagta aa dhiganeyso\n"))
				if haraaga > lacag:
					haray = int(haraaga - lacag)
					print(f"Waxaad {lacag}$ dhigatay koontada {salam} Salam somali bank haraagagu waa {haray}")
				else:
					print("Haraaga xisaabtada kuguma filna")
			elif xisaabta==3:
				beeraha=int(input("Fadlan Accountiga\n"))
				maclumad=input("Fadlan geli macluumaad\n")
				lacag=int(input("Fadlan geli lacagta aa dhiganeyso\n"))
				if haraaga>lacag:
					haray=int(haraaga-lacag)
					print(f"Waxaad {lacag}$ dhigatay koontada {beeraha} Somali sch haraagagu waa {haray}")
				else:
					print("Haraaga xisaabtada kuguma filna")
			elif xisaabta==4:
				somali=int(input("Fadlan Accountiga\n"))
				maclumad=input("Fadlan geli macluumaad\n")
				lacag=int(input("Fadlan geli lacagta aa dhiganeyso\n"))
				if haraaga>lacag:
					haray=int(haraaga-lacag)
					print(f"Waxaad {lacag}$ dhigatay koontada {somali} Somali sch haraagagu waa haray")
				else:
					print("Haraaga xisaabtada kuguma filna")
			else:
				print("Fadlan dooro number sax ah")
		else:
			print("Fadlan dooro number sax ah")
	elif dooro==7:
		mar=int(input("1.Bedal lanbarka sirta ah\n2.Bedel luuqada\n3.Wergelin Mobile lumay\n4.Lacag xirasho\n5.U celi lacag qaldantay\n6.Enable mobile banking\n"))
		if mar==1:
			pin_c=int(input("Fadlan geli pin-kaga cusub\n"))
			pin_cv=int(input("Hubi pin-kaga cusub\n"))
			if pin_c and pin_cv!=passw:
				pin_cv and pin_c==passw
			else:
				print("Pinkaaga cusub iyo pinkaga hore isku mid ma noqon karaan")
		elif mar==2:
			luqad=int(input("Fadlan dooro luuqada\n1.English\n2.Somali\n"))
			if luqad==1:
				print=("[-EVCPLUS-]You have been successfully changed your language")
			elif luqad==2:
				print=("[-EVCPLUS-]Waad ku guuleysatay inaa badasho luuqadada")
			else:
				print("Fadlan dooro number sax ah")
		elif mar==3:
			lumay=int(input("Fadlan geli mobilka lumay\n"))
			print(f"Waxaa loo diiwan geliyay {lumay} inuu lumay")
		elif mar==4:
			lagu_khalday=int(input("Fadlan geli lambarka khalad-ka ah\n"))
			loo_rabay=int(input("Fadlan geli lambarka loo rabay\n"))
			macl=int(input("Fadlan geli maclumaad\n"))
			hubin=int(input("Ma hubtaa inad xayirato lacagtada\n1.Haa\n2.Maya\n"))
			if lagu_khalday!=loo_rabay:
				print("Waad ku guuleysatay inaad xayirato lacagtada")
			else:
				print("Qofka lagu khalday iyo qofka loo rabay isku mid ma noqon karaan fadlan ku laabo mar kale")
		elif mar==5:
			u_celi=int(input("Fadlan geli aqoonsiga lacag dirida\n"))
			print(f"Waxaad celisay $5 oo soo khaldoontay {u_celi}")
		elif mar==6:
			lam=int(input("Fadlan geli number-ka is diiwaan gelinta\n"))
			print("Activation record is not found")
		else:
			print("Fadlan dooro number sax ah")
	elif dooro==8:
		taaj=int(input("TAAJ\n1.Dibadda\n2.Ogow Khidmada\n3.Ogow macluumadka xawaalada\n"))
		if taaj==1:
			lam=int(input("Fadlan geli lanbarka qaataha\n"))
			magac=str(input("Fadlan geli magaca qaataha oo sedexan\n"))
			magalo= str(input("Fadlan geli magaalada uu joogo qaataha\n"))
			lacag= int(input("Fadlan geli lacagta aad u direyso\n"))
			macl= int(input("Fadlan geli macluumaad\n"))
			if haraaga > lacag:
				haray = int(haraaga - lacag)
				print(f"Waxaad ${lacag} u diray {magac} oo jooga haraagagu waa {haray}")
			else:
				print("Haraaga xisaabtada kuguma filna")
		elif taaj==2:
			shirkad=int(input("Fadlan dooro shirkada\n1.PAY TO EVCPLUS TMT\n2.TAAJ\n2.Taaj Pay\n4.New ETAAJ\n5.TAAJ IPS\n"))
			if shirkad==1:
				lam = int(input("Fadlan geli lanbarka qaataha\n"))
				lacag = int(input("Fadlan geli lacagta aad u direyso\n"))
				khidmo=lacag/100
				print(f"Khidmada ${lacag} waa ${khidmo}")
			elif shirkad == 2:
				lam = int(input("Fadlan geli lanbarka qaataha\n"))
				lacag = int(input("Fadlan geli lacagta aad u direyso\n"))
				khidmo = lacag / 100
				print(f"Khidmada ${lacag} waa ${khidmo}")
			elif shirkad == 3:
				lam = int(input("Fadlan geli lanbarka qaataha\n"))
				lacag = int(input("Fadlan geli lacagta aad u direyso\n"))
				khidmo = lacag / 100
				print(f"Khidmada ${lacag} waa ${khidmo}")
			elif shirkad == 4:
				lam = int(input("Fadlan geli lanbarka qaataha\n"))
				lacag = int(input("Fadlan geli lacagta aad u direyso\n"))
				khidmo = lacag / 100
				print(f"Khidmada ${lacag} waa ${khidmo}")
			elif shirkad == 5:
				lam = int(input("Fadlan geli lanbarka qaataha\n"))
				lacag = int(input("Fadlan geli lacagta aad u direyso\n"))
				khidmo = lacag / 100
				print(f"Khidmada ${lacag} waa ${khidmo}")
			else:
				print("Fadlan dooro number sax ah")
		elif taaj==3:
			aqonsi=int(input("Fadlan geli aqoonsiga lacag dirida\n"))
			lacag=int(input("Fadlan geli lacag aad direyso"))
			if haraaga > lacag:
				haray = int(haraaga - lacag)
				print(f"Waxaad ${lacag} aqoonsiga lambarkisu yahay {aqonsi} haragagu waa ${haray}")
			else:
				print("Haraaga xisaabtada kuguma filna")
		else:
			print("Fadlan dooro number sax ah")
	elif dooro==9:
		biil=int(input("EVCPLUS\n1.Itus Haraaga Bill ka\n2.Wada bixi Bill-ka\n3.Qeyb ka bixi Bill-ka\n"))
		if biil==1:
			itus=int(input("Fadlan geli Bill reference number\n"))
			print("Haraagaga bill-ka waa $10")
		elif biil==2:
			wada=int(input("Fadlan geli Bill reference number\n"))
			hubin=int(input("Ma hubtaa inaad wada bixiso bill-kaga\n1.Haa\n2.Maya"))
			if hubin==1:
				print("Waxaad wada bixisay bill-kaga oo dhan")
			elif hubin==2:
				print("Mahadsanid")
			else:
				print("Fadlan dooro number sax ah")
		elif biil==3:
			wada=int(input("Fadlan geli Bill reference number\n"))
			hubin=int(input("Ma hubtaa inaad wada bixiso bill-kaga\n1.Haa\n2.Maya\n"))
			if hubin==1:
				print("Waxaad wada bixisay bill-kaga oo dhan")
			elif hubin==2:
				print("Mahadsanid")
			else:
				print("Fadlan dooro number sax ah")
		else:
			print("Fadlan dooro number sax ah")
	else:
		print("Fadlan dooro number sax ah")
else:
	print("Pinka Aad gelisay Waa khalad Macsalaamo")
