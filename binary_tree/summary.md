# 二叉树

前序遍历法：
1. 访问根结点  
2. 访问左子树  
3. 访问右子树  

访问左子树时，首先访问的是左孩子结点，访问右子树时，访问的右孩子结点

中序和后序暂且不表

##     
1.理解二叉树的递归过程
遍历左子树返回时，左子树的每个节点经历过遍历左子树、右子树和访问节点的操作了，
即dfs(root)中，每个节点作为root都执行完了dfs函数。  
这是因为每个dfs都递归调用了两个dfs。  

2.理解一个二叉树算法：  

    1.理解算法的思想
    2.脑子里跟着代码执行一遍
    
3.注意有时候可以根据递归方法返回值判断是否可以剪枝