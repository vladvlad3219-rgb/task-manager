
from utils import get_non_empty_input

def show_tasks(tasks_list):

    if not tasks_list:
        print("задач пока нет.")
        return
    print("текущие задачи:")

    for i, task in enumerate(tasks_list, start=1):
        if task['done']:
            status = "\u2713"
        else:
            status = "\u2717"   
        print(f"{i}. {status} {task['title']}") 

def choose_task(tasks_list):
    while True:   
        try:
            mark = int(input("ВЫберите задачу:"))

            if mark < 1 or mark > len(tasks_list):
                print("такой задачи нет.")
                continue

            return mark - 1

        except ValueError:
            print("Ошибка, введите номер задачи:") 

def add_task(tasks_list):
    
    task = get_non_empty_input("Введите задачу:")
        

    new_task = {"title": task, "done": False}

    tasks_list.append(new_task)

    print("задача успешно добавлена!")

def edit_task(tasks_list):

    if not tasks_list:
        print("задач пока нет.")
        return
    print("Редактирование")
    
    show_tasks(tasks_list)
    
    index = choose_task(tasks_list)
                 
    task = tasks_list[index]
    old_title = task["title"]
    
    new_title = get_non_empty_input("введите новое название:")

    task["title"] = new_title
    print(f'задачa "{old_title}" успешо изменена на "{new_title}"!')
    return task


def delete_task(tasks_list):

    if not tasks_list:
        print("задач пока нет.")
        return
    print("Удаление задач")

    show_tasks(tasks_list)

    index = choose_task(tasks_list)

    deleted_task = tasks_list.pop(index)
    print(f'задача "{deleted_task["title"]}" успешно удалена!')
    return deleted_task


def toggle_task(tasks_list):

    if not tasks_list:
        print("задач пока нет.")
        return
    print("Изменение статуса задачи")

    show_tasks(tasks_list)

    index = choose_task(tasks_list)

    task = tasks_list[index]
    task["done"] = not task["done"]
    print("статус задачи изменен!")            
    return task

