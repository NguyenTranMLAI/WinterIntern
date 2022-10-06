# LOOP IN PYTHON

## FOR LOOP

### VÒNG LẶP FOR TRONG PYTHON LÀ GÌ?

Vòng lặp for trong Python được sử dụng để lặp qua một chuỗi ( danh sách , tuple , chuỗi ) hoặc các đối tượng có thể lặp lại khác. Lặp lại trên một trình tự được gọi là duyệt.

### cÚ PHÁP CỦA VÒNG LẶP fOR

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

Trong vòng lặp *while*, *expr* sẽ đ