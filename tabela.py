class Tabela:
    def __init__(self, subject: str, include_first_row = True):
        self.subject = subject
        self.columns = []
        self.rows = []
        self.include_first_row = include_first_row

    def create(self):
        print("─"*30)
        for i, _ in enumerate(self.rows):
            print("\n", end="")
            for j, w in enumerate(self.columns):
                detail = "│" if j + 1 == len(self.columns) else ""
                if i == 0 and j == 0 and self.include_first_row:
                    print(f"│ {w} {detail}", end="")
                else:
                    
                    print(f"│ {w} {detail}", end="")
            
t = Tabela("")
t.columns.append("Título")
t.columns.append(2)
t.columns.append(3)
t.columns.append(4)

t.rows.append(1)
t.rows.append(2)
t.rows.append(3)
t.rows.append(4)

t.create()