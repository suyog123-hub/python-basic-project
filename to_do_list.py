# Features: Add, View, Mark Complete, Delete
print('--'*2, "here is the lsit" ,'--'*2 )
to_do_list=[]
while True:
    print('''
    1---> add in the to do list
    2---> view the to do lsit
    3---> mark the completed task in the to do lsit
    4---> delete the to do list 
    5--->exit
          ''')
    choice=int(input("enter your choice from (1-4)"))
    if choice == 5:
        print("exiting...")
        break
    elif choice==1:
        add_items=input("enter the task you want to add in the to do list accordinf to time")
        to_do_list.append(add_items)
        print(f"'{add_items}' added successfully! in do to list")
        
    elif choice==2:
        for i in to_do_list:
            pass
        print(f"your to do lsit are{str(to_do_list)}")

    elif choice==3:
        user_mark=input("enter the task you have completed")
        if user_mark in to_do_list:
            print(f' congratulation!!!you have sucessfully completed you{user_mark} task')
            to_do_list.remove(user_mark)
            if  not to_do_list:
                    print(f' now you have no task to do right now')
            else:
                print(f'your remaining work  is{to_do_list}')

    elif choice ==4:
        user_delete=input("enter the task you want to delete from the to do lsist")
        if user_delete in to_do_list:
            to_do_list.remove(user_delete)
            print(f'{user_delete} sucessfully delete from your  to-do-list')
        else:
            print(" it is not availble in your to do list")

            

    

       
        


