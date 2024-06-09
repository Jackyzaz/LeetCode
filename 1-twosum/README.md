# #1 Two Sum (Easy)

<br/>

## Problem Description

### **Input** สำหรับโจทย์   ได้แก่
1. `nums` : array ที่ประกอบไปด้วยจำนวนเต็ม
2. `target` : จำนวนที่โจทย์ต้องการ
 
เป้าหมายคือการหาว่ามีจำนวนคู่ใดใน `nums` ที่บวกกันได้เท่ากับ `target`

<br/>

# Solution
1. **Simple Bruteforce**
2. **Pair Bruteforce**
3. **Hashtable**

<br/>

## Approch 1: Simple Bruteforce
#### Algorithm
1. Loop element ของ `nums` เพื่อมาจับคู่กันทีละตัว โดยผ่าน index `i` และ `j`
2. นำจำนวนมาบวกกันนั่นก็คือ `nums[i] + nums[j]`
3. เช็คค่าที่ว่า  `nums[i] + nums[j]` เท่ากับ `target` แล้วหรือยัง
4. เมื่อพบ return ค่าตำแหน่ง `i , j` ออกไป

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

<br/>

## Approch 2: Pair Bruteforce
วิธีนี้เพิ่มความเร็วด้วยมองหาจำนวนที่เป็นคู่กัน ทำให้เพิ่มประสิทธิได้เพิ่มขึ้นจากวิธีแรก
#### Algorithm
1. Loop element ของ `nums` เพื่อมาจับคู่กันทีละตัว โดยผ่าน index `i` และ `j`
2. ค้นหาค่าที่เป็นคู่กัน นั่นคือ `target - num[i]` 
3. เช็คค่าที่ว่า  `target - num[i]` เท่ากับ `target` แล้วหรือยัง
4. เมื่อพบ return ค่าตำแหน่ง `i , j` ออกไป

#### Implementation : Python 3 

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
       for j in range(i+1,len(nums)):
          if nums[j] == (target-nums[i]) 
             return [i,j]
```

#### Complexity Analysis

* Time complexity : *O(n<sup>2</sup>)*
>
> เหมือนกับวิธีแรก เนื่องจากในการ Loop แต่ละครั้งความซับซ้อนจะเพิ่มขึ้นตามขนาดของ `nums` ซึ่งวิธีนี้ใช้การ loop ครั้งแรกเกิด *O(n)* เมื่อซ้อน loop เข้าไปอีกครั้งทำให้ทวีคูณความซับซ้อนเป็น *O(n<sup>2</sup>)*
>
> ```python
>  for i in range(len(nums)):           <---- O(n)
>        for j in range(i+1,len(nums)): <---- O(n)
>                          O(n) * O(n) = O(n^2)
> ```
* Space complexity : *O(1)*
>
> เหมือนกับวิธีแรก ผลที่ได้จากการ loop แต่ละครั้งคือ `nums[i] + nums[j]` ดังนั้นหากไม่เจอผลลัพธ์ที่ต้องการ ผลบวกก็จะเขียนทับตัวแปรเดิมทำให้ใช้พื้นที่ของการคำนวณเป็นค่าคงที่
>
> ```python
>  if nums[j] == (target-nums[i]) : <---- ดึงค่าจาก nums[index] เพื่อคำนวณและไม่ได้เกิดการขยายพื้นที่เมื่อ nums มีขนาดมากขึ้น
>     return [i,j]
> ```

<br/>

## Approch 3: Hashtable
ใช้ประโยชน์จากโครงสร้างข้อมูลที่เรียกว่า Hashtable เพื่อลดความซับซ้อนที่เกิดขึ้น
#### Algorithm
1. สร้างตัวแปรเพื่อเก็บ Hashtable คือ `numMap`
2. Loop element จาก `nums` โดยมีเงื่อนไขคือ
* เก็บตัวแปรของคู่  `target - nums[i]`  ``
*
4. เช็คค่าที่ว่า  `target - num[i]` เท่ากับ `target` แล้วหรือยัง
5. เมื่อพบ return ค่าตำแหน่ง `i , j` ออกไป

#### Implementation : Python 3 

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i
        print(i,numMap)

```

#### Complexity Analysis

* Time complexity : *O(n<sup>2</sup>)*
>
> เหมือนกับวิธีแรก เนื่องจากในการ Loop แต่ละครั้งความซับซ้อนจะเพิ่มขึ้นตามขนาดของ `nums` ซึ่งวิธีนี้ใช้การ loop ครั้งแรกเกิด *O(n)* เมื่อซ้อน loop เข้าไปอีกครั้งทำให้ทวีคูณความซับซ้อนเป็น *O(n<sup>2</sup>)*
>
> ```python
>  for i in range(len(nums)):           <---- O(n)
>        for j in range(i+1,len(nums)): <---- O(n)
>                          O(n) * O(n) = O(n^2)
> ```
* Space complexity : *O(1)*
>
> เหมือนกับวิธีแรก ผลที่ได้จากการ loop แต่ละครั้งคือ `nums[i] + nums[j]` ดังนั้นหากไม่เจอผลลัพธ์ที่ต้องการ ผลบวกก็จะเขียนทับตัวแปรเดิมทำให้ใช้พื้นที่ของการคำนวณเป็นค่าคงที่
>
> ```python
>  if nums[j] == (target-nums[i]) : <---- ดึงค่าจาก nums[index] เพื่อคำนวณและไม่ได้เกิดการขยายพื้นที่เมื่อ nums มีขนาดมากขึ้น
>     return [i,j]
> ```

