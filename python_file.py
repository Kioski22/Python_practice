# with open('sample_file' , 'w') as file:
#     file.writelines(['trying this file creation',
#                      '\n the second line should be this one' ,
#                        '\n this should be the third line'])


print("-----------------python file creation--------------")

def ask():
    while True:
        file_name = input('name of the file:  ') 
        user_input = input('what do you want to input: ')
        File_creation(file_name, user_input)
        return file_name, user_input


def File_creation(file_name , user_input):
    with open(f'{file_name}', 'w') as file:
        file.writelines([f'{user_input}'])


ask()


