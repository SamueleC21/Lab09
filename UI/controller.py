import flet as ft



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        self._view.txt_result.clean()
        x = self._view.txt_distanza.value
        if x is None or x == "":
            self._view.create_alert("Inserire la distanza")
            return
        try:
            x = float(x)
        except:
            self._view.create_alert("Inserire un numero")
            self._view.update_page()
            return

        self._model.buildGrafo(x)
        numNodi = self._model.NumNodes()
        numArchi = self._model.NumArchi()
        self._view.txt_result.controls.append(
            ft.Text(f"Il garfo possiede {numNodi} nodi e {numArchi} archi")
        )

        archi = self._model._grafo.edges
        self._view.txt_result.controls.append(
            ft.Text(f"\n \n Gli archi sono; ")
        )
        for a in archi:
            self._view.txt_result.controls.append(
               ft.Text(f"{a[0]} --> {a[1]} con distanza media di {a[2]["weight"]}")
            )

        self._view.update_page()
