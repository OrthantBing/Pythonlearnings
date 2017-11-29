import linkedbinarytree
lbt = linkedbinarytree.LinkedBinaryTree()
lbt._add_root(10)
root = lbt.root()
left_10 = lbt._add_left(root, 5)
right_10 = lbt._add_right(root, 15)

left_5 = lbt._add_left(left_10, 3)
right_5 = lbt._add_right(left_10, 9)

left_15 = lbt._add_left(right_10, 11)
right_15 = lbt._add_right(right_10, 20)

for i in lbt:
    print(i)
