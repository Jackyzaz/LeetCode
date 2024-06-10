# #1 Two Sum `Easy` 
### url : <https://leetcode.com/problems/two-sum/>

ปัญหาข้อนี้คงจะเป็นข้อแรก ๆ ของหลายคนที่เล่น Leetcode และเป็นตัวอย่างที่ดีในการเริ่มต้นสาย Competitive Programming เพราะเป็นตัวอย่างที่เข้าใจง่ายแต่มีความซับซ้อนของการแก้ปัญหาในแต่ระดับ 
ซึ่งมีความน่าสนใจในเชิงการวิเคราะห์ความซับซ้อนของ algorithm 

ดังนั้น ใน solution นี้เราจะแนะนำวิธีการเข้าใจโจทย์ 3 วิธีที่จะทำให้เข้าใจการแก้ปัญหาในข้อนี้ได้ดีขึ้น
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
ใช้ประโยชน์จากโครงสร้างข้อมูลที่เรียกว่า Hashtable คือการเก็บข้อมูลที่เก็บในลักษณะของตารางที่มี key และ value ซึ่งนำมาประยุกต์เพื่อลดความซับซ้อนที่เกิดขึ้น โดยสำหรับโจทย์ข้อนี้เราจะให้ key หรือ `complement` แทนจำนวนเลขที่จะจับคู่ ส่วน value ให้แทน `index` หรือ `i`
#### Algorithm
1. สร้างตัวแปรเพื่อเก็บ Hashtable คือ `numMap`
2. Loop element จาก `nums` โดยมีเงื่อนไขคือ
   
&nbsp;&nbsp;&nbsp;&nbsp;2.1. ตรวจสอบ `target - nums[i]` 

* ถ้า **มี** ค่าอยู่ใน `numMap` นั่นคือพบคำตอบให้ return ค่า `i` และ `numMap[complement]` ออกไป 

* ถ้า **ไม่มี** ให้ทำ 2.2 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Note: `complement` เปรียบเสมือน key ของ hashtable*

&nbsp;&nbsp;&nbsp;&nbsp;2.2. ให้บันทึก `complement = target - nums[i]` ไว้ใน `numMap` จากนั้น Loop ใหม่

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
        # print(i,numMap)

```

#### Complexity Analysis

* Time complexity : *O(n)*
>
> เนื่องจากใช้ Loop เพียงครั้งเดียวความซับซ้อนจึงเพิ่มขึ้นตามขนาดของ `nums`
>
> ```python
>   for i in range(n): <------------------- O(n)
>        complement = target - nums[i]
>        if complement in numMap:
>            return [numMap[complement], i]
>        numMap[nums[i]] = i
> ```
* Space complexity : *O(n)*
>
> การใช้ Hashtable ทำให้สร้างพื้นที่พิเศษสำหรับการบันทึกข้อมูลที่เคยพบไว้แล้วดังนั้น พื้นที่จึงแปรผันตรงกับขนาดของ `nums`
>
> ```python
>  for i in range(n):
>        complement = target - nums[i]
>       if complement in numMap:
>            return [numMap[complement], i]
>        numMap[nums[i]] = i <------------- O(n)
> ```

