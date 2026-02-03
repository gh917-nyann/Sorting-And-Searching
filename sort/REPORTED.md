# BÁO CÁO KẾT QUẢ THỬ NGHIỆM
### Sinh viên thực hiện: Đỗ Gia Huy 
### MSSV: 25520681
### Lớp: ATTN2025
### Nội dung báo cáo:   
Báo cáo nhằm khảo sát, so sánh và đánh giá thời gian thực hiện của một số
thuật toán sắp xếp phổ biến dựa trên cùng một bộ dữ liệu.
#### I.	Kết quả thử nghiệm
   1.	Bảng thời gian thực hiện
<div align="center">

## Kết quả đo thời gian thực thi (ms)

| Dữ liệu | Quicksort | Heapsort | Mergesort | sort (C++) | sort (NumPy) |
|--------:|----------:|---------:|----------:|-----------:|-------------:|
| 1  | 708  | 3584 | 2315 | 134 | 55 |
| 2  | 670  | 3324 | 2063 | 89  | 45 |
| 3  | 1758 | 5540 | 3011 | 241 | 45 |
| 4  | 1788 | 5586 | 3032 | 233 | 43 |
| 5  | 1738 | 5585 | 3053 | 239 | 45 |
| 6  | 1813 | 5543 | 3038 | 246 | 44 |
| 7  | 1802 | 5546 | 3019 | 241 | 46 |
| 8  | 1778 | 5472 | 3156 | 237 | 43 |
| 9  | 1775 | 5360 | 2947 | 269 | 42 |
| 10 | 1723 | 5245 | 2949 | 239 | 44 |
| **Trung bình** | **1555.3** | **5018.5** | **2868.3** | **216.8** | **45.2** |
</div> 

   2.	Biểu đồ (cột) thời gian thực hiện  
    
   <img width="902" height="527" alt="image" src="https://github.com/user-attachments/assets/8bd46a83-706f-47ca-a220-61c00409249b" />

#### II.	Kết luận:
Theo kết quả thử nghiệm có thể thấy:
- Hàm sort của numpy cho ra thời gian chạy ngắn nhất thậm chí là vượt trội hơn hẳn so với các hàm sort còn lại. Heapsort cho ra thời gian chạy dài nhất tốc độ chậm hơn khoảng 100 lần so với hàm sort của numpy và 2-3 lần so với 2 hàm sort tự viết còn lại.
- Trong các hàm sort tự viết bằng python thì Quick sort có thời gian chạy ngắn nhất kế đến là Merge sort cuối cùng là Heap sort.
- Dù các hàm sort tự viết có độ phức tạp lý thuyết là O(nlogn) nhưng thực tế lại cho thấy Heap sort có chi phí hằng số lớn hơn nhiều dẫn đến tốc độ chạy kém hơn so với 2 thuật toán còn lại.
- Tốc độ của hàm sort (C++) nhanh hơn nhiều so với các hàm sort tự viết bằng python nhưng không bằng hàm sort của numpy.
