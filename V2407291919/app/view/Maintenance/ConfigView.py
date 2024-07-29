import view.UIElements.UIForm as UIForm
import view.UIElements.UIDetail as UIDetail
import ttkbootstrap as ttk
from ttkbootstrap import *


class ConfigView(UIForm.UIForm):
    def __init__(self, root) -> None:
        self.parent = root
        self.controller = None

    def set_controller(self, controller, data_content={}):
        self.controller = controller
        self.data_content = data_content

    def set_tab_display(self, tab_value):
        self.notebook.select(tab_value)
        self._notebook_click()

    def set_tab_insert(self, tab_value):
        self.notebook.select(tab_value)
        self._notebook_click()
    
    def set_tab_update(self, tab_value):
        self.notebook.select(tab_value)
        self._notebook_click()

    def set_tab_delete(self, tab_value):
        self.notebook.select(tab_value)
        self._notebook_click()

    def create(self):
        self.set_size_medium()
        data_geometry = self.set_geometry()
        self.parent.geometry(data_geometry)
        self.parent.resizable(False, False)

        frame_body = ttk.Frame(self.parent, bootstyle=DEFAULT)
        frame_body.pack(fill=BOTH, expand=True, padx=4,
                        pady=4, ipadx=6, ipady=6)

        self.csUIDetail = UIDetail.UIDetail(
            self.parent, frame_body, self.controller, self.data_content)
        self.csUIDetail.create_header()

        self.notebook = ttk.Notebook(frame_body, bootstyle=DARK)
        self.notebook.bind("<ButtonRelease-1>", self._notebook_click)
        self.notebook.pack(fill=BOTH, expand=True, padx=6, ipadx=6, ipady=6)

        frame_general = self._mount_tab_general(self.notebook)
        frame_details = self._mount_tab_details(self.notebook)

        self.notebook.add(frame_general, text="General Information")
        self.notebook.add(frame_details, text="Details")

        self.create_footer(frame_body)

        self._notebook_click()

    def _mount_tab_general(self, container):
        frame_tab = ttk.Frame(container, bootstyle=DEFAULT)
        frame_tab.pack(fill=BOTH, expand=True)

        self.selected_combobox = StringVar()

        frame_group_cmb = ttk.Frame(frame_tab, bootstyle=DEFAULT)

        label_combobox = ttk.Label(
            frame_group_cmb, text="Seleção do Bloco:", width=30, bootstyle=DARK)
        label_combobox.pack(fill=X, side=LEFT)

        data_list = []
        data_list.append("(Todos)")
        for item in self.data_content['Data']['Blocks']:
            data_list.append(item)

        combobox = ttk.Combobox(
            frame_group_cmb, textvariable=self.selected_combobox, bootstyle=DEFAULT)
        combobox['values'] = data_list
        combobox['state'] = 'readonly'
        combobox.current(0)
        combobox.pack(fill=X, expand=True)

        combobox.bind("<<ComboboxSelected>>", self._combobox_changed)

        frame_group_cmb.pack(fill=X, anchor=N, padx=6, pady=8)

        self._mount_data_tree(frame_tab)

        return frame_tab

    def _combobox_changed(self, event):
        for item in self.tree.get_children():
            self.tree.delete(item)

        section = self.selected_combobox.get()
        self.controller._load_data_tree(section)

        data_list = self.data_content['Data']['DataAllBlocks']

        for item in data_list:
            for k, v in item.items():
                item_key_value = (k, v)
                self.tree.insert('', tk.END, values=item_key_value)

    def _mount_tab_details(self, container):
        frame_tab = ttk.Frame(container, bootstyle=DEFAULT)
        frame_tab.pack(fill=BOTH, expand=True)

        frame_group = ttk.Frame(frame_tab, bootstyle=DEFAULT)
        frame_group_1 = ttk.Frame(frame_group, bootstyle=DEFAULT)
        label_block = ttk.Label(
            frame_group_1, text="Bloco:", width=30, bootstyle=DEFAULT)
        label_block.pack(fill=X, side=LEFT)

        self.entry_block = ttk.Entry(frame_group_1, bootstyle=DEFAULT)
        self.entry_block.pack(fill=X, expand=True, side=LEFT)
        frame_group_1.pack(fill=X, padx=6, pady=4)

        frame_group_2 = ttk.Frame(frame_group, bootstyle=DEFAULT)
        label_key = ttk.Label(frame_group_2, text="Chave:",
                              width=30, bootstyle=DEFAULT)
        label_key.pack(fill=X, side=LEFT)

        entry_key = ttk.Entry(frame_group_2, bootstyle=DEFAULT)
        entry_key.pack(fill=X, expand=True, side=LEFT)
        frame_group_2.pack(fill=X, padx=6, pady=4)

        frame_group_3 = ttk.Frame(frame_group, bootstyle=DEFAULT)
        label_value = ttk.Label(
            frame_group_3, text="Valor:", width=30, bootstyle=DEFAULT)
        label_value.pack(fill=X, anchor=N, side=LEFT)

        entry_value = ttk.Entry(frame_group_3, bootstyle=DEFAULT)
        entry_value.pack(fill=BOTH, expand=True, anchor=N, side=LEFT)
        frame_group_3.pack(fill=BOTH, expand=True, padx=6, pady=4)
        frame_group.pack(fill=BOTH, expand=True, pady=4)

        return frame_tab

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            record = item['values']
            # show a message
            # showinfo(title='Information', message=','.join(record))

    def _mount_data_tree(self, container):
        columns = ('column_key', 'column_value')

        frame_group = ttk.Frame(container, bootstyle=DEFAULT)

        self.tree = ttk.Treeview(frame_group, columns=columns, show='headings')

        self.tree.heading('column_key', text='KEY')
        self.tree.heading('column_value', text='VALUE')

        section = self.selected_combobox.get()
        self.controller._load_data_tree(section)

        data_list = self.data_content['Data']['DataAllBlocks']

        for item in data_list:
            for k, v in item.items():
                item_key_value = (k, v)
                self.tree.insert('', tk.END, values=item_key_value)

        # self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        # .grid(row=0, column=0, sticky='nsew')
        self.tree.pack(fill=BOTH, expand=True, side=LEFT)

        scrollbar = ttk.Scrollbar(
            frame_group, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        # .grid(row=0, column=1, sticky='ns')
        scrollbar.pack(fill=Y, side=RIGHT)

        frame_group.pack(fill=BOTH, expand=True)

    def _notebook_click(self, event=None):
        tab_name = self.notebook.select()
        self.tab_index = self.notebook.index(tab_name)

        if self.tab_index == 0:
            self.btn_fechar["text"] = "Fechar"
            self.btn_confirmar["text"] = "Novo"
            self.btn_editar.state(["!disabled"])
            self.btn_excluir.state(["!disabled"])
        elif self.tab_index == 1:
            self.btn_fechar["text"] = "Cancelar"
            self.btn_confirmar["text"] = "Confirmar"
            self.btn_editar.state(["disabled"])
            self.btn_excluir.state(["disabled"])
            self.entry_block.focus_set()
    
    def create_footer(self, container):
        frm_group = ttk.Frame(container, bootstyle=DEFAULT)

        self.btn_fechar = ttk.Button(frm_group, text="Fechar",
                            command=self._btClose_click, width=12, padding=8, bootstyle=DARK)
        self.btn_fechar.pack(side="left", padx=4, pady=2)
        self.btn_fechar.bind("<Return>", self._btClose_click)

        self.btn_confirmar = ttk.Button(frm_group, text="Confirmar",
                               command=self._btConfirm_click, width=12, padding=8, bootstyle=SUCCESS)
        self.btn_confirmar.pack(side="left", padx=4, pady=2)
        self.btn_confirmar.bind("<Return>", self._btConfirm_click)

        self.btn_editar = ttk.Button(frm_group, text="Editar",
                            command=self._btUpdate_click, width=12, padding=8, bootstyle=PRIMARY)
        self.btn_editar.pack(side="left", padx=4, pady=2)
        self.btn_editar.bind("<Return>", self._btUpdate_click)

        self.btn_excluir = ttk.Button(frm_group, text="Excluir",
                             command=self._btDelete_click, width=12, padding=8, bootstyle=DANGER)
        self.btn_excluir.pack(side="left", padx=4, pady=2)
        self.btn_excluir.bind("<Return>", self._btDelete_click)

        # btn_options = ttk.Button(frm_group, text="Opções",
        #                      command=self._btOptions_click, width=12, padding=8, bootstyle=SECONDARY)
        # btn_options.pack(side="left", padx=4, pady=2)
        # btn_options.bind("<Return>", self._btOptions_click)

        frm_group.pack(fill="x", padx=5, pady=5, anchor="se")

        self.parent.bind("<Any-KeyPress>", self._press_key_shortcut)
    
    def set_top_message_display(self, message_out=''):
        self.v_msg_display.set(message_out)

    def _btClose_click(self, event=None):
        if self.controller:
            self.controller._close(self.tab_index)

    def _btConfirm_click(self, event=None):
        if self.controller:
            self.controller._confirm(self.tab_index)

    def _btUpdate_click(self, event=None):
        if self.controller:
            self.controller._update(self.tab_index)

    def _btDelete_click(self, event=None):
        if self.controller:
            self.controller._delete(self.tab_index)

    # def _btOptions_click(self, event=None):
    #     if self.controller:
    #         self.controller._options(self.tab_index)

    def _press_key_shortcut(self, event):
        if (event.keysym == 'f' or event.keysym == 'F'):
            self._btClose_click()

        if (event.keysym == 'c' or event.keysym == 'C'):
            self._btConfirm_click()

        if (event.keysym == 'e' or event.keysym == 'E'):
            self._btUpdate_click()

        if (event.keysym == 'x' or event.keysym == 'X'):
            self._btDelete_click()

        # if (event.keysym == 'o' or event.keysym == 'O'):
        #     self._btOptions_click()
