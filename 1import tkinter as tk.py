import tkinter as tk
from tkinter import messagebox

# Definindo as classes Motorista, Viagem e Empresa de Transporte
class Motorista:
    def __init__(self, nome, cnh):
        self.nome = nome
        self.cnh = cnh

class Veiculo:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa

class Viagem:
    def __init__(self, origem, destino, motorista, veiculo, status="Pendente"):
        self.origem = origem
        self.destino = destino
        self.motorista = motorista
        self.veiculo = veiculo
        self.status = status

    def concluir(self):
        self.status = "Concluída"

    def __str__(self):
        return f"Viagem de {self.origem} para {self.destino} - Motorista: {self.motorista.nome} - Veículo: {self.veiculo.modelo} ({self.veiculo.placa}) - Status: {self.status}"

class EmpresaTransporte:
    def __init__(self):
        self.motoristas = []
        self.veiculos = []
        self.viagens = []

    def cadastrar_motorista(self, nome, cnh):
        motorista = Motorista(nome, cnh)
        self.motoristas.append(motorista)
        return f"Motorista {nome} cadastrado com sucesso!"

    def cadastrar_veiculo(self, modelo, placa):
        veiculo = Veiculo(modelo, placa)
        self.veiculos.append(veiculo)
        return f"Veículo {modelo} ({placa}) cadastrado com sucesso!"

    def registrar_viagem(self, origem, destino, motorista, veiculo):
        viagem = Viagem(origem, destino, motorista, veiculo)
        self.viagens.append(viagem)
        return f"Viagem de {origem} para {destino} registrada com sucesso!"

    def listar_motoristas(self):
        return "\n".join([f"{i+1}. {motorista.nome} - CNH: {motorista.cnh}" for i, motorista in enumerate(self.motoristas)])

    def listar_viagens(self):
        if not self.viagens:
            return "Nenhuma viagem registrada."
        else:
            return "\n".join([str(viagem) for viagem in self.viagens])

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Transporte")

        self.empresa = EmpresaTransporte()

        # Menu principal
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Menu de opções
        self.opcoes_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Opções", menu=self.opcoes_menu)
        self.opcoes_menu.add_command(label="Cadastrar Motorista", command=self.cadastrar_motorista)
        self.opcoes_menu.add_command(label="Cadastrar Veículo", command=self.cadastrar_veiculo)
        self.opcoes_menu.add_command(label="Registrar Viagem", command=self.registrar_viagem)
        self.opcoes_menu.add_command(label="Listar Motoristas", command=self.listar_motoristas)
        self.opcoes_menu.add_command(label="Listar Viagens", command=self.listar_viagens)
        self.opcoes_menu.add_command(label="Concluir Viagem", command=self.concluir_viagem)

    def cadastrar_motorista(self):
        # Criando janela para cadastrar motorista
        self.janela_motorista = tk.Toplevel(self.root)
        self.janela_motorista.title("Cadastrar Motorista")

        tk.Label(self.janela_motorista, text="Nome do Motorista:").grid(row=0, column=0)
        nome_entry = tk.Entry(self.janela_motorista)
        nome_entry.grid(row=0, column=1)

        tk.Label(self.janela_motorista, text="CNH:").grid(row=1, column=0)
        cnh_entry = tk.Entry(self.janela_motorista)
        cnh_entry.grid(row=1, column=1)

        def salvar_motorista():
            nome = nome_entry.get()
            cnh = cnh_entry.get()

   
