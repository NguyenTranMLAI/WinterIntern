# LOOP IN PYTHON

## FOR LOOP

### VÒNG LẶP FOR TRONG PYTHON LÀ GÌ?

Vòng lặp for trong Python được sử dụng để lặp qua một chuỗi ( danh sách , tuple , chuỗi ) hoặc các đối tượng có thể lặp lại khác. Lặp lại trên một trình tự được gọi là duyệt.

### CÚ PHÁP CỦA VÒNG LẶP fOR

```markdown
for val in sequence:
    loop body
```

*val* là biến nhận giá trị của mục bên trong chuỗi trên mỗi lần lặp

Vòng lặp tiếp tục cho đến khi đến mục cuối cùng trong chuỗi. Phần thân của vòng lặp FOR được phân tích khỏi phần còn lại của mã bằng cách sử dụng thụt đầu dòng.

### LƯU ĐỒ

![DiagramFOR](https://cdn.programiz.com/sites/tutorial2program/files/forLoop.jpg)

Vd:

```markdown
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0

for val in numbers:
    sum = sum+val

print("The sum is", sum)

# Output:  The sum is 48
```

### HÀM RANGE()

Chúng ta có thể tạo ra một dãy số bằng cách sử dụng *range()* hàm.

Cú pháp:

```markdown
range(start, stop, step_size)
```

*start* là điểm bắt đầu, *stop*-1 là điểm kết thúc và *step_size* là bước nhảy

Vd:

```markdown
print(range(10))
# Output: range(0, 10)

print(list(range(10)))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(2, 8)))
# Output: [2, 3, 4, 5, 6, 7]

print(list(range(2, 10)))
# Output: [2, 3, 4, 5, 6, 7, 8]
```

### FOR LOOP VỚI ELSE

Một vòng lặp *for* cũng có thể có một khối tùy chọn *else*. Phần *else* được thực thi nếu các mục trong trình tự được sử dụng trong vòng lặp *for* hết.

Vd:

``` markdown
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

# Output:
0
1
5
No items left
```

## WHILE LOOP

### VÒNG LẶP WHILE TRONG PYTHON LÀ GÌ?

Vòng lặp while trong Python được sử dụng để lặp qua một khối mã miễn là biểu thức kiểm tra (điều kiện) là đúng.

### CÚ PHÁP

```python
while <expr>:
    <statements>
```

Trong vòng lặp *while*, *expr* sẽ được kiểm tra đầu tiên, *statement* sẽ được thực thi nếu kiểm tra là đúng. Sau mỗi lần *statment* được thực thi, thì sẽ kiểm tra lại *expr*. Quá trình này lặp lại liên tục cho đến khi *expr* kiểm tra sai.

![DiagramWhiel](https://cdn.programiz.com/sites/tutorial2program/files/whileLoopFlowchart.jpg)

### VÒNG LẶP WHILE VỚI ELSE

```python
while <expr>:
    <statement>
else:
    <statement>
```

*statement* tron phần *else* được thực thi nếu điều kiện vòng lặp while là sai.

```python
counter = 0

while counter < 3:
    print("Inside_loop")
    counter = counter + 1
else:
    print("Inside_else")

# Output:
Inside_loop
Inside_loop
Inside_loop
Inside_else
```

## BREAK - CONTINUE

Trong Python, câu lệnh *break* và *continue* có thể thay đổi luồng của một vòng lặp bình thường.

Các vòng lặp lặp lại trên một khối mã cho đến khi biểu thức kiểm tra là sai, nhưng đôi khi chúng ta muốn kết thúc lặp lại hiện tại hoặc thậm chí toàn bộ vòng lặp mà không cần kiểm tra biểu thức kiểm tra.

Các  câu lệnh *break* và *continue* được sử dụng trong những trường hợp này.

### BREAK

Câu lệnh *break* kết thúc vòng lặp chứa nó. Điều khiển chương trình chuyến đến câu lệnh nga sau phần thân của vòng lặp.

Nếu câu lệnh *break* nằm trong một vòng lặp lồng nhau (vòng lặp bên trong một vòng lặp khác), câu lệnh *break* sẽ kết thúc vòng lặp trong cùng.

![DiagramBreak](https://cdn.programiz.com/sites/tutorial2program/files/flowchart-break-statement.jpg)

Hoạt động của câu lệnh *break* tron vòng lặp for và while:

![ActiveBreak](https://cdn.programiz.com/sites/tutorial2program/files/how-break-statement-works.jpg)

### CONTINUE

Câu lệnh *continue* được sử dụng để bỏ qua phần còn lại của mã bên trong vòng lặp chỉ cho lần lặp hiện tại. Vòng lặp không kết thúc nhưng tiếp tục với lần lặp tiếp theo.

![DiagramContinue](https://cdn.programiz.com/sites/tutorial2program/files/continue-statement-flowchart.jpg)

Hoạt động của câu lệnh *continue*:

![ActiveContinue](https://cdn.programiz.com/sites/tutorial2program/files/how-continue-statment-works.jpg)

## PASS STATEMENT

Trong lập trình Python, câu lệnh *pass* là một câu lệnh null. Sự khác biệt giữa một nhận xét và một câu lệnh *pass* trong Python là trong khi trình thông dịch hoàn toàn bỏ qua một nhận xét, *pass* thì không bị bỏ qua.

Tuy nhiên, không có gì xảy ra khi *pass* được thực hiện. Nó dẫn đến không hoạt động.

```python
pass
```

