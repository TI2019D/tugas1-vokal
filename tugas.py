
class HitungVokal:
	
	A = 0
	U = 0
	I = 0
	E = 0
	O = 0

	def Hitung(self, teks):

		# tulis implementasi di sini.

		pass # hapus pass.
		

	def Tampilkan(self):
		print(f"A={self.A}, I={self.I}, U={self.U}, E={self.E}, O={self.O}")
		



a = input("Masukkan Teks:")

vokal = HitungVokal()

vokal.Hitung(a)

vokal.Tampilkan()

