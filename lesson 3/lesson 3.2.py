def data(**kwargs):
    return kwargs


print(data(name=input('Enter name'), surname=input('Enter surname'),
           birth_year=input('Enter birthday'), city=input('Enter city'), email=input('Enter email'),
           phone=input('Enter phone number')))
