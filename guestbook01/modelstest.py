from guestbook01 import models



def test_findall():
    results=models.findall()
    for result in results:
        print(f'{result["no"]}:{result["name"]}:{result["reg_date"]}:{result["message"]}')

    print(results)

def test_insert():
    name='둘리'
    password='1234'
    message='호이~~~'

    result=models.insert(name,password,message)
    print(f'insert result: {result}')

def test_deleteby_no_and_password():
    no = 6
    password='1234'

    result=models.deleteby_no_and_password(no,password)
    print(f'delete result: {result}')

def main():
#    test_deleteby_no_and_password()
#    test_insert()
    test_findall()

if __name__=='__main__':
    main()