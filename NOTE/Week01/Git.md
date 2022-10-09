# GIT CƠ BẢN

+ Khái niệm:
  + Git là một trong những Hệ thống Quản lý Phiên bản Phân tán, được phát triển nhằm quản lý mã nguồn (source code) hữu hiệu.
  + Git lưu lại trạng thái của file khi có nhu cầu dưới dạng lịch sử cập nhật => nên có thể đưa file đã chỉnh sửa về trạng thái cũ hoặc hiển thị sự khác biệt giữa các trạng thái của file.
+ Ưu điểm:
  + Hệ thống được tất cả các trạng thái của file sau khi sửa/cập nhập khi có yêu cầu.
  + Giải quyết được vấn đề ghi đè/mất nội dung khi file được làm việc trong nhóm.
+ Respository: nơi ghi lại trạng thái (lịch sử thay đổi của nội dung) của thư mục và file.<br>
  + Remote respository: là repository để chia sẻ  giữa nhiều người và bố trí trên server chuyên dụng. Thông qua remote repository có thể lấy về nội dung công việc của người khác.
  + Local respository: là repository bố trí trên máy tính cá nhân cho một người sử dụng. Có thể chia sẻ nội dung công việc đã làm bằng cách upload lên remote respository.
  + Tạo local repository bằng cách:
    + Tạo repository mới

        ```markdown
        git init git_example
        ```

    + Clone remote repository

+ Commit: là thao tác ghi lại việc thêm/thay đổi file/thư mục vào repository. Khi commit, trong repository sẽ tạo ra commit đã ghi lại sự khác biệt từ trạng thái đã commit lần trước đến trạng thái hiện tại.<br>
![alt](https://backlog.com/git-tutorial/vn/img/post/intro/capture_intro1_3_1.png)<br>
Các commit được đặt tên bằng 40 ký tự alphabet, nên muốn chỉ định commit thì chỉ cần chỉ định tên này.<br>
Khi thực hiện commit sẽ yêu cầu nhập commit message (bắt buộc và không để trống).<br>
Nên nhập commit message như sau:

    ```markdown
    Dòng thứ 1: Tóm tặt nội dung thay đổi trong commit
    Dòng thứ 2: ‘trống’
    Dòng thứ 3 trở đi: Lý do thay đã thay đổi
    ```

+ Working Tree và Index:
![alt](https://backlog.com/git-tutorial/vn/img/post/intro/capture_intro1_4_1.png)<br>
  + Working tree là những thư mục được đặt trong sự quản lý của Git.<br>
  + Index là nơi ở giữa repository và working tree.<br>
  + Khi commit, repository sẽ ghi lại trạng thái đã được thiết lập của index, vì thế để ghi lại trạng thái của file bằng commit thì trước hết cần đăng ký file trong index.
<br>
<br>
<br>

# CHIA SẺ RESPOSITORY

+ Push: là thao tác upload lịch sử thay đổi trong local respository lên remote repository, và lịch sử thay đổi của remote repository sẽ có trạng thái giống với local repository.<br>
![alt](https://backlog.com/git-tutorial/vn/img/post/intro/capture_intro3_1_1.png)<br>
+ Clone remote repository:
  + Nếu có remote repository chứa lịch sử thay đổi của ai đó, thì sẽ có thể sao chép toàn bộ repository và bản thân có thể thao tác trên phần công việc đó.
  + Clone: là sao chép remote repository. Khi thực hiện clone, sẽ tải về toàn bộ nội dung của remote repository và tạo thành local repository ở máy.<br>

![alt](https://backlog.com/git-tutorial/vn/img/post/intro/capture_intro3_3_1.png)<br>

+ Pull từ remote repository:
  + Khi chia sẽ remote repository và nhiều người cũng thực hiện công việc, thì mọi người sẽ push lên remote repository. Khi đó cần lấy nội dung thay đổi mà người khác đã push lên.
  + Pull: là cập nhập local repository từ remote repository. Khi thực hiện pull, sẽ tải lịch sử thay đổi mới nhất từ remote repository về và đưa vào local repository của máy cá nhân.<br>
<br>
<br>
<br>

# MERGE LỊCH SỬ THAY ĐỔI

Trong khoảng thời gian sau khi pull lần cuối cho đến khi push lần tiếp theo, mà có người khác push rồi cập nhập remote repository, thì push của mình sẽ bị từ chối vì những thay đổi mà người khác đã push sẽ bị mất.
![alt](https://backlog.com/git-tutorial/vn/img/post/intro/capture_intro5_1_1.png)<br>
Trong trường hợp này phải thực hiện merge rồi tiếp nhận thay đổi của phần lịch sử khác. Bằng cách merge, Git sẽ tích hợp tự động chỗ thay đổi.<br>
Tuy nhiên vẫn có trường hợp Git không thể tích hợp tự động được, đó là trường hợp đã thay đổi ở nơi giống nhau trong file trên remote repository và local repository.<br>
Những nơi phát sinh xung đột, Git sẽ chỉnh sửa nội dung file giống như sơ đồ bên dưới, nên cần phải chỉnh sửa bằng tay.<br>
![alt](https://backlog.com/git-tutorial/vn/img/post/intro/capture_intro5_1_3.png)<br>

        Phần phía trên mà đã được chia ra bằng == là local repository, phía dưới được hiển thị là nội dung chỉnh sửa của remote repository.
Giống như sơ đồ tiếp theo, sau khi chỉnh sửa tất cả chỗ xung đột, nếu như tiến hành commit thì commit đã tích hợp thay đổi sẽ được tạo ra.
![alt](https://backlog.com/git-tutorial/vn/img/post/intro/capture_intro5_1_4.png)
