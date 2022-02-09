import asyncio, time

class Food:
    def __init__(self, name, calories, cooking_time):
        self.name = name
        self.calories = calories
        self.cooking_time = cooking_time

    def __str__(self):
        return f"{self.name} ({self.calories} cal)"

    async def prepare(self, n):
        batch = []
        while n > 0 : 
            print(f"Preparing {self.name} ...")
            await asyncio.sleep(self.cooking_time)
            print( f"{self.name} ready!")
            batch.append(self)
            n -= 1
        return batch

    

class Burger(Food):
    def __init__(self):
        super().__init__("🍔", 100, cooking_time=1)

class Salad(Food):
    def __init__(self):
        super().__init__("🥗", 20, 1.5)

class Pizza(Food):
    def __init__(self):
        super().__init__("🍕", 450, 2)

class FullMeal(Food):
    def __init__(self):
        super().__init__("🍽️", 800, 3.14159)

class Dog: 
    def __init__(self, name):
        self.name = name
        self.appetite = 2000
        # appetite means calories need

    def bark(self):
        print(f"{self.name} is barking")

    def __eating_speed(self):
        # The point is, the less appetite the dog has, the slower it will eat.
        t = - self.appetite * 0.001 + 2.5
        return t if t >= 0 else 0.5
        # t cannot be negative, because used in sleep() method !


    async def eat(self, food: Food):
        if self.isHungry():
            print(f"{self.name} is eating {food}...")
            await asyncio.sleep(self.__eating_speed())
            self.appetite -= food.calories
            print("That was delicious!")
        else:
            print(f"{self.name} is not hungry, refusing {food} :>")

    def info(self):
        print(f"{self.name} has {self.appetite} calories left")

    def isHungry(self):
        if self.appetite > 0:
            return True
        else:
            return False


async def main():    
    print(f"started at {time.strftime('%X')}")
    food_for_dog = []
    task  = asyncio.create_task(Burger().prepare(3))
    task2 = asyncio.create_task(Salad().prepare(2))
    task3 = asyncio.create_task(Pizza().prepare(2))
    task4 = asyncio.create_task(FullMeal().prepare(2))

    await task
    await task2
    await task3
    await task4

    print('all food is prepared. Time to feed doggo !')
    

    food_for_dog.extend(task.result())
    food_for_dog.extend(task2.result())
    food_for_dog.extend(task3.result())
    food_for_dog.extend(task4.result())

    zarra = Dog('🐶')
    zarra.bark()
    for food in food_for_dog:
        await zarra.eat(food)
        zarra.info()

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())