# Вспомогательные функции (если нужно выделять слова, подсветка и т.д.)
def highlight_word(text, word, color="red"):
    return text.replace(word, f"<span style='color:{color}'>{word}</span>")
