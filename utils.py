def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value: 
            return value
        
        print("пожалуйста прпробуйте еще раз:")