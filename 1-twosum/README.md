# #1 Two Sum (Easy)

<br/>

## Problem Description

### **Input** สำหรับโจทย์   ได้แก่
1. `nums` : array ที่ประกอบไปด้วยจำนวนเต็ม
2. `target` : จำนวนที่โจทย์ต้องการ
 
เป้าหมายคือการหาว่ามีจำนวนคู่ใดใน `nums` ที่บวกกันได้เท่ากับ `target`

<br/>

# Solution

<br/>

## Approch 1: Simple Bruteforce
#### Algorithm
1. Loop element ของ `nums` เพื่อมาจับคู่กันทีละตัว โดยผ่าน index `i` และ `j`
2. นำจำนวนมาบวกกันนั่นก็คือ `nums[i] + nums[j]`
3. เช็คค่าที่ว่า  `nums[i] + nums[j]` เท่ากับ `target` แล้วหรือยัง
4. เมื่อพบ return ค่า `nums[i] , nums[j]` ออกไป

#### Implementation : Python 3 

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (i != j ):
                if nums[i] + nums[j] == target :
                    return [i,j]
```

#### Complexity Analysis

* Time complexity : *O(n<sup>2</sup>)*
>
> เนื่องจากในการ Loop แต่ละครั้งความซับซ้อนจะเพิ่มขึ้นตามขนาดของ `nums` ซึ่งวิธีนี้ใช้การ loop ครั้งแรกเกิด *O(n)* เมื่อซ้อน loop เข้าไปอีกครั้งทำให้ทวีคูณความซับซ้อนเป็น *O(n<sup>2</sup>)*
>
> ```python
>  for i in range(len(nums)):       <---- O(n)
>        for j in range(len(nums)): <---- O(n)
>                          O(n) * O(n) = O(n^2)
> ```
* Space complexity : *O(1)*
>
> ผลที่ได้จากการ loop แต่ละครั้งคือ `nums[i] + nums[j]` ดังนั้นหากไม่เจอผลลัพธ์ที่ต้องการ ผลบวกก็จะเขียนทับตัวแปรเดิมทำให้ใช้พื้นที่ของการคำนวณเป็นค่าคงที่
>
> ```python
>  if nums[i] + nums[j] == target : <---- ดึงค่าจาก nums[index] เพื่อคำนวณและไม่ได้เกิดการขยายพื้นที่เมื่อ nums มีขนาดมากขึ้น
>      return [i,j]
> ```
>
