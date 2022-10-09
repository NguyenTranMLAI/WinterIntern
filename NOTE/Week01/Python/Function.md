# PYTHON FUCTIONS

Trong Python, một hàm là một nhóm các câu lệnh có liên quan với nhau để thực hiện một tác vụ cụ thể.

Các hàm giúp chia nhỏ chương trình thành các phần nhỏ hơn và theo mô-đun. Khi chương trình càng phát triển lớn hơn, các chức năng làm cho nó có tổ chức và dễ quản lý hơn.

Hơn nữa, nó tránh lặp lại và làm cho mã có thể được sử dụng lại.

### CÚ PHÁP

```python
def function_name(parameters):
    """docstring"""
    statement(s)
    (return)
```

+ *def* đánh đấu sự bắt đầu của tiêu đề hàm
+ Tên hàm là tên duy nhất. Tuân theo quy tắc của Python.
+ Các tham số để truyền các giá trị cho một hàm.
+ Dấu ":" để đánh dấu phần cuối tiêu đề hàm.
+ Docstring để mô tả hoạt động của hàm.
+ Thân hàm là một hoặc chuỗi nhiều câu lệnh. Các câu lệnh phải có cùng mức thụt lề.
+ Return là tùy chọn để trả về giá trị của hàm.

```python
def greet(name):
    """
    This function greets to 
    person passed in as 
    a parameter
    """
    print("Hello, " + name + ". Good morning")
```

### GỌI HÀM

Khi chúng ta đã định nghĩa một hàm, chúng ta có thể gọi nó từ một hàm, chương trình khác hoặc thậm chí là dấu nhắc Python. Để gọi một hàm, chúng ta chỉ cần gõ tên hàm với các tham số thích hợp.

```python
>> greet("Paul")
Hello, Paul. Good morning
```

### DOCSTRING

Chuỗi đầu tiên sau tiêu đề hàm được gọi là docstring và là viết tắt của chuỗi tài liệu. Nó được sử dụng ngắn gọn để giải thích những gì một chức năng làm.

Để xem docstring:

```python
>> print(greet.__doc__)
This function greets to
the person passed in as
a parameter
```

### RETURN

Câu *return* lệnh được sử dụng để thoát khỏi một hàm và quay trở lại vị trí mà nó được gọi.

```python
reurn [expression_list]
```

Câu lệnh này có thể chứa một biểu thức được đánh giá hoặc giá trị được trả về. Nếu không có biểu thức nào trong câu lệnh hoặc *return* bản thân câu lệnh không có bên trong một hàm, thì hàm sẽ trả về *None* đối tượng.

```python
>> print(greet("May))
Hello, May. Good morning!
None
```

### HOẠT ĐỘNG CỦA HÀM TRONG PYTHON

![ActiveFunction](https://cdn.programiz.com/sites/tutorial2program/files/python-how-function-works_1.jpg)

### PHẠM VI VÀ THỜI GIAN TỒN TẠI CỦA BIẾN

Phạm vi của một biến là một phần của chương trình mà biến được nhận dạng. Các tham số và biến được xác định bên trong một hàm không được nhìn thấy từ bên ngoài hàm. Do đó, chúng có phạm vi cục bộ.

Thời gian tồn tại của một biến là khoảng thời gian mà biến tồn tại trong bộ nhớ. Thời gian tồn tại của các biến bên trong một hàm miễn là hàm thực thi.

Chúng sẽ bị phá hủy khi chúng ta quay trở lại từ hàm. Do đó, một hàm không nhớ giá trị của một biến từ các lần gọi trước của nó.

## PYTHON FUNCTION ARGUMENTS

### ARGUMENT

```python
def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")
```

Ở đây, hàm greet()có hai tham số.

Vì chúng tôi đã gọi hàm này với hai đối số nên nó chạy trơn tru và chúng tôi không gặp bất kỳ lỗi nào.

Nếu chúng ta gọi nó với một số đối số khác, trình thông dịch sẽ hiển thị thông báo lỗi. Dưới đây là lệnh gọi hàm này với một và không có đối số cùng với các thông báo lỗi tương ứng của chúng.

```python
>>> greet("Monica")    # only one argument
TypeError: greet() missing 1 required positional argument: 'msg'
```

### VARIABLE FUNCTION ARGUMENTS

các hàm có một số đối số cố định. Trong Python, có nhiều cách khác để định nghĩa một hàm có thể nhận số lượng đối số thay đổi.

#### DEFAULT ARGUMENTS

Các đối số của hàm có thể có giá trị mặc định trong Python.

Chúng ta có thể cung cấp giá trị mặc định cho một đối số bằng cách sử dụng toán tử gán *=*.

```python
def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")

# Output:
Hello Kate, Good morning!
Hello Bruce, How do you do?
```

#### KEYWORD ARGUMENTS

Khi chúng ta gọi một hàm với một số giá trị, các giá trị này sẽ được gán cho các đối số theo vị trí của chúng.

Python cho phép các hàm được gọi bằng cách sử dụng các đối số từ khóa. Khi chúng ta gọi các hàm theo cách này, thứ tự (vị trí) của các đối số có thể bị thay đổi. Các lệnh gọi sau đến hàm trên đều hợp lệ và tạo ra cùng một kết quả.

```python
# 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Bruce") 

1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?")           
```

#### ARBITRARY ARGUMENTS

Đôi khi, chúng ta không biết trước số lượng đối số sẽ được truyền vào một hàm. Python cho phép chúng ta xử lý loại tình huống này thông qua các lệnh gọi hàm với số lượng đối số tùy ý.

+ *args:
    - args đại diện cho danh sách (dạng list)
    - nhận tất cả tham số truyền vào theo dạng đối số

+ **kwargs:
    - kwargs (keyword argument) đại diện cho danh sách các [key-val] (dictionary)
    - nhận tất cả các tham số truyền vào theo dạng tường minh

```python
def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")

# Output:
Xin chào Monica
Xin chào Luke
xin chào Steve
chào John
```

## RECURSION

Đệ quy là quá trình xác định một cái gì đó về mặt chính nó.

Một hàm có thể gọi các hàm khác. Nó thậm chí có thể cho chức năng gọi chính nó. Các loại cấu trúc này được gọi là các hàm đệ quy.

![RecursiveFunction](https://cdn.programiz.com/cdn/farfuture/6i17bRQT6hWIqw9JE5rMMyW527g7It_68T7kSzpIplo/mtime:1591262415/sites/tutorial2program/files/python-recursion-function.png)

Đệ quy kết thúc khi số lượng giảm xuống 1. Đây được gọi là điều kiện cơ sở.

Mọi hàm đệ quy phải có một điều kiện cơ sở để dừng đệ quy hoặc nếu không hàm gọi chính nó vô hạn.

## LAMBDA FUNCTION

Một hàm ẩn danh là một hàm được định nghĩa mà không có tên.

Trong khi các hàm bình thường được định nghĩa bằng cách sử dụng *def* từ khóa trong Python, các hàm ẩn danh được xác định bằng cách sử dụng *lambda* từ khóa.

```python
lambda arguments: expression
```

Các hàm lambda có thể có bất kỳ số lượng đối số nào nhưng chỉ có một biểu thức. Biểu thức được đánh giá và trả về. Các hàm Lambda có thể được sử dụng ở bất cứ nơi nào yêu cầu các đối tượng hàm.

## GLOBAL, LOCAL AND NONLOCAL VARIABLES

### GLOBAL VARIABLES

Một biến được khai báo bên ngoài hàm hoặc trong phạm vi toàn cục được gọi là biến toàn cục. Điều này có nghĩa là một biến toàn cục có thể được truy cập bên trong hoặc bên ngoài hàm.

```python
x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)

# Output:
x inside: global
x outside: global
```

### LOCAL VARIABLES

Một biến được khai báo bên trong thân của hàm hoặc trong phạm vi cục bộ được gọi là biến cục bộ.

```python
def foo():
    y = "local"


foo()
print(y)

# Output:
NameError: name 'y' is not defined
```

### GLOBAL AND LOCAL VARIABLES

```python
x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()

# Output:
global global 
local
```

```python
x = 5

def foo():
    x = 10
    print("local x:", x)


foo()
print("global x:", x)

# Output:
local x: 10
global x: 5
```

### NONLOCAL VARIABLES

Các biến phi địa phương được sử dụng trong các hàm lồng nhau có phạm vi cục bộ không được xác định. Điều này có nghĩa là biến không thể nằm trong phạm vi cục bộ hoặc toàn cục.

```python
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

# Output:
inner: nonlocal
outer: nonlocal
```
