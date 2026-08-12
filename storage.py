import json
def save_tasks(tasks_list):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks_list, file, indent=4, ensure_ascii=False)

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            tasks_list = json.load(file)
            return tasks_list


    except FileNotFoundError:
        return[]    
    except json.JSONDecodeError:
        return[]