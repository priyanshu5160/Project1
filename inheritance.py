class Animal:
    def speak(self):
        print("animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("dog barks")

dog = Dog()
dog.speak()