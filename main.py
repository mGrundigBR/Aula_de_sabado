#!/usr/bin/env python


class Brighton(object):

	def __init__(self):
		self.l = []

	def bebidas(self):
		self.bebidas_precos = {
			"cerveja": 5,
			"suco": 3,
			"agua": 0,
		}

	def comida(self):
		self.comidas_precos = {
			"galinha": 5,
			"camarao": 10,
			"arroz": 3,
		}	
	def pedido(self, nome, quantidade, tipo):
		p = {
			"nome": nome,
			"quantidade": quantidade,
			"tipo": tipo,
		}

		self.l.append(p)

	def print_conta(self):
		preco_final = 0
		for pedido in self.l:
			nome = pedido["nome"]	
			quantidade = pedido["quantidade"]
			tipo = pedido["tipo"]

			if tipo == "comida":
				preco = self.comidas_precos[nome] * quantidade
				preco_final = preco_final + preco
			if tipo == "bebidas":
				preco = self.bebidas_precos[nome] * quantidade
				preco_final = preco_final + preco
		return preco_final


b = Brighton()
b.comida()
b.bebidas()
b.pedido("galinha", 2, "comida")
b.pedido("camarao", 1, "comida")
b.pedido("arroz", 3, "comida")
b.pedido("cerveja", 14, "bebidas")

conta = b.print_conta()

print(conta)

