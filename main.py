
from menu import show_menu
from storage import save_tasks, load_tasks
from tasks import (show_tasks, add_task, edit_task, delete_task, toggle_task)  

def main():
   tasks_list = load_tasks()

   print("=" * 40)
   print("МЕНЕДЖЕР ЗАДАЧ")
   print("версия 1.2.0 - ветка expirement")
   print("=" * 40)


   while True:
    
       show_menu()

       choice = input("\nВыберите действие:").strip()

       if choice == "1":
           add_task(tasks_list)
           save_tasks(tasks_list)

       elif choice == "2":
           show_tasks(tasks_list)

       elif choice == "3":
           print("до свидания!")
           break

       elif choice == "4":
           print("раздел в разработке")

       elif choice == "5":
           print("Автор новичок, не ругайте его!")

       elif choice ==  "6":   
           toggled_task = toggle_task(tasks_list)

           if toggled_task:
               save_tasks(tasks_list)

       elif choice == "7":
           edited_task = edit_task(tasks_list)

           if edited_task:
               save_tasks(tasks_list)

       elif choice == "8":
           deleted_task = delete_task(tasks_list)

           if deleted_task:
               save_tasks(tasks_list)
               print(f'Удаленная задача: "{deleted_task["title"]}"')
             
       else:
           print("такой команды нет!")

if __name__ == "__main__":
    main()