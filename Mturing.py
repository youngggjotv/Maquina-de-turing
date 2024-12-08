class TuringMachine:
    def __init__(self, num_states, symbols, transitions, start_state, accept_state, reject_state):
        self.num_states = num_states
        self.symbols = symbols
        self.transitions = transitions
        self.state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.head = 0
        self.tape = []
    def initialize_tape(self, input_string):
        self.tape = list(input_string) + ['_']  # Espacio en blanco al final
        self.head = 0
        self.state = 0
    def step(self):
        current_symbol = self.tape[self.head]
        if (self.state, current_symbol) not in self.transitions:
            self.state = self.reject_state
            return False
        new_state, write_symbol, direction = self.transitions[(self.state, current_symbol)]
        self.tape[self.head] = write_symbol
        self.state = new_state
        if direction == 'R':
            self.head += 1
            if self.head == len(self.tape):  # Extiende la cinta si el cabezal supera el límite
                self.tape.append('_')
        elif direction == 'L':
            self.head = max(0, self.head - 1)
        return True
    def run(self):
        while self.state not in {self.accept_state, self.reject_state}:
            if not self.step():
                break
        return self.state == self.accept_state
def main():
    # Entrada según el ejemplo
    num_states = 4
    symbols = ['a', 'b', '_']
    transitions = {
        (0, 'a'): (1, '_', 'R'),
        (0, 'b'): (2, '_', 'R'),
        (0, '_'): (3, '_', 'N'),
        (1, 'a'): (1, 'a', 'R'),
        (1, 'b'): (1, 'b', 'R'),
        (1, '_'): (3, '_', 'L'),
        (2, 'a'): (2, 'a', 'R'),
        (2, 'b'): (2, 'b', 'R'),
        (2, '_'): (3, '_', 'L'),
    }
    # Estados
    start_state = 0
    accept_state = 3
    reject_state = -1
    # Cadenas de prueba
    input_strings = ["abaabb", "aaabb"]
    tm = TuringMachine(num_states, symbols, transitions, start_state, accept_state, reject_state)
    for i, string in enumerate(input_strings, 1):
        print(f"Caso {i}")
        print("Cadena de entrada:", string)
        tm.initialize_tape(string)
        print("Cinta inicial:", ''.join(tm.tape))
        result = tm.run()
        print("Cinta final:  ", ''.join(tm.tape))
        print("Posición del cabezal:", tm.head)
        print(f"La cadena {'es aceptada' if result else 'no es aceptada'}.\n")
if __name__ == "__main__":
    main()
