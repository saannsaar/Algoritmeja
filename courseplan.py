class CoursePlan:
    def __init__(self):
        self.verkko = {}

    def add_course(self, course):
        self.verkko[course] = []

    def add_requisite(self, course1, course2):
        self.verkko[course1].append(course2)

    def find_order(self):
        self.onkoSykli = False
        self.kayty = {}  
        self.vastaus = []

        for solmu in self.verkko:
            if solmu not in self.kayty:
                self.apufunkt(solmu)

        if self.onkoSykli or any(x not in self.vastaus for x in self.verkko):
            return None

        return list(reversed(self.vastaus))

    def apufunkt(self, solmu):
        self.kayty[solmu] = False  
        for viereinen in self.verkko[solmu]:
            if viereinen not in self.kayty:
                self.apufunkt(viereinen)
            elif self.kayty[viereinen] is False:
                self.onkoSykli = True
                return

        self.kayty[solmu] = True  
        self.vastaus.append(solmu)


if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe", "Ohja")
    c.add_requisite("Ohja", "Tira")
    c.add_requisite("Jym", "Tira")
    print(c.find_order())  # Output: ['Ohpe', 'Jym', 'Ohja', 'Tira']

    c.add_requisite("Tira", "Tira")
    print(c.find_order())  # Output: None (cycle detected)
