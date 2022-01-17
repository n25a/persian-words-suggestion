from typing import List, Tuple
from rich.table import Table


class Suggerstor:
    class Rule:
        _types = {
            "contains",
            "not_contains",
            "set",
            "not_set",
        }
        def __init__(self, type: str, char: Tuple[str, List[str]], pos: int = None):
            if type in self._types:
                self.type = type
            else:
                raise ValueError("Invalid type")
            
            self.char = char
            self.pos = pos

    db: set = None
    rules: List[Rule] = []
    length: int = None

    def __init__(self):
        self.read_db()

    def read_db(self):
        with open("words/distinct_words.txt", "r") as file:
            self.db = set(file.read().strip().split("\n"))

    def set_length(self, length: int):
        self.length = length

    def contains(self, chars: List[str]):
        self.rules.append(
            self.Rule(
                type="contains",
                char=chars,
            )
        )

    def not_contains(self, chars: List[str]):
        self.rules.append(
            self.Rule(
                type="not_contains",
                char=chars,
            )
        )
    
    def set(self, char: str, position: int):
        self.rules.append(
            self.Rule(
                type="set",
                char=char,
                pos=position,
            )
        )
        
    def not_set(self, char: str, position: int):
        self.rules.append(
            self.Rule(
                type="not_set",
                char=char,
                pos=position,
            )
        )

    def show(self, data: List[str], console, clear):
        clear()
        table = Table(show_header=True, header_style="bold magenta")
        
        table.add_column("ID", style="dim", width=12)
        table.add_column("Word", )

        for i in range(len(data)):
            table.add_row(
                f"{i}", 
                f"{data[i]}",
            )

        console.print(table)

        input("Press enter to continue...")

    def suggest(self, console, clear):
        words = []

        for word in self.db:
            if len(word) == self.length:
                words.append(word)

        for rule in self.rules:
            if rule.type == "contains":
                new_words = []
                for word in words:
                    word_splited = list(word)
                    flag = True
                    for char in rule.char:
                        if char not in word_splited:
                            flag = False
                            break
                    if flag:
                        new_words.append(word)

                words = new_words

            elif rule.type == "not_contains":
                new_words = []
                for word in words:
                    word_splited = list(word)
                    flag = True
                    for char in rule.char:
                        if char in word_splited:
                            flag = False
                            break
                    if flag:
                        new_words.append(word)

                words = new_words

            elif rule.type == "set":
                new_words = []
                for word in words:
                    if word[rule.pos] == rule.char:
                        new_words.append(word)

                words = new_words

            elif rule.type == "not_set":
                new_words = []
                for word in words:
                    if word[rule.pos] != rule.char:
                        new_words.append(word)

                words = new_words

            else:
                raise ValueError("Invalid rule type")

        self.show(words, console, clear)
