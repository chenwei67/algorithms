#二分搜索的两种写法：
## 一: 自己总结的
### 总结：
0. while循环不需要等号

1. nums[mid]等于target时，根据是否需要排除mid，分配到"1"或另一个判断句

2. mid取整方式取决于"1"在小于还是大于的判断句

3. 值与target为不等关系时，值不排除不能有"1"，值排除可以无"1"

### 关键：
0. "1"与"nums[mid]==target"，决定了二分法怎么写  

### 步骤：
**0. 确定循环主体**  
**1. 确定m的计算方式**  
**2. 这种方法无法越界，确定结果为越界的情况时的边界处理**  







## 二：学习到的，更简单，思维负担更小(ps:但这不是万能的，比如剑指offer11题【寻找旋转数组最小值】)
### 总结：
0. while带等号
1. 判断句都有"1"
2. mid固定向下取整
3. 退出循环时，i = j + 1
4. 题目不同，返回的指针不同，且等号的处理也不同

### 关键：
0. 返回哪个指针

# 边界二分查找：
##种类
边界值可以是最后一个小于target值，第一个大于target值,等于的情况可以转为对立的边界  

## 算法解析
1. 初始化： 左边界 i = 0 ，右边界 j = len(nums) - 1。

2. 循环二分： 当闭区间 [i, j] 无元素时跳出；

3. 计算中点 m = (i + j) / 2 （向下取整）；

4. 若 nums[m] < target ，则 target 在闭区间 [m + 1, j] 中，因此执行 i = m + 1；

5. 若 nums[m] > target ，则 target 在闭区间 [i, m - 1] 中，因此执行 j = m - 1；

6. 若 nums[m] = target ，则右边界 right 在闭区间 [m+1, j] 中；左边界 left 在闭区间 [i, m-1]中。因此分为以下两种情况：  
若查找 右边界 right ，则执行 i = m + 1；（跳出时 i 指向右边界）  
若查找 左边界 left ，则执行 j = m - 1；（跳出时 j 指向左边界）  


链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/solution/mian-shi-ti-53-i-zai-pai-xu-shu-zu-zhong-cha-zha-5/

来源：力扣（LeetCode）
