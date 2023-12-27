#Intuitive idea of async programming- Similar scenario can be used to monitor lp pools on Univswap V2/V3

#Port this to pools monitoring scripts

import asyncio

async def cook_dish(name, time):
    print(f"Start cooking {name}")
    await asyncio.sleep(time)
    print(f"{name} is ready")

async def main():
    # Create tasks for different dishes
    dish1 = cook_dish("Pasta", 3)
    dish2 = cook_dish("Steak", 5)
    dish3 = cook_dish("Salad", 2)

    # Start the event loop to coordinate the tasks
    await asyncio.gather(dish1, dish2, dish3)

# Run the main function
asyncio.run(main())
