import customtkinter as ctk

version = (1.0,"kararlı sürüm")

def program():
	def tus_bir_1F():
		main_print_panel.insert("end","1")
	def tus_iki_1F():
		main_print_panel.insert("end","2")
	def tus_uc_1F():
		main_print_panel.insert("end","3")
	def tus_dort_2F():
		main_print_panel.insert("end","4")
	def tus_bes_2F():
		main_print_panel.insert("end","5")
	def tus_alti_2F():
		main_print_panel.insert("end","6")
	def tus_yedi_3F():
		main_print_panel.insert("end","7")
	def tus_sekiz_3F():
		main_print_panel.insert("end","8")
	def tus_dokuz_3F():
		main_print_panel.insert("end","9")
	def tus_sifir_0F():
		main_print_panel.insert("end","0")

	def tus_toplamaF():
		main_print_panel.insert("end","+")
	def tus_cikarmaF():
		main_print_panel.insert("end","-")
	def tus_carpmaF():
		main_print_panel.insert("end","*")
	def tus_bolmeF():
		main_print_panel.insert("end","/")

	def tus_esittirF():
		main_print_panel_oldData = main_print_panel.get("0.0", ctk.END).strip()
    
		if main_print_panel_oldData:
			try:
				result = eval(main_print_panel_oldData)
            
				main_print_panel.delete("0.0", ctk.END)
				main_print_panel.insert("0.0", str(result))
			except Exception as e:
				main_print_panel.delete("0.0", ctk.END)
				main_print_panel.insert("0.0", "Hata!")
		else:
			main_print_panel.insert("0.0", "Boş ifade!")



	window = ctk.CTk()
	window.title("Micro Hesap Makinesi")
	window.minsize(1000,700)
	window.maxsize(100,700)
	window.geometry("1000x700")

	color_tus = "#660099"
	color_main_print_panel = "#6A5ACD"
	color_tus2 = "#800080"

	class konum:
		def __init__(self,x=0,y=0):
			self.x = x
			self.y = y

	tuslar_height = 100
	tuslar_width = 240
	tuslar_konum = konum(x=10,y=200)
	tuslar_boyut = 40

	void = ctk.CTkLabel(
		window,
		text="")
	void.pack()

	main_print_panel = ctk.CTkTextbox(
		window,
		height=140,
		width=970,
		fg_color=color_main_print_panel,
		text_color="white",
		font=("italic",tuslar_boyut * 2))
	main_print_panel.pack()
	def disable_enter(event):
		return "break"
	main_print_panel.bind("<Return>",disable_enter)


	tus_bir_1 = ctk.CTkButton(
		window,
		text="1",
		height=tuslar_height,
		width=tuslar_width,
		fg_color=color_tus,
		font=("italic",tuslar_boyut),
		command=tus_bir_1F
		)
	tus_bir_1.place(x=tuslar_konum.x,y=tuslar_konum.y)

	tus_iki_1 = ctk.CTkButton(
		window,
		text="2",
		height=tuslar_height,
		width=tuslar_width,
		fg_color=color_tus,
		font=("italic",tuslar_boyut),
		command=tus_iki_1F
		)
	tus_iki_1.place(x=tuslar_konum.x + 250 ,y=tuslar_konum.y)

	tus_uc_1 = ctk.CTkButton(
		window,
		text="3",
		height=tuslar_height,
		width=tuslar_width,
		fg_color=color_tus,
		font=("italic",tuslar_boyut),
		command=tus_uc_1F
		)
	tus_uc_1.place(x=tuslar_konum.x + 500 ,y=tuslar_konum.y)

	tus_dort_2 = ctk.CTkButton(
		window,
		text="4",
		height=tuslar_height,
		width=tuslar_width,
		fg_color=color_tus,
		font=("italic",tuslar_boyut),
		command=tus_dort_2F
		)
	tus_dort_2.place(x=tuslar_konum.x,y=tuslar_konum.y + 120)

	tus_bes_2 = ctk.CTkButton(
		window,
		text="5",
		height=tuslar_height,
		width=tuslar_width,
		fg_color=color_tus,
		font=("italic",tuslar_boyut),
		command=tus_bes_2F
		)
	tus_bes_2.place(x=tuslar_konum.x + 250,y=tuslar_konum.y + 120)

	tus_alti_2 = ctk.CTkButton(
		window,
		text="6",
		height=tuslar_height,
		width=tuslar_width,
		fg_color=color_tus2,
		font=("italic",tuslar_boyut),
		command=tus_alti_2F
		)
	tus_alti_2.place(x=tuslar_konum.x + 500,y=tuslar_konum.y + 120)

	tus_yedi_3 = ctk.CTkButton(
		window,
		text="7",
		height=tuslar_height,
		width=tuslar_width,
		fg_color=color_tus,
		font=("italic",tuslar_boyut),
		command=tus_yedi_3F
		)
	tus_yedi_3.place(x=tuslar_konum.x,y=tuslar_konum.y + 120 * 2)

	tus_sekiz_3 = ctk.CTkButton(
		window,
		text="8",
		height=tuslar_height,
		width=tuslar_width,
		fg_color=color_tus2,
		font=("italic",tuslar_boyut),
		command=tus_sekiz_3F
		)
	tus_sekiz_3.place(x=tuslar_konum.x + 250,y=tuslar_konum.y + 120 * 2)

	tus_dokuz_3 = ctk.CTkButton(
		window,
		text="9",
		height=tuslar_height,
		width=tuslar_width,
		fg_color=color_tus2,
		font=("italic",tuslar_boyut),
		command=tus_dokuz_3F
		)
	tus_dokuz_3.place(x=tuslar_konum.x + 500,y=tuslar_konum.y + 120 * 2)

	tus_sifir_0 = ctk.CTkButton(
		window,
		text="0",
		height=tuslar_height,
		width=tuslar_width * 2,
		fg_color=color_tus2,
		font=("italic",tuslar_boyut),
		command=tus_sifir_0F
		)
	tus_sifir_0.place(x=tuslar_konum.x,y=tuslar_konum.y + 120 * 3)


	islem_konum = konum(x=800,y=200)

	tus_toplama = ctk.CTkButton(
		window,
		text="+",
		height=tuslar_height,
		width=tuslar_width - 90,
		fg_color=color_tus,
		font=("italic",tuslar_boyut),
		command=tus_toplamaF
		)
	tus_toplama.place(x=islem_konum.x,y=islem_konum.y)

	tus_cikarma = ctk.CTkButton(
		window,
		text="-",
		height=tuslar_height,
		width=tuslar_width - 90,
		fg_color=color_tus2,
		font=("italic",tuslar_boyut),
		command=tus_cikarmaF
		)
	tus_cikarma.place(x=islem_konum.x,y=islem_konum.y + 120)

	tus_carpma = ctk.CTkButton(
		window,
		text="*",
		height=tuslar_height,
		width=tuslar_width - 90,
		fg_color=color_tus2,
		font=("italic",tuslar_boyut),
		command=tus_carpmaF
		)
	tus_carpma.place(x=islem_konum.x,y=islem_konum.y + 240)

	tus_bolme = ctk.CTkButton(
		window,
		text="/",
		height=tuslar_height,
		width=tuslar_width - 90,
		fg_color=color_tus2,
		font=("italic",tuslar_boyut),
		command=tus_bolmeF
		)
	tus_bolme.place(x=islem_konum.x,y=islem_konum.y + 360)

	tus_esittir = ctk.CTkButton(
		window,
		text="=",
		height=tuslar_height,
		width=tuslar_width,
		fg_color=color_tus2,
		font=("italic",tuslar_boyut),
		command=tus_esittirF
		)
	tus_esittir.place(x=tuslar_konum.x + 500,y=tuslar_konum.y + 120 * 3)

	window.mainloop()


if __name__ == "__main__":
	program()