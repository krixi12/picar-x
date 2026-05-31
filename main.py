from control import control_main, control_init
from picarx import Picarx


class Main:
    px = None

    def main(self):
        self.main_init()
        control_init()
        while True:
            control_main(self.px)

    def main_init(self):
        self.px = Picarx()


if __name__ == "__main__":
    Main().main()
