task = {}

while True:
    tasks = input("Enter the task or write done to exit: ")
    if tasks.lower() in ["done", "exit"]:
        break
    priority = input("Set a priority (High/Medium/Low): ")
    task[tasks] = {"priority" : priority , "completed" : False } 

print("\n YOUR To-do list:")
for name, info in task.items():
    status = "Done" if info["completed"] else "Not - Done"
    print(f"{name}-{info['priority']} {status}")


while True:
    a = input("Enter the task you want to mark compelete or write the \"exit\" to finish: ")  
    if a == "exit":
        break
    if a in task:
      task[a]["completed"] = True
    else:
        print(f"{a} is not the in the to-do list")

print("\n📋 Final To-Do List:")
for name , info in task.items():
    status = "Done" if info["completed"] else "Not - Done"
    print(f"{name}-{info["completed"]} {status}")
