# CONDITION STATEMENT

Câu lệnh có điều kiện trong Python thực hiện các tính toán hoặc hành động khác nhau tùy thuộc vào việc một ràng buộc Boolean cụ thể đánh giá là đúng hay sai. Các câu lệnh điều kiện được xử lý bởi các câu lệnh IF trong Python.

## CÂU LỆNH IF TRONG PYTHON LÀ GÌ?

Python if Statement được sử dụng cho các hoạt động ra quyết định. Nó chứa phần nội dung mã chỉ chạy khi điều kiện được đưa ra trong câu lệnh if là đúng.

### LOẠI CÂU LỆNH *IF* ĐƠN GIẢN NHẤT

```markdown
if <expr>:
    <statement>
```

Trong hình thức hiển thị ở trên:

+ *expr* là một biểu thức được đánh giá trong ngữ cảnh Boolean.
+ *statement* là một câu lệnh Python hợp lệ, câu lệnh này phải được thụt lề.

Nếu *expr* được đánh giá một giá trị là True, thì *statement* được thực thi. Nếu *expr* được đánh giá một giá trị là False, thì *statement* sẽ bị bỏ qua và không được thực thi.

```markdown
x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

# Output: yes


if y < x:                            # Falsy
    print('yes')

# Output:


if x:                                # Falsy
    print('yes')

# Output:


if y:                                # Truthy
    print('yes')

# Output: yes


if x or y:                           # Truthy
    print('yes')

# Output: yes


if x and y:                          # Falsy
    print('yes')

# Output:


if 'aul' in 'grault':                # Truthy
    print('yes')

# Output: yes


if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')

# Output: 
```

### GROUPING STATEMENTS

Giả sử bạn muốn đánh giá một điều kiện và sau đó làm nhiều hơn một điều nếu điều đó là đúng:

```markdown
Nếu thời tiết đẹp, tôi sẽ:
    + Cắt cỏ
    + Loại bỏ các vườn
    + Dắt chó đi dạo

(Nếu thời tiết không đẹp, thì tôi sẽ không làm bất kỳ điều gì trong số này.)
```

Python tuân theo một quy ước được gọi là quy tắc ngoài lề, các câu lệnh liền kề được thụt vào cùng một mức được coi là một phần của cùng một khối.

Câu lệnh compound IF:

```markdown
if <expr>:
    <statement>
    <statement>
    ...
    <statement>
<following_statement>
```

Chương trình sẽ được thực thi như sau:
![CompoundIF](https://files.realpython.com/media/t.78f3bacaa261.png)

Vd:

```markdown
# Exemple 1
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

# Output: 
After conditional


# Exemple 2
if 'foo' in ['foo', 'bar', 'baz']:
    print('Outer condition is true')

    if 10 > 20:
        print('Inner condition 1')

    print('Between inner conditions')

    if 10 < 20:
        print('Inner condition 2')

    print('End of outer condition')
print('After outer condition')

# Output: 
Outer condition is true   
Between inner conditions
Inner condition 2
End of outer condition
After outer condition
```

### CÂU LỆNH *IF ... ELSE*

```markdown
if <expr>:
    <statement(s)>
else:
    <statement(s)>
```

Nếu *expr* đúng, bộ đầu tiên được thực thi và bộ thứ hai bị bỏ qua. Nếu *expr* sai, bộ thứ nhất sẽ bị bỏ qua và bộ thứ hai được thực thi.
![IlElse](https://st.quantrimang.com/photos/image/2017/10/13/Python-if-else-so-do.jpg)

Vd:

```markdown
# Exemple 1
x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

# Output: 
(first suite)
x is small


# Exemple 2
x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

# Output: 
(second suite)
x is large
```

### CÂU LỆNH *IF ... ELIF ... ELSE*

```markdown
if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
    ...
else:
    <statement(s)>
```

![IfElif](https://st.quantrimang.com/photos/image/2017/10/13/Python-if-elif-else-so-do.jpg)

Vd:

```markdown
name = 'Joe'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Joe':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

# Output: 
Hello Joe
```

### CÂU LỆNH *IF* MỘT DÒNG

```markdown
if <expr>: <statement>
```

```markdown
if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
```

Có hai cách giải thích:

+ Nếu *expr* đúng, hãy thực thi *statement_1*.

    Sau đó, thực hiện *statement_2* ... *statement_n* vô điều kiện, không phân biệt có *expr* đúng hay không.
+ Nếu *expr* đúng, hãy thực thi tất cả *statement_1* ... *statement_n*. Nếu không, đừng thực thi bất kỳ cái nào trong số chúng.

```markdown
# Exemple 1
if 'f' in 'foo': print('1'); print('2')
# Output:
1
2
3


if 'z' in 'foo': print('1'); print('2')
# Output:


# Exemple 2
x = 2
if x == 1: print('foo'); print('bar')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')
# Output:
qux
quux


# Exemple 3
x = 3
if x == 1: print('foo'); print('bar')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')
# Output:
corge
grault
```

### BIỂU THỨC CÓ ĐIỀU KIỆN

```markdown
<expr1> if <conditional_expr> else <expr2>
```

*conditional_expr* được đánh giá đầu tiên. Nếu đúng, biểu thức đánh giá là *expr1*. Nếu nó sai, biểu thức đánh giá là *expr2*.

Vd:

```markdown
# Exemple 1
raining = False
print("Let's go to the", 'beach' if not raining else 'library')
# Output: Let's go to the beach


# Exemple 2
raining = True
print("Let's go to the", 'beach' if not raining else 'library')
# Output: Let's go to the library


# Exemple 3
age = 12
s = 'minor' if age < 21 else 'adult'
print(s)
# Output: minor


# Exemple 4
'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
# Output: no


# Exemple 5
x = 2
s = ('foo' if (x == 1) else
     'bar' if (x == 2) else
     'baz' if (x == 3) else
     'qux' if (x == 4) else
     'quux'
     )
print(s)
# Output: bar
```

### CÂU LỆNH *PASS*

Nó được sử dụng như một trình giữ chỗ để giữ cho trình biên dịch không báo lỗi trong bất kỳ tình huống nào mà một câu lệnh được yêu cầu về mặt cú pháp, nhưng bạn không thực sự muốn làm bất cứ điều gì:

```markdown
if True:
    pass
print('Pass Statement')

# Output: Pass Statement
```
