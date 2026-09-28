import tkinter as tk
from tkinter import ttk, messagebox


# ============================================================
# ARCHI AI - AI HOME DESIGN GENERATOR
# Full Desktop Application
# ============================================================

# ---------------- COLORS ----------------

BG = "#F3F6FB"
WHITE = "#FFFFFF"
NAVY = "#172554"
BLUE = "#2563EB"
SKY = "#0EA5E9"
CYAN = "#06B6D4"
TEAL = "#0F766E"
GREEN = "#16A34A"
PURPLE = "#7C3AED"
ORANGE = "#F59E0B"
RED = "#EF4444"

TEXT = "#172033"
MUTED = "#64748B"
BORDER = "#DCE3EE"

LIGHT_BLUE = "#EFF6FF"
LIGHT_PURPLE = "#F5F3FF"
LIGHT_GREEN = "#ECFDF5"
LIGHT_ORANGE = "#FFF7ED"


class AIHomeDesignGenerator:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "ARCHI AI - Home Design Generator"
        )

        self.root.geometry("900x600")

        self.root.resizable(False, False)

        self.root.configure(
            bg=BG
        )

        # ---------------- DESIGN DATA ----------------

        self.design = {
            "length": 40,
            "width": 30,
            "floors": 1,
            "bedrooms": 2,
            "bathrooms": 2,
            "style": "Modern",
            "kitchen": True,
            "parking": True,
            "garden": True,
            "balcony": False
        }

        # Interior room list

        self.rooms = [
            "LIVING ROOM",
            "BEDROOM",
            "KITCHEN",
            "BATHROOM"
        ]

        self.current_room = 0

        self.visual_canvas = None

        self.show_dashboard()

    # ========================================================
    # CLEAR
    # ========================================================

    def clear(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # ========================================================
    # HEADER
    # ========================================================

    def header(self, active="HOME"):

        header = tk.Frame(
            self.root,
            bg=WHITE,
            height=68
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        # Logo

        logo = tk.Frame(
            header,
            bg=WHITE
        )

        logo.pack(
            side="left",
            padx=18
        )

        tk.Label(
            logo,
            text="A",
            font=("Segoe UI", 18, "bold"),
            bg=BLUE,
            fg=WHITE,
            width=2
        ).pack(
            side="left",
            padx=(0, 8)
        )

        brand = tk.Frame(
            logo,
            bg=WHITE
        )

        brand.pack(
            side="left"
        )

        tk.Label(
            brand,
            text="ARCHI AI",
            font=("Segoe UI", 14, "bold"),
            bg=WHITE,
            fg=NAVY
        ).pack(
            anchor="w"
        )

        tk.Label(
            brand,
            text="HOME DESIGN STUDIO",
            font=("Segoe UI", 7, "bold"),
            bg=WHITE,
            fg=MUTED
        ).pack(
            anchor="w"
        )

        # Navigation

        nav = tk.Frame(
            header,
            bg=WHITE
        )

        nav.pack(
            side="right",
            padx=12
        )

        items = [
            ("HOME", self.show_dashboard),
            ("DESIGN", self.show_create),
            ("2D PLAN", self.show_floor_plan),
            ("3D VIEW", self.show_visualization),
            ("COST", self.show_cost),
            ("SUMMARY", self.show_summary)
        ]

        for title, command in items:

            if title == active:
                button_bg = BLUE
                button_fg = WHITE
            else:
                button_bg = WHITE
                button_fg = MUTED

            tk.Button(
                nav,
                text=title,
                command=command,
                font=("Segoe UI", 8, "bold"),
                bg=button_bg,
                fg=button_fg,
                activebackground=BLUE,
                activeforeground=WHITE,
                relief="flat",
                bd=0,
                padx=7,
                pady=7,
                cursor="hand2"
            ).pack(
                side="left",
                padx=2
            )

        tk.Frame(
            self.root,
            bg=BLUE,
            height=3
        ).pack(
            fill="x"
        )

    # ========================================================
    # DASHBOARD
    # ========================================================

    def show_dashboard(self):

        self.clear()

        self.header("HOME")

        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            fill="both",
            expand=True,
            padx=22,
            pady=15
        )

        # Hero

        hero = tk.Frame(
            main,
            bg=NAVY,
            height=175
        )

        hero.pack(
            fill="x"
        )

        hero.pack_propagate(False)

        left = tk.Frame(
            hero,
            bg=NAVY
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=25,
            pady=22
        )

        tk.Label(
            left,
            text="DESIGN YOUR DREAM HOME",
            font=("Segoe UI", 21, "bold"),
            bg=NAVY,
            fg=WHITE
        ).pack(
            anchor="w"
        )

        tk.Label(
            left,
            text="AI planning  •  2D floor plan  •  Interior  •  Exterior",
            font=("Segoe UI", 9),
            bg=NAVY,
            fg="#BFDBFE"
        ).pack(
            anchor="w",
            pady=(5, 14)
        )

        tk.Button(
            left,
            text="START DESIGN  →",
            command=self.show_create,
            font=("Segoe UI", 9, "bold"),
            bg=CYAN,
            fg=NAVY,
            activebackground="#67E8F9",
            relief="flat",
            bd=0,
            padx=18,
            pady=9,
            cursor="hand2"
        ).pack(
            anchor="w"
        )

        # Hero right

        right = tk.Frame(
            hero,
            bg="#1E3A8A",
            width=230
        )

        right.pack(
            side="right",
            fill="y"
        )

        right.pack_propagate(False)

        tk.Label(
            right,
            text="3D",
            font=("Segoe UI", 40, "bold"),
            bg="#1E3A8A",
            fg="#93C5FD"
        ).pack(
            pady=(15, 0)
        )

        tk.Label(
            right,
            text="INSIDE + OUTSIDE",
            font=("Segoe UI", 9, "bold"),
            bg="#1E3A8A",
            fg=WHITE
        ).pack()

        # Stats

        stats = tk.Frame(
            main,
            bg=BG
        )

        stats.pack(
            fill="x",
            pady=11
        )

        self.stat_card(
            stats,
            "PLOT AREA",
            f"{self.plot_area():,.0f} sq.ft",
            BLUE
        )

        self.stat_card(
            stats,
            "BUILT-UP",
            f"{self.built_up():,.0f} sq.ft",
            TEAL
        )

        self.stat_card(
            stats,
            "BEDROOMS",
            str(self.design["bedrooms"]),
            PURPLE
        )

        self.stat_card(
            stats,
            "EST. COST",
            self.money(self.cost()),
            ORANGE
        )

        tk.Label(
            main,
            text="QUICK ACCESS",
            font=("Segoe UI", 11, "bold"),
            bg=BG,
            fg=TEXT
        ).pack(
            anchor="w"
        )

        quick = tk.Frame(
            main,
            bg=BG
        )

        quick.pack(
            fill="x",
            pady=7
        )

        self.quick_card(
            quick,
            "01",
            "Create Design",
            "Set home requirements",
            BLUE,
            self.show_create
        )

        self.quick_card(
            quick,
            "02",
            "2D Floor Plan",
            "View room arrangement",
            PURPLE,
            self.show_floor_plan
        )

        self.quick_card(
            quick,
            "03",
            "Interior View",
            "Explore inside rooms",
            TEAL,
            self.show_visualization
        )

        self.quick_card(
            quick,
            "04",
            "Cost Estimate",
            "Check project budget",
            ORANGE,
            self.show_cost
        )

    # ========================================================
    # STAT CARD
    # ========================================================

    def stat_card(
        self,
        parent,
        title,
        value,
        color
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            height=70,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=4
        )

        card.pack_propagate(False)

        tk.Frame(
            card,
            bg=color,
            width=5
        ).pack(
            side="left",
            fill="y"
        )

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 8, "bold"),
            bg=WHITE,
            fg=MUTED
        ).pack(
            anchor="w",
            padx=12,
            pady=(10, 1)
        )

        tk.Label(
            card,
            text=value,
            font=("Segoe UI", 13, "bold"),
            bg=WHITE,
            fg=color
        ).pack(
            anchor="w",
            padx=12
        )

    # ========================================================
    # QUICK CARD
    # ========================================================

    def quick_card(
        self,
        parent,
        number,
        title,
        description,
        color,
        command
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            height=100,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=4
        )

        card.pack_propagate(False)

        tk.Button(
            card,
            text=number,
            command=command,
            font=("Segoe UI", 10, "bold"),
            bg=color,
            fg=WHITE,
            relief="flat",
            bd=0,
            width=4,
            cursor="hand2"
        ).pack(
            anchor="w",
            padx=11,
            pady=(10, 4)
        )

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 9, "bold"),
            bg=WHITE,
            fg=TEXT
        ).pack(
            anchor="w",
            padx=11
        )

        tk.Label(
            card,
            text=description,
            font=("Segoe UI", 8),
            bg=WHITE,
            fg=MUTED
        ).pack(
            anchor="w",
            padx=11
        )

    # ========================================================
    # CREATE DESIGN
    # ========================================================

    def show_create(self):

        self.clear()

        self.header("DESIGN")

        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            fill="both",
            expand=True,
            padx=22,
            pady=14
        )

        tk.Label(
            main,
            text="CREATE YOUR HOME",
            font=("Segoe UI", 20, "bold"),
            bg=BG,
            fg=TEXT
        ).pack(
            anchor="w"
        )

        tk.Label(
            main,
            text="Configure the property and generate your AI home concept.",
            font=("Segoe UI", 9),
            bg=BG,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(2, 10)
        )

        body = tk.Frame(
            main,
            bg=BG
        )

        body.pack(
            fill="both",
            expand=True
        )

        # Left

        left = tk.Frame(
            body,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 7)
        )

        tk.Label(
            left,
            text="SITE CONFIGURATION",
            font=("Segoe UI", 10, "bold"),
            bg=WHITE,
            fg=BLUE
        ).pack(
            anchor="w",
            padx=18,
            pady=(13, 7)
        )

        self.length_var = tk.StringVar(
            value=str(self.design["length"])
        )

        self.width_var = tk.StringVar(
            value=str(self.design["width"])
        )

        self.floors_var = tk.StringVar(
            value=str(self.design["floors"])
        )

        self.bedrooms_var = tk.StringVar(
            value=str(self.design["bedrooms"])
        )

        self.bathrooms_var = tk.StringVar(
            value=str(self.design["bathrooms"])
        )

        self.input_row(
            left,
            "Plot Length (ft)",
            self.length_var
        )

        self.input_row(
            left,
            "Plot Width (ft)",
            self.width_var
        )

        self.combo_row(
            left,
            "Floors",
            self.floors_var,
            ["1", "2", "3"]
        )

        self.combo_row(
            left,
            "Bedrooms",
            self.bedrooms_var,
            ["1", "2", "3", "4", "5", "6"]
        )

        self.combo_row(
            left,
            "Bathrooms",
            self.bathrooms_var,
            ["1", "2", "3", "4", "5"]
        )

        # Right

        right = tk.Frame(
            body,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        right.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(7, 0)
        )

        tk.Label(
            right,
            text="HOME REQUIREMENTS",
            font=("Segoe UI", 10, "bold"),
            bg=WHITE,
            fg=PURPLE
        ).pack(
            anchor="w",
            padx=18,
            pady=(13, 7)
        )

        self.style_var = tk.StringVar(
            value=self.design["style"]
        )

        tk.Label(
            right,
            text="Architecture Style",
            font=("Segoe UI", 8, "bold"),
            bg=WHITE,
            fg=TEXT
        ).pack(
            anchor="w",
            padx=18
        )

        style_frame = tk.Frame(
            right,
            bg=WHITE
        )

        style_frame.pack(
            fill="x",
            padx=18,
            pady=5
        )

        for name, color in [
            ("Modern", BLUE),
            ("Traditional", TEAL),
            ("Luxury", PURPLE)
        ]:

            tk.Radiobutton(
                style_frame,
                text=name,
                variable=self.style_var,
                value=name,
                font=("Segoe UI", 8, "bold"),
                bg=WHITE,
                fg=color,
                activebackground=WHITE,
                selectcolor=WHITE
            ).pack(
                side="left",
                padx=(0, 8)
            )

        tk.Label(
            right,
            text="Features",
            font=("Segoe UI", 8, "bold"),
            bg=WHITE,
            fg=TEXT
        ).pack(
            anchor="w",
            padx=18
        )

        self.kitchen_var = tk.BooleanVar(
            value=self.design["kitchen"]
        )

        self.parking_var = tk.BooleanVar(
            value=self.design["parking"]
        )

        self.garden_var = tk.BooleanVar(
            value=self.design["garden"]
        )

        self.balcony_var = tk.BooleanVar(
            value=self.design["balcony"]
        )

        for text, variable in [
            ("Kitchen", self.kitchen_var),
            ("Parking", self.parking_var),
            ("Garden", self.garden_var),
            ("Balcony", self.balcony_var)
        ]:

            tk.Checkbutton(
                right,
                text=text,
                variable=variable,
                font=("Segoe UI", 8),
                bg=WHITE,
                fg=TEXT,
                activebackground=WHITE,
                selectcolor=WHITE
            ).pack(
                anchor="w",
                padx=18
            )

        tk.Button(
            right,
            text="GENERATE AI HOME DESIGN",
            command=self.generate_design,
            font=("Segoe UI", 10, "bold"),
            bg=BLUE,
            fg=WHITE,
            activebackground="#1D4ED8",
            relief="flat",
            bd=0,
            pady=10,
            cursor="hand2"
        ).pack(
            fill="x",
            padx=18,
            pady=8
        )

    # ========================================================
    # INPUT
    # ========================================================

    def input_row(
        self,
        parent,
        label,
        variable
    ):

        row = tk.Frame(
            parent,
            bg=WHITE
        )

        row.pack(
            fill="x",
            padx=18,
            pady=3
        )

        tk.Label(
            row,
            text=label,
            font=("Segoe UI", 8),
            bg=WHITE,
            fg=MUTED,
            width=17,
            anchor="w"
        ).pack(
            side="left"
        )

        tk.Entry(
            row,
            textvariable=variable,
            font=("Segoe UI", 9),
            bg="#F8FAFC",
            fg=TEXT,
            relief="flat",
            width=15
        ).pack(
            side="right",
            ipady=5
        )

    # ========================================================
    # COMBO
    # ========================================================

    def combo_row(
        self,
        parent,
        label,
        variable,
        values
    ):

        row = tk.Frame(
            parent,
            bg=WHITE
        )

        row.pack(
            fill="x",
            padx=18,
            pady=3
        )

        tk.Label(
            row,
            text=label,
            font=("Segoe UI", 8),
            bg=WHITE,
            fg=MUTED,
            width=17,
            anchor="w"
        ).pack(
            side="left"
        )

        ttk.Combobox(
            row,
            textvariable=variable,
            values=values,
            state="readonly",
            width=13
        ).pack(
            side="right",
            ipady=3
        )

    # ========================================================
    # GENERATE DESIGN
    # ========================================================

    def generate_design(self):

        try:

            length = float(
                self.length_var.get()
            )

            width = float(
                self.width_var.get()
            )

            if length <= 0 or width <= 0:
                raise ValueError

            self.design["length"] = length
            self.design["width"] = width

            self.design["floors"] = int(
                self.floors_var.get()
            )

            self.design["bedrooms"] = int(
                self.bedrooms_var.get()
            )

            self.design["bathrooms"] = int(
                self.bathrooms_var.get()
            )

            self.design["style"] = (
                self.style_var.get()
            )

            self.design["kitchen"] = (
                self.kitchen_var.get()
            )

            self.design["parking"] = (
                self.parking_var.get()
            )

            self.design["garden"] = (
                self.garden_var.get()
            )

            self.design["balcony"] = (
                self.balcony_var.get()
            )

            messagebox.showinfo(
                "AI Design Generated",
                "Your AI home design has been generated successfully."
            )

            self.show_dashboard()

        except:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid plot dimensions."
            )

    # ========================================================
    # 2D FLOOR PLAN
    # ========================================================

    def show_floor_plan(self):

        self.clear()

        self.header("2D PLAN")

        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            fill="both",
            expand=True,
            padx=22,
            pady=12
        )

        tk.Label(
            main,
            text="2D FLOOR PLAN",
            font=("Segoe UI", 20, "bold"),
            bg=BG,
            fg=TEXT
        ).pack(
            anchor="w"
        )

        tk.Label(
            main,
            text="AI generated room arrangement",
            font=("Segoe UI", 9),
            bg=BG,
            fg=MUTED
        ).pack(
            anchor="w",
            pady=(2, 7)
        )

        card = tk.Frame(
            main,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="both",
            expand=True
        )

        canvas = tk.Canvas(
            card,
            bg="#F8FAFC",
            highlightthickness=0
        )

        canvas.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

        self.draw_floor_plan(
            canvas
        )

        buttons = tk.Frame(
            main,
            bg=BG
        )

        buttons.pack(
            fill="x",
            pady=(7, 0)
        )

        tk.Button(
            buttons,
            text="← BACK TO HOME",
            command=self.show_dashboard,
            font=("Segoe UI", 9, "bold"),
            bg=WHITE,
            fg=TEXT,
            relief="flat",
            bd=0,
            padx=15,
            pady=7
        ).pack(
            side="left"
        )

        tk.Button(
            buttons,
            text="OPEN 3D VISUALIZATION →",
            command=self.show_visualization,
            font=("Segoe UI", 9, "bold"),
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            bd=0,
            padx=15,
            pady=7
        ).pack(
            side="right"
        )

    # ========================================================
    # DRAW FLOOR PLAN
    # ========================================================

    def draw_floor_plan(
        self,
        canvas
    ):

        x = 60
        y = 18

        w = 680
        h = 330

        canvas.create_rectangle(
            x,
            y,
            x + w,
            y + h,
            fill="#E0F2FE",
            outline=NAVY,
            width=4
        )

        rooms = [
            (
                x,
                y,
                x + 245,
                y + 155,
                "LIVING ROOM",
                "#DBEAFE",
                BLUE
            ),
            (
                x + 245,
                y,
                x + 435,
                y + 155,
                "KITCHEN",
                "#CCFBF1",
                TEAL
            ),
            (
                x,
                y + 155,
                x + 245,
                y + h,
                "BEDROOM 1",
                "#EDE9FE",
                PURPLE
            ),
            (
                x + 245,
                y + 155,
                x + 435,
                y + h,
                "BEDROOM 2",
                "#FEF3C7",
                ORANGE
            ),
            (
                x + 435,
                y,
                x + w,
                y + 105,
                "BATHROOM",
                "#DCFCE7",
                GREEN
            ),
            (
                x + 435,
                y + 105,
                x + w,
                y + 205,
                "ENTRY",
                "#F1F5F9",
                MUTED
            )
        ]

        for (
            x1,
            y1,
            x2,
            y2,
            name,
            fill,
            outline
        ) in rooms:

            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill=fill,
                outline=outline,
                width=2
            )

            canvas.create_text(
                (x1 + x2) / 2,
                (y1 + y2) / 2,
                text=name,
                font=("Segoe UI", 9, "bold"),
                fill=TEXT
            )

        if self.design["parking"]:

            canvas.create_rectangle(
                x + 435,
                y + 205,
                x + w,
                y + h,
                fill="#E2E8F0",
                outline=MUTED,
                width=2
            )

            canvas.create_text(
                x + 555,
                y + 267,
                text="PARKING",
                font=("Segoe UI", 10, "bold"),
                fill=TEXT
            )

    # ========================================================
    # VISUALIZATION
    # ========================================================

    def show_visualization(self):

        self.clear()

        # Top bar

        top = tk.Frame(
            self.root,
            bg=NAVY,
            height=60
        )

        top.pack(
            fill="x"
        )

        top.pack_propagate(False)

        tk.Button(
            top,
            text="← BACK TO HOME",
            command=self.show_dashboard,
            font=("Segoe UI", 9, "bold"),
            bg=BLUE,
            fg=WHITE,
            activebackground="#3B82F6",
            relief="flat",
            bd=0,
            padx=14,
            pady=7,
            cursor="hand2"
        ).pack(
            side="left",
            padx=14,
            pady=11
        )

        tk.Label(
            top,
            text="3D HOME VISUALIZATION",
            font=("Segoe UI", 15, "bold"),
            bg=NAVY,
            fg=WHITE
        ).pack(
            side="left",
            padx=12
        )

        tk.Button(
            top,
            text="RESET VIEW",
            command=self.reset_visualization,
            font=("Segoe UI", 8, "bold"),
            bg="#334155",
            fg=WHITE,
            relief="flat",
            bd=0,
            padx=12,
            pady=7
        ).pack(
            side="right",
            padx=14
        )

        # Mode bar

        mode = tk.Frame(
            self.root,
            bg=BG,
            height=60
        )

        mode.pack(
            fill="x"
        )

        mode.pack_propagate(False)

        tk.Label(
            mode,
            text="VIEW",
            font=("Segoe UI", 8, "bold"),
            bg=BG,
            fg=MUTED
        ).pack(
            side="left",
            padx=(18, 7)
        )

        tk.Button(
            mode,
            text="EXTERIOR",
            command=self.draw_exterior_view,
            font=("Segoe UI", 9, "bold"),
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            bd=0,
            padx=17,
            pady=7,
            cursor="hand2"
        ).pack(
            side="left",
            padx=3
        )

        tk.Button(
            mode,
            text="INTERIOR",
            command=self.draw_interior_view,
            font=("Segoe UI", 9, "bold"),
            bg=PURPLE,
            fg=WHITE,
            relief="flat",
            bd=0,
            padx=17,
            pady=7,
            cursor="hand2"
        ).pack(
            side="left",
            padx=3
        )

        tk.Label(
            mode,
            text="ROOM",
            font=("Segoe UI", 8, "bold"),
            bg=BG,
            fg=MUTED
        ).pack(
            side="left",
            padx=(20, 6)
        )

        for i, room in enumerate(self.rooms):

            tk.Button(
                mode,
                text=room.title(),
                command=lambda index=i:
                    self.select_room(index),
                font=("Segoe UI", 8, "bold"),
                bg=WHITE,
                fg=TEXT,
                relief="flat",
                bd=0,
                padx=6,
                pady=6,
                cursor="hand2"
            ).pack(
                side="left",
                padx=2
            )

        self.visual_canvas = tk.Canvas(
            self.root,
            bg="#DDE8F5",
            highlightthickness=0
        )

        self.visual_canvas.pack(
            fill="both",
            expand=True,
            padx=14,
            pady=(0, 10)
        )

        self.draw_exterior_view()

    # ========================================================
    # RESET VIEW
    # ========================================================

    def reset_visualization(self):

        self.current_room = 0

        self.draw_exterior_view()

    # ========================================================
    # SELECT ROOM
    # ========================================================

    def select_room(self, index):

        self.current_room = index

        self.draw_interior_view()

    # ========================================================
    # EXTERIOR
    # ========================================================

    def draw_exterior_view(self):

        canvas = self.visual_canvas

        canvas.delete("all")

        # Sky

        canvas.create_rectangle(
            0,
            0,
            900,
            270,
            fill="#BFE3FF",
            outline=""
        )

        # Clouds

        self.cloud(
            canvas,
            100,
            65
        )

        self.cloud(
            canvas,
            650,
            55
        )

        # Ground

        canvas.create_rectangle(
            0,
            270,
            900,
            450,
            fill="#A7D49B",
            outline=""
        )

        # Road

        canvas.create_rectangle(
            650,
            270,
            900,
            450,
            fill="#555B65",
            outline=""
        )

        # House

        wall = self.house_wall_color()

        canvas.create_polygon(
            205,
            260,
            205,
            120,
            530,
            120,
            635,
            180,
            635,
            260,
            fill=wall,
            outline=NAVY,
            width=3
        )

        # Second floor

        if self.design["floors"] >= 2:

            canvas.create_rectangle(
                275,
                62,
                560,
                155,
                fill=wall,
                outline=NAVY,
                width=3
            )

        # Roof

        canvas.create_polygon(
            175,
            120,
            365,
            22,
            600,
            120,
            fill="#334155",
            outline=NAVY,
            width=3
        )

        # Door

        canvas.create_rectangle(
            382,
            180,
            445,
            260,
            fill="#5B3A29",
            outline="#3B2418",
            width=3
        )

        canvas.create_oval(
            430,
            218,
            437,
            225,
            fill=ORANGE,
            outline=""
        )

        # Windows

        self.window(
            canvas,
            245,
            165
        )

        self.window(
            canvas,
            495,
            165
        )

        if self.design["floors"] >= 2:

            self.window(
                canvas,
                325,
                82
            )

            self.window(
                canvas,
                475,
                82
            )

        # Balcony

        if self.design["balcony"]:

            canvas.create_rectangle(
                320,
                140,
                470,
                180,
                fill="#64748B",
                outline=NAVY,
                width=2
            )

            for x in range(
                330,
                470,
                15
            ):

                canvas.create_line(
                    x,
                    140,
                    x,
                    180,
                    fill=WHITE,
                    width=2
                )

        # Garden

        if self.design["garden"]:

            self.tree(
                canvas,
                100,
                290
            )

            self.tree(
                canvas,
                165,
                310
            )

            self.tree(
                canvas,
                800,
                285
            )

        # Parking

        if self.design["parking"]:

            canvas.create_rectangle(
                650,
                280,
                850,
                380,
                fill="#4B5563",
                outline=""
            )

            self.car(
                canvas,
                680,
                310
            )

        # Label

        canvas.create_rectangle(
            290,
            385,
            610,
            425,
            fill=NAVY,
            outline=""
        )

        canvas.create_text(
            450,
            405,
            text="EXTERIOR HOME VIEW",
            font=("Segoe UI", 13, "bold"),
            fill=WHITE
        )

    # ========================================================
    # INTERIOR
    # ========================================================

    def draw_interior_view(self):

        canvas = self.visual_canvas

        canvas.delete("all")

        room = self.rooms[
            self.current_room
        ]

        # Back wall

        canvas.create_polygon(
            185,
            110,
            680,
            110,
            680,
            350,
            185,
            350,
            fill="#EEF2F7",
            outline="#CBD5E1",
            width=3
        )

        # Left wall

        canvas.create_polygon(
            100,
            35,
            185,
            110,
            185,
            350,
            100,
            430,
            fill="#DCE6F2",
            outline="#CBD5E1",
            width=2
        )

        # Right wall

        canvas.create_polygon(
            765,
            35,
            680,
            110,
            680,
            350,
            765,
            430,
            fill="#D6E0EC",
            outline="#CBD5E1",
            width=2
        )

        # Ceiling

        canvas.create_polygon(
            100,
            35,
            765,
            35,
            680,
            110,
            185,
            110,
            fill="#F8FAFC",
            outline="#CBD5E1",
            width=2
        )

        # Floor

        canvas.create_polygon(
            100,
            430,
            765,
            430,
            680,
            350,
            185,
            350,
            fill="#B89572",
            outline="#967250",
            width=2
        )

        # Ceiling lamp

        canvas.create_oval(
            410,
            55,
            470,
            78,
            fill="#FFF7B2",
            outline="#EAB308",
            width=2
        )

        # Room content

        if room == "LIVING ROOM":
            self.draw_living_room(canvas)

        elif room == "BEDROOM":
            self.draw_bedroom(canvas)

        elif room == "KITCHEN":
            self.draw_kitchen(canvas)

        elif room == "BATHROOM":
            self.draw_bathroom(canvas)

        # Room title

        canvas.create_rectangle(
            20,
            18,
            250,
            62,
            fill=NAVY,
            outline=""
        )

        canvas.create_text(
            135,
            40,
            text=room,
            font=("Segoe UI", 12, "bold"),
            fill=WHITE
        )

        # Navigation

        canvas.create_rectangle(
            30,
            375,
            115,
            420,
            fill=WHITE,
            outline=BORDER
        )

        canvas.create_text(
            72,
            397,
            text="← PREV",
            font=("Segoe UI", 9, "bold"),
            fill=BLUE
        )

        canvas.create_rectangle(
            745,
            375,
            850,
            420,
            fill=WHITE,
            outline=BORDER
        )

        canvas.create_text(
            797,
            397,
            text="NEXT →",
            font=("Segoe UI", 9, "bold"),
            fill=PURPLE
        )

        # Mouse navigation

        canvas.bind(
            "<Button-1>",
            self.interior_click
        )

    # ========================================================
    # INTERIOR CLICK
    # ========================================================

    def interior_click(self, event):

        if event.x < 130:

            self.current_room = (
                self.current_room - 1
            ) % len(self.rooms)

            self.draw_interior_view()

        elif event.x > 735:

            self.current_room = (
                self.current_room + 1
            ) % len(self.rooms)

            self.draw_interior_view()

    # ========================================================
    # LIVING ROOM
    # ========================================================

    def draw_living_room(self, canvas):

        # TV

        canvas.create_rectangle(
            390,
            145,
            565,
            255,
            fill="#263238",
            outline="#111827",
            width=3
        )

        canvas.create_rectangle(
            405,
            160,
            550,
            235,
            fill="#111827",
            outline="#60A5FA",
            width=2
        )

        # TV stand

        canvas.create_rectangle(
            370,
            250,
            585,
            272,
            fill="#5B3A29",
            outline=""
        )

        # Sofa

        canvas.create_rectangle(
            235,
            250,
            395,
            325,
            fill="#2563EB",
            outline="#1E3A8A",
            width=3
        )

        canvas.create_rectangle(
            225,
            220,
            405,
            275,
            fill="#3B82F6",
            outline="#1E3A8A",
            width=3
        )

        # Cushions

        canvas.create_oval(
            245,
            232,
            290,
            265,
            fill="#93C5FD",
            outline=""
        )

        canvas.create_oval(
            335,
            232,
            380,
            265,
            fill="#93C5FD",
            outline=""
        )

        # Table

        canvas.create_polygon(
            400,
            300,
            530,
            300,
            560,
            335,
            370,
            335,
            fill="#8B5E3C",
            outline="#5B3A29",
            width=2
        )

        # Window

        self.large_window(
            canvas,
            220,
            125,
            125,
            85
        )

        # Plant

        self.plant(
            canvas,
            615,
            280
        )

    # ========================================================
    # BEDROOM
    # ========================================================

    def draw_bedroom(self, canvas):

        # Headboard

        canvas.create_rectangle(
            290,
            140,
            555,
            265,
            fill="#475569",
            outline="#334155",
            width=3
        )

        # Bed

        canvas.create_polygon(
            270,
            260,
            570,
            260,
            615,
            330,
            230,
            330,
            fill="#E5E7EB",
            outline="#64748B",
            width=3
        )

        # Blanket

        canvas.create_polygon(
            390,
            260,
            570,
            260,
            602,
            320,
            390,
            320,
            fill="#93C5FD",
            outline=""
        )

        # Pillows

        canvas.create_oval(
            285,
            270,
            350,
            302,
            fill=WHITE,
            outline="#CBD5E1"
        )

        canvas.create_oval(
            350,
            270,
            415,
            302,
            fill=WHITE,
            outline="#CBD5E1"
        )

        # Wardrobe

        canvas.create_rectangle(
            580,
            135,
            660,
            300,
            fill="#7C4A2D",
            outline="#4B2E1E",
            width=3
        )

        canvas.create_line(
            620,
            135,
            620,
            300,
            fill="#B88964",
            width=2
        )

        # Side table

        canvas.create_rectangle(
            195,
            275,
            265,
            320,
            fill="#8B5E3C",
            outline=""
        )

        # Lamp

        canvas.create_rectangle(
            225,
            245,
            230,
            275,
            fill="#334155",
            outline=""
        )

        canvas.create_polygon(
            210,
            245,
            245,
            245,
            238,
            230,
            218,
            230,
            fill="#FDE68A",
            outline=""
        )

        # Window

        self.large_window(
            canvas,
            210,
            120,
            105,
            85
        )

    # ========================================================
    # KITCHEN
    # ========================================================

    def draw_kitchen(self, canvas):

        # Cabinets

        canvas.create_rectangle(
            205,
            135,
            660,
            220,
            fill="#334155",
            outline="#1E293B",
            width=3
        )

        for x in [
            250,
            325,
            400,
            475,
            550,
            620
        ]:

            canvas.create_line(
                x,
                135,
                x,
                220,
                fill="#94A3B8",
                width=2
            )

        # Counter

        canvas.create_rectangle(
            195,
            220,
            670,
            270,
            fill="#9CA3AF",
            outline="#475569",
            width=3
        )

        # Sink

        canvas.create_rectangle(
            330,
            232,
            420,
            258,
            fill="#DDE8F5",
            outline="#64748B",
            width=2
        )

        # Island

        canvas.create_polygon(
            300,
            285,
            545,
            285,
            585,
            335,
            265,
            335,
            fill="#CBD5E1",
            outline="#64748B",
            width=2
        )

        # Chairs

        for x in [
            280,
            530
        ]:

            canvas.create_rectangle(
                x,
                330,
                x + 35,
                360,
                fill="#475569",
                outline=""
            )

        # Window

        self.large_window(
            canvas,
            230,
            85,
            125,
            85
        )

    # ========================================================
    # BATHROOM
    # ========================================================

    def draw_bathroom(self, canvas):

        # Tiles

        for x in range(
            185,
            681,
            45
        ):

            canvas.create_line(
                x,
                110,
                x,
                350,
                fill="#CBD5E1"
            )

        for y in range(
            110,
            351,
            45
        ):

            canvas.create_line(
                185,
                y,
                680,
                y,
                fill="#CBD5E1"
            )

        # Mirror

        canvas.create_rectangle(
            220,
            135,
            350,
            220,
            fill="#BDE3F4",
            outline="#64748B",
            width=3
        )

        # Sink

        canvas.create_rectangle(
            230,
            230,
            350,
            285,
            fill="#F8FAFC",
            outline="#64748B",
            width=3
        )

        # Faucet

        canvas.create_arc(
            270,
            210,
            315,
            250,
            start=180,
            extent=180,
            style="arc",
            outline="#475569",
            width=3
        )

        # Bathtub

        canvas.create_oval(
            400,
            220,
            625,
            325,
            fill="#F8FAFC",
            outline="#64748B",
            width=3
        )

        # Toilet

        canvas.create_oval(
            575,
            135,
            650,
            220,
            fill=WHITE,
            outline="#64748B",
            width=3
        )

        canvas.create_rectangle(
            585,
            125,
            640,
            170,
            fill=WHITE,
            outline="#64748B",
            width=2
        )

    # ========================================================
    # WINDOW
    # ========================================================

    def window(
        self,
        canvas,
        x,
        y
    ):

        canvas.create_rectangle(
            x,
            y,
            x + 65,
            y + 55,
            fill="#7DD3FC",
            outline="#1E3A8A",
            width=3
        )

        canvas.create_line(
            x + 32,
            y,
            x + 32,
            y + 55,
            fill=WHITE,
            width=2
        )

        canvas.create_line(
            x,
            y + 27,
            x + 65,
            y + 27,
            fill=WHITE,
            width=2
        )

    # ========================================================
    # LARGE WINDOW
    # ========================================================

    def large_window(
        self,
        canvas,
        x,
        y,
        w,
        h
    ):

        canvas.create_rectangle(
            x,
            y,
            x + w,
            y + h,
            fill="#9BDCF5",
            outline="#2563EB",
            width=4
        )

        canvas.create_line(
            x + w / 2,
            y,
            x + w / 2,
            y + h,
            fill=WHITE,
            width=3
        )

        canvas.create_line(
            x,
            y + h / 2,
            x + w,
            y + h / 2,
            fill=WHITE,
            width=3
        )

    # ========================================================
    # CLOUD
    # ========================================================

    def cloud(
        self,
        canvas,
        x,
        y
    ):

        canvas.create_oval(
            x,
            y + 15,
            x + 70,
            y + 50,
            fill=WHITE,
            outline=""
        )

        canvas.create_oval(
            x + 25,
            y,
            x + 85,
            y + 50,
            fill=WHITE,
            outline=""
        )

        canvas.create_oval(
            x + 55,
            y + 15,
            x + 115,
            y + 50,
            fill=WHITE,
            outline=""
        )

    # ========================================================
    # TREE
    # ========================================================

    def tree(
        self,
        canvas,
        x,
        y
    ):

        canvas.create_rectangle(
            x - 6,
            y,
            x + 6,
            y + 42,
            fill="#7C4A2D",
            outline=""
        )

        canvas.create_oval(
            x - 32,
            y - 38,
            x + 5,
            y + 5,
            fill="#15803D",
            outline=""
        )

        canvas.create_oval(
            x - 5,
            y - 50,
            x + 35,
            y + 5,
            fill="#16A34A",
            outline=""
        )

    # ========================================================
    # PLANT
    # ========================================================

    def plant(
        self,
        canvas,
        x,
        y
    ):

        canvas.create_rectangle(
            x - 12,
            y,
            x + 12,
            y + 30,
            fill="#A16207",
            outline=""
        )

        canvas.create_oval(
            x - 35,
            y - 45,
            x,
            y - 5,
            fill="#16A34A",
            outline=""
        )

        canvas.create_oval(
            x,
            y - 50,
            x + 35,
            y - 5,
            fill="#22C55E",
            outline=""
        )

    # ========================================================
    # CAR
    # ========================================================

    def car(
        self,
        canvas,
        x,
        y
    ):

        canvas.create_rectangle(
            x,
            y,
            x + 120,
            y + 38,
            fill="#2563EB",
            outline=NAVY,
            width=2
        )

        canvas.create_polygon(
            x + 22,
            y,
            x + 48,
            y - 25,
            x + 90,
            y - 25,
            x + 112,
            y,
            fill="#60A5FA",
            outline=NAVY
        )

        canvas.create_oval(
            x + 15,
            y + 27,
            x + 38,
            y + 50,
            fill="#111827",
            outline=""
        )

        canvas.create_oval(
            x + 85,
            y + 27,
            x + 108,
            y + 50,
            fill="#111827",
            outline=""
        )

    # ========================================================
    # WALL COLOR
    # ========================================================

    def house_wall_color(self):

        if self.design["style"] == "Luxury":
            return "#E7D7B8"

        if self.design["style"] == "Traditional":
            return "#C99168"

        return "#DCE5EE"

    # ========================================================
    # COST PAGE
    # ========================================================

    def show_cost(self):

        self.clear()

        self.header("COST")

        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            fill="both",
            expand=True,
            padx=22,
            pady=18
        )

        tk.Label(
            main,
            text="PROJECT COST ESTIMATE",
            font=("Segoe UI", 20, "bold"),
            bg=BG,
            fg=TEXT
        ).pack(
            anchor="w"
        )

        total = tk.Frame(
            main,
            bg=NAVY,
            height=125
        )

        total.pack(
            fill="x",
            pady=12
        )

        total.pack_propagate(False)

        tk.Label(
            total,
            text="ESTIMATED CONSTRUCTION COST",
            font=("Segoe UI", 10, "bold"),
            bg=NAVY,
            fg="#BFDBFE"
        ).pack(
            pady=(20, 3)
        )

        tk.Label(
            total,
            text=self.money(self.cost()),
            font=("Segoe UI", 26, "bold"),
            bg=NAVY,
            fg=WHITE
        ).pack()

        row = tk.Frame(
            main,
            bg=BG
        )

        row.pack(
            fill="x"
        )

        self.cost_card(
            row,
            "PLOT AREA",
            f"{self.plot_area():,.0f} sq.ft",
            BLUE
        )

        self.cost_card(
            row,
            "BUILT-UP AREA",
            f"{self.built_up():,.0f} sq.ft",
            TEAL
        )

        self.cost_card(
            row,
            "STYLE",
            self.design["style"],
            PURPLE
        )

        self.cost_card(
            row,
            "FLOORS",
            str(self.design["floors"]),
            ORANGE
        )

        tk.Button(
            main,
            text="← BACK TO HOME",
            command=self.show_dashboard,
            font=("Segoe UI", 9, "bold"),
            bg=WHITE,
            fg=TEXT,
            relief="flat",
            bd=0,
            padx=15,
            pady=8
        ).pack(
            anchor="w",
            pady=15
        )

    # ========================================================
    # COST CARD
    # ========================================================

    def cost_card(
        self,
        parent,
        title,
        value,
        color
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            height=80,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=4
        )

        card.pack_propagate(False)

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 8, "bold"),
            bg=WHITE,
            fg=MUTED
        ).pack(
            pady=(14, 2)
        )

        tk.Label(
            card,
            text=value,
            font=("Segoe UI", 12, "bold"),
            bg=WHITE,
            fg=color
        ).pack()

    # ========================================================
    # SUMMARY
    # ========================================================

    def show_summary(self):

        self.clear()

        self.header("SUMMARY")

        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            fill="both",
            expand=True,
            padx=22,
            pady=15
        )

        tk.Label(
            main,
            text="DESIGN SUMMARY",
            font=("Segoe UI", 20, "bold"),
            bg=BG,
            fg=TEXT
        ).pack(
            anchor="w"
        )

        card = tk.Frame(
            main,
            bg=WHITE,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="both",
            expand=True,
            pady=10
        )

        left = tk.Frame(
            card,
            bg=WHITE
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        data = [
            (
                "Plot Size",
                f"{self.design['length']} × "
                f"{self.design['width']} ft"
            ),
            (
                "Plot Area",
                f"{self.plot_area():,.0f} sq.ft"
            ),
            (
                "Floors",
                str(self.design["floors"])
            ),
            (
                "Bedrooms",
                str(self.design["bedrooms"])
            ),
            (
                "Bathrooms",
                str(self.design["bathrooms"])
            ),
            (
                "Architecture",
                self.design["style"]
            ),
            (
                "Built-up Area",
                f"{self.built_up():,.0f} sq.ft"
            )
        ]

        for title, value in data:

            row = tk.Frame(
                left,
                bg=WHITE
            )

            row.pack(
                fill="x",
                pady=4
            )

            tk.Label(
                row,
                text=title,
                font=("Segoe UI", 9),
                bg=WHITE,
                fg=MUTED,
                width=18,
                anchor="w"
            ).pack(
                side="left"
            )

            tk.Label(
                row,
                text=value,
                font=("Segoe UI", 9, "bold"),
                bg=WHITE,
                fg=TEXT
            ).pack(
                side="left"
            )

        right = tk.Frame(
            card,
            bg="#F8FAFC",
            width=270
        )

        right.pack(
            side="right",
            fill="y"
        )

        right.pack_propagate(False)

        tk.Label(
            right,
            text="AI DESIGN TYPE",
            font=("Segoe UI", 8, "bold"),
            bg="#F8FAFC",
            fg=MUTED
        ).pack(
            pady=(35, 5)
        )

        tk.Label(
            right,
            text=self.ai_type(),
            font=("Segoe UI", 16, "bold"),
            bg="#F8FAFC",
            fg=BLUE,
            wraplength=220
        ).pack()

        tk.Label(
            right,
            text="Estimated Cost",
            font=("Segoe UI", 9),
            bg="#F8FAFC",
            fg=MUTED
        ).pack(
            pady=(22, 3)
        )

        tk.Label(
            right,
            text=self.money(self.cost()),
            font=("Segoe UI", 18, "bold"),
            bg="#F8FAFC",
            fg=GREEN
        ).pack()

        tk.Button(
            right,
            text="OPEN INTERIOR",
            command=self.show_visualization,
            font=("Segoe UI", 9, "bold"),
            bg=PURPLE,
            fg=WHITE,
            relief="flat",
            bd=0,
            padx=20,
            pady=9,
            cursor="hand2"
        ).pack(
            pady=22
        )

    # ========================================================
    # CALCULATIONS
    # ========================================================

    def plot_area(self):

        return (
            self.design["length"]
            *
            self.design["width"]
        )

    def built_up(self):

        return (
            self.plot_area()
            *
            0.78
            *
            self.design["floors"]
        )

    def cost(self):

        rates = {
            "Modern": 2200,
            "Traditional": 1900,
            "Luxury": 3000
        }

        rate = rates.get(
            self.design["style"],
            2200
        )

        return (
            self.built_up()
            *
            rate
        )

    def money(self, amount):

        if amount >= 10000000:

            return (
                f"₹ {amount / 10000000:.2f} Cr"
            )

        if amount >= 100000:

            return (
                f"₹ {amount / 100000:.2f} L"
            )

        return (
            f"₹ {amount:,.0f}"
        )

    def ai_type(self):

        area = self.plot_area()

        if area < 800:

            return "Compact Smart Home"

        elif area < 1500:

            return "Modern Family Home"

        elif area < 2500:

            return "Spacious Premium Home"

        return "Luxury Large Residence"


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = AIHomeDesignGenerator(
        root
    )

    root.mainloop()