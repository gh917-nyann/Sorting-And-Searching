# BÁO CÁO KẾT QUẢ THỬ NGHIỆM
### Sinh viên thực hiện: Đỗ Gia Huy 
### MSSV: 25520681
### Lớp: ATTN2025
### Nội dung báo cáo:   
Báo cáo nhằm khảo sát, so sánh và đánh giá thời gian thực hiện của một số
thuật toán sắp xếp phổ biến dựa trên cùng một bộ dữ liệu.
#### I.	Kết quả thử nghiệm
   1.	Bảng thời gian thực hiện (ms)
<div align="center">

| Dữ liệu        | Quicksort | Heapsort  | Mergesort | sort (numpy) |
| -------------- | --------- | --------- | --------- | ------------ |
| 1              | 284       | 1013      | 868       | 9            |
| 2              | 18        | 140       | 180       | 9            |
| 3              | 93        | 229       | 206       | 9            |
| 4              | 92        | 224       | 194       | 9            |
| 5              | 94        | 222       | 195       | 10           |
| 6              | 97        | 227       | 194       | 9            |
| 7              | 94        | 226       | 209       | 8            |
| 8              | 95        | 235       | 195       | 8            |
| 9              | 103       | 235       | 215       | 9            |
| 10             | 95        | 334       | 214       | 8            |
| **Trung bình** | **106.5** | **308.5** | **267.0** | **8.8**      |
</div> 

   2.	Biểu đồ (cột) thời gian thực hiện  
    
   <img width="902" height="548" alt="image" src="https://github.com/user-attachments/assets/37e58065-6c06-4627-98d0-d12164d91b64" />


#### II.	Kết luận:
Theo kết quả thử nghiệm có thể thấy:
-	Hàm sort của numpy có tốc độ thực hiện nhanh đáng kể so với các hàm sort tự viết còn lại. Tốc độ cũng duy trì ổn định hơn qua các test (trong khoảng 9-10 ms).
-	Hàm Quick sort có tốc độ nhanh thứ hai so với hàm sort của numpy và nhanh nhất so với các hàm sort tự viết. 
-	Merge sort nhanh hơn Heap sort nhưng vẫn chậm hơn so với Quick sort.
-	Hàm Heap sort tốc độ thực hiện chậm nhất đặc biệt đối với bộ dữ liệu đầu tiên (bộ dữ liệu đã sắp xếp) tốc độ lên đến ~ 1013 ms.
-	Thứ tự các hàm sort có thể sắp xếp: Numpy sort -> Quick sort -> Merge sort -> Heap sort.
