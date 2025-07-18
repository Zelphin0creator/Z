import re

class Colors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'

class ZTerminal:
    def __init__(self):
        self.lines = []
        self.variables = {}

    def run(self):
        print(f"{Colors.OKGREEN}🧡 /Z\\ Terminal v1.1 — Logic, Loops, do(), Variables, and in!() Input Enabled")
        print("Type 'exit' to quit. Write multiple lines and type 'play' to run them.\n")

        while True:
            user_input = input("   $ ").strip()
            if user_input == 'exit':
                break
            elif user_input == 'play':
                self.execute_lines()
            elif user_input == 'cls':
                self.lines.clear()
                print("\033c", end='')  # Clear screen
            else:
                self.lines.append(user_input)

    def execute_lines(self):
        i = 0
        while i < len(self.lines):
            line = self.lines[i]
            if line.startswith('//') or 'TTP' in line:
                i += 1
                continue
            elif line.startswith('say:'):
                self.say_command(line[4:].strip())
            elif line.startswith('^@set'):
                self.set_variable(line)
            elif line.startswith('L00p/'):
                self.parse_l00p(line)
            elif line.startswith('Lpf'):
                self.parse_lpf()
            elif line.startswith('L('):
                self.parse_L_loop(line)
            elif line.startswith('do'):
                i += 1
                continue
            else:
                print("Unknown or invalid Zelphin command.")
            i += 1

    def say_command(self, message):
        for var in re.findall(r'{(.*?)}', message):
            message = message.replace(f'{{{var}}}', self.variables.get(var, f'{{{var}}}'))
        print(message)

    def set_variable(self, line):
        match = re.match(r'\^@set\((\w+)\)\s*=\s*(.+)', line)
        if not match:
            print("Invalid set command.")
            return
        var_name, value = match.groups()
        if value.startswith('in!(') and value.endswith(')'):
            prompt = value[4:-1]
            self.variables[var_name] = input(prompt + " ")
        else:
            self.variables[var_name] = value

    def parse_l00p(self, line):
        match = re.match(r'L00p/(\d+)/(.*)', line)
        if match:
            count, content = int(match.group(1)), match.group(2)
            for _ in range(count):
                self.say_command(content)

    def parse_lpf(self):
        print("Lpf loop (3x):")
        for _ in range(3):
            self.say_command("Looping with Lpf")

    def parse_L_loop(self, line):
        match = re.match(r'L\((.+),\s*(\d+)\)', line)
        if match:
            content, count = match.groups()
            count = int(count)
            if content.startswith('say:'):
                msg = content[4:].strip()
                for _ in range(count):
                    self.say_command(msg)
            elif content.startswith('L('):
                for _ in range(count):
                    self.parse_L_loop(content)

ZTerminal().run()   