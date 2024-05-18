from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('mrt_code_name.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city

def Write_to_file(country_name, city_name):
    with open('mrt_code_name.txt', 'a') as file:
        file.write('\n' +country_name +'/' +city_name)

print('Ask the Expert - Mrt stations of SG')
root = Tk()
root.withdraw()
the_world = {}
read_from_file()
while True:
    query_country = simpledialog.askstring('MRT', 'Type in a Mrt station code of SG:')
    if query_country in the_world:
        result= the_world[query_country]
        messagebox.showinfo('Answer', 'The name of ' + query_country +' is '+result+'!' )
    else:
        new_city = simpledialog.askstring('Teach me', 'I don\'t know!' + ' what is the name of ' + query_country +'?' )
        the_world[query_country] = new_city
        Write_to_file(query_country, new_city)