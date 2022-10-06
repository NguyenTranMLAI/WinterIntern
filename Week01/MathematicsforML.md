# MATHEMATICS FOR MACHINE LEARNING

## THE RELATIONSHIP BETWEEN MACHINE LEARNING, LINEAR ALGEBRA, AND VECTOR AND MATRICES

Ung dung cua Dai so tuyen tinh:

- Bieu dien cac gia tri (dac trung) cua mot du lieu
- Tong quat hoa tap cac phep toan de tim ra cach giai quyet van de nay trong truong hop tong quat
- Mo ta gan chinh xac (tong quat) cho tap du lieu phuc tap cho mot cai nhin hinh dung de hieu

## A VECTOR IS

- a list of numbers: Các vectơ thường được máy tính xem như một danh sách có thứ tự các số mà chúng có thể thực hiện các phép toán – một số hoạt động rất tự nhiên và như chúng ra sẽ thấy.
- position in three dimensions of space and in one dimension of the time: một vectơ trong không-thời gian có thể được mô tả bằng cách sử dụng 3 chiều không gian và 1 chiều thời gian theo một hệ tọa độ nào đó.
- something which moves in a space of fitting parameters: vectơ có thể được xem như một danh sách các số mô tả một số vấn đề tối ưu hóa.

## OPERATION WITH VECTOR

Cho các vectơ: $u = (uj, ui); v = (vj, vi); t = (tj, ti)$

- Cộng 2 vectơ: $u+v = v+u = (uj+vj, ui+vi)$
- Trừ vectơ: $-u = (-uj,ui); u-v = (uj-vj, ui-vi)$
- Nhân một số với vectơ: $a.u = a.(uj, ui) = (auj, aui)$
- Norm: $|u| = \sqrt{uj^2 - ui^2}$
- Tích vô hướng: $u.v = v.u = uj.vj + ui.vi$
- Góc giữa 2 vectơ: $\alpha = {argcos[(u.v) \over (|u|.|v|)]}$<br>
Chứng minh: $(u-v)^2 = |u|^2 + |v|^2 - 2.|u|.|v|.cos(\alpha)$<br>
=> $(u-v).(u-v) = |u|^2 + |v|^2 - 2.|u|.|v|.cos(\alpha)$<br>
=> $|u|^2 + |v|^2 - 2.u.v = |u|^2 + |v|^2 - 2.|u|.|v|.cos(\alpha)$<br>
=> $u.v = |u|.|v|.cos(\alpha)$
- Hình chiếu vô hướng: $u.v = |u|.|v|.cos(\alpha)$<br>
=> $|v|.cos(\alpha) = {u.v \over |u|}$<br>
![alt](https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Projection_and_rejection.png/200px-Projection_and_rejection.png)
- $Hình chiếu vectơ = {r.s \over |r|}.{r \over |r|}$

## CƠ SỞ

### CƠ SỞ CỦA KHÔNG GIAN VECTƠ

Trong không gian Rn mỗi hệ gồm n véctơ {P1,P2,...,Pn} độc lập tuyến tính được gọi là một cơ sở của không gian Rn.

Ví dụ: Hệ gồm 2 vectơ P1 = (1,2), P2 = (-2, 1) là một cơ sở của không gian $R^2$ vì P1, P2 độc lập tuyến tính do không tỉ lệ.

### TỌA ĐỘ CỦA MỘT VECTƠ ĐỐI VỚI MỘT CƠ SỞ

Giả sử hệ vectơ P1, P2, ..., Pn là một cơ sở của $R^n$. Khi đó mọi vectơ X thuộc $R^n$ đều được biểu diễn tuyến tính một cách duy nhất qua hệ vecto P1, P2, ..., Pn tức luôn tồn tại duy nhất n số thực $\alpha1, \alpha2, ..., \alpha n$ sao cho X = $P1\alpha1 +  P2\alpha2, ..., Pn\alpha n$.

Bộ số ($\alpha1, \alpha2, ..., \alpha n$) được gọi là tọa độ của vectơ X trong cơ sở {P1, P2, ..., Pn}.

Ta đã biết rằng ($\alpha1, \alpha2, ..., \alpha n$) là nghiệm của hệ tuyến tính có ma trận hệ số mở rộng A_hat = (P1P2...PnX) trong đó P1, P2, ..., Pn, X viết dưới dạng cột.

