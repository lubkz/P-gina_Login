import flet
import flet as ft

def main(pagina):
    titulo = ft.Text("HashZap")
    print("Eu odeio gatos")

    teste = ft.FilePicker

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto = f"{campo_nome_usuario.value}: {texto_mensagem.value}"

        pagina.pubsub.send_all(texto)

        texto_mensagem.value = ""

        pagina.update()

    texto_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([texto_mensagem, botao_enviar])

    chat = ft.Column()

    def entrar_chat(evento):
        pagina.remove(botao_iniciar)
        pagina.remove(titulo)

        janela.open = False

        pagina.add(chat)

        pagina.add(linha_mensagem)

        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat."
        pagina.pubsub.send_all(texto_entrou_chat)



        pagina.update()

    titulo_janela = ft.Text("Bem vindo ao HashZap!")
    campo_nome_usuario = ft.TextField(label="Digite seu nome aqui")
    botao_iniciar_chat = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)


    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_iniciar_chat])

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)