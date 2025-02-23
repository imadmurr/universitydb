import tkinter as tk

from shared import theme


def create_card(parent, title, value):
    """Creates a card with a title and value"""
    card = tk.Frame(parent, bg=theme.CARD_COLOR, relief="flat", width=200, height=120)
    card.grid_propagate(False)  # Prevent the card from resizing to fit contents
    card.pack(side="left", padx=10, pady=10)

    title_label = tk.Label(card, text=title, font=("Arial", 14, "bold"), bg=theme.CARD_COLOR, fg=theme.SIDEBAR_COLOR)
    title_label.pack(pady=10)

    value_label = tk.Label(card, text=value, font=("Arial", 18, "bold"), bg=theme.CARD_COLOR, fg=theme.SIDEBAR_COLOR)
    value_label.pack(pady=5)